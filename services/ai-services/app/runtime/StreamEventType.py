from enum import Enum


class StreamEventType(str, Enum):

    TEXT = "text"

    TOOL_START = "tool_start"

    TOOL_END = "tool_end"

    STATUS = "status"

    ERROR = "error"

    DONE = "done"