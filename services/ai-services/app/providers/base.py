from abc import ABC, abstractmethod
from app.runtime.ProviderRequest import ProviderRequest
from app.runtime.ProviderResponse import ProviderResponse

class ILLMProvider(ABC):

    @abstractmethod
    def chat(self, request: ProviderRequest) -> ProviderResponse:
        ...

    @abstractmethod
    def stream(self, messages , tools=None , model="llama-3.3-70b-versatile"):
        ...