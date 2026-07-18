from app.runtime.ProviderMessage import ProviderMessage
from app.runtime.ToolCall import ToolCall
from app.runtime.ToolResult import ToolResult


class MessageFactory:

    @staticmethod
    def assistant_tool_call(
        message: ProviderMessage,
    ) -> dict:

        return {
            "role": "assistant",
            "content": message.content,
            "tool_calls": [
                {
                    "id": tool_call.id,
                    "type": tool_call.type,
                    "function": {
                        "name": tool_call.function.name,
                        "arguments": tool_call.function.arguments,
                    },
                }
                for tool_call in message.tool_calls
            ],
        }

    @staticmethod
    def tool_result(
        tool_call: ToolCall,
        result: ToolResult,
    ) -> dict:

        return {
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": (
                str(result.output)
                if result.success
                else f"Tool execution failed: {result.error}"
            ),
        }
        