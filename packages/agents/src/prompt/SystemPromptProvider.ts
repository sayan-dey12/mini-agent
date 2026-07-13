import type { ChatMessage } from "@mini-agent/shared";

export class SystemPromptProvider {

    getSystemPrompt(): ChatMessage {

        return {
            role: "system",
            content:
                "You are Mini Agent, an accurate, concise and professional AI assistant.",
        };

    }

}