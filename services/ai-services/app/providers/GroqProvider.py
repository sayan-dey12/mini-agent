import os

from groq import Groq
from dotenv import load_dotenv
from app.providers.base import ILLMProvider

load_dotenv()

class GroqProvider(ILLMProvider):
    def __init__(self):
        api_key = os.environ.get("GROQ_API_KEY")
        if not api_key:
            raise RuntimeError("GROQ_API_KEY environment variable is not set.")
        self.client = Groq(
            api_key=api_key,
        )

    def chat(self, messages, tools=None, model="llama-3.3-70b-versatile"):
        response = self.client.chat.completions.create(
            model=model,
            messages=messages,
            tools=tools
        )
        
        # message = response.choices[0].message
        # if message.tool_calls:
        #     print("Tool call detected: ", message.tool_calls)
        # else:
        #     return message.content
        
        return response.choices[0].message
            
    def stream(self , messages , model="llama-3.3-70b-versatile"):
        response = self.client.chat.completions.create(
            model=model,
            messages=messages,
            stream=True
        )
        for chunk in response:
            delta = chunk.choices[0].delta.content
            if delta:
                yield delta
        
