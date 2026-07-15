from app.tools.base import Tool
from app.tools.builtin.filesystem.path_utils import resolve_workspace_path


class CreateDirectoryTool(Tool):

    name = "create_directory"

    description = (
        "Create a directory (folder). "
        "Never use this tool to create files."
    )

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

        directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        return "Directory created."