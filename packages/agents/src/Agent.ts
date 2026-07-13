import type {IAgent} from "./interfaces/IAgent.js";
import type {AgentRequest} from "./types/AgentRequest.js";
import type {AgentResponse} from "./types/AgentResponse.js";

import type {IProvider} from "@mini-agent/providers";
import {PromptBuilder} from "./prompt/PromptBuilder.js";
export class Agent implements IAgent{
    constructor(
        private provider: IProvider,
        private readonly promptBuilder: PromptBuilder = new PromptBuilder()
    ){}
    
    async execute(request: AgentRequest): Promise<AgentResponse> {
        const prompt = this.promptBuilder.build(request);
        const response = await this.provider.generate(
            {messages: prompt}
        )
        const fullResponse: AgentResponse = { text: response.text };
        return fullResponse;
    }
    async *stream(
        request: AgentRequest
    ): AsyncIterable<string> {

        const prompt = this.promptBuilder.build(request);

        for await (
            const chunk of this.provider.stream({
                messages: prompt,
            })
        ) {

            yield chunk;

        }

    }
}