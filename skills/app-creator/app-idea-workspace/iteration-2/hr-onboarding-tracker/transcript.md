# Interview transcript

Persona: `personas/hr-onboarding-tracker.md`  
Model: `claude-sonnet-5`  
Skill: `/Users/bret/code/github/bretfisher/app-creator-framework/skills/app-creator/app-idea`

### App Creator

Hi, I want to build a dashboard that shows me where every new hire is in their onboarding. Right now it's a nightmare spreadsheet.

---

### Agent (turn 1)

A dashboard for new hire onboarding status. I understand the pain point. I saved a draft plan at `project-brief.md`. I will update it as we talk.

Tell me about a specific recent time the spreadsheet failed you. What happened?

---

### App Creator

Oh, last week. A guy started on Monday, IT never got the laptop request. Nobody flagged it to me because it wasn't on my radar until his manager pinged me Tuesday asking why the new hire couldn't log in. I had no idea. Spent half my morning chasing IT and apologizing to the manager.

---

### Agent (turn 2)

That's a clear failure: a step got missed, and you only found out when the manager complained, not before.

How often does something like this happen — a step slipping through unnoticed until someone complains?

---

### App Creator

Honestly? At least once or twice a month. Maybe more during the busy hiring months. It's always something — laptop, badge, benefits paperwork not signed. I just don't have a good way to see it coming.

---

### Agent (turn 3)

That gives me a sense of scale. Roughly how many new hires do you onboard in a typical month, and in a busy month?

---

### App Creator

Normal month, maybe 15 to 25. But January and September are brutal, like double that, because of the warehouse seasonal hiring. Those months are chaos.

---

### Agent (turn 4)

That's real volume — up to 50 a month in peak season. Besides you, who else deals with this pain when a step gets missed? Think IT, benefits, hiring managers.

---

### App Creator

Well, hiring managers get annoyed, obviously, they're the ones stuck with a new hire who can't do anything day one. IT and Facilities get emails from me chasing them. And honestly Priya and Marcus on my team deal with the same headache — they do onboarding too, mostly for the warehouse sites.

---

### Agent (turn 5)

That's helpful — so you, Priya, and Marcus all run into this, and IT, Facilities, and hiring managers feel the ripple effects.

What would "better" look like for you? Not the tool itself — what would actually change about your day if this problem went away?

---

### App Creator

I'd just... not have to chase people by email all day. I'd open one thing, see everyone starting this month, see what's ticked off and what's not, and know instantly who's behind. I could leave myself a note on someone instead of trying to remember it or digging through my inbox.

---

### Agent (turn 6)

One more on the problem: have you tried to fix this before — a different spreadsheet, a shared tool, anything? What happened?

---

### App Creator

Yeah, a couple years back I set up a SharePoint list for it. Died fast — nobody but me ever updated it, so it went stale and I gave up and went back to Excel.

---

### Agent (turn 7)

Let's update the plan with what's settled: the problem is you, Priya, and Marcus have no single view of onboarding status across up to 50 new hires a month, so steps like laptops, badges, and paperwork slip silently until a manager complains. A past SharePoint attempt died because only you kept it updated. Next I want to nail down exactly who'd use this new one.

Would IT and Facilities check things off themselves in the app, or would you, Priya, and Marcus be the ones marking a step done after you chase them by email or phone?

---

### App Creator

Us — me, Priya, Marcus. IT and Facilities would still just email us like they do now, or maybe we'd chase them, and we'd tick it off. Though honestly it'd be great if hiring managers could at least look at their own new hire's status so they'd stop asking me too. They don't need to edit anything, just see it.

---

### Agent (turn 8)

Good — so hiring managers get read-only visibility into just their own new hires, nothing more. Roughly how many different hiring managers would that be touching in a typical month?

---

### App Creator

Oh, across the whole company? There's like 60 hiring managers total, spread across every department and site. Not all active at once obviously, but any of them could have a new hire in a given month.

---

### Agent (turn 9)

That's a big reach for a read-only view, but it's still just look-not-touch, tied to their own new hire — good to know for later. If you moved to a different role, who'd take over owning this app — Priya, Marcus, or someone else?

---

### App Creator

Probably Priya, she's been here longest after me. Or honestly it'd just stay with whoever's doing my job. Sam, my HR Director, would be the one who'd know for sure.

---

### Agent (turn 10)

Last people question: who needs to say yes before you start using something like this — is that Sam, or someone else?

---

### App Creator

Sam, yeah. Actually Sam's already on board with this — I mentioned it in a 1:1 a while back and Sam said "sounds good." So I think we're clear there.

---

### Agent (turn 11)

Quick check on that: has Sam actually seen a plan like this one, or was that "sounds good" more of a general reaction to the idea in passing?

---

### App Creator

Huh. No, actually, just the passing comment. Sam hasn't seen anything written down. I guess I should show them this before I get too far ahead of myself.

---

### Agent (turn 12)

Here's where we stand: the problem is clear, and so is who's involved — you, Priya, and Marcus update it; hiring managers just look at their own new hire; IT and Facilities stay outside the app. Next I want to understand what you'd actually do inside it.

Walk me through it for one new hire, start to finish. What would you do first?

---

### App Creator

First thing, I'd want to see the person show up — their name, start date, department, manager, location, job title — so I know who's coming. That stuff's all in Workday already, so I'd just want it to pull in automatically instead of me copying it over every Monday like I do now.

---

### Agent (turn 13)

Got it — new hire info pulled automatically from Workday instead of copied by hand. After that shows up, what's next? What are the steps you'd track for each person?

---

### App Creator

Then there's a bunch of tasks that need to happen. IT stuff — laptop, accounts set up. Facilities — badge, desk, locker if it's a warehouse person. The hiring manager's supposed to do a first-week plan and set up a buddy. And then HR stuff — paperwork, policy sign-off, benefits enrollment. I'd want to see all of that per person and tick each one off as it gets done.

---

### Agent (turn 14)

That gives a clear checklist: Workday info up top, then IT, Facilities, manager, and HR tasks, each tickable.

Now the exception case — like the laptop story. When does a task like that go wrong, and would you want the app to flag it before day one, or just show you what's not done yet when you look?

---

### App Creator

I mean ideally it'd tell me before it becomes a problem, not just sit there quietly. Like if something's overdue and it hasn't been done, send me an email. Doesn't need to be instant — once a day is plenty. And send it to whoever owns the task too, not just me, so they get nagged directly instead of me having to do it.

---

### Agent (turn 15)

That overdue-email idea makes sense — a quiet checklist doesn't help if nobody's watching it. For a task to be "overdue," the app needs to know when it's supposed to be done by. Is that always "before the start date," or do some tasks have their own deadline — like benefits enrollment being due some days after start?

---

### App Creator

Hmm, good question, I haven't really thought about it that precisely. I guess laptop and badge really need to be done before start date, that's the urgent one. Benefits and some of the paperwork happens over the first few weeks — the whole onboarding process kind of runs about 90 days total. So yeah, different tasks probably need different deadlines, not all tied to day one.

---

### Agent (turn 16)

That's useful — different tasks, different deadlines, spread across a 90-day window. When a task like "order laptop" goes overdue, who exactly should get that email — a specific IT contact, or a general IT inbox?

---

### App Creator

Honestly I don't know off the top of my head — there's a general IT helpdesk email I use now when I chase them, so probably that. Same idea for Facilities, they've got a shared inbox too. Not sure about the hiring managers, that'd just go to them directly since it's their own name on it.

---

### Agent (turn 17)

Good, that's enough to go on for now — exact addresses can be nailed down later. If you could only have one piece of this working first, which matters most: seeing the checklist status for everyone, or the automatic overdue emails?

---

### App Creator

The checklist for sure. Just seeing where everyone stands would already be huge. The emails would be great on top of it but I could live without them for a while if I had to.

---

### Agent (turn 18)

Good — the status checklist is the core, and overdue emails are a strong second. Now the once-only question: what else would be great to have, even if it's not in the first version?

---

### App Creator

Oh, honestly? It would be amazing if ticking something off in the dashboard also marked it complete in Workday automatically, so I'm not doing double entry anywhere. But that's not essential, the spreadsheet doesn't do that either, so I can live without it.

---

### Agent (turn 19)

Noted — that's a nice-to-have for later, not this version, and it's a write-back into Workday, so it'd need extra care when it comes up. What would tell you the checklist view is actually working — what would you check, or show Sam, to know it's doing its job?

---

### App Creator

Honestly, just — I stop getting surprised. If I can look at it any given day and know exactly who's behind and on what, without emailing anyone to ask, that's success. And if Sam asks "how's onboarding going this month" I can just pull it up instead of scrambling to build a summary.

---

### Agent (turn 20)

Let's lock in what we've settled: the checklist view is the core — new hire info from Workday, a per-person task list across IT/Facilities/manager/HR, ticked off as done. Overdue email nagging and a Workday write-back are real wants, but not required for the first version. Success looks like: no more surprises, and a one-glance answer when Sam asks how onboarding's going.

Now let's nail down the data side, since this is what IT needs most. You mentioned copying new hire info from Workday every Monday — how do you get it today? Do you log into Workday yourself and pull a report, or does someone send it to you?

---

### App Creator

There's a report someone in IT set up for me in Workday, I just run it myself and copy the rows into my spreadsheet. I don't really do anything fancy in there, I just pull that one report.

---

### Agent (turn 21)

Good, that clarifies your access today. That report exists, but it's a manual pull — for the dashboard to update itself, IT would need to set up an automatic feed instead of you running it by hand. Do you know who manages Workday on the IT side — a specific team or person?

---

### App Creator

Not really, no. I just email the general IT helpdesk and someone gets assigned to it. I've never had to ask for anything like an automatic feed before, I just assumed it's all in Workday already so IT could just connect it up. Is that not how it works?

---

### Agent (turn 22)

Good question, and the honest answer is: not always automatically. Connecting two systems usually needs a specific setup step on IT's side, and since nobody's asked for this kind of automatic feed before, I can't tell you how long that takes here. I'll flag it as something for IT to arrange — it's not a blocker to writing the plan, just something they'll need to act on.

Next: once a new hire finishes onboarding, do you ever need to look back at their record — say, six months later — or is it done once they're through the 90 days?

---

### App Creator

Oh yeah, I need to look back sometimes. Audits, or if someone asks "why did this person's onboarding drag on so long," I need to go dig up what happened. Probably want to keep it around for like a year at least.

---

### Agent (turn 23)

A year sounds reasonable for that — good default for audits. Since this tracks specific people: besides names and job details, will any task involve sensitive info — things like benefits plan choices, salary, or ID numbers — or is it really just "done / not done" status on each step?

---

### App Creator

Well, yeah, I guess. My notes sometimes have stuff like — background check still pending, or someone's visa/right-to-work status, or if a manager tells me privately "this person's struggling," or an accommodation request came in. It's not on the checklist itself exactly, it's more in the notes I leave myself. But yeah, that's personal stuff.

---

### Agent (turn 24)

That's sensitive material — background checks, immigration status, accommodation requests, private manager comments. Those notes should stay separate from what hiring managers see, correct? Just for you, Priya, and Marcus, while managers only see the plain checklist status?

---

### App Creator

Yeah, exactly, definitely not managers. That stuff's just for us three, not for anyone else to see.

---

### Agent (turn 25)

Good, that's clear. Given how sensitive some of this is: if a task got marked done or a note got changed, would you ever need to know who made that change and when?

---

### App Creator

Yeah, probably good to have, especially for the audit stuff. If Sam asks "who marked this done" or "when did this note get added," I'd want an answer.

---

### Agent (turn 26)

Good — a record of who did what will matter here. Next: where would you, Priya, and Marcus mostly use this — at your desks, or on your phones moving around too? And what about the hiring managers checking their view?

---

### App Creator

Mostly at my desk, honestly, that's where I do most of this stuff. But I'd like to be able to glance at it on my phone too, like the night before someone's first day just to double check things are set.

---

### Agent (turn 27)

And hiring managers checking their own new hire — desk browser too, or would some want it on their phone as well?

---

### App Creator

Honestly probably mixed. Head office managers all have laptops so they'd just use that. But warehouse site managers mostly work off a shared PC in the site office, so it'd probably be their phone otherwise — everyone's got a work phone, right?

---

### Agent (turn 28)

That's exactly the kind of thing worth double-checking rather than assuming. Do all the warehouse site managers actually have a work phone, or is that true for most but not all of them?

---

### App Creator

Huh. Actually... now that you say it, I'm not sure that's true. I think some of them just use their own personal phone for everything, we don't necessarily give them company ones. I was assuming, yeah. Good catch.

---

### Agent (turn 29)

Good catch again — noted. Since managers might use personal phones for this, that's worth flagging for IT to confirm their policy on that, though the risk is low since managers only ever see plain status, never the sensitive notes.

Next: if the dashboard was down for an afternoon, what would that actually mean for you?

---

### App Creator

Not the end of the world, honestly. Annoying, but I'd just go back to checking my email and the spreadsheet for a bit until it's back. Nobody's going to lose their job over it being down an afternoon.

---

### Agent (turn 30)

Good — business-hours availability is plenty; this doesn't need to be always-on critical infrastructure. Last one on this topic: would everyone — you, Priya, Marcus, and the hiring managers — log in with your normal work accounts, the same one you use for email and everything else?

---

### App Creator

Yeah, I'd expect so, same login as everything else. I don't want another password to remember, God knows I have enough of those already.

---

### Agent (turn 31)

Just about everything is settled now. Last question before I put together the full plan: has IT already set up a project space for this app, or is this the first anyone's heard of it?

---

### App Creator

No, I don't think so. This is the first time I'm even writing any of this down. I'm not really sure who I'd even ask about that, honestly.

---

### Agent (turn 32)

I've saved the full plan. Before we finish, let me read Part 1 back to you — your part of the plan — so you can check I got it right.

**The problem:** You, Priya, and Marcus track onboarding in a spreadsheet. Steps like laptops, badges, and paperwork slip through silently until a manager complains. This happens once or twice a month, more during your busy seasons (January and September). A recent example: a new hire had no laptop on day one because IT never got the request.

**Who uses it:** You, Priya, and Marcus see and update everything, including private notes. About 60 hiring managers across the company can look at their own new hire's plain status only — no notes, nothing they can change. IT and Facilities don't log in; they'd get an email if we add that feature later.

**What it does:** Pulls new hire info from Workday automatically. Shows a checklist per new hire — IT, Facilities, manager, and HR tasks — each with its own deadline across the 90-day onboarding period. Lets you tick off tasks and leave private notes. Lets a hiring manager check their own new hire's status.

**What it won't do yet:** Automatic overdue emails (a strong second priority, added later). Writing completed tasks back into Workday (not planned at all right now).

**Data it needs:** New hire profile info from Workday — you have manual report access today, but an automatic connection has never been requested. Task checklists and notes are new information the app keeps itself, kept for a year, and some of it is confidential (background checks, immigration status, accommodation requests).

**Confirmed assumptions:** Sam has not actually seen this plan yet. Nobody has asked IT about an automatic Workday connection before. Not every warehouse manager has a work phone.

**Open questions:** Sam's approval, IT's answer on the Workday connection, and IT's policy on personal phones.

Did I get all of that right, or is anything off?

---

### App Creator

Yeah, that all sounds right to me. Good summary.

---

### Agent (turn 33)

Good, your plan is confirmed and saved.

Your plan is in the file **project-brief.md**. Keep this file — you'll need it for the next step. It also has a Part 2, written for IT, that turns your plan into their language. You don't need to read that part yourself.

**What happens next:** Show this plan to Sam first, since Sam hasn't seen a written version yet. After that, send the file to your IT contact for review. Two things in it need IT's direct attention: the request to pull new hire data from Workday automatically, and a check on how the confidential notes (background checks, immigration status, accommodation requests) get handled.

**What you need to do:** Send the file to Sam, then to IT. If they ask about the Workday connection or the personal-phone question, those are the open items to raise.

[INTERVIEW COMPLETE]

---

