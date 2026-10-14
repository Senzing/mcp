# Senzing MCP Server

Entity resolution for AI assistants and agents. The Senzing MCP server gives any
[Model Context Protocol](https://modelcontextprotocol.io) client grounded, current Senzing
knowledge — data mapping to the Senzing Entity Specification, SDK code for five languages,
documentation search, error troubleshooting and real sample data — without connecting to your
data or your Senzing instance.

| | |
|---|---|
| **Endpoint** | `https://mcp.senzing.com/mcp` (Streamable HTTP) |
| **Authentication** | None |
| **Registry name** | `com.senzing/mcp` ([official MCP registry](https://registry.modelcontextprotocol.io/v0/servers?search=com.senzing)) |
| **Cost** | Free |

## Connect

**VS Code** — `.vscode/mcp.json`:

```json
{
  "servers": {
    "senzing": { "type": "http", "url": "https://mcp.senzing.com/mcp" }
  }
}
```

**Claude Code:**

```bash
claude mcp add --transport http senzing https://mcp.senzing.com/mcp
```

**Claude Desktop, Cursor and other clients** — add to the client's MCP configuration:

```json
{
  "mcpServers": {
    "senzing": { "type": "http", "url": "https://mcp.senzing.com/mcp" }
  }
}
```

Clients that only speak stdio can use `npx -y mcp-remote https://mcp.senzing.com/mcp`.
If your network restricts egress, allow `mcp.senzing.com`.

## What it can do

| Area | Tools |
|------|-------|
| Map your data to Senzing | `mapping_workflow` (guided, step by step), `analyze_record`, `download_resource` |
| Install and code against the SDK | `sdk_guide`, `generate_scaffold` (Python, Java, C#, Rust, TypeScript), `get_sdk_reference` |
| Find answers | `search_docs`, `find_examples`, `explain_error_code` |
| Try it with real data | `get_sample_data` (CORD datasets and the Senzing truth set) |
| Report on results | `reporting_guide` |
| Get started / give feedback | `get_capabilities`, `submit_feedback` (including a free evaluation license) |

The server also provides ready-made prompts (map a data source, build an SDK integration,
troubleshoot an error, plan a proof of concept, and more). Mapping and analysis run on **your**
machine: the server returns the scripts and steps, and your data never leaves it.

## More from Senzing for AI tools

| | What it is | Where |
|---|---|---|
| **Claude Code plugin** | Senzing skills for Claude Code — install, analyze, build, demo, troubleshoot, recipes | [Senzing/senzing-claude-plugins](https://github.com/Senzing/senzing-claude-plugins) |
| **Agent Skill** | Portable skill that teaches any skill-capable agent how to use this server | [Senzing/senzing-mcp-skill](https://github.com/Senzing/senzing-mcp-skill) |
| **Ask Senzing** | Chat with the Senzing docs in your browser, powered by this server | [ask.senzing.com](https://ask.senzing.com) |
| **Distributed build** | The same server for air-gapped and private networks (stdio or HTTP), for licensed Senzing customers | [Contact Senzing](https://senzing.com/contact/) |

## Building your own agent

To keep an agent's Senzing answers grounded in this server rather than model training data, force
a tool call on the first turn (`tool_choice: any`), use a model that accepts forced tool use, and
keep extended thinking off. Details and measurements: [docs/grounded-agents.md](docs/grounded-agents.md).

## Terms

The hosted server is provided AS-IS, without warranty or support commitment. Do not send personal
data, credentials or other sensitive information; tool calls and parameters may be logged. See
the `senzing://terms-of-service` resource the server exposes.

Questions: [senzing.com/contact](https://senzing.com/contact/) · support@senzing.com
