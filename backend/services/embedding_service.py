import ollama
import numpy as np

class embeddingService:
    def __init__(self,model_name="llama3"):
        self.model = model_name

    def embed_text(self,text:str):
        response = ollama.embeddings(
            model = self.model,
            prompt= text
        )
        return np.array(response["embedding"], dtype=np.float32)