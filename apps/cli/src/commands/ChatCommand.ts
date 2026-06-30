import readline from "node:readline/promises";
import { stdin, stdout } from "node:process";

import { ApplicationContainer } from "@mini-agent/core";
import type { ChatMessage } from "@mini-agent/agents";

export class ChatCommand {

    async execute(): Promise<void> {

        const agent = ApplicationContainer.agent();

        const rl = readline.createInterface({
            input: stdin,
            output: stdout,
        });

        console.log("Mini Agent Chat");
        console.log("Type 'exit' to quit.\n");

        const messages: ChatMessage[] = [];

        while (true) {

            const input = await rl.question("You > ");

            if (input.toLowerCase() === "exit") {
                break;
            }

            messages.push({
                role: "user",
                content: input,
            });

            const response = await agent.execute({
                messages,
            });

            console.log(`AI  > ${response.text}\n`);

            messages.push({
                role: "assistant",
                content: response.text,
            });

        }

        rl.close();

    }

}