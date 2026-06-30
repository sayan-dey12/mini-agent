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
    }
}