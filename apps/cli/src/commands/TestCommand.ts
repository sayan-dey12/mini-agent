import { Agent } from "@mini-agent/agents";
import type { AgentRequest } from "@mini-agent/agents";

const message: AgentRequest = {
    message: "Hello Agent!",
}

export class TestCommand {
  async execute(): Promise<void> {
    const agent = new Agent();

    const response = await agent.execute(message);

    console.log(response.text);
  }
}