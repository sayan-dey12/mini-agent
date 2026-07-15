from __future__ import annotations

import json

from app.providers.base import ILLMProvider
from app.runtime.ProviderRequest import ProviderRequest
from app.tools.executor import ToolExecutor
from app.tools.registry import ToolRegistry
from app.runtime.MessageFactory import MessageFactory
from app.tools.manager import ToolManager

class ReasoningEngine:

    MAX_ITERATIONS = 5

    def __init__(
        self,
        provider: ILLMProvider,
        registry: ToolRegistry,
        tool_manager: ToolManager,
    ):
        self.provider = provider
        self.registry = registry
        self.tool_manager = tool_manager

    def run(self, messages: list[dict]) -> str:

        for _ in range(self.MAX_ITERATIONS):

            request = ProviderRequest(
                messages=messages,
                tools=self.registry.schemas(),
            )

            response = self.provider.chat(request)

            message = response.message

            if not message.tool_calls:
                return message.content or ""

            messages.append(
                MessageFactory.assistant_tool_call(message)
            )

            for tool_call in message.tool_calls:

                arguments = json.loads(
                    tool_call.function.arguments
                )

                result = self.tool_manager.execute(
                    tool_call.function.name,
                    arguments,
                )

                messages.append(
                    MessageFactory.tool_result(
                        tool_call=tool_call,
                        result=result
                    )
                )

        raise RuntimeError(
            "Maximum reasoning iterations exceeded."
        )