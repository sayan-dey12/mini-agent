from __future__ import annotations

import json

from app.providers.base import ILLMProvider
from app.runtime.ProviderRequest import ProviderRequest
from app.tools.executor import ToolExecutor
from app.tools.registry import ToolRegistry


class ReasoningEngine:

    MAX_ITERATIONS = 5

    def __init__(
        self,
        provider: ILLMProvider,
        registry: ToolRegistry,
        executor: ToolExecutor,
    ):
        self.provider = provider
        self.registry = registry
        self.executor = executor

    def run(self, messages: list[dict]) -> str:

        for _ in range(self.MAX_ITERATIONS):

            request = ProviderRequest(
                messages=messages,
                tools=self.registry.schemas(),
            )

            response = self.provider.chat(request)

            message = response.message

            if not message.tool_calls:
                return message.content or ""

            messages.append(
                {
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
            )

            for tool_call in message.tool_calls:

                arguments = json.loads(
                    tool_call.function.arguments
                )

                result = self.executor.execute(
                    tool_call.function.name,
                    arguments,
                )

                messages.append(
                    {
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": (
                            result.output
                            if result.success
                            else result.error
                        ),
                    }
                )

        raise RuntimeError(
            "Maximum reasoning iterations exceeded."
        )