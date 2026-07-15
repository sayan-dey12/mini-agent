from app.providers.GroqProvider import GroqProvider
from app.tools.registry import ToolRegistry
from app.tools.executor import ToolExecutor
from app.tools.builtin.calculator import CalculatorTool
from app.providers.base import ILLMProvider
import json
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
        arguments = json.loads(tool_call.function.arguments)
        
        result = self.executor.execute(
            tool_call.function.name , arguments
        )
        
        messages.append(
            {
                "role": "assistant",
                "content": message.content,
                "tool_calls": [
                    {
                        "id": tool_call.id,
                        "type": "function",
                        "function": {
                            "name": tool_call.function.name,
                            "arguments": tool_call.function.arguments,
                        },
                    }
                ],
            }
        )
        messages.append(
            {
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": result,
            }
        )
        final = self.provider.chat(messages , self.registry.schemas())
        return final.content
    
    def stream(self,messages):
        yield from self.provider.stream(messages)