from pathlib import Path
import importlib

from app.tools.base import Tool
from app.tools.registry import ToolRegistry
from app.logging.RuntimeLogger import RuntimeLogger

class ToolLoader:

    def __init__(self):

        self.root = (
            Path(__file__)
            .parent
            / "builtin"
        )
        self.logger = RuntimeLogger()
        
    IGNORED = {
        "__init__.py",
        "path_utils.py",
    }

    def load(
        self,
        registry: ToolRegistry,
    ):

        for file in self.root.rglob("*.py"):

            if file.name in self.IGNORED:
                continue

            module = (
                file.relative_to(
                    Path(__file__).parent.parent
                )
                .with_suffix("")
                .as_posix()
                .replace("/", ".")
            )

            module = f"app.{module}"

            imported = importlib.import_module(
                module
            )

            for obj in vars(imported).values():

                if (
                    isinstance(obj, type)
                    and issubclass(obj, Tool)
                    and obj is not Tool
                ):

                    registry.register(
                        obj()
                    )
                    self.logger.tool(
                        "Loaded tool",
                        tool=obj().name
                    )