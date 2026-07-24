class ProviderFactory:

    @staticmethod
    def create(config: GenerationConfig):

        if config.provider == "groq":
            return GroqProvider()

        if config.provider == "ollama":
            return OllamaProvider()

        raise ValueError(...)