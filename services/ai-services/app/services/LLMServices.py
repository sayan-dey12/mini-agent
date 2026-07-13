from app.providers.GroqProvider import GroqProvider
from app.tools.registry import ToolRegistry
from app.tools.executor import ToolExecutor
from app.tools.builtin.calculator import CalculatorTool

class LLMService:

    def __init__(self):
        self.provider = GroqProvider()
        self.registry = ToolRegistry()

        self.registry.register(
            CalculatorTool()
        )

        self.executor = ToolExecutor(
            self.registry
        )

    def chat(self, messages):

        return self.provider.chat(messages)
    
    def stream(self,messages):
        yield from self.provider.stream(messages)