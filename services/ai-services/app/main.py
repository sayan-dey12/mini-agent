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

    last_user_message = next(
        (
            message for message in reversed(request.messages) if message.role == "user"
        ),
        None,
    )

    return ChatResponse(
        text=f"Python received: {last_user_message.content if last_user_message else ''}"
    )