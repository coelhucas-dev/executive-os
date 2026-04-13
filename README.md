# Business OS for Obsidian

Business OS is a vault operating system for Brazilian entrepreneurs who run their week through meetings, follow-ups, decisions, projects, and content.

Instead of treating Obsidian as a generic note app, this repo sets up a structured operational environment that AI agents can use with narrow retrieval, atomic notes, and predictable routing rules.

## Who This Is For

- founders and operators
- executives with many parallel threads
- business owners who need continuity across meetings, delegated work, and decisions
- people using Codex or Claude as an operational copilot

## What It Solves

- scattered follow-ups across chats, calls, and notes
- unclear ownership between people, companies, projects, and meetings
- AI assistants reading too much context and still missing the important thread
- operational knowledge living only in your head

## What Ships In Public v1

- a public vault spec optimized for executive operations
- vault templates and dashboards
- `sb-` skills for Codex
- official adapters for `Codex` and `Claude`
- a CLI installer with public configuration for vault name and path

Experimental integrations:

- `Cursor`
- `Antigravity`

## Quick Start

Dry-run the full setup:

```bash
python3 installer/install.py \
  --dry-run \
  --tool codex \
  --tool claude \
  --vault-path /tmp/business-os \
  --generate-vault
```

Generate a new vault:

```bash
python3 installer/install.py \
  --vault-path /tmp/business-os \
  --generate-vault
```

Install the official adapters into your local tools:

```bash
python3 installer/install.py \
  --tool codex \
  --tool claude \
  --vault-path /tmp/business-os
```

If you want the CLI instructions to reference a different displayed vault name, pass `--vault-name`.

## First Week of Use

1. Capture loose items into `00 Inbox`.
2. Route people, companies, meetings, projects, and tasks into their owner folders.
3. Use `Today` and `This Week` as your operating dashboards.
4. Split durable decisions and follow-ups into their own notes instead of appending to history dumps.

## Product Notes

- Public launch scope is Brazil-first in language and onboarding.
- Folder names and metadata stay in English for consistency.
- Note titles and note bodies can be in Portuguese.

## Repo Layout

- `spec/`: public vault specification and manifest
- `templates/`: markdown templates and dashboards
- `skills/`: Codex skills prefixed with `sb-`
- `adapters/`: tool-specific instruction payloads
- `installer/`: installation and vault generation logic
- `docs/`: product-facing usage guidance

## Supporting Docs

- [Setup guiado por IA](docs/setup-guiado-por-ia.md)
- [Primeira semana](docs/primeira-semana.md)
- [Como a IA opera](docs/como-a-ia-opera.md)
- [Como usar com IA](docs/uso-com-ia.md)
- [Operações do dia a dia](docs/operacoes-do-dia-a-dia.md)
- [One-shot prompt](prompts/one-shot-business-os.md)
- [Prompt few-shot de onboarding para Claude](prompts/few-shot-onboarding-claude.md)
- [Exemplos few-shot de onboarding para Claude](prompts/few-shot-onboarding-claude-examples.md)
