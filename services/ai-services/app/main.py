from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def home():
    return {"message": "Mini Agent AI Service Running 🚀"}