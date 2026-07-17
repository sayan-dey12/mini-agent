from app.tools.base import Tool


class CalculatorTool(Tool):

    @property
    def name(self) -> str:
        return "calculator"

    @property
    def description(self) -> str:
        return (
            "Use this tool whenever the user asks to perform "
            "any arithmetic or mathematical calculation. "
            "The input must be a single arithmetic expression "
            "as a string. "
            "Return only the numerical result."
        )
    
    @property
    def parameters(self):
        return {
            "type": "object",
            "properties": {
                "expression": {
                    "type": "string",
                    "description": "Mathematical expression."
                }
            },
            "required": ["expression"]
        }


    def execute(self, arguments: dict) -> str:

        expression = arguments.get("expression", "")

        try:
            result = eval(expression, {}, {})
            return str(result)

        except Exception as error:
            return f"Error: {error}"