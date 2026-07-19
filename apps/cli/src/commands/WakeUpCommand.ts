import { select , isCancel } from "@clack/prompts";
import figlet from "figlet";
import gradient from "gradient-string";
import { ConfigCommand } from "./ConfigCommand.js";
import { ChatCommand } from "./ChatCommand.js";

export class WakeUpCommand{

    async execute(): Promise<void>{

        console.clear();
        // Huge Banner
        console.log(
        gradient.instagram.multiline(
            figlet.textSync("Mini Agent", {
            font: "ANSI Shadow",
            horizontalLayout: "default",
            })
        )
        );

        console.log();

        const choice = await select({
            message: "Select your option...",
            options: [
                {value: 'chat' , label: 'Chat'},
                {value: 'config' , label: 'Configuration'},
                {value: 'exit' , label: 'Exit'},
            ]
        })

        if (isCancel(choice) || choice === "exit") {
                return;
        }

        switch(choice){
            case "config":
                await new ConfigCommand().execute();
                break;
            case "chat":
                await new ChatCommand().execute();
                break;
        }
    }
}