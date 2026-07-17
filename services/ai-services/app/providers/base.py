from abc import ABC, abstractmethod
from app.runtime.ProviderRequest import ProviderRequest
from app.runtime.ProviderResponse import ProviderResponse
from typing import Iterator
from app.runtime.ProviderChunk import ProviderChunk

class ILLMProvider(ABC):

    @abstractmethod
    def chat(self, request: ProviderRequest) -> ProviderResponse:
        ...

    @abstractmethod
    def stream(self, request: ProviderRequest) -> Iterator[ProviderChunk]:
        ...