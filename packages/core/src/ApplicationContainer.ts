import { Agent } from "@mini-agent/agents";

import { MockProvider } from "@mini-agent/providers";

import type { IAgent } from "@mini-agent/agents";

export class ApplicationContainer {

    private static _agent : IAgent;

    static agent(): IAgent {
        if(!this._agent){
            const provider = new MockProvider();
            this._agent = new Agent(provider);

        }
        return this._agent;
    }

}