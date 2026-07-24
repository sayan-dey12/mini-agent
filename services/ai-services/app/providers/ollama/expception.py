class OllamaStartupError(Exception):
    """Raised when Ollama cannot be started."""


class OllamaConnectionError(Exception):
    """Raised when Ollama cannot be reached."""

class ProviderError(Exception):
    pass