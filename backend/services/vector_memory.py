import faiss
import numpy as np

class VectorMemory:
    def __init__(self, vector_size=4096):
        self.index = faiss.IndexFlatL2(vector_size)
        self.texts = []

    def add(self, vector, text):
        self.index.add(np.array([vector])) # pyright: ignore[reportCallIssue]
        self.texts.append(text)

    def search(self, vector, k=3):
        distances, indices = self.index.search(np.array([vector]), k) # pyright: ignore[reportCallIssue]
        results = []
        for idx in indices[0]:
            if idx < len(self.texts):
                results.append(self.texts[idx])
        return results