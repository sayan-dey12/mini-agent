from dataclasses import dataclass , field
from typing import Optional

from app.runtime.ToolCall import ToolCall


@dataclass
class ProviderChunk:

    content: str = ""

    tool_calls: Optional[list[ToolCall]] = field(default_factory=list)

    finish_reason: str | None = None