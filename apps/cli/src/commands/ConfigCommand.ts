import { CONFIG_CATALOG, FileConfigService } from "@mini-agent/core";
import { isCancel, select , text } from "@clack/prompts";
import { mind } from "gradient-string";

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
                    await this.changeProvider(configServices);
                    break;
                case "model":
                    await this.changeModel(configServices);
                    break;
                case "mode":
                    await this.changeMode(configServices);
                    break;                    
                case "temperature":
                    await this.changeTemperature(configServices);
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

    private async changeModel(configServices: FileConfigService){
        const config = await configServices.load();
        const provider = CONFIG_CATALOG.providers.find(
            p => p.id === config.provider
        )

        if(!provider) return;

        const choice = await select(
            {
                message: "Choose model...",
                options: provider.models.map(
                    model => (
                        {value: model.id , label: model.label}
                    )
                )
            }
        )
        if (isCancel(choice)) return;

        await configServices.update({
            model: choice
        })

    }

    private async changeProvider(configServices: FileConfigService){
        const choice = await select({
            message: "Choose provider...",
            options: CONFIG_CATALOG.providers.map(
                provider => (
                    {value: provider.id , label: provider.label}
                )
            )
        })

        if(isCancel(choice)){
            return;
        }

        const provider = CONFIG_CATALOG.providers.find( p => p.id == choice);

        await configServices.update(
            {
                provider: provider?.id,
                model: provider?.models[0].id
            }
        )
    }

    private async changeTemperature(configServices: FileConfigService){

        const limit = CONFIG_CATALOG.temperature;

        while(true){
            const value = await text({
                message: `Temperature (${limit.min} - ${limit.max})`,
                placeholder: `${limit.default}`,
            });

            if (isCancel(value)) {
                return;
            }

            const temperature = Number(value);

            if (Number.isNaN(temperature)) {
                console.log("Please enter a valid number.");
                continue;
            }

            if (temperature>limit.max || temperature<limit.min){
                console.log(`Temperature must be between ${limit.min} and ${limit.max}.`);
                continue;
            }

            const remainder = (temperature - limit.min) % limit.step;
            if(Math.abs(remainder) > Number.EPSILON){
                console.log(`Temperature must be in steps of ${limit.step}.`);
            continue;
            }

            await configServices.update({
                temperature: temperature,
            });
               
            return;
        }
    }
       
}