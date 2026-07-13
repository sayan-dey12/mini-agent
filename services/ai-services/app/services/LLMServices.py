from app.providers.GroqProvider import GroqProvider

class LLMService:

    def __init__(self):
        self.provider = GroqProvider()

    def chat(self, messages):

        return self.provider.chat(messages)
    
    def stream(self,messages):
        yield from self.provider.stream(messages)