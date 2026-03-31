---
name: memory-confidentiality
description: Decide what information should be remembered, where it should be stored, and what should remain compartmentalized or omitted. Use when handling sensitive information, updating memory files, separating project-local vs long-term knowledge, deciding whether a detail is safe to retain, or preventing confidential context from leaking across projects, chats, or outputs.
---

# Memory Confidentiality

Remember deliberately. Store minimally. Separate aggressively.

## Core rules

- Do not store sensitive details by default.
- Do not mix information across projects.
- Do not move project-local detail into long-term memory unless clearly durable and safe.
- Do not assume that useful means storable.
- When in doubt, summarize at a higher level or ask.

## Storage layers

Use these layers deliberately:

### 1. Ephemeral working context

Use for:
- temporary reasoning
- intermediate synthesis
- volatile leads
- details that do not need persistence

Default here first.

### 2. Daily memory

Use `memory/YYYY-MM-DD.md` for:
- what happened today
- decisions taken today
- work performed
- short-term follow-up context
- lightweight project notes if not sensitive

Do not put raw secrets here.

### 3. Long-term memory

Use `MEMORY.md` only for:
- durable preferences
- stable working patterns
- important long-term decisions
- recurring constraints
- identity/context that helps future work across sessions

Do not use it as a project dump.

### 4. Project-local records

Use project-specific storage when details are:
- investigation-specific
- operationally sensitive
- only relevant to one project
- likely to contaminate other work if generalized

Prefer project-local storage over global memory.

## Retention test

Before writing anything persistent, ask:
- Is it durable?
- Is it necessary?
- Is it safe?
- Is it project-specific?
- Would storing it create leakage risk later?

If any answer is problematic, reduce detail or avoid writing it.

## What usually belongs in memory

Safe candidates:
- communication preferences
- work style preferences
- stable tool/setup choices
- recurring boundaries
- durable project-management rules
- stable identity/context

## What usually does not belong in memory

Avoid storing unless explicitly approved:
- passwords
- tokens
- raw personal data
- unpublished sensitive findings
- source identities that require protection
- operational details that increase exposure risk
- speculative allegations
- unverified claims as if they were facts

## Write-down rules

When writing daily memory:
- keep entries factual
- prefer summaries over raw dumps
- avoid secrets and credentials
- note decisions, not every keystroke

When writing long-term memory:
- store distilled patterns, not chronology
- merge duplicates
- keep language stable and concise
- remove stale or risky detail when noticed

## Project separation rules

When a detail belongs to one project:
- keep it inside that project’s notes/dashboard/record
- do not echo it into unrelated summaries
- do not use it as assumed context elsewhere

If cross-project synthesis is requested:
- synthesize only at the level necessary
- avoid transferring sensitive specifics
- label uncertainty and scope clearly

## Output rules

When asked to summarize sensitive work:
- default to least exposure
- omit unnecessary identifiers
- redact operational details when possible
- separate public-safe summary from private notes if needed

## Escalation cases

Ask before storing when information includes:
- private personal details
- confidential source information
- credentials or access details
- legal/reputational risk
- sensitive investigation material that may later be published

## Compact decision model

Use this shorthand:
- `remember globally` = durable, safe, broadly useful
- `remember locally` = useful but project-bound
- `log today only` = short-term continuity
- `do not store` = sensitive, unnecessary, or risky
