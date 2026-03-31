# Dashboard Schema Reference

Use this reference when writing updates into the dashboard or preparing structured summaries.

## Core fields

Each project should map cleanly to:
- `id`
- `name`
- `status`
- `updatedAt`
- `summary`
- `tags[]`
- `activities[]`

## Activity object

Preferred shape:
- `date`
- `title`
- `note`

## Writing rules

- `id`: lowercase, hyphenated, stable
- `name`: human-readable title
- `status`: use the default project-ops status model unless the user changes it
- `summary`: one short paragraph max
- `tags[]`: 1-5 tags, lowercase when possible
- `activities[]`: newest-first if manually updating

## Good activity examples

- date: 2026-03-31
  title: Dashboard deployed
  note: Railway service linked correctly and live domain verified.

- date: 2026-03-31
  title: Source structure defined
  note: Project containers and tracking model established for separated workstreams.

## Avoid

- long essays in `summary`
- vague activity titles like "work" or "update"
- mixing blockers and milestones into generic notes
- creating multiple ids for the same project
