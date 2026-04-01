# OpenClaw Clean Reinstall Plan

## Goal

Perform a clean reinstall of OpenClaw while preserving Ronin Bolt's identity, memory, workspace, custom skills, and as much session/channel continuity as practical.

## Guiding principle

Back up first, reinstall second, restore in layers.

Do not rely on memory or assumptions during the reinstall. Preserve the full `~/.openclaw/` tree before deleting or replacing anything.

## Phase 1 — Preserve

### Primary backup target

- `~/.openclaw/`

This is the safest source-of-truth backup because it should include:
- workspace files
- memory
- agent/session state
- custom skills
- config
- auth/session state
- local metadata

### Most critical paths

- `~/.openclaw/workspace/`
- `~/.openclaw/agents/`

### Critical workspace files

- `SOUL.md`
- `USER.md`
- `IDENTITY.md`
- `AGENTS.md`
- `TOOLS.md`
- `memory/`
- `skills/`
- all project folders and files

### Backup outputs to create

- one dated archive of `~/.openclaw/`
- one manifest file with key paths and checksums
- optionally one second copy on another disk or cloud destination

## Phase 2 — Export diagnostics

Before reinstalling, capture a small before-state snapshot:

- `openclaw status`
- `openclaw update status`
- `openclaw security audit`
- OpenClaw version
- linked channel state
- current workspace location

This makes validation easier after reinstall.

## Phase 3 — Clean reinstall

### High-level steps

1. Stop OpenClaw services and active processes.
2. Confirm the backup archive exists and is readable.
3. Preserve a frozen copy of current state.
4. Remove the existing OpenClaw installation.
5. Optionally remove the existing `~/.openclaw/` working state after backup verification.
6. Reinstall OpenClaw fresh.
7. Launch once to confirm the clean install starts.
8. Do not begin broad reconfiguration yet.

### Two reinstall styles

#### A. Reinstall app, keep data directory
- lower risk
- faster
- may preserve old configuration issues

#### B. Full clean reinstall with selective restore
- cleanest result
- best for eliminating state/config drift
- requires disciplined restore order

Recommended: **B**, only after a verified full backup of `~/.openclaw/`.

## Phase 4 — Restore in layers

### Layer 1 — Identity and memory

Restore first:
- `~/.openclaw/workspace/`

Priority within workspace:
- `SOUL.md`
- `USER.md`
- `IDENTITY.md`
- `AGENTS.md`
- `TOOLS.md`
- `memory/`
- `skills/`
- project files

This restores Ronin's identity and memory.

### Layer 2 — Agent/session continuity

Restore next:
- `~/.openclaw/agents/`

This may recover:
- agent state
- session metadata
- conversation continuity
- cached runtime state

### Layer 3 — Config and channel/auth state

Restore selectively:
- configuration files
- channel auth/session state
- provider-specific cached state

Reason for caution:
- if the original issue lives in config or state, restoring everything blindly can reintroduce it

Best practice:
1. restore workspace
2. test
3. restore agents
4. test
5. restore config/auth only as needed

## What matters most to preserve

Priority order:
1. workspace
2. memory
3. identity
4. skills
5. project files
6. agent/session state
7. config/auth state

## Risks

Usually safe to preserve:
- workspace
- identity
- long-term memory
- daily notes
- project files
- custom skills

Potentially fragile across versions:
- live sessions
- cached runtime state
- provider auth/session internals
- old config that may contain the bug you are trying to eliminate

## Success criteria

A successful reinstall means:
- OpenClaw launches cleanly
- workspace path is correct
- Ronin identity is intact
- memory is still present
- custom skills still exist
- project files are present
- sessions work
- WhatsApp is linked or can be cleanly relinked
- no critical startup errors

## Recommended deliverables

- backup checklist
- backup script
- reinstall guide
- restore verification checklist
