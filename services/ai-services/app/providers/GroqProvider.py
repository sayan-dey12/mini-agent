from email.mime import message
import os

from groq import Groq , APIError
from dotenv import load_dotenv
from app.providers.base import ILLMProvider
from app.runtime.ToolCall import ToolCall
from app.runtime.ToolFunction import ToolFunction
from app.runtime.ProviderMessage import ProviderMessage
from app.runtime.ProviderRequest import ProviderRequest
from app.runtime.ProviderResponse import ProviderResponse
from app.runtime.ProviderChunk import ProviderChunk

load_dotenv()

class GroqProvider(ILLMProvider):
    def __init__(self):
        api_key = os.environ.get("GROQ_API_KEY")
        if not api_key:
            raise RuntimeError("GROQ_API_KEY environment variable is not set.")
        self.client = Groq(
            api_key=api_key,
        )

    def chat(self, request: ProviderRequest) -> ProviderResponse:
        
        try:
            
            response = self.client.chat.completions.create(
                model=request.model or "llama-3.3-70b-versatile" , 
                messages=request.messages,
                tools=request.tools,
                temperature=request.temperature if request.temperature is not None else 0.2,
            )
            
            # message = response.choices[0].message
            # if message.tool_calls:
            #     print("Tool call detected: ", message.tool_calls)
            # else:
            #     return message.content
            
            message = response.choices[0].message
            tool_calls = []
            if message.tool_calls:
                for call in message.tool_calls:
                    tool_calls.append(
                        ToolCall(
                            id=call.id,
                            type=call.type,
                            function=ToolFunction(
                                name=call.function.name,
                                arguments=call.function.arguments,
                            ),
                        )
                    )
                    
            return ProviderResponse(
                message = ProviderMessage(
                    role = message.role,
                    content = message.content,
                    tool_calls = tool_calls
                )
            )
            
        except APIError as e:
            return ProviderResponse(
                message = ProviderMessage(
                    role="assistant",
                    content=f"__PROVIDER_ERROR__:{e}",
                    tool_calls=[],
                )
            )
        
            
    def stream(self , request: ProviderRequest):
        try:
            response = self.client.chat.completions.create(
                model=request.model or "llama-3.3-70b-versatile",
                messages=request.messages,
                stream=True,
                tools=request.tools,
                temperature=request.temperature if request.temperature is not None else 0.2,
                
            )
            for chunk in response:

                choice = chunk.choices[0]
                # print("finish_reason:", choice.finish_reason)
                # print("delta:", choice.delta)
                delta = choice.delta

                # Stream normal text
                if delta.content:
                    yield ProviderChunk(
                        content=delta.content,
                    )
                    
                # for tool call
                if delta.tool_calls:

                    tool_calls = []

                    for call in delta.tool_calls:

                        tool_calls.append(
                            ToolCall(
                                id=call.id,
                                type=call.type,
                                function=ToolFunction(
                                    name=call.function.name,
                                    arguments=call.function.arguments,
                                ),
                            )
                        )

                    yield ProviderChunk(
                        tool_calls=tool_calls,
                    )


                # End of generation
                if choice.finish_reason:
                    yield ProviderChunk(
                        finish_reason=choice.finish_reason,
                    )

                
        except APIError as e:
            yield ProviderChunk(finish_reason="error", content=f"__PROVIDER_ERROR__:{e}")
        