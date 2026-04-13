# Business OS Vault Spec

## Purpose

Business OS is an executive vault designed for AI-assisted operation. It is optimized for:

- narrow retrieval
- atomic notes
- durable relationships through links
- deterministic routing rules
- reusable installation across users and tools

## Core Principles

1. Folders define ownership.
2. Links define relationships.
3. Use one note per entity, event, or decision.
4. Avoid growing accumulator files like `Meetings.md`, `Decisions.md`, or `Tasks.md`.
5. Agents must read the smallest relevant note set possible.
6. Dashboards and home notes summarize and point outward; they do not become history dumps.
7. Folder names, template names, and metadata keys stay in English.
8. Note titles and note bodies may use any language.

## Top-Level Structure

- `00 Inbox`
- `01 Dashboards`
- `02 Daily`
- `03 Reviews`
- `10 People`
- `20 Companies`
- `30 Projects`
- `40 Meetings`
- `50 Content`
- `60 Knowledge`
- `70 Tasks`
- `80 Routines`
- `90 Personal Ops`
- `95 Life Modules`
- `99 Templates`
- `90 Archive`

## Ownership Rules

- `10 People`: one note per person
- `20 Companies`: one folder per company with atomic child notes
- `30 Projects`: one folder per project
- `40 Meetings`: one note per meeting, usually partitioned by date
- `50 Content`: one note per content piece; platform strategy lives separately
- `60 Knowledge`: one note per evergreen concept or playbook
- `70 Tasks`: one note per task cluster, follow-up thread, or recurring workflow
- `80 Routines`: one note per routine
- `90 Personal Ops`: one note per high-leverage operational thread

## Retrieval Rules

Agents should:

1. Start from the relevant dashboard or home note when available.
2. Search the narrowest relevant folder before broad vault reads.
3. Open only the atomic notes needed for the task.
4. Prefer creating a new atomic note instead of appending to a large history file.
5. Keep dashboards and index notes lightweight.

## Metadata

Common frontmatter keys:

```yaml
type:
status:
created:
updated:
tags:
```

Optional keys:

```yaml
company:
project:
people:
platform:
owner:
meeting_date:
```

## Note Types

- `dashboard`
- `person`
- `company`
- `project`
- `meeting`
- `decision`
- `content-piece`
- `knowledge-note`
- `task-cluster`
- `routine`
- `personal-op`
- `daily-note`
- `journal-entry`
- `index`

## Specialist Behavior

- Capture lands in `00 Inbox` unless a narrower destination is already known.
- Meeting ingestion creates one meeting note, then separate decision and task notes when needed.
- Decision handling uses one note per decision.
- Task handling uses one note per task cluster, delegated thread, or recurring workflow.
- Content ops uses platform strategy notes plus one-note-per-content-piece pipeline notes.

## Optional Modules

`95 Life Modules` is optional and may include:

- journaling
- reflection
- religion
- learning
- relationships
- long-term vision

These are modules, not mandatory core operating areas.
