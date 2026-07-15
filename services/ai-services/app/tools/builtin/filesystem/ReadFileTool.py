from app.tools.base import Tool
from app.tools.builtin.filesystem.path_utils import resolve_workspace_path


class ReadFileTool(Tool):

    name = "read_file"

    description = "Read a UTF-8 text file."

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

        path = resolve_workspace_path(
            arguments["path"]
        )

        return path.read_text(
            encoding="utf-8"
        )