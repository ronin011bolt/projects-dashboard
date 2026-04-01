# OpenClaw Restore and Verification Checklist

Use this after a clean reinstall.

## Restore order

Restore in layers, testing after each layer.

### Layer 1 — Workspace
Restore:
- `~/.openclaw/workspace/`

Confirm:
- `SOUL.md` present
- `USER.md` present
- `IDENTITY.md` present
- `AGENTS.md` present
- `TOOLS.md` present
- `memory/` present
- `skills/` present
- project files present

### Layer 2 — Agents
Restore:
- `~/.openclaw/agents/`

Confirm:
- agent directories present
- sessions visible if compatible
- no immediate startup errors

### Layer 3 — Config/auth state
Restore only if needed:
- config files
- channel auth/session data
- provider-specific local state

Confirm:
- WhatsApp channel visible
- link state preserved or relink path clear
- no recurring old config errors

## Post-restore checks

Run or verify:
- OpenClaw starts successfully
- `openclaw status`
- workspace path is correct
- expected memory files are available
- custom skills are available
- active projects remain intact
- channel connectivity is healthy

## Success criteria

The restore is successful if:
- Ronin identity is intact
- memory persists
- project files are present
- custom skills are available
- OpenClaw is stable
- channels work or can be relinked cleanly

## If something breaks

Fallback sequence:
1. keep the fresh install
2. restore only workspace
3. retest
4. restore only agents
5. retest
6. restore config/auth selectively
7. avoid mass-copying unknown broken state back into the fresh install

## Notes

If session continuity does not fully survive, preserving workspace + memory still preserves the important continuity.
