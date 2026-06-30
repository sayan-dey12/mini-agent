from fastapi import FastAPI

from app.schemas.chat import ChatRequest
from app.schemas.chat import ChatResponse

from app.services.LLMServices import LLMService

app = FastAPI()

llm = LLMService()


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