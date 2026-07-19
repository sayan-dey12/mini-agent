import { ChatMessage } from "@mini-agent/shared";

export interface AgentRequest {
    messages: ChatMessage[];
     config?: {
        model: string;
        temperature: number;
    };
}