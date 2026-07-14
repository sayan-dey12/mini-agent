from abc import ABC, abstractmethod


class ILLMProvider(ABC):

    @abstractmethod
    def chat(self, messages , tools=None):
        ...

    @abstractmethod
    def stream(self, messages , tools=None , model="llama-3.3-70b-versatile"):
        ...