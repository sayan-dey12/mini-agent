export const CONFIG_CATALOG = {
    modes: [
        {
            id: "stream",
            label: "Streaming",
        },
        {
            id: "full",
            label: "Full Response",
        },
    ],

    providers: [
        {
            id: "groq",
            label: "Groq",

            models: [
                {
                    id: "llama-3.3-70b-versatile",
                    label: "Llama 3.3 70B Versatile",
                },
                {
                    id: "llama-3.1-8b-instant",
                    label: "Llama 3.1 8B",
                },
                {
                    id: "openai/gpt-oss-20b",
                    label: "GPT OSS 20B",
                },
            ],
        },

        {
            id: "ollama",
            label: "Ollama",

            models: [
                {
                    id: "llama3.2",
                    label: "Llama 3.2",
                },
                {
                    id: "qwen3:0.6b",
                    label: "Qwen 3:0.6B",
                },
                {
                    id: "gemma:2b",
                    label: "Gemma:2B"
                }
            ],
        },
    ],

    temperature: {
        min: 0,
        max: 2,
        step: 0.1,
        default: 0.2,
    },
} as const;