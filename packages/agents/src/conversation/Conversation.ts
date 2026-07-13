import type { ChatMessage } from "@mini-agent/shared";

export class Conversation {

    private readonly messages: ChatMessage[] = [];

    addUserMessage(content: string): void {
        this.messages.push({
            role: "user",
            content,
        });
    }

    addAssistantMessage(content: string): void {
        this.messages.push({
            role: "assistant",
            content,
        });
    }

    addSystemMessage(content: string): void {
        this.messages.push({
            role: "system",
            content,
        });
    }

    getMessages(): ChatMessage[] {
        return [...this.messages];
    }

    clear(): void {
        this.messages.length = 0;
    }

    removeLastMessage(): void{
        this.messages.pop();
    }

    size(): number{
        return this.messages.length;
    }

    isEmpty(): boolean{
        return this.messages.length === 0;
    }
}