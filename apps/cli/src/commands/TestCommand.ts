import { Agent } from "@mini-agent/agents";
import type { AgentRequest } from "@mini-agent/agents";
import { MockProvider } from "@mini-agent/providers";

const message: AgentRequest = {
    message: "Hello Agent!",
}

export class TestCommand {
  async execute(): Promise<void> {
    const provider = new MockProvider();
    const agent = new Agent(provider);

    const response = await agent.execute(message);

    console.log(response.text);
  }
}