# Discovery Checklist

What must be known before the Project Brief can be called complete. Use this to decide what to ask next and when to stop. The order is a suggestion; follow the conversation where it goes, but come back for anything unchecked.

Within a phase, ask items in dependency order. Some items only make sense after another is answered (you can't ask how many of each kind of person there are until you know the kinds). When an answer opens something new, ask about that next, then return to the list. Never ask a question built on a guess about an answer you haven't heard.

At each phase boundary, tell the AC in two or three sentences what is settled and what you'll ask about next.

Write to the draft brief as you learn things. Don't hold everything in your head until the end. If the session is cut short, the AC should still have a useful partial document.

## Phase 1: The problem (do this first, spend real time here)

- [ ] What is painful, slow, or error-prone today, in the AC's own words
- [ ] A specific recent example of the pain (a real day, a real incident)
- [ ] How they do it today (spreadsheet, email, paper, another system, memory)
- [ ] Who else feels this pain, and how many of them there are
- [ ] What "better" looks like to them, in outcomes rather than features
- [ ] Whether they've tried to solve it before and what happened

Stop signal: you could explain the problem to a stranger in two sentences and the AC would nod.

## Phase 2: The people

- [ ] The AC's own name, job title, and team, for the brief header (ask once, early; it also tells you how to address them)
- [ ] Every kind of person who'd *look at* it, with their job and what they need to see
- [ ] Every kind of person who'd *update* it (usually a smaller group)
- [ ] Rough count of each kind
- [ ] Who'd be the *owner* if the AC changed jobs
- [ ] Who needs to say yes before it's used (manager, data owner, anyone else)
- [ ] Whether anyone outside the AC's team or department would use it

Stop signal: every actor row in the Technical Brief can be filled in.

## Phase 3: What it does

- [ ] The main path, start to finish, as a story
- [ ] The exceptions and annoying cases
- [ ] Which single capability matters most if only one could ship first
- [ ] Asked "what else would be nice to have?" once, and sorted each answer into first version / later / not this app
- [ ] Things that came up but are being left out, and why
- [ ] For each main capability, a concrete way the AC would check it works

Stop signal: each capability has at least one checkable "how we'll know it's working" line.

## Phase 4: Information

This phase matters most to IT. Data access is the most common thing that stalls an App Creator project. Be thorough here even if the AC finds it tedious.

For information the app reads from elsewhere:
- [ ] What it is
- [ ] Where it lives today (system name if they know it)
- [ ] Who owns it (team or person)
- [ ] Whether the AC has access today, and how they get at it (screen, export, report)
- [ ] Whether anything needs to be *written back* to another system (flag as higher risk)
- [ ] How often that information is wrong, or changes after the AC first sees it (start dates that move, names that get corrected). This decides how often the app must refresh and whether stale data is a risk

For information the app keeps itself:
- [ ] What it needs to remember between uses
- [ ] How long it needs to be kept
- [ ] Whether any of it is about specific people (names, contact, health, pay, performance, ID numbers)

- [ ] Whether any information is confidential, regulated, or would be embarrassing if seen by the wrong person

Stop signal: both data tables in Part 1 are filled in, with no "not sure" left unexplored.

## Phase 5: Rules and expectations

- [ ] Who can see what
- [ ] Who can change what
- [ ] Whether anyone needs a record of who did what
- [ ] Where and on what device people use it
- [ ] What happens if it's unavailable for an afternoon
- [ ] Whether anyone needs to be notified of anything, and how fast
- [ ] Rough volume: how many of the main thing happen per day, and on a busy day
- [ ] Whether this is ongoing or for a one-time event

Stop signal: the non-functional requirements table has a source line for every row you filled in, and blank rows are deliberately blank.

## Phase 6: Assumptions and fit

- [ ] Every assumption heard during the conversation is listed, with confirmed / corrected / unknown
- [ ] Anything nobody could answer is in Open Questions with a name next to it
- [ ] App Creator model fit assessed (see SKILL.md and any thresholds in org-profile.md)
- [ ] Golden path match assessed against the signals in golden-paths.md, with evidence per signal
- [ ] If either fit is conditional or poor, the AC has been told plainly and kindly, and the reason is recorded
- [ ] Hard requirements from org-profile.md copied into Part 2
- [ ] Extra discovery questions from org-profile.md asked
- [ ] Asked whether IT has already set up a project space for this app, and recorded the answer (Yes / No / Not sure)

## Done

Nothing is left silently assumed. Every branch the conversation opened is either answered or written down as an open question with a name next to it. Concretely, the brief is complete when:

1. Every phase's stop signal is met, or the gap is recorded as an open question.
2. The AC has read Part 1 (or had it read back to them) and said it's right.
3. Part 2 contains nothing that Part 1 doesn't support.
4. Both fit assessments, the org policy section, and the next step are filled in.
5. No template placeholder text remains anywhere in the brief, including the header table.
6. The document is saved, and the AC knows how to get it and where it goes next. If no project space exists, that is recorded as an open item for IT.
