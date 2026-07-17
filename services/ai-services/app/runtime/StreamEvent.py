from dataclasses import dataclass
from typing import Any, Literal


@dataclass
class StreamEvent:
    """
    High-level runtime event.

    The CLI, REST API,
    Telegram Bot,
    VS Code extension,
    etc. consume these events.
    """

    type: Literal[
        "text",
        "tool_start",
        "tool_end",
        "status",
        "error",
        "done",
    ]

    data: Any