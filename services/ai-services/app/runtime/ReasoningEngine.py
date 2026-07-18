from __future__ import annotations

import json
import time

from app.providers.base import ILLMProvider
from app.runtime.ProviderRequest import ProviderRequest
from app.tools.executor import ToolExecutor
from app.tools.registry import ToolRegistry
from app.runtime.MessageFactory import MessageFactory
from app.tools.manager import ToolManager
from app.logging.RuntimeLogger import RuntimeLogger
from app.runtime.StreamEvent import StreamEvent
from app.runtime.StreamEventType import StreamEventType
from app.runtime.ProviderMessage import ProviderMessage
from app.runtime.ToolCall import ToolCall
class ReasoningEngine:

    MAX_ITERATIONS = 5

    def __init__(
        self,
        provider: ILLMProvider,
        registry: ToolRegistry,
        tool_manager: ToolManager,
        logger: RuntimeLogger,
    ):
        self.provider = provider
        self.registry = registry
        self.tool_manager = tool_manager
        self.logger =logger

    def _execute_tool_calls(
        self,
        messages: list[dict],
        tool_calls: list[ToolCall],
        streaming: bool = False,
    ):
        """
        Executes all tool calls.

        If streaming=True, StreamEvents are yielded.
        """

        for tool_call in tool_calls:

            if streaming:
                yield StreamEvent(
                    type=StreamEventType.TOOL_START,
                    data=tool_call.function.name,
                )

            arguments = json.loads(
                tool_call.function.arguments
            )

            self.logger.tool(
                "Executing tool",
                tool=tool_call.function.name,
            )

            result = self.tool_manager.execute(
                tool_call.function.name,
                arguments,
            )

            self.logger.tool(
                "Tool execution finished",
                tool=tool_call.function.name,
            )

            if streaming:
                yield StreamEvent(
                    type=StreamEventType.TOOL_END,
                    data={
                        "tool": tool_call.function.name,
                        "success": result.success,
                    },
                )

            messages.append(
                MessageFactory.tool_result(
                    tool_call,
                    result,
                )
            )

    def run(self, messages: list[dict]) -> str:
        
        self.logger.reasoning("Reasoning started.")          #logger

        for iteration in range(1,self.MAX_ITERATIONS+1):
            self.logger.reasoning(
                "Reasoning iteration",
                iteration=iteration,
            )  #logger
            request = ProviderRequest(
                messages=messages,
                tools=self.registry.schemas(),
            )
            start = time.perf_counter()
            self.logger.provider("Sending request to provider...")  #logger

            response = self.provider.chat(request)
            
            elapsed = (
                time.perf_counter() - start
            ) * 1000

            self.logger.provider(
                "Response received",
                latency=f"{elapsed:.2f} ms",        #logger
            )

            message = response.message

            if not message.tool_calls:
                messages.append({
                    "role": "assistant",
                    "content": message.content,
                })
                 
                self.logger.reasoning(
                    "No tool calls detected."       #logger
                )

                self.logger.reasoning(
                    "Reasoning finished."           #logger
                )
                return message.content or ""

            messages.append(
                MessageFactory.assistant_tool_call(message)
            )

            for _ in self._execute_tool_calls(
                messages=messages,
                tool_calls=message.tool_calls,
            ):
                pass
                
        self.logger.error(
            "Maximum reasoning iterations exceeded."            #logger
        )

        raise RuntimeError(
            "Maximum reasoning iterations exceeded."
        )
        
    def stream(
        self,
        messages: list[dict],
    ):

        self.logger.reasoning(
            "Streaming reasoning started."
        )

        for iteration in range(
            1,
            self.MAX_ITERATIONS + 1,
        ):

            self.logger.reasoning(
                "Streaming iteration",
                iteration=iteration,
            )
            
            # print("=" * 80)
            # print("TOOLS SENT TO GROQ:")
            # print(json.dumps(self.registry.schemas(), indent=2))
            # print("=" * 80)

            request = ProviderRequest(
                messages=messages,
                tools=self.registry.schemas(),
                stream=True,
            )

            content_parts: list[str] = []

            tool_calls: list[ToolCall] = []

            for chunk in self.provider.stream(request):

                if chunk.content:

                    content_parts.append(
                        chunk.content
                    )

                    yield StreamEvent(
                        type=StreamEventType.TEXT,
                        data=chunk.content,
                    )

                if chunk.tool_calls:

                    tool_calls.extend(
                        chunk.tool_calls
                    )
                    
            content = "".join(content_parts)

            #
            # No tool calls
            #
            if not tool_calls:
                
                messages.append({
                    "role": "assistant",
                    "content": content,
                })

                self.logger.reasoning(
                    "Streaming finished."
                )

                yield StreamEvent(
                    type=StreamEventType.DONE,
                    data=None,
                )

                return

            #
            # Add assistant message
            #
            messages.append(
                MessageFactory.assistant_tool_call(
                    ProviderMessage(
                        role="assistant",
                        content=content,
                        tool_calls=tool_calls,
                    )
                )
            )

            #
            # Execute every tool
            #
            yield from self._execute_tool_calls(
                messages=messages,
                tool_calls=tool_calls,
                streaming=True,
            )

        raise RuntimeError(
            "Maximum reasoning iterations exceeded."
        )