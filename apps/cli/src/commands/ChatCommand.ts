import readline from "node:readline/promises";
import { stdin, stdout } from "node:process";
import {AgentFactory} from "@mini-agent/agents";

// import { Agent } from "@mini-agent/agents";
// import { MockProvider } from "@mini-agent/providers";

export class ChatCommand {

    async execute(): Promise<void> {

        const agent = AgentFactory.create();

        const rl = readline.createInterface({
            input: stdin,
            output: stdout,
        });

        console.log("Mini Agent Chat");
        console.log("Type 'exit' to quit.\n");

        while (true) {

            const message = await rl.question("You > ");  //returns a promise

            if (message.toLowerCase() === "exit") {
                break;
            }

            const response = await agent.execute({
                message,
            });

            console.log(`AI  > ${response.text}\n`);

        }

        rl.close();

    }

}