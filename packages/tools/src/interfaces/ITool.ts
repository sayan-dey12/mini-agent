import type { ToolRequest } from "../types/ToolRequest.js";
import type { ToolResponse } from "../types/ToolResponse.js";

export interface ITool {

    readonly name: string;

    readonly description: string;

    execute(
        request: ToolRequest
    ): Promise<ToolResponse>;

}