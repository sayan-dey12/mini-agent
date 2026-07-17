import type {ProviderRequest} from "../types/ProviderRequest.js";
import type {ProviderResponse} from "../types/ProviderResponse.js";
import type { StreamEvent } from "@mini-agent/shared";
export interface IProvider {
    generate(request: ProviderRequest): Promise<ProviderResponse>;
    stream(request: ProviderRequest): AsyncIterable<StreamEvent>;
}