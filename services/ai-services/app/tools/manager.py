from app.runtime.ToolResult import ToolResult
from app.tools.executor import ToolExecutor


class ToolManager:

    def __init__(
        self,
        executor: ToolExecutor,
    ):
        self.executor = executor

    def execute(
        self,
        tool_name: str,
        arguments: dict,
    ) -> ToolResult:

        return self.executor.execute(
            tool_name,
            arguments,
        )