from dataclasses import dataclass
from typing import Any

@dataclass
class ToolResult:
    success: bool
    output: Any
    error: str | None = None