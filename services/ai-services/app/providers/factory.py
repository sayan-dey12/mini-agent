from typing import Type

from app.providers.base import ILLMProvider
from app.providers.GroqProvider import GroqProvider
from app.providers.OllamaProvider import OllamaProvider


class ProviderFactory:
    """
    Creates LLM provider instances.
    """

    _providers: dict[str, Type[ILLMProvider]] = {
        "groq": GroqProvider,
        "ollama": OllamaProvider,
    }

    @classmethod
    def create(
        cls,
        provider: str,
    ) -> ILLMProvider:

        provider_class = cls._providers.get(provider.lower())

        if provider_class is None:
            supported = ", ".join(sorted(cls._providers.keys()))
            raise ValueError(
                f"Unsupported provider '{provider}'. "
                f"Supported providers: {supported}"
            )

        return provider_class()