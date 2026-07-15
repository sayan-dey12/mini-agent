from app.tools.base import Tool
from app.tools.builtin.filesystem.path_utils import resolve_workspace_path


class WriteFileTool(Tool):

    name = "write_file"

    description = "Write UTF-8 text to a file."

    parameters = {
        "type": "object",
        "properties": {
            "path": {
                "type": "string"
            },
            "content": {
                "type": "string"
            }
        },
        "required": [
            "path",
            "content"
        ]
    }

    def execute(self, arguments):

        path = resolve_workspace_path(
            arguments["path"]
        )

        path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        path.write_text(
            arguments["content"],
            encoding="utf-8"
        )

        return f"File written: {path.name}"