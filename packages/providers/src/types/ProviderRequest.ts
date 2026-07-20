import { ChatMessage, GenerationConfig } from "@mini-agent/shared";
export interface ProviderRequest {
    messages: ChatMessage[];
    config? : GenerationConfig;
}