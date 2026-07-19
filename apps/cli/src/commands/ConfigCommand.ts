import { FileConfigService } from "@mini-agent/core";
import { isCancel, select } from "@clack/prompts";

export class ConfigCommand{
    async execute(): Promise<void>{
        const configServices = new FileConfigService();

        while(true){
            const config = await configServices.load();

            const choice = await select({
                message: "Configuration",
                options:[
                    {value:"provider", label: "Provider"},
                    {value:"model", label:"Model"},
                    {value: "mode", label: "Mode"},
                    {value: "temperature", label:"Temperature"},
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
                    console.log("Model....");
                    break;
                case "mode":
                    console.log("Mode....");
                    break;                    
                case "temperature":
                    console.log("Temperature...");
                    break;
                    
            }
        }
    }
}