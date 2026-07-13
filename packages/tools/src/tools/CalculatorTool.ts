import type { ITool } from "../interfaces/ITool.js";
import type { ToolRequest } from "../types/ToolRequest.js";
import type { ToolResponse } from "../types/ToolResponse.js";

export class CalculatorTool implements ITool {

    readonly name = "calculator";

    readonly description =
        "Evaluates basic mathematical expressions.";

    async execute(
        request: ToolRequest
    ): Promise<ToolResponse> {

        try {

            const result = Function(
                `"use strict"; return (${request.input})`
            )();

            return {
                success: true,
                output: String(result),
            };

        } catch {

            return {
                success: false,
                output: "",
                error: "Invalid mathematical expression.",
            };

        }

    }

}