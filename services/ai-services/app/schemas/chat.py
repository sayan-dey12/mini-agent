from typing import Literal
from pydantic import BaseModel

class ChatMessage(BaseModel):
    role: Literal["system", "user", "assistant"]
    content: str
    
class GenerationConfig(BaseModel):
    model: str
    temperature: float
class ChatRequest(BaseModel):
    messages: list[ChatMessage]
    config: GenerationConfig
    
class ChatResponse(BaseModel):
    text: str
