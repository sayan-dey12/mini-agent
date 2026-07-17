from __future__ import annotations

import json

from app.runtime.StreamEvent import StreamEvent


class StreamEventSerializer:
    @staticmethod
    def serialize(
        event: StreamEvent,
    ) -> str:
        """
        Converts a StreamEvent into a JSON line.
        """

        return (
            json.dumps(
                {
                    "type": event.type.value,
                    "data": event.data,
                }
            )
            + "\n"
        )