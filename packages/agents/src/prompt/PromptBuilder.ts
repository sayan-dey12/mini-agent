import type { AgentRequest } from "../types/AgentRequest.js";
import type { ChatMessage } from "@mini-agent/shared";

export class PromptBuilder {

    build(
        request: AgentRequest
    ): ChatMessage[] {

        return [...request.messages];

    }

}