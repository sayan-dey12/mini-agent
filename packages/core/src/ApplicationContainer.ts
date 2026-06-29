import { Agent } from "@mini-agent/agents";

import { MockProvider } from "@mini-agent/providers";

import type { IAgent } from "@mini-agent/agents";

export class ApplicationContainer {

    static agent(): IAgent {

        const provider = new MockProvider();

        return new Agent(provider);

    }

}