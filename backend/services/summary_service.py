import ollama

class SummaryService:
    def __init__(self, model_name="llama3"):
        self.model_name = model_name
        self.summary = ""

    def update_summary(self, new_info: str):
        prompt = f"""
        You are an AI assistant maintaining a long-term memory summary for a user.

        Here is the existing memory summary:
        {self.summary}

        New information to include:
        {new_info}

        Update the summary to include ALL important details.
        Keep it short, clear, and only store facts that matter long-term.
        """
        response = ollama.chat(
            model=self.model_name,
            messages=[{"role": "user", "content": prompt}]
        )
        self.summary = response["message"]["content"]

    def get_summary(self):
        return self.summary