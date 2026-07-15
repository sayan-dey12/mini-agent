from dataclasses import dataclass
from typing import Any


@dataclass
class ProviderRequest:

    messages: list[dict]

    tools: list[dict] | None = None

    model: str | None = None

    temperature: float | None = None

    stream: bool = False