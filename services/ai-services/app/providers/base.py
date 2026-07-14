from abc import ABC, abstractmethod


class ILLMProvider(ABC):

    @abstractmethod
    def chat(self, messages):
        ...

    @abstractmethod
    def stream(self, messages):
        ...