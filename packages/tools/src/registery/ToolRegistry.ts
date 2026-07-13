import type {ITool} from "../interfaces/ITool.js";

export class ToolRegistry{
    private readonly tools: Map<string , ITool> = new Map<string , ITool>();

    register(tool: ITool):void{
        this.tools.set(tool.name,tool);
    }

    get(name:string):ITool | undefined{
        return this.tools.get(name);
    }

    has(name:string):boolean{
        return this.tools.has(name);
    }

    list():ITool[]{
        return [...this.tools.values()];
    }
}