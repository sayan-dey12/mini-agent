from app.tools.base import Tool


class ToolRegistry:

    def __init__(self):

        self._tools: dict[str, Tool] = {}

    def register(self, tool: Tool):

        self._tools[tool.name] = tool

    def get(self, name: str) -> Tool | None:

        return self._tools.get(name)

    def list(self):

        return list(self._tools.values())   
    
    
    def schemas(self) -> list[dict]:

        return [

            {
                "type": "function",
                "function": {
                    "name": tool.name,
                    "description": tool.description,
                    "parameters": tool.parameters,
                },
            }

            for tool in self.list()

        ]