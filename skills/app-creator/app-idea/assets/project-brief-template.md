# {{App Name}} — Project Brief

| | |
|---|---|
| **Status** | Draft / Confirmed by App Creator / Under IT review |
| **App Creator** | {{name, title, department}} |
| **Who else was consulted** | {{names or "none yet"}} |
| **Last updated** | {{date}} |
| **App Creator fit** | Good fit / Fit with conditions / Recommend IT project (see Part 2) |
| **Golden path** | {{path name}} / No match (see Part 2) |

---

# Part 1: Your App Plan

*This part is written for you, the App Creator, and addressed to you. It should read like a description of your app in your own words. If anything here is wrong or missing, say so, because everything in Part 2 is built from it.*

## The problem we're solving

{{Two or three sentences. What is slow, annoying, error-prone, or impossible today? Who feels the pain? Use the App Creator's own words and examples.}}

## Who will use it

{{List each kind of person. For each: what's their job, what do they need from this app, roughly how many of them are there.}}

- **{{Role, e.g. "Me and the two other schedulers"}}** — {{what they do with it}}
- **{{Role}}** — {{what they do with it}}

## What it will do

{{The main things a person can do with the app, in the order they'd normally happen. Each one should be something the App Creator could demonstrate.}}

1. **{{Thing}}** — {{one sentence on what happens}}
2. **{{Thing}}** — {{one sentence}}

## What it won't do (for now)

{{Things that came up but are deliberately left out of the first version. Naming these prevents disappointment later.}}

- {{Thing}} — {{why it's later, or who else owns it}}

## Information the app needs

### Information it looks up from other places

{{Things the app reads but does not own. For each: where it lives today, who owns it, whether the App Creator already has access.}}

| What | Where it lives today | Who owns it | Do you have access today? |
|---|---|---|---|
| {{e.g. "Staff list with departments"}} | {{e.g. "HR system"}} | {{e.g. "HR"}} | {{Yes / No / Not sure}} |

### Information it keeps track of itself

{{Things the app creates and stores. For each: what it is, how long it should be kept, whether it includes anything about people.}}

| What | Kept for how long | About people? |
|---|---|---|
| {{e.g. "Each shift request and its status"}} | {{e.g. "Two years"}} | {{Yes / No}} |

## Who can see and change what

{{Plain rules. "Everyone on the team can see all requests. Only the scheduler can approve one. Nobody outside the team can see anything."}}

## How this fits with how apps get built here

{{One or two plain sentences. Either: "This fits the standard way apps are built here, so it should need fewer approvals and start faster." Or: "This needs a bit more help from IT than usual because <plain reason>." No technology names.}}

## How we'll know it's working

{{Concrete, checkable statements the App Creator agrees to. These become the test list.}}

- [ ] {{e.g. "A staff member can submit a shift swap request in under a minute from their phone."}}
- [ ] {{e.g. "The scheduler sees all pending requests in one list and can approve or decline each."}}

## Things we assumed, and you confirmed

{{Every assumption surfaced during discovery, and what the App Creator said about it.}}

- **Assumed:** {{e.g. "Everyone on the team has a work phone."}} **Confirmed:** {{Yes / No, corrected to...}}

## Open questions

{{Things nobody could answer yet, and who might know.}}

- {{Question}} — {{who to ask}}

---

# Part 2: Technical Brief

*This part is written for IT staff and the agents that will build the app. It is a translation of Part 1 into delivery language and must not introduce requirements that Part 1 does not support.*

## Summary

{{One paragraph: problem, primary actors, core capability, expected scale.}}

## Actors and personas

| Actor | Description | Approx. count | Access level |
|---|---|---|---|
| {{e.g. Scheduler}} | {{role and goals}} | {{n}} | {{e.g. admin}} |

## User stories and acceptance criteria

Each story maps to an item in Part 1 "What it will do". Acceptance criteria map to "How we'll know it's working".

### US-1: {{Short title}}

**As a** {{actor}}, **I want** {{capability}}, **so that** {{outcome}}.

Acceptance criteria:
- Given {{context}}, when {{action}}, then {{observable result}}.

### US-2: {{Short title}}

...

## Data

### External data sources and integrations

| Source | System / owner | Access pattern | Sensitivity | Access status | Notes |
|---|---|---|---|---|---|
| {{dataset}} | {{system, owning team}} | Read / Write / Both | {{None, Internal, Confidential, Regulated (PII/PHI/PCI)}} | {{Granted / Requested / Not yet requested}} | {{API available? Export only? Unknown?}} |

### Owned data

| Entity | Key attributes | Retention | Contains personal data? | Notes |
|---|---|---|---|---|
| {{entity}} | {{fields}} | {{duration and reason}} | {{Yes / No}} | |

## Access control and audit

- Authentication: {{e.g. org SSO, assumed}}
- Authorization model: {{roles and what each can do, derived from Part 1}}
- Audit requirements: {{what actions need a record of who did what, when}}

## Non-functional requirements

| Category | Requirement | Source in Part 1 |
|---|---|---|
| Availability | {{e.g. business hours only is acceptable}} | {{quote or section}} |
| Performance | {{e.g. no operation over 3 seconds}} | |
| Device / platform | {{e.g. must work on mobile browser}} | |
| Accessibility | {{org standard applies}} | |
| Notifications | {{e.g. email on approval}} | |
| Data residency / compliance | {{any regulated data flags}} | |

## Assumptions and risks

| Assumption or risk | Confirmed by AC? | Impact if wrong | Mitigation or owner |
|---|---|---|---|
| | | | |

## App Creator fit assessment

**Result:** Good fit / Fit with conditions / Recommend IT project

Reasoning against the App Creator model (personal software for the creator and those around them, single team or department, not a system of record for a critical process, no regulated data without approval):

- {{finding}}

Conditions or recommendations:

- {{e.g. "Proceed, but HR data access requires approval before build."}}

## Golden path match

**Result:** {{Path name}} / No match

| Signal | Matches? | Evidence from Part 1 |
|---|---|---|
| {{signal from golden-paths.md}} | Yes / No / Unknown | {{quote or section}} |

If no match: which signals failed, and whether a path could reasonably be extended to cover this.

## Org policy requirements applied

{{Hard requirements copied from org-profile.md. These were not discussed with the AC.}}

- {{requirement}}

## Out of scope

- {{item}} — {{reason}}

## Open items for IT

| Item | Type | Blocking build? | Suggested owner |
|---|---|---|---|
| {{e.g. "Read access to HR staff list"}} | Data access | Yes | {{team}} |

## Suggested next step

{{e.g. "Proceed to build-app skill once HR data access is confirmed." or "Route to IT intake for evaluation as a formal project."}}
