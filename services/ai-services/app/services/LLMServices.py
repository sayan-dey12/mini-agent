from app.providers.GroqProvider import GroqProvider
from app.tools.registry import ToolRegistry
from app.tools.executor import ToolExecutor
from app.tools.builtin.calculator import CalculatorTool
from app.providers.base import ILLMProvider
class LLMService:

    def __init__(self , provider: ILLMProvider ):
        self.provider = provider
        self.registry = ToolRegistry()

        self.registry.register(
            CalculatorTool()
        )

        self.executor = ToolExecutor(
            self.registry
        )

    def chat(self, messages):

        return self.provider.chat(messages , self.registry.schemas())
    
    def stream(self,messages):
        yield from self.provider.stream(messages)