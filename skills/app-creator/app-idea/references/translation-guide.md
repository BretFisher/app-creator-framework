# Translation Guide: Business Language ↔ Delivery Language

The App Creator (AC) thinks in terms of their job. IT and build agents think in terms of agile delivery and platform engineering. This guide maps between the two so you can ask questions in the left column and write the Technical Brief in the right column.

The AC should never need to learn the right-column words. If they use one on their own, fine, mirror it. Otherwise stay on the left.

## Contents

1. Concept map (what to ask, what to write)
2. Words to avoid and what to say instead
3. Question patterns that work with non-technical people
4. Recognizing an assumption when you hear one

---

## 1. Concept map

| What you're trying to learn | How to ask the AC | What you write in the Technical Brief |
|---|---|---|
| The problem | "Tell me about the last time this was a pain. What happened?" | Problem statement; business justification |
| Who uses it | "Who would need to look at this?" then, separately, "Who would actually update it?" | Actors, personas, user counts, read vs write roles |
| What it does | "Walk me through what you'd do, start to finish, on a normal day." | User stories (As a / I want / so that) |
| Success | "How would you know it's working? What would you show your boss?" | Acceptance criteria (Given / When / Then) |
| Priority | "If we could only do one of these first, which one?" | Backlog ordering; MVP scope |
| Data it reads | "What information do you look up to do this today? Where do you look it up?" | External data sources; integrations; read access requests |
| Data it writes elsewhere | "When you tick something off here, should anything change in another system too?" Ask this even if it seems unlikely. | Write integrations (higher risk, flag for IT) |
| Nice-to-haves | "What else would be great, even if it's not for the first version?" (ask once) | Backlog candidates; hidden scope and write-back risks |
| Data it owns | "What would the app need to remember from one day to the next?" | Owned entities; persistence; schema |
| Data quality and churn | "How often is that information wrong, or does it change after you first see it?" | Data freshness / sync frequency; data quality risk; reconciliation needs |
| Retention | "How long do you need to be able to look back at old records?" | Retention policy |
| Personal data | "Does any of this include names, contact details, health, pay, or anything about a specific person?" | PII / PHI / regulated data flags |
| Permissions | "Who should be able to see this? Who should be able to change it? Anyone who shouldn't?" | Authorization model; RBAC roles |
| Accountability | "If something was changed wrongly, would you need to know who did it?" | Audit logging |
| Login | "Would people use their normal work login?" | Authentication (usually org SSO) |
| Availability | "If it was down for an afternoon, what would happen?" | Availability target; business-hours vs always-on |
| Speed | "How fast does it need to feel? Is waiting a few seconds fine?" | Performance NFRs |
| Devices | "Where are people when they use it? Desk, phone, on the floor, in a vehicle?" | Platform and responsive requirements |
| Notifications | "Does anyone need to be told when something happens? How, and how quickly?" | Notification requirements; async jobs |
| Volume | "Roughly how many of these happen a day? A busy day?" | Scale estimate; capacity |
| Boundaries | "What's this app *not* going to do, even if someone asks?" | Out of scope |
| Dependencies on people | "Who else would need to say yes before you could use this?" | Stakeholders; approval gates |
| Existing workarounds | "How do you do this today? Spreadsheet, email, paper?" | Current state; migration or import needs |
| Lifespan | "Is this for a one-time thing, or ongoing?" | Lifecycle; decommission criteria |
| Project space | "Has IT already set up a project space for this, or is this the first anyone's heard of it?" (ask near the end) | Repository exists Yes / No / Unknown; open item to create one |
| Fit | "Would people outside your team want this too?" | App Creator fit assessment; graduation risk |
| Golden path | (don't ask directly; infer from device, data, notification, and write-back answers) | Golden path match, with signals and evidence |

---

## 2. Words to avoid, and what to say instead

Use the right column when talking to the AC. Use the left column only in Part 2 of the brief.

| Avoid | Say instead |
|---|---|
| user story, requirement | "a thing the app does", "something you'd do with it" |
| acceptance criteria, test | "how we'll know it's working", "what you'd check" |
| persona, actor, stakeholder | "the people who'd use it", "who needs to say yes" |
| MVP, iteration, sprint, backlog | "the first version", "what comes first", "the list of what's next" |
| API, integration, endpoint | "connect to", "pull information from", "the system where that lives" |
| database, schema, table, entity, record | "what the app keeps track of", "the information it saves" |
| persistence, storage | "remember", "save" |
| authentication, SSO | "logging in", "your normal work login" |
| authorization, RBAC, permissions model | "who can see what", "who's allowed to change it" |
| audit log | "a record of who did what" |
| NFR, SLA, SLO, uptime | "how reliable it needs to be", "what happens if it's down" |
| PII, PHI, PCI, regulated data | "information about a specific person", "health or payment details" |
| deploy, release, ship, environment, production | "make it available", "turn it on for the team" |
| repo, commit, PR, branch, git | "a project space IT sets up", "I've saved your plan", "the file with your plan in it" |
| backend, frontend, UI, UX | "the screens", "what you see", "how it works behind the scenes" |
| scope, out of scope | "what's in the first version", "what we're leaving out for now" |
| edge case | "what happens when things go wrong or aren't normal" |
| data model, ERD | "how the pieces of information relate" |
| latency, performance | "how fast it feels" |
| tech debt, refactor | (don't mention) |
| golden path, stack, platform, Kubernetes, container, Postgres, Node | "the standard way apps get built here", "a good fit for how we build things" |

If the AC asks "what does that mean?" about any word you used, that's a signal you slipped. Answer plainly and switch vocabulary.

---

## 3. Question patterns that work

**Ask for a story, not a specification.** "Tell me about the last time you did this" gets real details. "What are your requirements?" gets a blank stare.

**Ask about yesterday, not the future.** People describe current pain accurately and imagined solutions poorly. Get the current process first. The solution falls out of it.

**Ask for the exception after the rule.** After they describe the normal flow: "And when does that *not* work? What's the annoying case?" That's where the real complexity lives.

**Offer two concrete options instead of an open question.** "Would people mostly do this at their desk, or on their phone while walking around?" is easier to answer than "What are your device requirements?"

**Count things.** "About how many people?" "About how many times a day?" Rough numbers are fine. They separate a five-person tool from a department system.

**Suggest a default on preferences, not on facts.** "A year of history is probably plenty. Sound right?" works for retention, refresh frequency, devices, and notification timing. It does not work for "IT owns that data, right?" or "Your manager's approved this, right?" because the AC will agree to a plausible guess. Facts get open questions; preferences can get defaults.

**Look it up before you ask.** If the org profile, golden paths, or a data catalog can answer it, don't ask the AC. They should only be asked what they alone know.

**Reflect back in their words before moving on.** "So right now you copy the roster from the HR site into your spreadsheet every Monday, and the problem is it's out of date by Wednesday. Did I get that right?" Confirmation catches misunderstandings early and shows you were listening.

**Separate the problem from their proposed solution.** ACs often arrive with a solution ("I need a spreadsheet with a button that emails people"). Take it seriously, then ask what the button is for. The underlying need is what goes in the brief. Their solution idea goes in as one option, not the requirement.

**One question at a time.** A list of five questions gets one answered.

---

## 4. Recognizing an assumption when you hear one

Assumptions are stated as facts by someone who has never had to check. Listen for these shapes:

| What it sounds like | The assumption underneath | Ask |
|---|---|---|
| "Everyone has..." / "Everyone can..." | Universal access to a device, system, or skill | "Everyone? Including new hires, contractors, the night shift?" |
| "It's all in [system]" | The data exists, is accurate, is accessible, and is in a usable form | "Have you pulled that data out yourself before? What did it look like?" |
| "IT can just give us access" | Access is available and quick to grant | "Do you know who owns that data? Has your team asked for it before?" |
| "It's just a simple..." | The task is small | "Walk me through it anyway; the simple ones surprise us." |
| "People will use it because..." | Adoption is automatic | "What happens to someone who keeps using the old spreadsheet?" |
| "We'd never need to..." | A case will never happen | "Has it ever happened, even once?" |
| "My manager is fine with it" | Approval exists | "Have they seen the idea, or is that your read of them?" |
| "It only needs to work for us" | Scope stays small | "If it works well, who'd be the first person outside your team to ask for it?" |
| "The numbers are always right" | Upstream data quality | "When was the last time you found a mistake in it?" |

Record every assumption you hear in the "Things we assumed, and you confirmed" section, with the AC's answer. Unconfirmed assumptions go to "Open questions". Do this even when the assumption turns out to be true. IT needs to know it was checked.
