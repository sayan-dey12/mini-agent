import logging

from app.logging.LogEvent import LogEvent


class RuntimeLogger:

    def __init__(self):

        self.logger = logging.getLogger("MiniAgent")

        if not self.logger.handlers:

            handler = logging.StreamHandler()

            formatter = logging.Formatter(
                "[%(levelname)s] %(message)s"
            )

            handler.setFormatter(formatter)

            self.logger.addHandler(handler)

            self.logger.setLevel(logging.INFO)

    def log(
        self,
        event: LogEvent,
    ) -> None:

        metadata = ""

        if event.metadata:

            metadata = " | " + ", ".join(
                f"{key}={value}"
                for key, value in event.metadata.items()
            )

        self.logger.info(
            f"[{event.category}] {event.message}{metadata}"
        )

    def reasoning(
        self,
        message: str,
        **metadata,
    ) -> None:

        self.log(
            LogEvent(
                category="Reasoning",
                message=message,
                metadata=metadata,
            )
        )

    def provider(
        self,
        message: str,
        **metadata,
    ) -> None:

        self.log(
            LogEvent(
                category="Provider",
                message=message,
                metadata=metadata,
            )
        )

    def tool(
        self,
        message: str,
        **metadata,
    ) -> None:

        self.log(
            LogEvent(
                category="Tool",
                message=message,
                metadata=metadata,
            )
        )

    def warning(
        self,
        message: str,
    ) -> None:

        self.logger.warning(message)

    def error(
        self,
        message: str,
    ) -> None:

        self.logger.error(message)