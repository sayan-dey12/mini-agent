import { AgentConfig } from "@mini-agent/shared";

export interface IConfigService{
    load() : Promise<AgentConfig>;
    save(config: AgentConfig) : Promise<void>;
    update(partial: Partial<AgentConfig>) : Promise<void>;
    reset() : Promise<void>
}