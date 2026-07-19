export interface AgentConfig{
    provider: string;
    model: string;
    mode: 'stream' | 'full';
    temperature: number;
}