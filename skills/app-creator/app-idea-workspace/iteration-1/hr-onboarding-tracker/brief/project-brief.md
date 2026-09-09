# New Hire Onboarding Dashboard — Project Brief

| | |
|---|---|
| **Status** | Confirmed by App Creator |
| **App Creator** | Dana Whitfield, HR Business Partner, HR |
| **Who else was consulted** | none yet |
| **Last updated** | 2026-09-09 |
| **App Creator fit** | Fit with conditions (see Part 2) |
| **Golden path** | Internal Web App (see Part 2) |

---

# Part 1: Your App Plan

*This part is written for you, the App Creator. It should read like a description of your app in your own words. If anything here is wrong or missing, say so, because everything in Part 2 is built from it.*

## The problem we're solving

Dana tracks new hire onboarding in a spreadsheet, and it does not keep up with changes. Last month, a new hire's start date changed but the update never reached IT. The laptop was not ready on day one, the person sat with nothing to do for half a day, and the hiring manager escalated it by emailing Sam. Onboarding involves several teams handing off tasks in sequence, and today nobody has one place to see whether every piece is done.

## Who will use it

People who log in and use the dashboard directly:

- **Dana (HR Business Partner)** — tracks all onboarding tasks and paperwork, owns the overall picture
- **Priya and Marcus (HR team)** — do the same job for warehouse-site hires, would take over if Dana changed jobs

Hiring managers log in too, but only to look, not to touch:

- **Hiring managers** — can see the task status for their own new hire only, so they stop needing to email Dana to ask "is the laptop ready yet." They cannot check anything off and cannot see Dana's notes. They're spread across head office (usually a laptop) and warehouse sites (often a shared site-office computer, sometimes a phone).

People the dashboard tracks work for, but who won't log in at all (they get email instead):

- **IT** — sets up laptops and accounts
- **Facilities** — issues badges and lockers, mostly for warehouse hires

Volume: usually 15–25 new hires a month, 30–50 in January and September (warehouse hiring season). Roughly one hiring manager per new hire, so the number of managers looking at the tool moves with that same volume, across many different departments and sites.

Approvals: Sam (HR Director) has given a verbal yes. IT has not been consulted yet — open question below.

## What it will do

1. **New hires show up automatically once their start date is locked in** — pulled from the HR system each morning, so nobody has to type in name, start date, site, department, job title, or manager by hand. (Most important piece — the one-place list is what fixes the spreadsheet problem.)
2. **See every onboarding task for that new hire** — laptop ordered, badge made, first week plan, paperwork, and so on.
3. **Tick off tasks as they get done, and leave notes** — done by Dana, Priya, or Marcus based on what IT, Facilities, or the manager tell them. The tool remembers who checked it off and when.
4. **Pick up start date changes automatically** — about a third of start dates move at least once; the tool refreshes from the HR system once a day so a moved date doesn't get missed.
5. **Let a hiring manager look up their own new hire's progress** — a simple status view, no notes, no editing, so managers stop needing to email Dana to ask if the laptop is ready.
6. **Get a daily email if a task is overdue** — sent to Dana (or whoever owns that new hire), and to a fixed IT or Facilities team inbox, or the hiring manager, depending on which task is late. (Nice to have — item 1 matters most.)

## What it won't do (for now)

- **Anything before the start date is confirmed** — recruiting owns that, in a different system.
- **Letting IT, Facilities, or hiring managers log in themselves** — they're not asked to use a new system; they get told by email instead.
- **Instant or text alerts** — a once-a-day overdue email is enough for now.
- **Anything with bank details or social security numbers** — that stays in the HR and payroll systems.

## Information the app needs

### Information it looks up from other places

| What | Where it lives today | Who owns it | Do you have access today? |
|---|---|---|---|
| New hire name, start date, site, department, job title, and manager | Workday | HR systems team | Yes — Dana already runs a report with this today, by hand, once a week |
| Hiring manager's contact details | Workday | HR systems team | Yes, same report |

### Information it keeps track of itself

| What | Kept for how long | About people? |
|---|---|---|
| Each new hire's task list and status (laptop, badge, first week plan, paperwork, etc.) | 1 year after start date, for audits and "did you follow up on this" questions | Yes |
| Notes on each new hire | 1 year after start date | Yes — may include sensitive things like pending background check results, visa status, or accommodation requests |
| Who checked off each task and when | 1 year after start date | Yes |

## Who can see and change what

Dana, Priya, and Marcus can see and update every new hire, including notes — nobody is restricted to their own sites, since they cover for each other. A hiring manager can log in and see only their own new hire's task status — no notes, and no ability to check anything off. IT and Facilities never log in; they only ever receive an email.

## How this fits with how apps get built here

This looks like a good match for the standard way apps get built here: a small team, a browser-based tool, reading information from one other system without changing it, and sending the occasional email. It should need fewer approvals and start faster, though the piece that checks a system each morning for changed start dates needs IT to confirm it can be built that way.

## How we'll know it's working

- [ ] A new hire who gets a locked-in start date in Workday shows up on the dashboard the next morning, with no typing required.
- [ ] If a start date moves in Workday, the dashboard shows the new date within a day, without Dana updating it by hand.
- [ ] Dana, Priya, or Marcus can open any new hire and see every onboarding task, tick one off, and leave a note.
- [ ] The tool shows who checked off a task and when, for at least the past year.
- [ ] If a task is still open close to the start date, an email goes out once a day to the right inbox (IT, Facilities, or the manager) and to Dana.
- [ ] IT and Facilities never need to log in to get their reminder.
- [ ] A hiring manager can log in and see their own new hire's task status, but not Dana's notes, and cannot check anything off.
- [ ] A hiring manager cannot see any other new hire besides their own.

## Things we assumed, and you confirmed

- **Assumed:** Everyone involved would use their normal work login. **Confirmed:** Yes.
- **Assumed:** IT can just connect this to Workday directly. **Status:** Not confirmed — Dana has only ever used a report someone in IT set up for her; whether an automatic daily connection is possible is for IT to check, not something we can assume yet.
- **Assumed:** Priya and Marcus are on board with using a new tool. **Status:** Not yet asked. This matters because an earlier attempt (a shared list) failed a couple of years ago when only Dana kept it updated and the other two kept emailing her instead.
- **Assumed:** Sam (HR Director) approves of this idea. **Confirmed:** Yes, verbally — Dana mentioned it and Sam said it sounds good, but Sam has not seen a written plan yet.
- **Assumed:** IT is fine with this being built. **Status:** Not yet asked — IT hasn't been told about this project.

## Open questions

- Can Workday changes (new hires, moved start dates) be picked up automatically once a day, or only through the manual report Dana already runs? — ask IT / the Workday systems team.
- Are Priya and Marcus actually willing to use this day to day? — Dana to ask them before build starts.
- Has Sam seen this written plan, not just the idea? — Dana to confirm.
- Has anyone told IT this project exists? — Dana to raise it, since IT is one of the teams the emails go to.

---

# Part 2: Technical Brief

*This part is written for IT staff and the agents that will build the app. It is a translation of Part 1 into delivery language and must not introduce requirements that Part 1 does not support.*

## Summary

An HR Business Partner (Dana) and two teammates (Priya, Marcus) currently track new hire onboarding in a spreadsheet manually copied from Workday each week, which has caused missed handoffs (e.g., a start date change that never reached IT, leaving a new hire without a laptop). The app is a browser dashboard that pulls new hire data from Workday daily, lets the three HR coordinators track and check off onboarding tasks with notes, gives hiring managers a read-only view of their own new hire's status, and sends daily overdue-task emails to the responsible party. Expected scale: 15–25 new hires/month (30–50 in January/September), 3 editing users, and a rotating set of viewing hiring managers roughly matching new hire volume.

## Actors and personas

| Actor | Description | Approx. count | Access level |
|---|---|---|---|
| HR onboarding coordinator (Dana, Priya, Marcus) | HR team members who track onboarding tasks for all new hires, across sites | 3 | Full read/write on all new hire records, including notes |
| Hiring manager | Manager of a specific new hire; wants to check progress without emailing HR | Roughly matches new hire volume (15–50/month), spread across many departments and sites | Read-only, scoped to their own new hire's task status only; no notes, no editing |
| IT (laptop/account setup) | Receives overdue-task emails for tasks assigned to IT | N/A — does not log in | None (email recipient only) |
| Facilities (badges/lockers) | Receives overdue-task emails for tasks assigned to Facilities | N/A — does not log in | None (email recipient only) |

## User stories and acceptance criteria

### US-1: Automatic new hire intake

**As an** HR onboarding coordinator, **I want** new hires to appear on the dashboard automatically once their start date is locked in Workday, **so that** I don't have to manually enter their details.

Acceptance criteria:
- Given a new hire's start date is confirmed in Workday, when the daily refresh runs, then the new hire appears on the dashboard with name, start date, site, department, job title, and manager, with no manual entry.

### US-2: Task tracking with notes

**As an** HR onboarding coordinator, **I want** to see every onboarding task for a new hire and check them off with notes, **so that** I have one place to track progress instead of a spreadsheet.

Acceptance criteria:
- Given a new hire is on the dashboard, when a coordinator opens their record, then they see the full task list (laptop, badge, first week plan, paperwork, etc.) and can mark each task done and attach a note.

### US-3: Change history for audit questions

**As an** HR onboarding coordinator, **I want** the dashboard to record who checked off a task and when, **so that** I can answer audit or follow-up questions without searching email.

Acceptance criteria:
- Given a task is marked done, when anyone with access views its history, then they see who did it and the date, retained for at least one year.

### US-4: Automatic start date sync

**As an** HR onboarding coordinator, **I want** start date changes in Workday to appear automatically, **so that** a moved date is never missed.

Acceptance criteria:
- Given a start date changes in Workday, when the next daily refresh runs, then the dashboard reflects the new date within 24 hours, with no manual update.

### US-5: Hiring manager self-service view

**As a** hiring manager, **I want** to see the onboarding status of my own new hire, **so that** I don't have to email HR to check if things are ready.

Acceptance criteria:
- Given a hiring manager is logged in, when they view the dashboard, then they see only their own new hire's task status, not HR's notes, and have no ability to edit anything.
- Given a hiring manager is logged in, when they try to view a different new hire, then access is denied.

### US-6: Daily overdue reminders

**As an** HR onboarding coordinator, **I want** a daily email when a task is overdue, **so that** nothing slips before someone's start date.

Acceptance criteria:
- Given a task is not marked done past its expected date, when the daily check runs, then one email is sent to the owning coordinator and one to the responsible party (a fixed IT inbox, a fixed Facilities inbox, or the hiring manager), at most once per day per overdue task.

## Data

### External data sources and integrations

| Source | System / owner | Access pattern | Sensitivity | Access status | Notes |
|---|---|---|---|---|---|
| New hire and manager details (name, start date, site, department, job title, manager, manager contact) | Workday / HR systems team | Read, daily automated refresh requested | Internal, contains personal data | Requested, not yet confirmed | AC has an existing manual report from Workday; whether an automated daily feed is possible is unconfirmed — the single biggest open technical question in this brief |

### Owned data

| Entity | Key attributes | Retention | Contains personal data? | Notes |
|---|---|---|---|---|
| New hire onboarding record | Name, start date, site, department, job title, manager, task list, task status, task due dates | 1 year from start date | Yes | Sourced from Workday, displayed to coordinators and (status only) the hiring manager |
| Coordinator notes | Free text per new hire | 1 year from start date | Yes — may include background check status, visa status, accommodation requests | Confidential; visible only to the 3 HR coordinators, never to hiring managers |
| Task check-off history | Task, who marked it done, timestamp | 1 year from start date | Yes | Supports audit / "did you follow up" questions |

## Access control and audit

- Authentication: org SSO / normal work login, assumed for both HR coordinators and hiring managers (org hard requirements on SSO were not available — org-profile.md is not yet customized; confirm with IT).
- Authorization model: HR onboarding coordinators (3) — full read/write on all new hire records and notes. Hiring managers — read-only, scoped to their own new hire's task status, notes excluded.
- Audit requirements: every task check-off recorded with who and when, retained for at least 1 year, viewable by the 3 coordinators.

## Non-functional requirements

| Category | Requirement | Source in Part 1 |
|---|---|---|
| Availability | Business-hours only is acceptable; an afternoon outage is a fallback-to-spreadsheet inconvenience, not urgent | "Rules and expectations" / availability discussion |
| Device / platform | Responsive browser: desktop for HR team and head-office managers, mobile/shared computer for warehouse-site managers | "Who will use it" / devices discussion |
| Notifications | Daily batch email only; no SMS or instant alerts | "What it will do" item 6 |
| Data sensitivity | Coordinator notes may contain confidential personal data (visa status, background check results, accommodation requests) — restrict to the 3 coordinators, exclude from manager view | "Information the app needs" |
| Accessibility | Org standard applies once defined (org-profile.md not yet customized) | Org policy gap |
| Data sync | Daily (not real-time) refresh from Workday is sufficient | "What it will do" item 4 |

## Assumptions and risks

| Assumption or risk | Confirmed by AC? | Impact if wrong | Mitigation or owner |
|---|---|---|---|
| Everyone would use their normal work login | Yes | Low | N/A |
| IT can connect this tool to Workday automatically once a day | Not confirmed | High — item 1 and item 4 (automatic intake and start-date sync) are the main value of the app; if only the existing manual report is available, coordinators may still need to upload it themselves | IT / Workday systems team to confirm feasibility before build |
| Priya and Marcus are willing to use this tool day to day | Not confirmed | High — a prior shared list failed because only Dana kept it updated | Dana to check with them before build starts |
| Sam (HR Director) approves | Confirmed verbally, not against a written plan | Low–Medium | Dana to share this brief with Sam |
| IT is aware of and supports this project | Not confirmed | Medium — IT is a data source owner and an email recipient | Dana to raise it with IT, ideally when sending this brief |

## App Creator fit assessment

**Result:** Fit with conditions

Reasoning against the App Creator model (personal software for the creator and those around them, single team or department, not a system of record for a critical process, no regulated data without approval):

- Good fit: built and owned by one HR team of 3, solves a problem Dana personally experiences, not a system of record for a business-critical process, and an outage is an inconvenience (fallback to spreadsheet), not an incident.
- Condition: coordinator notes may contain confidential personal data (visa status, background checks, accommodation requests) — needs IT/privacy review before build, and must stay restricted to the 3 coordinators.
- Condition: the core value of the app depends on an automated daily connection to Workday, which goes beyond the AC's current manual-report access — needs IT to confirm feasibility before committing to that scope.
- Note, not a blocker: hiring managers across many departments and sites will log in to view their own record. This is a narrow, read-only, self-scoped view (not general use of the tool by other departments), so it does not push this toward "recommend IT project" on its own, but IT should be aware the login population is wider than the 3-person editing team.

## Golden path match

**Result:** Internal Web App

| Signal | Matches? | Evidence from Part 1 |
|---|---|---|
| People use it from a browser, at a desk or on a phone | Yes | HR team mostly at desks; managers on shared warehouse computers or phones |
| Keeps track of its own records (requests, lists, statuses, notes) | Yes | Task lists, statuses, notes, check-off history |
| Looks up information from other systems but doesn't need to change those systems | Yes | Reads from Workday only; no write-back |
| Works with the normal work login | Yes | Confirmed for both coordinators and managers |
| Sends the occasional email but doesn't need texts or instant alerts | Yes | Daily batch overdue email only |
| Fewer than [N] users in one team or department | Unknown | Editing team is 1 team of 3; the org's user-count threshold isn't defined yet (org-profile.md not customized), and the read-only viewer population (hiring managers) spans many departments — IT should judge whether this counts against the threshold |

If no match: not applicable — this path matches. The one open signal (user count threshold across departments) is a judgment call for IT once org-profile.md defines a number.

## Org policy requirements applied

- None available. The organization profile for this framework (org-profile.md) has not been customized yet, so no org-specific hard requirements, data access process, or fit thresholds could be applied here. This is flagged as an open item for IT below.

## Out of scope

- Anything before the start date is confirmed — owned by recruiting, in a different system.
- IT, Facilities, or hiring managers editing anything — hiring managers get read-only view; IT and Facilities get email only.
- Real-time or instant alerts — a daily batch email is enough.
- Bank details or social security numbers — those stay in Workday/payroll systems.

## Open items for IT

| Item | Type | Blocking build? | Suggested owner |
|---|---|---|---|
| Confirm whether Workday can feed this tool automatically once a day, or only via the manual report Dana currently runs | Data access / integration | Yes | Workday systems team / IT |
| Review handling of confidential coordinator notes (visa status, background check results, accommodation requests) | Security / privacy review | Yes | IT security / privacy |
| No one in IT has been told this project exists yet | Stakeholder awareness | Yes | Dana |
| Organization profile (org-profile.md) is not yet customized — no hard requirements, data access process, or fit thresholds defined for this org | Framework setup | No | Platform/IT team |
| No project space exists yet for this app | Project setup | Yes | IT |
| Confirm Priya and Marcus are willing to use this tool before build (a prior shared list failed for this reason) | Adoption risk | No, but recommended before build | Dana |

## Suggested next step

Dana sends this brief to IT intake (no named contact or process is defined yet in org-profile.md, so use whatever general IT contact Dana normally uses) so the Workday connection and data-sensitivity questions can be looked at before build starts. In parallel, Dana should confirm Priya and Marcus's buy-in and share the written plan with Sam.
