interface ChatMessage {
    role: "system" | "user" | "assistant";
    content: string;
}

interface AgentRequest {
    messages: ChatMessage[];
}