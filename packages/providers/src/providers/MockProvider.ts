import type {IProvider} from "../interfaces/IProvider.js";
import type {ProviderRequest} from "../types/ProviderRequest.js";
import type {ProviderResponse} from "../types/ProviderResponse.js";

export class MockProvider implements IProvider{
    async generate(request: ProviderRequest): Promise<ProviderResponse>{
        return {text: `Mock response for message: ${request.message}`};
    }
}