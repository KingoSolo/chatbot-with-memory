import ollama
from services.memory_service import MemoryService
from services.embedding_service import EmbeddingService
from services.vector_memory import VectorMemory
from services.summary_service import SummaryService

class ChatService:
    def __init__(self, model_name="llama3"):
        self.model_name = model_name
        self.memory_list = MemoryService()
        self.embedder = EmbeddingService(model_name)
        self.vector_memory = VectorMemory(vector_size=4096)
        self.summary_service = SummaryService(model_name)

    def generate_response(self, message: str) -> str:
        # Step 1: Embed the user message
        vector = self.embedder.embed_text(message)

        # Step 2: Save it to vector memory
        self.vector_memory.add(vector, message)

        # Step 3: Search memory for meaning-related history
        related_memory = self.vector_memory.search(vector, k=3)

        # Step 4: Build context for Llama3
        system_context = "\n".join(related_memory)

        messages = [
            {"role": "system", "content": f"Relevant memory:\n{system_context}"},
            {"role": "user", "content": message}
        ]

        # Step 5: Get AI response
        response = ollama.chat(
            model=self.model_name,
            messages=messages
        )

        reply = response["message"]["content"]

        # Step 6: Store reply in simple memory
        self.memory_list.add_message("assistant", reply)

        return reply