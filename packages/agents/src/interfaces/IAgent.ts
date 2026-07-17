import type {AgentResponse} from "../types/AgentResponse.js";
import type {AgentRequest} from "../types/AgentRequest.js";
import { StreamEvent } from "@mini-agent/shared";

export interface IAgent {
    execute(request: AgentRequest): Promise<AgentResponse>;
    stream(request: AgentRequest): AsyncIterable<StreamEvent>;
}
