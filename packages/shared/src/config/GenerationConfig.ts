export interface GenerationConfig {
    provider: "groq" | "ollama";
    model: string | undefined;
    temperature: number | undefined;
}