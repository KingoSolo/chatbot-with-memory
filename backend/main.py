from fastapi import FastAPI
from pydantic import BaseModel
from services.chat_service import chatService

app = FastAPI()
chat_service = chatService(model_name="llama3")

class chatRequest(BaseModel):
    message: str

@app.get("/")
def home():
    return {"message": "fast api is working!"}


@app.post("/chat")
def chat(req: chatRequest):
    reply = chat_service.generate_response(req.message)
    return {"response": reply}

