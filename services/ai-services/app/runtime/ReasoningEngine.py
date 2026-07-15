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

            for tool_call in message.tool_calls:

                arguments = json.loads(
                    tool_call.function.arguments
                )
                
                self.logger.tool(
                    "Executing tool",               #logger
                    tool=tool_call.function.name,
                )

                result = self.tool_manager.execute(
                    tool_call.function.name,
                    arguments,
                )
                
                self.logger.tool(
                    "Tool execution finished",          #logger
                    tool=tool_call.function.name,
                )

                messages.append(
                    MessageFactory.tool_result(
                        tool_call=tool_call,
                        result=result
                    )
                )
                
        self.logger.error(
            "Maximum reasoning iterations exceeded."            #logger
        )

        raise RuntimeError(
            "Maximum reasoning iterations exceeded."
        )