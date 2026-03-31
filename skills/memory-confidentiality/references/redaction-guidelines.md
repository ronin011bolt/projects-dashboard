# Redaction Guidelines

Use redaction when the fact of an event matters more than the exact detail.

## Redact or generalize

Prefer replacing exact values with higher-level descriptions for:
- credentials
- private identifiers
- precise addresses/locations
- vulnerable source details
- account recovery data
- internal-only operational specifics

## Example transformations

Instead of:
- "Password set to X"

Write:
- "Dashboard password was set by the user and intentionally not stored in memory."

Instead of:
- "Source A from organization B sent document C"

Write:
- "A sensitive source provided supporting material; details kept out of shared memory."

## Principle

Keep the useful consequence. Drop the exploitable detail.
