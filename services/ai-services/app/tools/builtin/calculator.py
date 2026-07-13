from app.tools.base import Tool


class CalculatorTool(Tool):

    @property
    def name(self) -> str:
        return "calculator"

    @property
    def description(self) -> str:
        return "Evaluate mathematical expressions."

    def execute(self, arguments: dict) -> str:

        expression = arguments.get("expression", "")

        try:
            result = eval(expression, {}, {})
            return str(result)

        except Exception as error:
            return f"Error: {error}"