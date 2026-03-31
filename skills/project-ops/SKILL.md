---
name: project-ops
description: Manage multiple projects with strict separation, consistent naming, status tracking, milestone planning, blockers, and dashboard-ready updates. Use when creating a new project, organizing project work, logging progress, defining next actions, preparing weekly/project summaries, or deciding where new information belongs without contaminating other projects.
---

# Project Ops

Manage work as distinct projects. Preserve boundaries. Keep updates short, structured, and reusable.

## Core rule

Treat each project as its own container.

Never mix across projects unless the user explicitly asks for a cross-project synthesis.

For each project, maintain:
- name
- short id
- status
- summary
- activities
- milestones
- blockers
- next actions
- references/links if relevant

## Default status model

Use one of these unless the user asks for a different model:
- planning
- backlog
- active
- paused
- blocked
- done

Prefer `blocked` over vague language when something cannot move.

## Workflow

### 1. Identify or create the project

Ask or infer:
- project name
- project id
- current status
- one-line purpose

If the project already exists, work inside that project only.

If the request is ambiguous across multiple projects, stop and ask which project it belongs to.

### 2. Classify the incoming information

Place each new item into one of these buckets:
- activity update
- milestone
- blocker
- next action
- decision
- note/reference

Do not dump everything into a generic note.

### 3. Produce a compact update

When logging progress, prefer this structure:
- what changed
- why it matters
- what is blocked
- next action

Keep it short enough to fit into dashboards or chat updates.

### 4. Preserve separation

Before writing or summarizing, check:
- does this belong to one project only?
- is there any detail from another project leaking in?
- is the wording reusable in a dashboard without extra context?

If leakage is present, rewrite.

## Output patterns

### New project record

Use this structure:

- Name: <project name>
- ID: <short-id>
- Status: <status>
- Summary: <one sentence>
- Milestones:
  - <milestone>
- Blockers:
  - <blocker or none>
- Next actions:
  - <next action>

### Activity update

Use this structure:

- Date: <YYYY-MM-DD>
- Title: <short action title>
- Note: <1-3 sentence update>
- Status change: <optional>
- Next: <optional next action>

### Project snapshot

Use this structure:

- Project: <name>
- Status: <status>
- Summary: <brief state>
- Current focus:
  - <item>
- Blockers:
  - <item or none>
- Next:
  - <item>

## Decision rules

- Prefer concise, direct wording.
- Prefer one source of truth per project.
- Prefer updating an existing project record over creating duplicates.
- Prefer explicit next actions over abstract statements.
- If a project has too many unrelated threads, split it.

## When using a dashboard

If a dashboard exists, convert work into fields that fit the dashboard model:
- summary must stay brief
- activities should be atomic
- tags should be minimal and useful
- statuses should be standardized

Do not invent a new schema unless necessary.

## When to ask the user

Ask only when one of these is unclear:
- which project this belongs to
- whether to create a new project
- whether a cross-project summary is intended
- whether sensitive details should be stored

Otherwise proceed.
