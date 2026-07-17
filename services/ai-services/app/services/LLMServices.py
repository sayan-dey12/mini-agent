from app.runtime.ReasoningEngine import ReasoningEngine
from app.tools.registry import ToolRegistry
from app.tools.executor import ToolExecutor
from app.tools.builtin.calculator import CalculatorTool
from app.providers.base import ILLMProvider
from app.tools.manager import ToolManager
from app.logging.RuntimeLogger import RuntimeLogger
from app.tools.loader import ToolLoader
class LLMService:

    def __init__(self, provider: ILLMProvider):

        self.registry = ToolRegistry()
        ToolLoader().load( self.registry )

        # self.registry.register(
        #     CalculatorTool()
        # )
        # self.registry.register(ReadFileTool())
        # self.registry.register(WriteFileTool())
        # self.registry.register(ListDirectoryTool())
        # self.registry.register(CreateDirectoryTool())

        self.executor = ToolExecutor(
            self.registry
        )
        
        self.tool_manager = ToolManager(
            self.executor
        )
        
        self.logger = RuntimeLogger()

        self.engine = ReasoningEngine(
            provider=provider,
            registry=self.registry,
            tool_manager=self.tool_manager,
            logger = self.logger,
        )

    def chat(self, messages):

        return self.engine.run(messages)

    def stream(self, messages):

        yield from self.engine.stream(messages)