from abc import ABC, abstractmethod
from app.model.ProviderRequest import ProviderRequest
from app.model.ProviderResponse import ProviderResponse

class ILLMProvider(ABC):

    @abstractmethod
    def chat(self, request: ProviderRequest) -> ProviderResponse:
        ...

    @abstractmethod
    def stream(self, messages , tools=None , model="llama-3.3-70b-versatile"):
        ...