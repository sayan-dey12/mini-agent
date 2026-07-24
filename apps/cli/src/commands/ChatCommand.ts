import readline from "node:readline/promises";
import { stdin, stdout } from "node:process";

import { ApplicationContainer } from "@mini-agent/core";
import type { ChatMessage } from "@mini-agent/shared";
import {Conversation} from "@mini-agent/agents";
import { FileConfigService } from "@mini-agent/core";
import {isCancel, select , text , spinner} from "@clack/prompts"
export class ChatCommand {

    async execute(): Promise<void> {

        const agent = ApplicationContainer.agent();
        const configService = new FileConfigService();
        const config = await configService.load()

        console.log("🤖 Mini Agent Chat");
        console.log("Type 'exit' to quit.\n");
    
        // const chooseMode = await select({
        //     message : "Choose chat mode...",
        //     options: [
        //         {value: 'stream' , label: 'Stream'},
        //         {value: 'full' , label: 'Full Response'},
        //         {value: 'exit', label: 'Exit'}
        //     ]
        // })

        const chooseMode = config.mode

        if (isCancel(chooseMode)){
            process.exit(0);
        }
        
        // const rl = readline.createInterface({
        //     input: stdin,
        //     output: stdout,
        // });

        const conversation = new Conversation();

        while (true) {

            // const input = await rl.question("You > ");
            const input = await text(
                {message: 'You'}    
            )

            if (isCancel(input) || input.toLowerCase() === "exit"){
                break;
            }

            conversation.addUserMessage(input);
            const messages: ChatMessage[] = conversation.getMessages();
            
            
            try {

                if (chooseMode == 'stream'){
                    // for streaming response //
                    process.stdout.write("🤖 AI  > ");

                    let hadError = false
                    let assistantResponse = "";
                    for await (const event of agent.stream({
                                                            messages,
                                                            config:{
                                                                provider: config.provider,
                                                                model:config.model,
                                                                temperature: config.temperature,
                                                            }})){
                        switch(event.type){
                            case "text":
                                process.stdout.write(event.data as string);
                                assistantResponse += event.data as string;
                                break;

                            case "tool_start":
                                console.log(
                                    `\n⚙ Runnign ${event.data as string}...`
                                );
                                break;

                            case "tool_end":
                                console.log(
                                    `\n✓ ${(event.data as {tool: string}).tool} completed`
                                );
                                break;

                            case "done":
                                // console.log();
                                break;
                        
                            case "error":
                                hadError = true;
                                console.log(`\n⚠ ${event.data as string}`);
                                break;
                            }
                    }
                    process.stdout.write("\n")
                    // console.log("\n");
                    if (hadError){
                        conversation.removeLastMessage();
                    }else{
                        conversation.addAssistantMessage(assistantResponse);
                    }
                
                }else if(chooseMode == 'full'){
                     //for execute function -> all response together//

                    const spin = spinner();
                    spin.start("Thinking...")
                    try {
                        const response = await agent.execute({
                            messages,
                            config:{
                                provider: config.provider,
                                model: config.model,
                                temperature: config.temperature,
                            }                                   
                        });
                        spin.stop("Response ready")
                        console.log("\n🤖 AI >", response.text);
                        conversation.addAssistantMessage(response.text);
                    } catch (error) {
                        spin.stop("Failed");
                        throw error;
                    }
                    
                }

                    
            } catch (error) {

                console.error('\n❌ AI service error');
                if (error instanceof Error){
                    console.log("\nError message: ",error.message);
                }
                console.log("\nPlease try again...\n");

                conversation.removeLastMessage();
                continue;
                
            }

           
        

        }

        // rl.close();

    }

}