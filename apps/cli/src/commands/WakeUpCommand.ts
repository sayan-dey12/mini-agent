import { select , isCancel } from "@clack/prompts";
import chalk from "chalk";
import boxen from "boxen";
import figlet from "figlet";
import gradient from "gradient-string";
import logSymbols from "log-symbols";

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
    }
}