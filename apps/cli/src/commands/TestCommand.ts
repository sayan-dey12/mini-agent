import { Agent } from "@mini-agent/agents";


export class TestCommand {
  async execute(): Promise<void> {
    const agent = new Agent();

    const response = await agent.execute({
      message: "Hello Agent!",
    });

    console.log(response.text);
  }
}