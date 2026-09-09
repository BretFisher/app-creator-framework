---
name: customize
description: Guided interview for IT and platform engineering teams adopting the App Creator Framework. Fills in the organization-specific parts of the App Creator skills (org profile, golden paths, hard requirements, data access process, fit thresholds, next-step options) before those skills are uploaded for App Creators to use. Run this once during adoption and again whenever platform standards change.
disable-model-invocation: true
---

# Customize the App Creator Skills for Your Organization

> **Status: stub.** This skill's interview flow is not yet designed. This file records its purpose and the files it will write so the App Creator skills can be built against a stable contract.

## Purpose

The App Creator skills in `skills/app-creator/` are written to be organization-neutral. App Creators never see this repository; they only see the skill files your team uploads to your agent platform. That means every organization-specific fact the agent needs has to be baked into those skill files before upload.

This skill interviews the platform, security, and development staff adopting the framework and writes their answers into the App Creator skills' reference files.

## Files this skill writes

| File | What it holds |
|---|---|
| `skills/app-creator/app-idea/references/org-profile.md` | Org name, role naming, who reviews briefs, data access process, hard requirements, fit thresholds, culture notes, extra discovery questions, what-happens-next options |
| `skills/app-creator/app-idea/references/golden-paths.md` | Each approved golden path described technically and as plain-language matching signals |

Future App Creator skills (build-app, submit-app) will add their own customizable reference files here.

## Contract with the App Creator skills

- Placeholders in the reference files use handlebars style, `{{like_this}}`, so they never collide with markdown links or checkboxes. App Creator skills treat any remaining placeholder as "not customized" and fall back to neutral defaults, noting the gap in the Project Brief for IT.
- This skill must never remove a section from those files. App Creator skills depend on the section headings.
- Re-running this skill should update values in place and preserve anything the team hand-edited.

## Planned interview areas

1. Identity and naming (what the org calls the role and the program)
2. Intake: who reviews briefs, how, and how fast
3. Data: catalog or portal, request process, approved and forbidden datasets
4. Golden paths: what the platform can build and run today, and the signals that an idea fits each
5. Hard requirements: SSO, residency, compliance, accessibility
6. Fit thresholds: user counts, department span, sensitivity levels
7. Culture: tone, vocabulary, session length expectations
8. Next steps: what an App Creator can do after the brief is confirmed
