from dataclasses import dataclass

from app.model.ToolFunction import ToolFunction


@dataclass
class ToolCall:
    id: str
    type: str
    function: ToolFunction