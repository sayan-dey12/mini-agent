export interface ChatMessage {
    role: "system" | "user" | "assistant";
    content: string;
}

export interface ProviderRequest {
    messages: ChatMessage[];
}