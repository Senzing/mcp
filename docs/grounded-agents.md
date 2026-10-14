# Building a grounded agent on the Senzing MCP server

If you call a model API directly and give it this server's tools (a chatbot, a support
assistant, a pipeline step), four settings decide whether its Senzing answers come from this
server or from the model's training data:

1. **Force a tool call on the first turn** (`tool_choice: {"type": "any"}`). Without it, a model
   may answer from memory, which is how outdated V3 method names, invented flags and wrong prices
   get in. Later turns can use `auto` so the model can write its answer.
2. **Check that the model accepts forced tool use.** Some do not: in 2026-10,
   `claude-sonnet-5-5`, `claude-opus-5-5` and `claude-fable-5-1` reject `tool_choice` `any`/`tool`
   with HTTP 400. One request tells you; a request per thinking × `tool_choice` combination shows which work.
3. **Turn extended thinking off** (`thinking: {"type": "disabled"}`). In our measurements it
   added latency and did not make answers more grounded. The off value differs by model, and
   models that cannot turn thinking off cannot be forced to call a tool with it on except in
   `adaptive` mode.
4. **Verify after every deploy by asking a real question.** An HTTP 200 from your service does
   not prove the model call works.

Measured 2026-10-14 on the Ask Senzing chatbot: 25 real Senzing questions, every Senzing claim in
each answer checked against the tool results the bot received, forced tool use, thinking off
unless noted. This is one bot and one system prompt; re-measure before relying on it.

| Model | Ungrounded claims | Verified wrong facts | Median first response |
|-------|-------------------|----------------------|-----------------------|
| `claude-haiku-5-5` | 6.5% | 0 | 4.5 s |
| `claude-sonnet-5` | 10.5% | 0 | 6.8 s |
| `claude-sonnet-5`, adaptive thinking | 12.2% | 4 | 7.1 s |
| `claude-sonnet-4-6` | 18.4% | 2 | 13.4 s |

These settings apply to an application you control. An assistant such as Claude Code or Claude
Desktop picks its own model and tool behaviour; the server's instructions already tell it to use
these tools for every Senzing question.
