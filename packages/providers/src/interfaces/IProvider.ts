import type {ProviderRequest} from "../types/ProviderRequest.js";
import type {ProviderResponse} from "../types/ProviderResponse.js";

export interface IProvider {
    generate(request: ProviderRequest): Promise<ProviderResponse>;
    stream(request: ProviderRequest): AsyncIterable<string>;
}