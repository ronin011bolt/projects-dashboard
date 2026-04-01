# OpenClaw Backup Checklist

Use this before any reinstall, cleanup, migration, or risky repair.

## Required backup scope

Back up the full directory:

- `~/.openclaw/`

This is the preferred backup scope because it preserves both high-value content and operational state.

## Must-preserve items

### Workspace
- `~/.openclaw/workspace/`
- all project folders and files
- `SOUL.md`
- `USER.md`
- `IDENTITY.md`
- `AGENTS.md`
- `TOOLS.md`
- `memory/`
- `skills/`

### Agent/session state
- `~/.openclaw/agents/`

### Likely useful operational state
- OpenClaw config files under `~/.openclaw/`
- channel auth/session files
- local metadata/cache that may help continuity

## Backup outputs to produce

Create all of these:

1. Full dated archive of `~/.openclaw/`
2. Manifest of important files and sizes
3. Checksums for the archive
4. Optional second copy to another disk/cloud location

## Verification checklist

Before deleting or reinstalling anything, confirm:

- archive file exists
- archive size is non-trivial
- archive can be listed or tested
- manifest file exists
- checksum file exists
- at least one second copy exists if available

## Sensitive content warning

The backup may contain:
- memories
- identity files
- project data
- channel/session state
- auth-related local state

Treat the backup as sensitive.

## Minimum fallback set

If a full backup is impossible, preserve at least:

- `~/.openclaw/workspace/`
- `~/.openclaw/agents/`

But full `~/.openclaw/` is strongly preferred.

## Before-state snapshot

Capture and save command outputs for later comparison:

- `openclaw status`
- `openclaw update status`
- `openclaw security audit`

## Do not proceed until

- backup created
- backup verified
- restore path chosen
- reinstall path understood
