import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

class ChatClient:
    def __init__(self, model: str = "llama-3.3-70b-versatile"):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        self.model = model

    def send(self, messages: list) -> str:
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.7,
                max_tokens=500,
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return f"[Error] Could not reach the API: {e}"