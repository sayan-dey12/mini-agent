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

        message = self.provider.chat(messages , self.registry.schemas())
        if not message.tool_calls:
            return message.content
        tool_call = message.tool_calls[0]
        print("Tool call detected: ", tool_call)
        return "tool calling detected..."    
    def stream(self,messages):
        yield from self.provider.stream(messages)