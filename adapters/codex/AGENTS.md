# Business OS Codex Adapter

Use the Business OS Obsidian vault as the default source of truth for operational knowledge unless the user clearly points to another source.

When the user asks about priorities, meetings, companies, people, projects, delegated work, follow-ups, decisions, content, note routing, or vault organization, assume the request should use the Business OS vault even if Obsidian is not named.

When operating in a Business OS vault:

- prefer the `sb-` skills over ad hoc vault guesses
- prefer `$sb-vault` first when the right specialist skill is not obvious
- when using the Obsidian CLI, select the vault with `obsidian vault='{{OBSIDIAN_VAULT_NAME}}' ...`
- do not use the positional form `obsidian "{{OBSIDIAN_VAULT_NAME}}" ...`
- route notes according to the public Business OS spec
- keep notes atomic
- search narrowly before reading broadly
- never create rolling dump files like `Meetings.md`, `Decisions.md`, or `Tasks.md`

Use the relevant skills:

- `$sb-vault`
- `$sb-core`
- `$sb-create-vault`
- `$sb-capture`
- `$sb-meeting-ingestion`
- `$sb-routing-retrieval`
- `$sb-tasks-followups`
- `$sb-decisions`
- `$sb-content-ops`
