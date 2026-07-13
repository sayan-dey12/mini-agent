import type { AgentRequest } from "../types/AgentRequest.js";
import type { ChatMessage } from "@mini-agent/shared";
import { SystemPromptProvider } from "./SystemPromptProvider.js";

export class PromptBuilder {

    private readonly systemPrompt : SystemPromptProvider = new SystemPromptProvider();
    build(
        request: AgentRequest
    ): ChatMessage[] {

        return [this.systemPrompt.getSystemPrompt(),
            ...request.messages];

    }

}