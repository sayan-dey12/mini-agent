import { AgentConfig } from "@mini-agent/shared";

export const config = {
    aiServiceUrl:
        process.env.AI_SERVICE_URL ??
        "http://127.0.0.1:8000",
};

export const DEFAULT_CONFIG : AgentConfig ={
    provider: "groq",
    model: "llama-3.3-70b-versatile",
    mode: "stream",
    temperature: 0.2,
}