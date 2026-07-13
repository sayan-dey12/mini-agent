import { Agent } from "@mini-agent/agents";

import { MockProvider } from "@mini-agent/providers";
import {PythonProvider} from "@mini-agent/providers";

import type { IAgent } from "@mini-agent/agents";
import {config} from "./config/config.js";

export class ApplicationContainer {

    private static _agent : IAgent;

    static agent(): IAgent {
        if(!this._agent){
            const provider = new MockProvider();
           //const provider = new PythonProvider(config.aiServiceUrl);
            this._agent = new Agent(provider);

        }
        return this._agent;
    }

}