import type {IProvider} from "../interfaces/IProvider.js";
import type {ProviderRequest} from "../types/ProviderRequest.js";
import type {ProviderResponse} from "../types/ProviderResponse.js";

export class MockProvider implements IProvider{
    async generate(request: ProviderRequest): Promise<ProviderResponse>{
        const lastUserMessage = [...request.messages].reverse().find(msg =>msg.role === "user");
        return {text: `Mock response for message: ${lastUserMessage?.content ?? "No user message found"}`};
    }
    async *stream(
        request: ProviderRequest
    ): AsyncIterable<string> {

        const lastUserMessage =
            request.messages.findLast(
                m => m.role === "user"
            );

        const text = `Mock response for ${lastUserMessage?.content ?? ""}`;

        for (const word of text.split(" ")) {

            await new Promise(resolve =>
                setTimeout(resolve, 150)
            );

            yield word + " ";

        }

    }
}