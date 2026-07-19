import { CONFIG_CATALOG, FileConfigService } from "@mini-agent/core";
import { isCancel, select } from "@clack/prompts";

export class ConfigCommand{
    async execute(): Promise<void>{
        const configServices = new FileConfigService();

        while(true){
            const config = await configServices.load();

            const choice = await select({
                message: "Configuration",
                options:[
                    {value:"provider", label: `Provider (${config.provider})`},
                    {value:"model", label:`Model (${config.model})`},
                    {value: "mode", label: `Mode (${config.mode})`},
                    {value: "temperature", label:`Temperature (${config.temperature})`},
                    {value: "back" , label: "Back"}
                ]
            })

            if(isCancel(choice) || choice == "back"){
                return;
            }
            
            switch(choice){
                case "provider":
                    console.log("Provider.....");
                    break;
                case "model":
                    console.log("Model...");
                    break;
                case "mode":
                    await this.changeMode(configServices);
                    break;                    
                case "temperature":
                    console.log("Temperature...");
                    break;
                    
            }
        }
    }

    private async changeMode(configServices: FileConfigService){
        // const choice = await select({
        //     message: "Choose chat mode..",
        //     options: [
        //         {value: "stream", label: "Stream"},
        //         {value: "full", label: "Full Response"},
        //         {value: "exit", label: "Exit"},
        //     ]
        // })

        const choice = await select({
            message: "Choose chat mode...",
            options: CONFIG_CATALOG.modes.map(mode => ({
                value: mode.id, label: mode.label
            }))
        })

        if(isCancel(choice) || choice == "exit"){
                return;
        }
        if(choice == "full"){
            await configServices.update({mode: "full"});
        }
        else if(choice == "stream"){
            await configServices.update({mode: "stream"});
        }

    }
}