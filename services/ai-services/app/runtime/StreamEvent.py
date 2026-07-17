from dataclasses import dataclass
from typing import Any, Literal
from app.runtime.StreamEventType import StreamEventType

@dataclass
class StreamEvent:
    """
    High-level runtime event.

    The CLI, REST API,
    Telegram Bot,
    VS Code extension,
    etc. consume these events.
    """

    type: StreamEventType

    data: Any