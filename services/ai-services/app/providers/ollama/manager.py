import os
import time
import subprocess
import requests

from app.logging.RuntimeLogger import RuntimeLogger

logger = RuntimeLogger("Ollama")


class OllamaStartupError(Exception):
    """Raised when Ollama cannot be started."""


class OllamaConnectionError(Exception):
    """Raised when Ollama cannot be reached."""


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