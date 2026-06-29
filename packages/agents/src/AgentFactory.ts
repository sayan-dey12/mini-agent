import type {IAgent} from "./interfaces/IAgent.js";
import {Agent} from "./Agent.js";
import {ProviderFactory} from "@mini-agent/providers";

export class AgentFactory{
    static create():IAgent{
        const provider = ProviderFactory.createProvider();
        return new Agent(provider)
    }
}
