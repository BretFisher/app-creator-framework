# Grading: iteration-1 / hr-onboarding-tracker

Model: claude-sonnet-5 (both sides). 30 agent turns, 60 CLI calls, 8.9 min, $1.29. Agent ended on its own with the completion marker.

## Brief (expected outcomes 1–12)

| # | Check | Result | Evidence |
|---|---|---|---|
| 1 | Brief exists, Part 1 + Part 2, template order | PASS | All template sections present in order |
| 2 | Workday as external, read-only, owner, access unconfirmed | PASS | External table: Read, "Requested, not yet confirmed"; nuance that manual report access exists is captured |
| 3 | Tracking data as owned, ~1 yr retention, personal data Yes | PASS | Three owned entities, 1 year, all flagged Yes |
| 4 | Notes flagged as sensitive PII | PASS | Visa, background check, accommodation named; restricted to 3 coordinators |
| 5 | Manager visibility recorded, role split, cross-dept flagged | PASS (soft) | Role split exact. Flagged as "note, not a blocker" and deferred to org threshold. Manager count (60) never asked; estimated instead |
| 6 | Write-back to Workday as out of scope | NOT ELICITED | Agent never asked about write-back or nice-to-haves, so Dana never offered it. Golden path table asserts "no write-back" without having asked |
| 7 | Assumptions: Sam, Workday accuracy, work phones, IT can connect | PARTIAL | Sam and IT-can-connect recorded explicitly. Start-date churn captured as a requirement, not as a data-quality assumption. Work-phone assumption not tested; device answer captured warehouse reality anyway |
| 8 | Golden path match with per-signal evidence, threshold note | PASS | 5 Yes, 1 Unknown with reasoning about org threshold placeholder |
| 9 | Open item: Workday access, blocking | PASS | First row of Open items, Blocking = Yes |
| 10 | org-profile not customized recorded | PASS | Recorded in Access control, NFRs, Org policy, Open items |
| 11 | No technical vocabulary in Part 1 | PASS (style note) | No jargon. But Part 1 is written *about* Dana in third person, not *to* her |
| 12 | Plain next step, options-not-customized noted | PASS | Suggested next step names the gap |

## Transcript (expected outcomes 13–20)

| # | Check | Result | Evidence |
|---|---|---|---|
| 13 | Zero jargon flags | PASS | 0 `[JARGON]` markers in 30 AC replies |
| 14 | One question per message | PASS (28/30) | Turns 24 and 33-equivalent stack two questions; otherwise clean |
| 15 | Reflects back before moving on | PASS | Nearly every turn opens with a one-line reflection |
| 16 | Part 1 read back and confirmed before finishing | PASS | Turn 26 readback; Dana corrected manager visibility; turn 28 confirmed |
| 17 | No screen design or technology names | PASS | None |
| 18 | Three closing items | PASS | Turn 30: where the file is, what IT must answer, what Dana must do |
| 19 | Project-space question near the end only; no git | PASS | Asked at turn 29 after Part 1 confirmed; git disallowed and not attempted |
| 20 | No project space → downloadable file, send to IT, open item | PASS | Turn 30 and Open items row "No project space exists yet" |

## Findings that changed the skill

1. **Look vs update.** The agent asked "who else deals with this" and later "would IT/Facilities/manager log in and check off tasks?" Dana answered about *editing*, so the agent concluded managers don't use it. The readback caught it, which is the readback doing its job, but the question design caused the miss. Skill now asks who would *look at* it and who would *update* it as separate questions.
2. **Write-back never asked.** Checklist Phase 4 has the item; the agent skipped it and asserted "no write-back" in the golden path table. Skill now names write-back in the Phase 4 summary and the translation guide says to ask even if it seems unlikely.
3. **No nice-to-have question.** Hidden wishes (and the write-back risk) surface from "what else would be great?" Added once to Phase 3.
4. **Part 1 voice.** Written about Dana in third person. Skill and template now say second person.

## Not changed, worth watching

- Phase 1 (the problem) got one question before moving to people. The skill says "spend real time here." Acceptable this run because Dana's first answer was rich. Watch on other personas.
- Manager count never asked. Phase 2 has "rough count of each kind"; the agent estimated instead. Not changed yet; see if the look/update split fixes it.
- Cross-department manager viewing judged "note, not a blocker." Defensible. The org threshold placeholder is the right place for that call.
