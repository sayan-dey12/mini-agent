from dataclasses import dataclass
from typing import Optional

from app.model.ToolCall import ToolCall


@dataclass
class ProviderMessage:
    role: str
    content: Optional[str]
    tool_calls: list[ToolCall]