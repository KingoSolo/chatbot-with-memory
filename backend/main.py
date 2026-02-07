from fastapi import FastAPI
from pydantic import BaseModel
from services.chat_service import ChatService

app = FastAPI()
chat_service = ChatService(model_name="llama3")

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def home():
    return {"message": "fast api is working!"}


@app.post("/chat")
def chat(req: ChatRequest):
    reply = chat_service.generate_response(req.message)
    return {"response": reply}

