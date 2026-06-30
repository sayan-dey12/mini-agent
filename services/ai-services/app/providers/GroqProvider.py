import os

from groq import Groq
from dotenv import load_dotenv

load_dotenv()

class GroqProvider:
    def __init__(self):
        self.client = Groq(
            api_key=os.environ.get("GROQ_API_KEY"),
        )

    def chat(self, messages, model="llama-3.3-70b-versatile"):
        response = self.client.chat.completions.create(
            model=model,
            messages=messages,
        )
        return response.choices[0].message.content
