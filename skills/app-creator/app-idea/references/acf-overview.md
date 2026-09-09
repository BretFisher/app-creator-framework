# The App Creator Framework, in Brief

This file exists because the App Creator using this skill will never see the framework's source repository. Everything the agent needs to understand about the framework's purpose lives here.

## What the framework is

The App Creator Framework (ACF) is a way for organizations to let non-technical staff build small internal apps with AI agents, inside guardrails that IT defines. It combines policy, staff procedures, and agent automation so that platform engineers, security staff, and developers can offer a service to the rest of the organization: **describe what you need, and an agent will help you build it, safely.**

Each organization adopting the framework customizes it. The skills an App Creator uses (this one included) are configured by that organization's IT team before being handed out. See `org-profile.md` and `golden-paths.md` in this directory for that organization's specifics.

## Who App Creators are

An **App Creator** is a staff member who knows their own job deeply and has no software background. They can't read code and aren't expected to. The role is closer to a SharePoint site owner or a WordPress admin than to any kind of developer: lightly trained by IT, largely self-sufficient, building tools to get their own work done.

App Creators build software **for themselves and the people around them, within their own area of expertise.** They are not building for other departments, and they are not building enterprise systems. The framework calls this **personal software**. An app that grows beyond that, in users or in importance, eventually graduates to a formal IT project, and the App Creator becomes one stakeholder among many.

The framework deliberately avoids the terms "vibe coder", "citizen developer", and "casual developer". The role is a creative one, and the name should not imply the person is a kind of developer.

## Why the framework is careful about scope

Enterprise software needs a team to keep it stable, fast, and secure. The framework is not a substitute for that team. It produces a narrow slice of the software lifecycle, through pre-approved patterns called **golden paths**, so that small apps can be built and run safely without one. The fit checks in this skill exist to keep projects inside that slice, and to route projects that don't fit toward IT early, while the effort so far is still useful.

## Golden paths

A golden path is a pre-approved bundle of technology, hosting, data storage, and integration rules that the organization's platform can build, test, deploy, and secure with little human involvement. An idea that fits a golden path moves faster and needs fewer approvals. App Creators don't need to know what's in a golden path; the agent matches their needs against it and tells them, in plain language, whether their idea is a good fit for "the standard way apps get built here".

## The App Creator's journey

The framework gives App Creators three skills, used in order:

1. **app-idea** (this skill): a discovery conversation that turns an idea into a Project Brief. No code is written.
2. **build-app**: builds the app along a golden path, with tests, documentation, and a test environment. The App Creator may spend weeks iterating here.
3. **submit-app**: reviews the finished work and submits it for production approval.

Behind the scenes, IT runs its own skills: security review, supply chain validation, platform conformance, operational readiness, and release gates. The App Creator doesn't see those, but the Project Brief this skill produces is the first thing they read.

## Why data access matters so much

The hardest ongoing part of running this framework is getting App Creators access to the business data their apps need. Organizations with a central data catalog and API-first design make this quick; most organizations don't have that yet, and each new data source can mean a formal request and weeks of waiting. The discovery conversation spends more time on data than on anything else because a complete list of data needs, owners, and access status is what lets IT start those requests immediately.

## Where the human touchpoints are

Each organization decides how much IT involvement it wants, based on its maturity. Early on, IT reviews every brief and every production deployment. Over time, more of that review is automated. This skill doesn't need to know where an organization is on that curve; `org-profile.md` says who reviews briefs and what happens next.
