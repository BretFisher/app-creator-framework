# Skill notes: app-idea

Working notes for the first App Creator skill. Kept in the repo so the design reasoning and test history survive between work sessions. Update this file when the skill changes or a test iteration runs.

## Status (2026-09-09)

Draft complete and tested twice by simulation. Not yet tested with a real person. Not yet packaged for upload to an agent platform.

## What the skill is

`skills/app-creator/app-idea/` runs the discovery conversation that turns a non-technical App Creator's idea into a Project Brief. Part 1 of the brief is written to the App Creator in plain language. Part 2 is the translation into agile and platform-engineering terms for IT and build agents. No code is written. The skill is user-invoked only (`disable-model-invocation: true`).

Files:

| File | Purpose |
|---|---|
| `SKILL.md` | Conversation rules, workflow, two fit checks, finishing rules |
| `references/acf-overview.md` | Framework context, because App Creators never see this repo |
| `references/org-profile.md` | Org-specific values. Filled in by IT via the `customize` skill before upload. `{{placeholders}}` mean "not customized" |
| `references/golden-paths.md` | Approved app shapes, each described technically and as plain-language matching signals |
| `references/translation-guide.md` | Business language to delivery language, words to avoid, question patterns, assumption shapes |
| `references/discovery-checklist.md` | Six phases with stop signals, dependency-order rule, definition of done |
| `assets/project-brief-template.md` | The output document |

## Design decisions and why

- **One document, two parts.** One source of truth. Part 2 must cite Part 1; it is a translation, not an expansion. Prevents the agent inventing requirements.
- **Self-contained.** App Creators receive only the uploaded skill files. Everything about the framework and the org lives in `references/`.
- **Customization via reference files.** `org-profile.md` and `golden-paths.md` are the contract between this skill and the `skills/platform/customize/` skill. Handlebars-style `{{placeholders}}` mark unfilled values so they never collide with markdown links or `- [ ]` checkboxes.
- **No repo assumed.** The brief is a markdown file from the first minute. The agent asks about a "project space" only near the end. With none, the App Creator downloads the file and sends it to IT.
- **Two independent fit checks.** App Creator model fit (is this personal software?) and golden path fit (can the platform build this shape?). Recorded separately.
- **One question per turn.** Tested: the simulated App Creator answers only the first of several questions, as busy people do.
- **Frontier rule.** Never ask a question that depends on an unheard answer. Adopted after iteration 1 missed manager visibility.
- **Defaults on preferences, never on facts.** A non-technical person accepts a plausible default; the brief would then record a guess as confirmed.
- **Priority is not exclusion.** "Which matters most" orders the list; only explicit agreement moves an item out of scope.

## Test method

`make test-app-idea` runs `skills/app-creator/app-idea-workspace/run-interview.py`. Two `claude -p` Sonnet sessions talk through the script: one runs the skill, one role-plays a persona from `personas/`. The agent works in a throwaway directory outside this repo with all git subcommands disallowed. Each run writes `transcript.md`, `turns.jsonl`, and `brief/` into `iteration-N/<persona>/`. Grade against the persona's "Expected outcomes" and record in `grading.md`.

Persona so far: `hr-onboarding-tracker` (Dana, HR Business Partner, wants an onboarding dashboard; hidden facts include Workday read access, new tracking data, sensitive notes, 60 cross-department managers, an unverified manager approval).

## Test history

| Iteration | Turns | Jargon flags | Checks passed | What changed after |
|---|---|---|---|---|
| 1 | 30 | 0 | 17/20 | Look-vs-update questions, nice-to-have question, write-back question, second-person Part 1 |
| 2 | 33 | 0 | 19/20 | Ask AC's name, data quality/churn question, priority-is-not-exclusion rule |

Details in each iteration's `grading.md`.

## Future work

See the pull request for the live checklist. Summary:

- Run iteration 3 to confirm the iteration-2 fixes.
- Add two more personas: one that should fail the App Creator fit (cross-department, regulated data) and one that misses every golden path (write-back, offline hardware).
- Test the project-space-exists path with `--git-init`.
- Test with a real non-technical person.
- Design the `skills/platform/customize/` interview and have it write `org-profile.md` and `golden-paths.md`.
- Define the "what happens next" options after the brief, per org, in `org-profile.md`.
- Decide packaging: plugin marketplace for Claude, in-repo for Copilot, per the README.
- Turn the persona "Expected outcomes" into machine-checkable assertions.
