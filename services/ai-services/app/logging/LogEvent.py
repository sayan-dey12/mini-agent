from dataclasses import dataclass, field
from typing import Any


@dataclass
class LogEvent:
    category: str
    message: str
    metadata: dict[str, Any] = field(default_factory=dict)