# Grading: iteration-2 / hr-onboarding-tracker

Model: claude-sonnet-5 (both sides). 33 agent turns, 66 CLI calls, 8.5 min, $1.33. Ended on its own.

Skill changes tested this iteration: look-vs-update questions, nice-to-have question, write-back question, second-person Part 1, frontier rule, phase-boundary summaries, facts-vs-decisions, defaults on preferences only, "nothing silently assumed" done rule.

## Comparison to iteration 1

| # | Check | Iter 1 | Iter 2 | Note |
|---|---|---|---|---|
| 1 | Brief complete, template order | PASS | PASS | |
| 2 | Workday external, read-only, access unconfirmed | PASS | PASS | Owner now honestly "unknown" |
| 3 | Owned tracking data, ~1 yr, personal Yes | PASS | PASS | |
| 4 | Notes flagged sensitive | PASS | PASS | Surfaced at turn 23 |
| 5 | Manager visibility, role split, count, cross-dept flag | soft | **PASS** | Surfaced at turn 7 before readback; count of 60 asked at turn 8 |
| 6 | Write-back to Workday as out of scope | not elicited | **PASS** | Nice-to-have question at turn 18 drew it out; recorded with write-back risk |
| 7 | Assumptions: Sam, Workday accuracy, work phones, IT connect | 2 of 4 | 3 of 4 | Sam probed (turn 11), phones probed (turn 28), IT connect. **Start-date churn not surfaced** (was in iter 1) |
| 8 | Golden path per-signal evidence | PASS | PASS | |
| 9 | Workday access open item, blocking | PASS | PASS | |
| 10 | org-profile gap recorded | PASS | PASS | |
| 11 | No jargon in Part 1; second person | style miss | **PASS** | Written to "you" throughout |
| 12 | Plain next step, gap noted | PASS | PASS | |
| 13 | Zero jargon flags | PASS | PASS | 0 in 33 turns |
| 14 | One question per turn | 28/30 | 31/33 | Turn 26 stacked two; Dana answered the first only; agent followed up cleanly |
| 15 | Reflects back | PASS | PASS | |
| 16 | Part 1 read back and confirmed | PASS | PASS | Turn 32, after the project-space question (minor order swap) |
| 17 | No screens or technology | PASS | PASS | |
| 18 | Three closing items | PASS | PASS | |
| 19 | Project space asked near end; no git | PASS | PASS | Turn 31 |
| 20 | No project space → file + open item | PASS | PASS | |

New behaviors observed: phase-boundary summaries at turns 7, 12, 20. Defaults used on preferences ("a year sounds reasonable") and not on facts. Sam's approval probed rather than accepted, which flipped it from "confirmed" to open.

## Regressions and fixes applied

1. **AC's name never asked.** Header reads "[your name]". Iteration 1 asked at turn 4. Added to checklist Phase 2 and a Done rule: no placeholder text remains anywhere in the brief.
2. **Start-date churn not surfaced.** Iteration 1 captured "a third of start dates move" as a core requirement; iteration 2 never asked about data accuracy or change. Added a Phase 4 item and a translation-guide row for data quality and churn.
3. **Priority read as exclusion.** Dana said the checklist mattered most and she "could live without" emails for a while. The agent moved overdue emails to "What it won't do (for now)". Added to SKILL.md: priority orders the list; only explicit agreement to leave something out moves it to "won't do".

## Watching

- "How we'll know it's working" had 4 items vs 8 in iteration 1. Less concrete. Not changed; see if the data-churn question restores the missing checks.
- Project-space question came before the readback. Skill says after. Minor.
