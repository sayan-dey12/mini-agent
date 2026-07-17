export type StreamEventType =
    | "text"
    | "tool_start"
    | "tool_end"
    | "status"
    | "error"
    | "done";
export interface StreamEvent {
    type: StreamEventType;
    data: unknown;
}