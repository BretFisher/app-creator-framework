# Interview transcript

Persona: `personas/hr-onboarding-tracker.md`  
Model: `claude-sonnet-5`  
Skill: `/Users/bret/code/github/bretfisher/app-creator-framework/skills/app-creator/app-idea`

### App Creator

Hi, I want to build a dashboard that shows me where every new hire is in their onboarding. Right now it's a nightmare spreadsheet.

---

### Agent (turn 1)

I saved a start file for your plan. I have one question.

Tell me about the last time the spreadsheet caused a real problem. What happened?

---

### App Creator

Oh, last month. A new hire's laptop was not ready on day one. IT did not know the start date changed. The person sat with nothing to do for half a day. The manager was angry and emailed Sam directly.

---

### Agent (turn 2)

So the start date changed, but that update never made it to IT, and the spreadsheet did not catch it. The new hire lost half a day, and the manager escalated it by emailing Sam.

Who else deals with this kind of mess besides you? For example, IT, the manager, anyone else?

---

### App Creator

Yeah, IT for laptops and accounts. Facilities for badges and lockers, mostly warehouse. And the hiring manager for the first week plan and buddy. Then me for all the paperwork and benefits stuff.

---

### Agent (turn 3)

Four groups touch onboarding: IT, Facilities, the hiring manager, and you for paperwork and benefits.

About how many new hires do you onboard in a typical month?

---

### App Creator

Usually 15 to 25. January and September it's more like double that, warehouse hiring gets busy then.

---

### Agent (turn 4)

That's a real swing — 15 to 25 most months, 30 to 50 in January and September.

What's your job title and team, so I can put your name on the plan correctly?

---

### App Creator

Dana Whitfield, HR Business Partner. HR team, obviously.

---

### Agent (turn 5)

Got it, saved. This will be used by four groups: you in HR, IT, Facilities, and hiring managers.

If you changed jobs tomorrow, who would take over running this tool?

---

### App Creator

Priya or Marcus, probably. They're the other two on my team who do onboarding, mostly for the warehouse sites.

---

### Agent (turn 6)

Good, so it stays inside your team either way.

Does anyone need to give the go-ahead before your team starts using this, like your manager, or IT?

---

### App Creator

Sam, my HR Director, is already on board. I mentioned it to them, they said sounds good. IT I haven't talked to yet.

---

### Agent (turn 7)

That's good context — Sam's given a verbal yes, but IT hasn't been looped in yet. I'll flag that as something to confirm before building, since IT is one of the app's users.

Now let's talk about what the dashboard actually does. Walk me through it: from the day a new hire signs their offer to their first day, what would you want to see or update in this tool?

---

### App Creator

Oh, wait, not from the offer. That's recruiting's job, different team, different system. I only want it once the start date is confirmed. So once that's locked in, I want to see the new hire on the dashboard with all their tasks - laptop ordered, badge made, first week plan, paperwork, all that - and I want to tick things off as they get done and leave myself notes.

---

### Agent (turn 8)

So the tool starts once a start date is locked in, not before — recruiting's system handles everything before that. Got it, that's a clear boundary for the first version.

Here's an important one: would IT, Facilities, and the hiring manager each log in and check off their own tasks, or would you check everything off yourself based on what they tell you?

---

### App Creator

No no, I'd check it off myself, that's how it works now - they email me or I email them to ask. I don't think IT and Facilities want to log into some new system just for this. Just me, Priya, and Marcus updating it.

---

### Agent (turn 9)

That simplifies things a lot — it's really a tool for you, Priya, and Marcus to track tasks that other teams are responsible for, not something IT or Facilities log into.

Would you want the tool to remind you about anything — like an overdue task close to someone's start date — or is checking it yourself enough for now?

---

### App Creator

Yeah, an email if something's overdue would be great, to me and whoever it's supposed to go to. Once a day is fine, I don't need instant alerts blowing up my phone.

---

### Agent (turn 10)

Once-a-day overdue emails, good — that's simple and not urgent-alert territory.

For those overdue emails, would they go to the same fixed address each time — like an IT helpdesk inbox or a Facilities team address — or does it change depending on who's involved with that particular new hire?

---

### App Creator

Hmm, good question. I guess it'd depend on the task - if it's a laptop that's overdue, it should go to whoever in IT handles that, not just me. Same for Facilities and the manager. So it changes depending on the task, yeah.

---

### Agent (turn 11)

When a new hire comes in, do you already know exactly which person in IT and Facilities is handling their setup, and who the hiring manager is? Or would that take some digging each time?

---

### App Creator

The hiring manager, that's easy, it's right there in Workday. IT and Facilities, honestly it's usually just whoever picks up the ticket, there's a general inbox for each. So maybe I'd just want it to go to those team inboxes, not a specific person.

---

### Agent (turn 12)

That simplifies notifications nicely — fixed inboxes for IT and Facilities, and Workday for the hiring manager's email.

Since you mentioned Workday: does Workday also have the new hire's name, site, and start date, or do you get those from somewhere else first?

---

### App Creator

Yeah, that all comes from Workday. Every Monday I copy the new starters over into my spreadsheet from there. Name, start date, department, manager, location, job title, all of it's in Workday already.

---

### Agent (turn 13)

That current manual copy from Workday every Monday is exactly the kind of pain worth fixing.

When you pull that data from Workday, do you use a report or export file, or do you copy it by hand from the screen?

---

### App Creator

Someone in IT set up a report for me a while back, so I run that and copy it in. I've never actually pulled data out of Workday any other way, so I don't really know what else is possible - I just figured IT could hook it up directly for this.

---

### Agent (turn 14)

That's a good one to flag — you have a report you already run and have access to, but whether it can feed the tool automatically versus you still uploading it each week is something for IT to confirm, not something we can assume.

Next: once a new hire has started and everything's checked off, how long do you need to be able to look back at their onboarding record?

---

### App Creator

About a year, I'd say. Sometimes we get an audit question, or someone asks why a particular person's onboarding dragged on, and I need to go back and check.

---

### Agent (turn 15)

That's useful — a one-year lookback for audits and questions about delays.

Since audit questions come up: would you need to know who checked something off and when, not just that it's marked done today?

---

### App Creator

Yeah, actually, that would help. Right now if someone asks "did you follow up on this" I have to dig through my email to prove it. If the tool just remembered who checked it off and when, that'd save me a lot of time.

---

### Agent (turn 16)

That's a real time-saver — a record of who checked off what, and when.

Should Priya and Marcus be able to see and update every new hire in the tool, or just the ones at their own sites?

---

### App Creator

Honestly, I think all three of us should see everyone. Sometimes we cover for each other, and it's easier if nobody's locked out of anything.

---

### Agent (turn 17)

Good — simple: all three of you see and edit everything, nobody else gets in.

One more on sensitive info: besides names and job details, does any of the paperwork or benefits tracking involve things like social security numbers, bank details, or health information? Or does that live somewhere else entirely?

---

### App Creator

No, nothing like bank details or social security numbers, that's all in Workday or payroll systems, not something I'd put in this. But... well, yeah, I guess my notes do have some personal stuff. Like if a background check is still pending, or someone's visa status, or if a manager tells me someone's struggling, or there's an accommodation request. I just think of that as normal HR stuff, not "personal data" or whatever.

---

### Agent (turn 18)

That's important to flag — those notes could include visa status, background check status, health or accommodation details. That's sensitive personal information even if it feels like routine HR work to you, so I'll mark it for IT to review before building, and make sure it stays visible only to you three.

Now, devices: are you usually at your desk when you update this, or would you want to check it from your phone too?

---

### App Creator

Mostly at my desk. But sometimes I want to glance at it on my phone, like before someone's first day, just to double check everything's ready.

---

### Agent (turn 19)

If this tool was down for an afternoon, would that actually cause a problem, or would you just fall back to email like today?

---

### App Creator

Oh, that'd be annoying, not a crisis. I'd just go back to the spreadsheet for the afternoon, like I do now anyway half the time.

---

### Agent (turn 20)

That confirms this is genuinely low-stakes if it hiccups — good to know.

Would you and Priya and Marcus log in with your normal work login, the same one you use for email and other systems?

---

### App Creator

Yeah, I'd expect so. Same as everything else, I don't want another password to remember.

---

### Agent (turn 21)

Good, that'll be the normal work login, so no new password to manage.

If we could only build one piece first, which matters more to you: having every new hire's tasks in one place to look at, or the daily overdue-reminder emails?

---

### App Creator

Definitely having everyone in one place with the tasks. The reminders would be nice, but honestly just not having a nightmare spreadsheet would fix most of my problem.

---

### Agent (turn 22)

Makes sense — the one-place view is the core fix, reminders are a nice-to-have on top.

Before I move on: have you tried anything else to solve this before, like a shared spreadsheet or some other tool, and what happened with that?

---

### App Creator

Yeah, we tried a SharePoint list a couple years back. Died pretty fast, because nobody but me actually updated it. Priya and Marcus just kept emailing me stuff instead.

---

### Agent (turn 23)

That's an important data point — the SharePoint list failed because only you kept it updated. Let's make sure this one doesn't repeat that.

Have Priya and Marcus actually said they're on board with using this, or is that still something to check with them?

---

### App Creator

Honestly, I haven't asked them yet either. Probably should, huh.

---

### Agent (turn 24)

One more before we look at what it does: when a start date changes after you've already added someone, or a new hire falls through, what happens? Would you want the tool to help with that, or is that just something you'd handle manually for now?

---

### App Creator

Oh, that happens all the time, honestly - probably a third of start dates move at least once. I'd want the tool to just pick that up automatically from Workday whenever it changes, that's kind of the whole point of connecting the two, so I'm not manually updating dates all the time.

---

### Agent (turn 25)

That's the core of the original problem, so it's worth getting the details right.

When you say "pick it up automatically" — would once a day be enough, like an overnight refresh, or does it need to update the moment something changes in Workday?

---

### App Creator

Once a day is fine, overnight or first thing in the morning, whatever's easiest. I don't need it live.

---

### Agent (turn 26)

I've written up your full plan. Here it is in plain terms — tell me if anything is wrong or missing.

**The problem:** Your spreadsheet doesn't keep up. Last month a start date changed, IT never found out, and a new hire sat with no laptop for half a day. Nobody has one place to see if every onboarding task is done.

**Who uses it:** You, Priya, and Marcus log in and see everyone. IT, Facilities, and hiring managers never log in — they just get emails.

**What it does:**
1. New hires show up automatically each morning, pulled from Workday — no typing.
2. You see every task for each person: laptop, badge, first week plan, paperwork.
3. You tick off tasks and leave notes. It remembers who did it and when.
4. Start date changes get picked up automatically, once a day.
5. Overdue tasks trigger a daily email to you and to whoever owns that task (IT inbox, Facilities inbox, or the manager).

**What it won't do yet:** anything before the start date is locked in, logins for IT/Facilities/managers, instant alerts, or anything with bank details or social security numbers.

**Data:** it reads name, start date, site, department, job title, and manager from Workday. It keeps its own task list, notes, and a record of who checked off what and when, for a year.

**Access:** only the three of you can see or touch it.

**Open items I flagged:** whether IT can connect this to Workday automatically, whether Priya and Marcus are actually willing to use it, and whether IT or Sam have seen the actual written plan yet.

Does this match what you have in mind?

---

### App Creator

Wait, hold on. That's not quite right. I don't want managers checking things off, no, but I do want them to be able to look at their own new hire's progress. That's a big part of why I wanted this in the first place - so they stop emailing me every five minutes asking "is the laptop ready yet." So they need to see something, just not touch anything, and definitely not see my notes.

---

### Agent (turn 27)

Good catch, that's an important correction — thanks for flagging it.

Would hiring managers log in with their normal work login too, the same way you three would?

---

### App Creator

Yeah, same login as everything else. Most of head office has a laptop, though the warehouse managers mostly just use a shared computer in the site office, or their own phone I guess.

---

### Agent (turn 28)

I've updated the plan: hiring managers can log in to see only their own new hire's status, no notes, no editing — everything else stays the same.

Does that fix it, or is there still something off?

---

### App Creator

Yeah, that's it. That's exactly what I want.

---

### Agent (turn 29)

Great, Part 1 is locked in. One more question before I wrap up the plan.

Has IT already set up a project space for this app, or is this the first anyone's heard of it?

---

### App Creator

No, I don't think so. I haven't even talked to anyone in IT about this yet. Not sure who I'd even ask, honestly.

---

### Agent (turn 30)

Your plan is finished and saved as **project-brief.md** in your project folder. You can open or download it from there.

Here's what happens next, and what's on you:

1. **Send the file to your IT contact.** This organization hasn't set up a specific intake contact for these plans yet, so use whoever you'd normally go to in IT. Tell them this is an App Creator project brief.
2. **Two things in the plan need IT's answer before build starts:** whether Workday can feed this tool automatically each day, and how to handle the confidential notes (visa status, background checks, accommodation requests).
3. **Two things are on you before build starts:** check that Priya and Marcus actually want to use this day to day, and share the written plan with Sam — a verbal yes isn't the same as seeing it on paper.

Keep the file. Whoever builds this next will need it.

[INTERVIEW COMPLETE]

---

