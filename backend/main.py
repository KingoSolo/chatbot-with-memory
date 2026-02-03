from fastapi import FastAPI
from pydantic import BaseModel
from services.chat_service import chatService

app = FastAPI()
chat_service = chatService()

class chatRequest(BaseModel):
    message: str

@app.get("/")
def home():
    return {"message": "fast api is working!"}

@app.post("/chat")
 