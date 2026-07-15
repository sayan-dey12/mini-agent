from dataclasses import dataclass

from app.runtime.ToolFunction import ToolFunction


@dataclass
class ToolCall:
    id: str
    type: str
    function: ToolFunction