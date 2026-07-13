from app.tools.registry import ToolRegistry


class ToolExecutor:

    def __init__(self, registry: ToolRegistry):

        self.registry = registry

    def execute(
        self,
        tool_name: str,
        arguments: dict,
    ) -> str:

        tool = self.registry.get(tool_name)

        if tool is None:
            raise ValueError(
                f"Unknown tool: {tool_name}"
            )

        return tool.execute(arguments)