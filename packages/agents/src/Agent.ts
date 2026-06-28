import {IAgent} from "./interfaces/IAgent.js";
import {AgentRequest} from "./types/AgentRequest.js";
import {AgentResponse} from "./types/AgentResponse.js";

export class Agent implements IAgent{
    async execute(request: AgentRequest): Promise<AgentResponse> {
        return { text: `You said: ${request.message}` };
    }
}