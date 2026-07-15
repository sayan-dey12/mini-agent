import logging


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

    def info(self, message: str):
        self.logger.info(message)

    def warning(self, message: str):
        self.logger.warning(message)

    def error(self, message: str):
        self.logger.error(message)

    # ---------- Runtime Categories ----------

    def reasoning(self, message: str):
        self.logger.info(f"[Reasoning] {message}")

    def provider(self, message: str):
        self.logger.info(f"[Provider] {message}")

    def tool(self, message: str):
        self.logger.info(f"[Tool] {message}")