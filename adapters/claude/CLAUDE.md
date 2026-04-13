<!-- BEGIN BUSINESS OS MANAGED BLOCK -->
# Business OS Claude Code Adapter

Use Business OS as the default operating system for the user's durable business and life context.

## Trigger Rule

Do not wait for the user to mention Obsidian, notes, or the vault explicitly.

If the request touches any durable operational context, route through Business OS first. This includes:

- companies, clients, investors, partners, vendors
- people, hiring, delegation, follow-ups, waiting-for
- meetings, calls, transcripts, summaries
- projects, apps, launches, execution planning
- decisions, tradeoffs, priorities
- weekly planning, daily execution, coordination
- content, publishing, audience, brand
- executive life admin with ongoing operational consequence

These requests must be treated as Business OS requests even when phrased in natural language like:

- "how is my company doing?"
- "help me plan my app"
- "what do I need to follow up on today?"
- "what came out of that meeting?"
- "organize my week"

## Required Operating Behavior

When a request touches durable operational context:

1. Treat the Obsidian vault as the default source of truth unless the user clearly points elsewhere.
2. Use Business OS routing before answering from memory.
3. If the right workflow is not obvious, route through `sb-vault` first.
4. Use Obsidian CLI to read, verify, create, update, or route the real vault context.
5. Start from the closest dashboard or home note, then search the narrowest relevant folder, then open only the notes needed.
6. Prefer action over abstract advice.
7. Prefer creating a new atomic note over appending to large history files.
8. Never create rolling dump files like `Meetings.md`, `Decisions.md`, or `Tasks.md`.

## Skill Routing

Use the relevant Business OS skills whenever available:

- `sb-vault` as the default router when the correct specialist path is not obvious
- `sb-core` for structure and ownership rules
- `sb-create-vault` for vault setup and bootstrap
- `sb-capture` for inbox capture and triage
- `sb-meeting-ingestion` for meetings and transcripts
- `sb-routing-retrieval` for note placement and narrow retrieval
- `sb-tasks-followups` for tasks, delegated work, and waiting-for
- `sb-decisions` for durable decision notes
- `sb-content-ops` for content and publishing workflows

## Query vs Create Rule

- If the user asks about an existing business or life thread, check the vault first.
- If the user introduces a new durable thread, structure it into the vault instead of leaving it in chat only.
- If the user asks for conceptual guidance with no operational consequence, a direct answer is allowed.

## Failure Policy

If Business OS tools or the vault cannot be accessed or validated:

- fail closed for operational claims
- say you could not verify the state in the vault
- do not invent company status, project status, meeting outcomes, or task state
- if useful, provide a clearly labeled provisional answer plus the next vault action needed

## Obsidian CLI

When using Obsidian CLI:

- use `obsidian vault='{{OBSIDIAN_VAULT_NAME}}' ...`
- do not use the positional form `obsidian "{{OBSIDIAN_VAULT_NAME}}" ...`

Treat the public templates and vault manifest as the canonical public structure.
<!-- END BUSINESS OS MANAGED BLOCK -->
