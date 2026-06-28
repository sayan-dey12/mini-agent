import type {AgentResponse} from "../types/AgentResponse.js";
import type {AgentRequest} from "../types/AgentRequest.js";

export interface IAgent {
    execute(request: AgentRequest): Promise<AgentResponse>;
}
