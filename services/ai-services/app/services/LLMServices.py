from app.runtime.ReasoningEngine import ReasoningEngine
from app.tools.registry import ToolRegistry
from app.tools.executor import ToolExecutor
from app.tools.builtin.calculator import CalculatorTool
from app.providers.base import ILLMProvider
from app.tools.manager import ToolManager
from app.logging.RuntimeLogger import RuntimeLogger
from app.tools.loader import ToolLoader
from app.schemas.chat import GenerationConfig
class LLMService:

    def __init__(self):

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
            registry=self.registry,
            tool_manager=self.tool_manager,
            logger = self.logger,
        )

    def chat(self,messages: list[dict] , config: GenerationConfig ):

        return self.engine.run(
            messages=messages, 
            config=config,)

    def stream(self, messages: list[dict] , config: GenerationConfig):

        yield from self.engine.stream(
            messages=messages,
            config= config,)