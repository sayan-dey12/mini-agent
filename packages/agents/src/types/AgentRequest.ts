import { ChatMessage } from "@mini-agent/shared";
import { GenerationConfig } from "@mini-agent/shared"
export interface AgentRequest {
    messages: ChatMessage[];
    config?: GenerationConfig;
}