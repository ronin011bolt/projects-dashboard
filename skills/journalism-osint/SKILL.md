---
name: journalism-osint
description: Run journalism and OSINT work with structured evidence handling, claim tracking, source logging, hypothesis control, and publication-ready synthesis. Use when researching a topic, investigating digital threats or actors, organizing findings, separating verified facts from leads, preparing briefings, or turning raw investigation material into concise outputs without contaminating evidence.
---

# Journalism OSINT

Work like an investigator, not a content blender.

Separate facts, claims, hypotheses, sources, and unanswered questions.

## Core rules

- Never present an unverified lead as a fact.
- Distinguish clearly between source material and interpretation.
- Preserve provenance whenever possible.
- Note confidence explicitly when uncertainty matters.
- Keep operationally sensitive details compartmentalized.

## Investigation workflow

### 1. Define the research target

Start by stating:
- topic or subject
- primary question
- scope
- time window
- expected output

If the request is broad, reduce it to one primary question first.

### 2. Build the working structure

Organize findings into these buckets:
- verified facts
- claims requiring verification
- hypotheses
- sources
- evidence/artifacts
- unknowns
- risks

Do not merge these buckets.

### 3. Track sources

For each meaningful source, capture:
- source name
- source type
- link or reference
- date accessed if relevant
- relevance
- trust caveats

Preferred source types:
- primary document
- first-hand statement
- official record
- platform content
- secondary reporting
- analyst/research commentary

### 4. Evaluate claims

For each important claim, ask:
- who is making it?
- what exactly is being claimed?
- what evidence supports it?
- what evidence contradicts it?
- what remains unverified?

Then assign a working state:
- verified
- likely
- unclear
- disputed
- false

### 5. Handle evidence carefully

When evidence is available, preserve:
- original wording
- timestamp/date if known
- platform/location
- context of collection

Summarize separately from the raw artifact.

### 6. Write the synthesis

When producing an output, structure it as:
- what is known
- what is likely
- what is not yet verified
- why it matters
- what should be checked next

## Output patterns

### Research brief

Use this structure:
- Topic: <topic>
- Main question: <question>
- Known:
  - <verified fact>
- Likely:
  - <supported but not fully confirmed>
- Unverified:
  - <lead or claim>
- Sources:
  - <source>
- Next checks:
  - <next step>

### Claim log

Use this structure:
- Claim: <exact claim>
- Source: <who/where>
- Status: <verified|likely|unclear|disputed|false>
- Supporting evidence:
  - <item>
- Contradicting evidence:
  - <item>
- Notes:
  - <item>

### Source note

Use this structure:
- Source: <name>
- Type: <type>
- Relevance: <why it matters>
- Reliability caveats: <biases/gaps>
- Key takeaways:
  - <item>

## Red flags

Slow down when you see:
- screenshots without provenance
- recycled claims with no primary source
- coordinated amplification
- identity assumptions based on weak indicators
- timeline gaps
- emotionally framed but weakly sourced narratives

## Decision rules

- Prefer primary sources over commentary.
- Prefer exact wording over paraphrase when precision matters.
- Prefer dated notes over vague memory.
- Prefer a smaller verified brief over a larger muddy one.
- If attribution is weak, say so plainly.

## For digital threat or actor research

Track separately:
- actor/entity
- behavior/activity
- infrastructure/accounts
- targets/audience
- timeline
- indicators
- confidence

Do not collapse actor assessment and evidence into one statement.

## When to ask the user

Ask only when one of these blocks progress:
- scope is too broad to investigate well
- requested output format is unclear
- a sensitive handling choice affects storage or publication
- multiple projects/investigations may be getting mixed together

Otherwise proceed.
