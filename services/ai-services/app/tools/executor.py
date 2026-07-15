from app.tools.registry import ToolRegistry
from app.model.ToolResult import ToolResult

class ToolExecutor:

    def __init__(self, registry: ToolRegistry):

        self.registry = registry

    def execute(
        self,
        tool_name: str,
        arguments: dict,
    ) -> ToolResult:

        tool = self.registry.get(tool_name)

        if tool is None:
            return ToolResult(
                success = False,
                output = None,
                error = f"Unknown tool: {tool_name}"
            )
            
        output = tool.execute(arguments)
        try:
             return ToolResult(
                success = True,
                output = output,
            ) 
        except Exception as e:
            return ToolResult(
                success = False,
                output = None,
                error = str(e)
            )
       
