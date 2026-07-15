from app.providers.GroqProvider import GroqProvider
from app.tools.registry import ToolRegistry
from app.tools.executor import ToolExecutor
from app.tools.builtin.calculator import CalculatorTool
from app.providers.base import ILLMProvider
import json
import pprint
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

        MAX_ITERATIONS = 5
        for _ in range(MAX_ITERATIONS):
            # print("\n===== Messages Sent to Groq =====")
            # pprint.pp(messages)
            # print("=================================\n")
            message = self.provider.chat(messages , self.registry.schemas())
            
            # no more tool calls, return the content directly
            if not message.tool_calls:
                return message.content
            
            #save assistant message with tool calls
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
                            for tool_call in message.tool_calls
                        ],
                    }
                )
            
            #execute every requested tools
            for tool_call in message.tool_calls:
                arguments = json.loads(tool_call.function.arguments)
                
                result = self.executor.execute(
                    tool_call.function.name , arguments
                )
                
                messages.append(
                    {
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": result,
                    }
                )
        
        raise RuntimeError(
            "Maximum tool-calling iterations exceeded."
        )
        
    def stream(self,messages):
        yield from self.provider.stream(messages)