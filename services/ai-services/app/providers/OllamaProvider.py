from typing import Iterator

import requests
import json

from app.providers.base import ILLMProvider
from app.providers.ollama.manager import (
    OllamaManager,
    OllamaConnectionError,
    OllamaStartupError,
)
from app.runtime.ProviderRequest import ProviderRequest
from app.runtime.ProviderResponse import ProviderResponse
from app.runtime.StreamEvent import StreamEvent , StreamEventType
from app.logging.RuntimeLogger import RuntimeLogger

REQUEST_TIMEOUT = 60
logger = RuntimeLogger()


class OllamaProvider(ILLMProvider):

    def __init__(self):

        self.manager = OllamaManager()
        self.base_url = self.manager.base_url

    def chat(
        self,
        request: ProviderRequest,
    ) -> ProviderResponse:

        self.manager.ensure_running()

        payload = self._build_request(
            request=request,
            stream=False,
        )

        try:
            logger.provider(
                "Sendign request",
                model= request.model )

            response = requests.post(
                f"{self.base_url}/api/chat",
                json=payload,
                timeout=REQUEST_TIMEOUT,
            )

            response.raise_for_status()

            return self._handle_response(response)

        except (
            requests.RequestException,
            OllamaConnectionError,
            OllamaStartupError,
        ) as error:

            self._raise_provider_error(error)

    def stream(
        self,
        request: ProviderRequest,
    ) -> Iterator[StreamEvent]:

        self.manager.ensure_running()

        payload = self._build_request(
            request=request,
            stream=True,
        )

        try:
            
            logger.provider(
                "Sendign request",
                model= request.model )

            response = requests.post(
                f"{self.base_url}/api/chat",
                json=payload,
                stream=True,
                timeout=REQUEST_TIMEOUT,
            )

            response.raise_for_status()

            yield from self._handle_stream(response)

        except (
            requests.RequestException,
            OllamaConnectionError,
            OllamaStartupError,
        ) as error:

            self._raise_provider_error(error)

    def _build_request(
        self,
        request: ProviderRequest,
        stream: bool,
    ) -> dict:

        return {
            "model": request.model,
            "messages": request.messages,
            "stream": stream,
            "options": {
                "temperature": request.temperature,
            },
        }

    def _handle_response(
        self,
        response: requests.Response,
    ) -> ProviderResponse:

        data = response.json()
        message = data.get("message",{})

        return ProviderResponse(
            text=message.get("content","")
        )

    def _handle_stream(
        self,
        response: requests.Response,
    ) -> Iterator[StreamEvent]:

        for line in response.iter_lines():

            if not line:
                continue

            chunk = json.loads(line)

            if chunk.get("done"):
                break
            
            message = chunk.get("message")

            if not message:
                continue
            
            content = message.get("content")

            if not content:
                continue


            yield StreamEvent(
                type=StreamEventType.TEXT_DELTA,
                data=content
            )

    def _raise_provider_error(
        self,
        error: Exception,
    ) -> None:

        logger.error(f"Provider error: {error}")

        raise self.ProviderError(
            f"Unable to communicate with Ollama: {error}"
        ) from error
        