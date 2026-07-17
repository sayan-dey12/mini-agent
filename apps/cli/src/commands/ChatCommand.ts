import readline from "node:readline/promises";
import { stdin, stdout } from "node:process";

import { ApplicationContainer } from "@mini-agent/core";
import type { ChatMessage } from "@mini-agent/shared";
import {Conversation} from "@mini-agent/agents";

export class ChatCommand {

    async execute(): Promise<void> {

        const agent = ApplicationContainer.agent();

        const rl = readline.createInterface({
            input: stdin,
            output: stdout,
        });

        console.log("Mini Agent Chat");
        console.log("Type 'exit' to quit.\n");

        const conversation = new Conversation();

        while (true) {

            const input = await rl.question("You > ");

            if (input.toLowerCase() === "exit") {
                break;
            }

            conversation.addUserMessage(input);
            const messages: ChatMessage[] = conversation.getMessages();
            
            // for streaming response // 

            process.stdout.write("AI  > ");

            let assistantResponse = "";
            for await (const chunk of agent.stream({messages})){
                process.stdout.write(chunk);
                assistantResponse += chunk;
            }

            console.log("\n");
            conversation.addAssistantMessage(assistantResponse);
            
            //for execute function -> all response together

            // const response = await agent.execute({
            //     messages,                                   
            // });
            // console.log(`AI  > ${response.text}\n`);
            // conversation.addAssistantMessage(response.text);

        

        }

        rl.close();

    }

}