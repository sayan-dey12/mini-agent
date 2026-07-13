import type { IProvider } from "../interfaces/IProvider.js";
import type { ProviderRequest } from "../types/ProviderRequest.js";
import type { ProviderResponse } from "../types/ProviderResponse.js";

export class PythonProvider implements IProvider {
    constructor(
        private readonly baseUrl: string
    ) {}

    async generate(
        request: ProviderRequest
    ): Promise<ProviderResponse> {

        const controller = new AbortController();
        const timeout = setTimeout(()=>{
            controller.abort();
        }, 20000); // 20 seconds timeout
        
        try {
            const response = await fetch(
                `${this.baseUrl}/chat`,
                {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify({
                        messages: request.messages,
                    }),
                    signal: controller.signal,
                }
            );
             if (!response.ok) {
                throw new Error(
                    `Python AI Service returned ${response.status}`
                );
            }
            const data: ProviderResponse = await response.json();

            return {
                text: data.text,
            };

        } catch (error) {
            
            if (error instanceof Error) {

                if (error.name === "AbortError") {
                    throw new Error(
                        "AI Service request timed out."
                    );
                }

                throw new Error(
                    `Unable to communicate with AI Service: ${error.message}`
                );
            }

            throw new Error(
                "Unknown error while communicating with AI Service."
            );

        } finally {

            clearTimeout(timeout);

        }
        
    }

    async *stream(
        request: ProviderRequest
    ): AsyncIterable<string> {

        const controller = new AbortController();

        const timeout = setTimeout(
            () => controller.abort(),
            10000
        );

        try {

            const response = await fetch(
                `${this.baseUrl}/chat/stream`,
                {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify({
                        messages: request.messages,
                    }),
                    signal: controller.signal,
                }
            );

            if (!response.ok) {
                throw new Error(
                    `AI Service returned ${response.status}`
                );
            }

            if (!response.body) {
                throw new Error(
                    "Response body is empty."
                );
            }

            const reader = response.body.getReader();
            const decoder = new TextDecoder();

            while (true) {

                const { done, value } =
                    await reader.read();

                if (done) {
                    break;
                }

                yield decoder.decode(
                    value,
                    { stream: true }
                );

            }

        } finally {

            clearTimeout(timeout);

        }

    }
}