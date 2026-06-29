import type {IAgent} from "./interfaces/IAgent.js";
import type {AgentRequest} from "./types/AgentRequest.js";
import type {AgentResponse} from "./types/AgentResponse.js";

import type {IProvider} from "@mini-agent/providers";
export class Agent implements IAgent{
    constructor(private provider: IProvider){}

    async execute(request: AgentRequest): Promise<AgentResponse> {
        const response = await this.provider.generate(
            {message: request.message}
        )
        const fullResponse: AgentResponse = { text: response.text };
        return fullResponse;
    }
}