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
        """
        Generate a chatbot response using:
        - short-term vector memory (FAISS)
        - long-term summary memory
        - semantic retrieval
        - local Llama 3 model via Ollama
        """

        # Step 1 — Embed the user message
        vector = self.embedder.embed_text(message)

        # Step 2 — Store the embedded message in vector memory
        self.vector_memory.add(vector, message)

        # Step 3 — Retrieve meaning-related past context
        related_memory = self.vector_memory.search(vector, k=3)
        related_context = "\n".join(related_memory)

        # Step 4 — Get long-term summary memory
        long_term_summary = self.summary_service.get_summary()

        # Step 5 — Build the full system message
        system_context = f"""
Long-term memory:
{long_term_summary}

Relevant short-term memory:
{related_context}
"""

        # Step 6 — Chat with Llama3 using memory-enhanced context
        messages = [
            {"role": "system", "content": system_context},
            {"role": "user", "content": message}
        ]

        response = ollama.chat(
            model=self.model_name,
            messages=messages
        )

        reply = response["message"]["content"]

        # Step 7 — Update long-term memory summary
        important_info = f"User: {message}\nAssistant: {reply}"
        self.summary_service.update_summary(important_info)

        # Step 8 — Also store assistant reply in simple list memory
        self.memory_list.add_message("assistant", reply)

        return reply
