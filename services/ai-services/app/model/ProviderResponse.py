from dataclasses import dataclass

from app.model.ProviderMessage import ProviderMessage


@dataclass
class ProviderResponse:

    message: ProviderMessage