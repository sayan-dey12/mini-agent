import { ChatMessage } from "@mini-agent/shared";
export interface ProviderRequest {
    messages: ChatMessage[];
    model?: string;
    temperature?: string;
}