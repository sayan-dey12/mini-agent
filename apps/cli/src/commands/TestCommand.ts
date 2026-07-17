//import { Agent } from "@mini-agent/agents";
import type { AgentRequest } from "@mini-agent/agents";
//import { MockProvider } from "@mini-agent/providers";
//import {AgentFactory} from "@mini-agent/agents";
import { ApplicationContainer } from "@mini-agent/core";

const message: AgentRequest = {
  messages:[
    {
      role: "user",
      content: "Hello Agent!",
    }
  ]
}

export class TestCommand {
  async execute(): Promise<void> {
    const agent = ApplicationContainer.agent();

    const response = await agent.execute(message);

    console.log(response.text);
  }
}