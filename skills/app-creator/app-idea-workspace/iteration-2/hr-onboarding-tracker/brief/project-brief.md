# New Hire Onboarding Tracker — Project Brief

| | |
|---|---|
| **Status** | Confirmed by App Creator |
| **App Creator** | [your name], HR onboarding coordinator |
| **Who else was consulted** | none yet — Priya and Marcus have not been asked directly during this conversation |
| **Last updated** | 2026-09-09 |
| **App Creator fit** | Fit with conditions (see Part 2) |
| **Golden path** | Likely fits the standard browser-app way of building here, with one unresolved signal (see Part 2) |

---

# Part 1: Your App Plan

*This part is written for you, and describes your app in your own words. If anything here is wrong or missing, say so. Everything in Part 2 comes from this part.*

## The problem we're solving

You, Priya, and Marcus track every new hire's onboarding in a spreadsheet. Steps like laptop requests, badges, and benefits paperwork slip through silently, and nobody notices until a manager complains — it happens at least once or twice a month, more in your busy hiring months (January and September, driven by warehouse seasonal hiring, when volume roughly doubles, from 15–25 new hires a month to as many as 50). A recent example: a new hire started on a Monday with no laptop because IT never got the request, and you only found out Tuesday when the manager asked why the person couldn't log in. You tried a SharePoint list a couple of years back, but it died because nobody except you kept it updated.

"Better" means: one place to see everyone starting this month, what's done and what's not, know instantly who's falling behind, and leave yourself notes on a person instead of digging through email.

## Who will use it

- **You, Priya, and Marcus (HR onboarding team, 3 people)** — see and update onboarding status and notes for every new hire, across corporate and warehouse sites.
- **Hiring managers (about 60 across the company, not all active at once)** — look-only access to the plain checklist status of just their own new hire(s). No notes, no other new hires, nothing they can change.
- **IT and Facilities** — not logged-in users. You'll still chase them the way you do today (IT helpdesk inbox, Facilities shared inbox); the tool would email them directly when a task they own is overdue.

If you moved to a different role, Priya would likely take over ownership. Sam, your HR Director, would confirm who owns it.

**Important:** Sam has not yet seen a written version of this idea — only reacted positively in passing. Getting Sam to look at this plan is an open item below, not a done deal.

## What it will do

1. **Pull in new hire info automatically** — name, start date, department, manager, location, and job title come from Workday instead of you copying it by hand every Monday.
2. **Show a per-person checklist** — IT tasks (laptop, accounts), Facilities tasks (badge, desk, locker), manager tasks (first-week plan, buddy), and HR tasks (paperwork, policy sign-off, benefits), each with its own deadline across the roughly 90-day onboarding window (not everything is due on day one — laptop and badge are, benefits and paperwork happen over the following weeks).
3. **Let you tick off tasks as done** — and keep a record of who did it and when, so you can answer "who marked this done" later.
4. **Let you leave private notes on a new hire** — for sensitive things like a pending background check, visa/right-to-work status, a manager's private concern, or an accommodation request. These notes are visible only to you, Priya, and Marcus — never to hiring managers.
5. **Let a hiring manager check their own new hire's status** — plain checklist only, nothing else.

## What it won't do (for now)

- **Automatic overdue email nagging** — a once-a-day email to you and to whoever owns an overdue task (IT helpdesk inbox, Facilities inbox, or the hiring manager directly) would be a big help, but you said you could live without it for a while if the checklist view came first. This is the next thing to add after the first version.
- **Automatically marking things done back in Workday** — you'd love this, but it's not essential (your spreadsheet doesn't do it either), and it means the app would be changing data in another system, not just reading it, which needs extra care. Leaving it out for now.

## Information the app needs

### Information it looks up from other places

| What | Where it lives today | Who owns it | Do you have access today? |
|---|---|---|---|
| New hire profile: name, start date, department, manager, location, job title | Workday | Not sure — you access it via a report an IT contact set up for you; the exact owning team is unknown | Yes, but only as a manual report you run yourself and copy by hand. An automatic feed into the dashboard has never been requested — open item for IT. |

### Information it keeps track of itself

| What | Kept for how long | About people? |
|---|---|---|
| Each new hire's task checklist (task, category, deadline, done or not, who marked it done and when) | 1 year after onboarding finishes, for audits and "why did this drag on" questions | Yes |
| Private notes on a new hire | 1 year | Yes — can include background check status, immigration/right-to-work status, accommodation requests, and private manager comments. Treat as confidential. |

## Who can see and change what

You, Priya, and Marcus can see and change everything, including the private notes. Hiring managers can only see the plain checklist status for their own new hire — no notes, no other employees, and nothing they can edit. IT and Facilities never log in; they only get an overdue email for tasks assigned to them. Every checklist change and note is recorded with who made it and when.

## How this fits with how apps get built here

This mostly fits the standard way apps are built here, so it should move faster than a custom project. Two things need IT's attention before building starts: some of what you'd track is confidential personal information (background checks, immigration status, accommodation requests), and pulling new hire data automatically from Workday isn't something that's been set up before, so IT needs to confirm it's possible and how long it'll take.

## How we'll know it's working

- [ ] You can look at the dashboard on any given day and know exactly who's behind and on what, without emailing anyone to check.
- [ ] When Sam asks how onboarding is going this month, you can pull it up instead of building a summary from scratch.
- [ ] A hiring manager can check their own new hire's status without asking you.
- [ ] You can answer "who marked this done, and when" for any task.

## Things we assumed, and you confirmed

- **Assumed:** Sam has approved this idea. **Confirmed:** No — Sam reacted positively in a passing conversation but hasn't seen a written plan. Open question below.
- **Assumed:** IT can easily connect Workday data automatically, since "it's all in Workday already." **Confirmed:** Not sure — nobody on your team has asked for anything like this before. Open item for IT to investigate.
- **Assumed:** every warehouse site manager has a work phone. **Confirmed:** No — some use personal phones. Since the app works in a browser, this should be fine either way, but it raises a policy question for IT (see below).
- **Confirmed directly (not an assumption):** onboarding task deadlines vary by task across a ~90-day window; they're not all due on the start date.

## Open questions

- Has Sam seen and approved this written plan? — ask Sam
- Who owns the Workday data, and can IT set up an automatic feed instead of a manual report? How long would that take? — ask IT (via your usual helpdesk)
- Is there a company policy on hiring managers using personal phones to access internal tools like this? — ask IT

---

# Part 2: Technical Brief

*Written for IT staff and build agents. A translation of Part 1, not an expansion of it.*

## Summary

Three HR onboarding coordinators need a single view of onboarding-task status for every new hire (15–25 a month, up to ~50 in peak season) to replace an error-prone spreadsheet and catch missed steps (laptop, badge, paperwork) before they cause day-one problems. Core capability: new hire profile data ingested from Workday, a per-person checklist of IT/Facilities/manager/HR tasks with individual deadlines across a 90-day onboarding window, confidential free-text notes, and an audit trail. About 60 hiring managers get scoped, read-only visibility into their own new hire's checklist status. A daily overdue-task email digest is a fast-follow, not part of the first version.

## Actors and personas

| Actor | Description | Approx. count | Access level |
|---|---|---|---|
| HR onboarding coordinator | Owns onboarding tracking; updates checklist and notes | 3 | Full read/write, including confidential notes |
| Hiring manager | Wants to know if their new hire's onboarding is on track | ~60 (not all active at once), every department and site | Read-only, scoped to own new hire(s), checklist status only, no notes |
| IT helpdesk | Owns IT onboarding tasks (laptop, accounts) | 1 shared inbox | No login; receives overdue-task email only (fast-follow feature) |
| Facilities | Owns facilities onboarding tasks (badge, desk, locker) | 1 shared inbox | No login; receives overdue-task email only (fast-follow feature) |

## User stories and acceptance criteria

### US-1: Automatic new hire import

**As an** HR onboarding coordinator, **I want** new hire info (name, start date, department, manager, location, job title) to appear automatically from Workday, **so that** I don't have to copy it by hand every week.

Acceptance criteria:
- Given a new hire is added in Workday, when the sync runs, then their profile appears in the dashboard without manual entry.

### US-2: Per-person onboarding checklist

**As an** HR onboarding coordinator, **I want** a checklist of IT, Facilities, manager, and HR tasks for each new hire, each with its own deadline within the 90-day onboarding window, **so that** I can see exactly what's outstanding and by when.

Acceptance criteria:
- Given a new hire record exists, when I open it, then I see every task, its category, its deadline, and whether it's done.

### US-3: Mark tasks done

**As an** HR onboarding coordinator, **I want** to tick off a task as complete, **so that** the status reflects reality.

Acceptance criteria:
- Given a task is outstanding, when I mark it done, then it shows as complete and records who did it and when.

### US-4: Private notes

**As an** HR onboarding coordinator, **I want** to leave notes on a new hire visible only to my team, **so that** I can track sensitive information (e.g. a pending background check or accommodation request) without exposing it to hiring managers.

Acceptance criteria:
- Given I add a note to a new hire, when a hiring manager views that new hire, then the note is not shown to them.

### US-5: Hiring manager view

**As a** hiring manager, **I want** to see the onboarding checklist status for my own new hire, **so that** I know if anything is behind without emailing HR.

Acceptance criteria:
- Given I am a hiring manager, when I log in, then I see only checklist status (not notes) for new hires I manage, and nothing for anyone else's.

### US-6: Audit trail

**As an** HR onboarding coordinator, **I want** a record of who changed what and when, **so that** I can answer questions from Sam or during an audit.

Acceptance criteria:
- Given any checklist or note change, when I view its history, then I see who made the change and when.

### US-7: Overdue task email digest (second priority — not first version)

**As an** HR onboarding coordinator, **I want** a once-daily email when a task is overdue, sent to me and to whoever owns the task (IT helpdesk inbox, Facilities inbox, or the hiring manager directly), **so that** people are nagged automatically instead of me chasing them.

Acceptance criteria:
- Given a task passes its deadline without being marked done, when the daily check runs, then an email goes to the coordinators and the task owner.

## Data

### External data sources and integrations

| Source | System / owner | Access pattern | Sensitivity | Access status | Notes |
|---|---|---|---|---|---|
| New hire profile (name, start date, department, manager, location, job title) | Workday; owning team unknown | Read | Internal (names/roles; not regulated on its own) | Not yet requested — AC has only a manual report, run and copied by hand; no automatic feed has ever been asked for | Blocking: IT must confirm feasibility and timeline for an automatic feed |

### Owned data

| Entity | Key attributes | Retention | Contains personal data? | Notes |
|---|---|---|---|---|
| Onboarding task | task name, category (IT/Facilities/Manager/HR), deadline, done status, who/when marked done | 1 year after onboarding completes | Yes | Deadlines vary per task across a ~90-day window, not all tied to start date |
| New hire note | free text, author, timestamp | 1 year | Yes — confidential | Can include background check status, immigration/right-to-work status, accommodation requests, private manager comments; visible only to the 3 coordinators |

## Access control and audit

- Authentication: org SSO, same login coordinators and hiring managers already use.
- Authorization model: coordinators (3) — full read/write including notes. Hiring managers (~60) — read-only, scoped to their own new hire(s), checklist status only. IT/Facilities — no login, notification-only.
- Audit requirements: every checklist status change and note addition/edit is timestamped and attributed to a user, visible to coordinators.

## Non-functional requirements

| Category | Requirement | Source in Part 1 |
|---|---|---|
| Availability | Business-hours availability is sufficient; an afternoon outage is tolerable | "Not the end of the world... I'd just go back to checking email and the spreadsheet" |
| Performance | No specific requirement raised | not discussed |
| Device / platform | Responsive browser; mainly desk use, occasional phone use (company or personal) | "mostly at my desk... glance at it on my phone"; some warehouse managers use personal phones |
| Accessibility | Org standard applies | org policy — org-profile.md not yet customized for this organization |
| Notifications | Once-daily email digest for overdue tasks (fast-follow, not first version) | "once a day is plenty... send it to whoever owns the task too" |
| Data residency / compliance | Contains confidential personal data (background check status, immigration/right-to-work status, disability accommodation requests) — flag for security review | "background check still pending... visa/right-to-work status... accommodation request" |

## Assumptions and risks

| Assumption or risk | Confirmed by AC? | Impact if wrong | Mitigation or owner |
|---|---|---|---|
| Sam (HR Director) has approved this idea | No — reacted positively in passing only | Could stall or reshape the plan once Sam actually reviews it | AC to show Sam this brief before proceeding |
| An automatic Workday feed is straightforward for IT to set up | Not confirmed — never requested before | Could delay build significantly if it takes weeks to arrange | IT to investigate and estimate; treat as blocking |
| All warehouse site managers have a work phone | No — some use personal phones | Low impact, since the app is browser-based and works on any device; may raise a BYOD policy question | IT to confirm personal-device access policy |
| Onboarding task deadlines vary per task within a 90-day window | Confirmed directly by AC | If wrong, "overdue" flags would mislead coordinators | Coordinators to define deadline rules per task type during build |

## App Creator fit assessment

**Result:** Fit with conditions

Reasoning against the App Creator model (personal software for the creator and those around them, single team or department, not a system of record for a critical process, no regulated data without approval):

- Good fit: built by and for a 3-person team within the AC's own area of expertise (HR onboarding); the AC already has some access to the source data; Workday remains the system of record for HR data, this app only tracks task status; an afternoon outage is tolerable, not a crisis.
- Condition: the app will store confidential personal data — background check status, immigration/right-to-work status, and disability accommodation requests — recommend IT security review before build.
- Condition: needs a data access change not yet in place (automatic Workday feed); treat as blocking until IT confirms feasibility and timeline.
- Note: read-only access reaches roughly 60 hiring managers across every department and site — broader than the 3-person core team, though each manager sees only a narrow, view-only slice (their own new hire). Flagged for IT to weigh against any org-wide threshold for app reach, since org-profile.md does not yet set one.

Conditions or recommendations:

- Proceed with this brief, but hold build until: (1) Sam has seen and approved it, (2) IT has assessed the Workday feed request, and (3) IT/security has reviewed handling of the confidential note content.

## Golden path match

**Result:** Likely matches the standard browser-based internal app pattern; one signal unresolved

| Signal | Matches? | Evidence from Part 1 |
|---|---|---|
| Used from a browser, at a desk or on a phone | Yes | "mostly at my desk... phone the night before" |
| Keeps track of its own records | Yes | per-person checklist and notes |
| Looks up information from other systems but doesn't change them | Yes, for the first version | Workday read-in only; write-back to Workday explicitly deferred |
| Works with the normal work login | Yes | "same login as everything else" |
| Sends occasional email, not instant alerts | Yes (fast-follow feature) | once-daily digest, no SMS |
| Fewer than [org threshold, not yet set] users in one team or department | Unclear | 3 core users plus ~60 read-only viewers spanning every department; org-profile.md has no threshold defined yet |

If no match / unclear: the read-only audience spans every department company-wide, which may exceed whatever user or department threshold this organization intends for this path. Since each manager's view is narrow and read-only, IT may reasonably decide this still fits; recorded here as a decision for IT rather than assumed.

## Org policy requirements applied

- None available — org-profile.md has not been customized for this organization yet (placeholder text throughout). No hard requirements could be applied. Flagged below.

## Out of scope

- Automatically marking tasks complete back in Workday — a write-back into another system, higher risk; deferred indefinitely. The current spreadsheet doesn't do this either, so nothing is lost.
- Overdue email digest — not permanently out of scope, but deferred to the version after the core checklist ships.

## Open items for IT

| Item | Type | Blocking build? | Suggested owner |
|---|---|---|---|
| Organization profile (org-profile.md) has not been customized for this org | Setup gap | No | Platform/IT team administering this framework |
| No project space exists yet for this app | Setup gap | Yes | IT intake / whoever sets up project spaces here |
| Automatic Workday feed for new hire data — feasibility and timeline unknown, never requested before | Data access | Yes | IT / Workday admin, via the AC's usual helpdesk |
| Confidential personal data (background checks, immigration status, accommodations) needs security review | Security review | Yes | IT security |
| Policy question: hiring managers accessing this from personal phones | Policy question | No | IT |
| Sam's (HR Director) approval of this written brief | Approval | Yes | Sam |

## Suggested next step

Org-profile.md does not specify how briefs reach IT here, so the default applies: the App Creator shows this brief to Sam for approval, then sends it to their IT contact for review — especially the Workday data access request and the security review of the confidential note content — before starting to build.
