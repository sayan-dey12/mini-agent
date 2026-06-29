from fastapi import FastAPI

from app.schemas.chat import ChatRequest
from app.schemas.chat import ChatResponse

app = FastAPI()


@app.get("/")
async def home():
    return {
        "message": "Mini Agent AI Service Running 🚀"
    }


@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):

    return ChatResponse(
        text=f"Python received: {request.message}"
    )