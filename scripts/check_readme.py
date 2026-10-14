#!/usr/bin/env python3
"""Check that every way README.md tells a client to connect points at the real endpoint.

The endpoint is read from server.json (remotes[0].url) — the same manifest the MCP registry
publishes — so the README cannot drift from it. Checks:

* every ```json / ```toml block parses;
* every one-click install link (VS Code, VS Code Insiders, Visual Studio, Cursor) decodes to a
  config whose URL is the endpoint;
* every https URL that mentions the endpoint's host is exactly the endpoint.

Exits 1 with one line per problem.
"""
import base64
import json
import pathlib
import re
import sys
import tomllib
import urllib.parse

ROOT = pathlib.Path(__file__).resolve().parent.parent
README = (ROOT / "README.md").read_text(encoding="utf-8")
ENDPOINT = json.loads((ROOT / "server.json").read_text(encoding="utf-8"))["remotes"][0]["url"]
HOST = urllib.parse.urlparse(ENDPOINT).netloc

problems: list[str] = []


def check_blocks() -> int:
    blocks = re.findall(r"^```(json|toml)\n(.*?)^```", README, flags=re.M | re.S)
    for lang, body in blocks:
        try:
            if lang == "json":
                json.loads(body)
            else:
                tomllib.loads(body)
        except (ValueError, tomllib.TOMLDecodeError) as err:
            problems.append(f"{lang} block does not parse: {err}\n{body}")
    return len(blocks)


def install_config(link: str) -> dict:
    parsed = urllib.parse.urlparse(link)
    query = urllib.parse.parse_qs(parsed.query)
    if parsed.netloc.endswith("vscode.dev"):
        return json.loads(query["config"][0])
    if parsed.netloc == "aka.ms":
        return json.loads(urllib.parse.unquote(parsed.query))
    if parsed.netloc == "cursor.com":
        return json.loads(base64.b64decode(query["config"][0]))
    raise ValueError(f"unknown install link host {parsed.netloc}")


def check_install_links() -> int:
    links = re.findall(
        r"https://(?:insiders\.)?vscode\.dev/redirect/mcp/install\?[^\s\"')]+"
        r"|https://aka\.ms/vs/mcp-install\?[^\s\"')]+"
        r"|https://cursor\.com/[a-z/]*install-mcp\?[^\s\"')]+",
        README,
    )
    for link in links:
        try:
            url = install_config(link).get("url")
        except (ValueError, KeyError, json.JSONDecodeError) as err:
            problems.append(f"install link does not decode ({err}): {link}")
            continue
        if url != ENDPOINT:
            problems.append(f"install link points at {url!r}, not {ENDPOINT}: {link}")
    return len(links)


def check_endpoint_mentions() -> int:
    mentions = re.findall(rf"https://{re.escape(HOST)}[^\s\"'`)<>\]]*", README)
    for url in mentions:
        if url.rstrip(".,") != ENDPOINT:
            problems.append(f"endpoint mention {url!r} is not {ENDPOINT}")
    return len(mentions)


blocks = check_blocks()
links = check_install_links()
mentions = check_endpoint_mentions()
if links == 0:
    problems.append("no one-click install links found — the pattern list is out of date")
for p in problems:
    print(f"FAIL: {p}")
print(f"{blocks} code blocks, {links} install links, {mentions} endpoint mentions checked "
      f"against {ENDPOINT}: {'FAILED' if problems else 'ok'}")
sys.exit(1 if problems else 0)
