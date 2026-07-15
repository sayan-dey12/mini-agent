from dataclasses import dataclass

from app.runtime.ProviderMessage import ProviderMessage


@dataclass
class ProviderResponse:

    message: ProviderMessage