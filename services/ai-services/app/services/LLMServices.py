from app.runtime.ReasoningEngine import ReasoningEngine
from app.tools.registry import ToolRegistry
from app.tools.executor import ToolExecutor
from app.tools.builtin.calculator import CalculatorTool
from app.providers.base import ILLMProvider
from app.tools.manager import ToolManager

class LLMService:

    def __init__(self, provider: ILLMProvider):

        self.registry = ToolRegistry()

        self.registry.register(
            CalculatorTool()
        )

        self.executor = ToolExecutor(
            self.registry
        )
        
        self.tool_manager = ToolManager(
            self.executor
        )

        self.engine = ReasoningEngine(
            provider=provider,
            registry=self.registry,
            tool_manager=self.tool_manager,
        )

    def chat(self, messages):

        return self.engine.run(messages)

    def stream(self, messages):

        yield from self.engine.stream(messages)