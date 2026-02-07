import ollama
from services.memory_service import MemoryService

class chatService:
    def __init__(self, model_name= "llama3"):
        self.model_name = model_name
        self.memory = MemoryService()

    def generate_response(self, prompt: str) -> str:
        self.memory.add_message("user", prompt)
        conversation = self.memory.get_history()

        
        response = ollama.chat(
                    model=self.model_name,
                    messages=conversation
                )

        reply = response["message"]["content"]

                # Add assistant reply to memory
        self.memory.add_message("assistant", reply)
        return reply

