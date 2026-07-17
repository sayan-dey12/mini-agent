from dataclasses import dataclass
from typing import Optional

from app.runtime.ToolCall import ToolCall


@dataclass
class ProviderChunk:

    content: str = ""

    tool_calls: Optional[list[ToolCall]] = None

    finish_reason: str | None = None