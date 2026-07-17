// @ts-nocheck

import type {IProvider} from "./interfaces/IProvider.js";
import {MockProvider} from "./providers/MockProvider.js";

export class ProviderFactory{
    static createProvider():IProvider{
        return new MockProvider();
    }
}