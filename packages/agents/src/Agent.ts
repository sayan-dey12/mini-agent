import type {IAgent} from "./interfaces/IAgent.js";
import type {AgentRequest} from "./types/AgentRequest.js";
import type {AgentResponse} from "./types/AgentResponse.js";

import type {IProvider} from "@mini-agent/providers";
import {PromptBuilder} from "./prompt/PromptBuilder.js";
import type { StreamEvent } from "@mini-agent/shared";
export class Agent implements IAgent{
    constructor(
        private provider: IProvider,
        private readonly promptBuilder: PromptBuilder = new PromptBuilder()
    ){}
    
    async execute(request: AgentRequest): Promise<AgentResponse> {
        const prompt = this.promptBuilder.build(request);
        const response = await this.provider.generate(
            {
                messages: prompt,
                config: {
                    model: request.config?.model,
                    temperature: request.config?.temperature
                }
               
            
            }
        )
        const fullResponse: AgentResponse = { text: response.text };
        return fullResponse;
    }
    async *stream(
        request: AgentRequest
    ): AsyncIterable<StreamEvent> {

        const prompt = this.promptBuilder.build(request);

        for await (
            const event of this.provider.stream({
                messages: prompt,
            })
        ) {

            yield event;

        }

    }
}