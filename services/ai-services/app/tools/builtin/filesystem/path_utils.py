from pathlib import Path

from app.config.settings import WORKSPACE_ROOT


def resolve_workspace_path(path: str) -> Path:

    resolved = (WORKSPACE_ROOT / path).resolve()

    if WORKSPACE_ROOT not in resolved.parents and resolved != WORKSPACE_ROOT:
        raise ValueError(
            "Access outside workspace is not allowed."
        )

    return resolved