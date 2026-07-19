export interface AgentConfig{
    provider: string;
    model: string;
    mode: 'stream' | 'full' | 'exit';
    temperature: number;
}