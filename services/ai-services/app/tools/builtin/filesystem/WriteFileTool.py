from app.tools.base import Tool
from app.tools.builtin.filesystem.path_utils import (
    resolve_workspace_path,
)


class WriteFileTool(Tool):

    name = "write_file"

    description = (
        "Create a text file or overwrite an existing text file. "
        "Use this tool whenever the user asks to create, edit, "
        "or save a file."
    )

    parameters = {
        "type": "object",
        "properties": {
            "path": {
                "type": "string",
            },
            "content": {
                "type": "string",
            },
        },
        "required": [
            "path",
            "content",
        ],
    }

    def execute(self, arguments):

        path = resolve_workspace_path(
            arguments["path"]
        )

        if path.exists() and path.is_dir():

            raise IsADirectoryError(
                f'"{path.name}" already exists as a directory.'
            )

        path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        path.write_text(
            arguments["content"],
            encoding="utf-8",
        )

        return f'Created "{path.name}".'