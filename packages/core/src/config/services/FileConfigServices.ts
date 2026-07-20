import { promises as fs } from "node:fs";
import os from "node:os";
import path from "node:path";

import { DEFAULT_CONFIG } from "../config.js";
import type { AgentConfig } from "@mini-agent/shared";
import type { IConfigService } from "../interfaces/IConfigService.js";

export class FileConfigService implements IConfigService {

    private readonly configDir: string;
    private readonly configPath: string;

    constructor() {
        this.configDir = path.join(os.homedir(), ".mini-agent");
        this.configPath = path.join(this.configDir, "config.json");
    }

    async load(): Promise<AgentConfig> {

        await this.ensureConfigExists();

        const raw = await fs.readFile(this.configPath, "utf8");

        try {
            const parsed = JSON.parse(raw) as Partial<AgentConfig>;
            return {...DEFAULT_CONFIG , ...parsed}; 
        } catch (error) {
            await this.reset();
            return DEFAULT_CONFIG;
        }
        
    }

    async save(config: AgentConfig): Promise<void> {

        await this.ensureConfigExists();

        await fs.writeFile(
            this.configPath,
            JSON.stringify(config, null, 2),
            "utf8"
        );
    }

    async update(partial: Partial<AgentConfig>): Promise<void> {

        const current = await this.load();

        const updated: AgentConfig = {
            ...current,
            ...partial,
        };

        await this.save(updated);
    }

    async reset(): Promise<void> {

        await this.save(DEFAULT_CONFIG);
    }

    private async ensureConfigExists(): Promise<void> {

        await fs.mkdir(this.configDir, {
            recursive: true,
        });

        try {

            await fs.access(this.configPath);

        } catch {

            await fs.writeFile(
                this.configPath,
                JSON.stringify(DEFAULT_CONFIG, null, 2),
                "utf8"
            );

        }
    }

}