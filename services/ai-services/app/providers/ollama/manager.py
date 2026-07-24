import os
import time
import subprocess
import requests

from app.providers.ollama.expception import (OllamaStartupError , OllamaConnectionError)
from app.logging.RuntimeLogger import RuntimeLogger

logger = RuntimeLogger()


class OllamaManager:

    DEFAULT_URL = "http://localhost:11434"

    def __init__(
        self,
        base_url: str | None = None,
        startup_mode: str | None = None,
        container_name: str | None = None,
        timeout: int = 30,
    ):

        self.base_url = (
            base_url
            or os.getenv("OLLAMA_BASE_URL")
            or self.DEFAULT_URL
        )

        self.startup_mode = (
            startup_mode
            or os.getenv("OLLAMA_STARTUP")
            or "docker"
        )

        self.container_name = (
            container_name
            or os.getenv("OLLAMA_CONTAINER")
            or "ollama"
        )

        self.timeout = timeout
        
    def is_running(self) -> bool:
        try:
            response = requests.get(
                f"{self.base_url}/api/tags",
                timeout=2,
            )
            
            return response.status_code == 200
        
        except requests.RequestException:
            return False
        
        
    def ensure_running(self) -> None:

        if self.is_running():

            logger.reasoning("Ollama is already running")

            return

        logger.reasoning("Ollama is not running.")

        self.start()

        self.wait_until_ready()
        
    def start(self) -> None:

        logger.reasoning(
            f"Starting Ollama using '{self.startup_mode}'."
        )

        if self.startup_mode == "docker":

            self._start_docker()

            return

        if self.startup_mode == "native":

            self._start_native()

            return

        raise OllamaStartupError(
            f"Unknown startup mode '{self.startup_mode}'."
        )
        
    
    def _start_docker(self) -> None:

        try:

            subprocess.run(
                [
                    "wsl",
                    "-d",
                    "UbuntuF",
                    "docker",
                    "start",
                    self.container_name,
                ],
                check=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.PIPE,
                text=True,
            )

            logger.reasoning(
                "Docker container started."
            )

        except FileNotFoundError as e:

            raise OllamaStartupError(
                "Docker executable not found."
            ) from e

        except subprocess.CalledProcessError as e:

            raise OllamaStartupError(
                f"Unable to start Docker container '{self.container_name}'.\n"
                f"{e.stderr.strip()}"
            ) from e
            
            
    def _start_native(self) -> None:

        try:

            subprocess.Popen(
                ["ollama", "serve"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )

            logger.reasoning(
                "Started native Ollama."
            )

        except FileNotFoundError as e:

            raise OllamaStartupError(
                "Ollama executable not found."
            ) from e
            
            
            
    def wait_until_ready(self) -> None:

        logger.reasoning(
            "Waiting for Ollama..."
        )

        deadline = time.time() + self.timeout

        while time.time() < deadline:

            if self.is_running():

                logger.reasoning(
                    "Ollama is ready."
                )

                return

            time.sleep(1)

        raise OllamaConnectionError(
            "Timed out waiting for Ollama."
        )
        
        
    def list_models(self) -> list[str]:

        try:

            response = requests.get(
                f"{self.base_url}/api/tags",
                timeout=5,
            )

            response.raise_for_status()

            data = response.json()

            return [
                model["name"]
                for model in data.get("models", [])
            ]

        except requests.RequestException as e:

            raise OllamaConnectionError(
                "Unable to retrieve installed models."
            ) from e