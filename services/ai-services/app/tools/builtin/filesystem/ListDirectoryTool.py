from app.tools.base import Tool
from app.tools.builtin.filesystem.path_utils import resolve_workspace_path


class ListDirectoryTool(Tool):

    name = "list_directory"

    description = "List files and directories."

    parameters = {
        "type": "object",
        "properties": {
            "path": {
                "type": "string"
            }
        },
        "required": ["path"]
    }

    def execute(self, arguments):

        directory = resolve_workspace_path(
            arguments["path"]
        )

        return [
            item.name
            for item in directory.iterdir()
        ]