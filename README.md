<h1 align="center">Senzing MCP Server</h1>

<p align="center">
  <b>Entity resolution for Identity Intelligence: dedupe, match, and link people and company records across systems. Know who is who. Reveal hidden relationships.</b>
</p>

<p align="center">
  <a href="https://registry.modelcontextprotocol.io/v0/servers/com.senzing%2Fmcp/versions/latest"><img src="https://img.shields.io/badge/MCP_Registry-com.senzing%2Fmcp-000000?logo=modelcontextprotocol&logoColor=white" alt="MCP Registry: com.senzing/mcp"></a>
  <img src="https://img.shields.io/badge/Transport-Streamable_HTTP-0098FF" alt="Transport: Streamable HTTP">
  <img src="https://img.shields.io/badge/Auth-none-2EBC4F" alt="Authentication: none">
  <img src="https://img.shields.io/badge/Hosted_server-free_to_use-2EBC4F" alt="Hosted server: free to use">
</p>

<p align="center">
  <a href="#install">Install</a> ·
  <a href="#what-you-can-ask">What you can ask</a> ·
  <a href="#tools">Tools</a> ·
  <a href="#prompts">Prompts</a> ·
  <a href="#privacy-and-terms">Privacy and terms</a> ·
  <a href="#questions-and-feedback">Questions and feedback</a>
</p>

---

The [Senzing®](https://senzing.com) MCP server is a forward-deployed engineer in a box: ask it
anything about Senzing. Every answer is grounded in Senzing's own documentation and indexed code
rather than model training data. Use it to deduplicate lists, match or merge records across
sources, screen against watchlists, and produce the resolved entities that golden records for MDM
and customer 360 are built from.

Because it carries the full runbook, you don't drive it one step at a time. Hand your AI assistant
a few unmapped data files and describe what you want, and it can map your sources, deploy and load
Senzing, resolve and analyze the data, and build an interactive explorer over the results. What is
normally a multi-week integration becomes an afternoon, with no entity-resolution background
required.

You just ask. Then start answering who is who and who is related to whom, or build an
entity-resolved knowledge graph that surfaces the connections nobody declared. Every resolution
carries its evidence: why two records came together, or why they didn't. Your assistant can surface
that explanation for any match you question.

## Install

**Endpoint:** `https://mcp.senzing.com/mcp` (Streamable HTTP, no authentication) · **Registry
name:** `com.senzing/mcp` · The hosted server is free to use; Senzing software is licensed
separately.

[![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_Server-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect/mcp/install?name=senzing&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Fmcp.senzing.com%2Fmcp%22%7D)
[![Install in VS Code Insiders](https://img.shields.io/badge/VS_Code_Insiders-Install_Server-24bfa5?style=flat-square&logo=visualstudiocode&logoColor=white)](https://insiders.vscode.dev/redirect/mcp/install?name=senzing&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Fmcp.senzing.com%2Fmcp%22%7D&quality=insiders)
[![Install in Visual Studio](https://img.shields.io/badge/Visual_Studio-Install_Server-C16FDE?style=flat-square&logo=visualstudio&logoColor=white)](https://aka.ms/vs/mcp-install?%7B%22name%22%3A%22senzing%22%2C%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Fmcp.senzing.com%2Fmcp%22%7D)
[![Install in Cursor](https://img.shields.io/badge/Cursor-Install_Server-000000?style=flat-square&logo=cursor&logoColor=white)](https://cursor.com/install-mcp?name=senzing&config=eyJ1cmwiOiJodHRwczovL21jcC5zZW56aW5nLmNvbS9tY3AifQ==)

The buttons above install the server in one click. For other clients:

| Client | How to connect |
| --- | --- |
| **Claude** (claude.ai, Desktop, Cowork) | Install from the [Connectors Directory](https://claude.ai/directory/senzing), or **Customize → Connectors → + Add → Add custom connector** with the URL `https://mcp.senzing.com/mcp` (Team and Enterprise owners: **Organization settings → Connectors**) |
| **Claude Code** | `claude mcp add --transport http senzing https://mcp.senzing.com/mcp` |
| **OpenAI Codex** | `codex mcp add senzing --url https://mcp.senzing.com/mcp` |
| **Gemini CLI** | `gemini mcp add --transport http senzing https://mcp.senzing.com/mcp` |
| **VS Code** (manual) | `.vscode/mcp.json` — see below |
| **Cursor** (manual) | `.cursor/mcp.json` or `~/.cursor/mcp.json` — see below |
| **Kiro** | `.kiro/settings/mcp.json` or `~/.kiro/settings/mcp.json` — see below |
| **stdio-only clients** | Run it through `mcp-remote` — see below |
| **Any other MCP client** | Add a remote (Streamable HTTP) server with the URL `https://mcp.senzing.com/mcp` |

<details>
<summary><b>VS Code</b> — <code>.vscode/mcp.json</code></summary>

```json
{
  "servers": {
    "senzing": {
      "type": "http",
      "url": "https://mcp.senzing.com/mcp"
    }
  }
}
```

</details>

<details>
<summary><b>Cursor and Kiro</b> — <code>mcp.json</code></summary>

```json
{
  "mcpServers": {
    "senzing": {
      "url": "https://mcp.senzing.com/mcp"
    }
  }
}
```

</details>

<details>
<summary><b>stdio-only clients</b> — via <code>mcp-remote</code></summary>

```json
{
  "mcpServers": {
    "senzing": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://mcp.senzing.com/mcp"]
    }
  }
}
```

</details>

<details>
<summary><b>Codex</b> — <code>~/.codex/config.toml</code></summary>

```toml
[mcp_servers.senzing]
url = "https://mcp.senzing.com/mcp"
```

</details>

**Tip:** for the best experience, use an agentic coding client (Claude Code, Codex, Gemini CLI,
Cursor); if your environment restricts network access, allowlist `mcp.senzing.com`. Mapping your own
data and running Senzing need an assistant that can run code; questions, documentation search and
SDK code work in any client.

## What you can ask

- "Match these payment records to my customers and show me which ones didn't match."
- "Dedupe this list of people and show me the duplicates it found."
- "Here are three customer files from different systems. Build me a demo that finds the same people across them and lets me explore the matches."
- "Build me a service that matches incoming payment records to my customer master as they arrive."
- "How would entity resolution help with my problem, and what would it cost?"

## Tools

Each piece is also available on its own: SDK code in Python, Java and C# (official SDKs) and Rust
and TypeScript/Node.js (community SDKs), installation and deployment, error troubleshooting, V3→V4
migration, and pricing and ROI.

| Area | Tool | What it does |
| --- | --- | --- |
| **Start here** | `get_capabilities` | Overview of the server and suggested workflows |
| **Map your data** | `mapping_workflow` | Guided 8-step mapping of source data to the Senzing Entity Specification |
| | `analyze_record` | Analyzer script that validates your mapped records on your machine |
| | `download_resource` | Workflow resources, as a fallback when a URL can't be fetched |
| **Build with the SDK** | `sdk_guide` | Install and setup across Linux (apt/yum), macOS, Windows and Docker, for each SDK language |
| | `generate_scaffold` | SDK code from real indexed snippets: Python, Java, C# (official); Rust, TypeScript/Node.js (community) |
| | `get_sdk_reference` | Method signatures per language binding, flags, response schemas, V3→V4 migration |
| **Find answers** | `search_docs` | Full-text search of Senzing documentation |
| | `find_examples` | Code examples from the indexed Senzing GitHub repositories |
| | `explain_error_code` | Senzing error codes with causes and fixes |
| **Try it** | `get_sample_data` | Real sample data: CORD datasets (Las Vegas, London, Moscow) and the Senzing truth set |
| **Report** | `reporting_guide` | Reporting and visualization patterns: export, SQL analytics, data mart, dashboards, graph |
| **Feedback** | `submit_feedback` | Send feedback or request a free evaluation license |

## Prompts

The server also ships 31 ready-made prompts: workflow templates your client can offer as slash
commands or menu items. A few of them:

| Prompt | What it walks through |
| --- | --- |
| `why-senzing` | Explains Senzing for a given audience |
| `plan-a-poc` | Planning a proof of concept |
| `map-data-source` | Mapping a data source to the Entity Specification |
| `install-senzing` | Installing and configuring the SDK |
| `build-sdk-integration` | Building an SDK integration in your language |
| `troubleshoot-error` | Diagnosing a Senzing error code |
| `migrate-v3-to-v4` | Migrating from Senzing V3 to V4 |

Ask your assistant to list the Senzing prompts to see them all.

## More from Senzing

| Project | What it is | Where |
| --- | --- | --- |
| **Claude Code plugin** | Senzing skills for Claude Code: install, analyze, build, demo, troubleshoot, recipes and more | [Senzing/senzing-claude-plugins](https://github.com/Senzing/senzing-claude-plugins) |
| **Agent Skill** | Portable skill that teaches any skill-capable agent how to use this server | [Senzing/senzing-mcp-skill](https://github.com/Senzing/senzing-mcp-skill) |
| **Ask Senzing** | Chat with the Senzing docs in your browser, powered by this server | [ask.senzing.com](https://ask.senzing.com) |
| **Distributed build** | The same server for air-gapped and private networks, for licensed Senzing customers | [Contact Senzing](https://senzing.com/contact/) |
| **Building your own agent** | How to keep an API-driven agent's answers grounded in this server | [docs/grounded-agents.md](docs/grounded-agents.md) |

## Privacy and terms

- The server needs no live Senzing instance and no authentication. Your data files never leave
  your machine: mapping and resolution run locally, and only the tool arguments you send (field
  names, settings, questions) reach this server.
- Senzing is a headless developer library your assistant deploys locally in your environment.
  Mapping and resolution run there, never on Senzing's servers, and Senzing contains only the data
  you load into it.
- Do not send personal data, credentials or other sensitive information in prompts or tool
  arguments. Tool calls and their parameters may be logged.
- The hosted server is provided AS-IS, without warranty or support commitment. The server also
  exposes these terms as the `senzing://terms-of-service` resource.

## Questions and feedback

Use [senzing.com/contact](https://senzing.com/contact/) or <support@senzing.com>, or ask your
assistant to use `submit_feedback`.

See [LICENSE](LICENSE).
