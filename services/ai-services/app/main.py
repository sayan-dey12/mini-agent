from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from app.schemas.chat import ChatRequest
from app.schemas.chat import ChatResponse
from app.providers.GroqProvider import GroqProvider

from app.services.LLMServices import LLMService
from app.runtime.StreamEventSerializer import StreamEventSerializer

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

    text = llm.chat(
        [message.model_dump() for message in request.messages]
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
        for event in llm.stream(messages):
            yield StreamEventSerializer.serialize(event)

    return StreamingResponse(
        generate(),
        media_type="application/x-ndjson"
    )