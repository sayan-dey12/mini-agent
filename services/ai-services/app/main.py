from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from app.schemas.chat import ChatRequest
from app.schemas.chat import ChatResponse
from app.providers.GroqProvider import GroqProvider

from app.services.LLMServices import LLMService
from app.runtime.StreamEventSerializer import StreamEventSerializer
from app.runtime.StreamEvent import StreamEvent
from app.runtime.StreamEventType import StreamEventType

app = FastAPI()

provider = GroqProvider()
llm = LLMService(provider)


@app.get("/")
async def home():
    return {
        "message": "Mini Agent AI Service Running 🚀"
    }


@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    messages = [message.model_dump() for message in request.messages]
    text = llm.chat(
        messages=messages,
        config=request.config,
    )
    

    return ChatResponse(
        text=text
    )
    
    
@app.post("/chat/stream")
async def stream_chat(request: ChatRequest):

    def generate():

        messages = [
            message.model_dump()
            for message in request.messages
        ]
        
        try:
            for event in llm.stream(
                messages,
                config=request.config):
                yield StreamEventSerializer.serialize(event)
        except Exception as e:
            yield StreamEventSerializer.serialize(StreamEvent(type=StreamEventType.ERROR, data=str(e)))

    return StreamingResponse(
        generate(),
        media_type="application/x-ndjson"
    )