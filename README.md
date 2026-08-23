# The App Creator Framework (aka Enterprise Vibe Coding Platform)

Guidance for organizations to provide a platform for staff to build internal, AI-generated apps with IT-governed guardrails and agentic SDLC automation.

# Overview

The App Creator Framework (ACF) is a set of policy guides, staff procedures, and agentic automations that bring together platform engineers, security staff, and software engineering teams to create an internal organizational solution that provides non-IT staff a path to use agents for software design and development, with limited engineering involvement.

I call these customers (end-users) of the ACF "App Creators", and describe my reasons for that new job role title below. Anyone outside traditional SDLC roles in an organization could be a candidate for the App Creator role.

## What encompasses this framework?

The ACF covers multiple technical and procedural sub-projects to fully implement a platform and service offering that, if taken as far as it can go, will allow App Creators to start a new project on their own without IT involvement and see it through to production with very little human oversight. Each org can decide the human touchpoints, largely based on its SDLC maturity and org culture. With sufficient infrastructure, policy, and automation, an internal IT department may only need to onboard the App Creator initially and then be involved only at deliberate gates, such as the initial production deployment.

## Focus areas of this framework:

- **App Creator tooling.**
  - Web/Mobile agent chat. No local tooling required.
  - No local dev/test environments. All development via remote agents environments.
  - Onboarding docs and tutorials, maybe even a practice app to build.
  - Access to skills, MCPs, and plugins that are hopefully centrally managed.
  - **Initial App Creator Skills**
    1. **app-idea - Define the App** — Guides discovery; defines scope, users, requirements, and acceptance criteria; confirms the idea fits the App Creator model.
    2. **build-app - Build the App** — Selects the golden path; creates and modifies the app; produces tests, documentation, test/UAT environments, and deployment configuration. App Creator could spend weeks iterating with this skill. Each change committed to the repo via PRs. This could also be multi-user building.
    3. **submit-app - Prepare the Change** — Reviews work, preform final checks, then submits production deployment request to IT.
- **Strategies on how to apply the SDLC to the workflow of a App Creator.**
  - Largely implemented as event-based agent automation and skills for App Creator use.
- **Likely touchpoints for security staff, platform engineering staff, and developer team staff.**
  - Data access requests may need approval, secrets, etc.
  - IT may choose to review a new project before prod deploy.
  - Automated agent PR/deployment reviews may flag issues for manual IT resolution.
  - Many touchpoints at ACF Level 1 (below) and automating many of those as org matures.
  - **Initial DevSecOps Skills**
    1. **Security Review** — Reviews code, dependencies, secrets, data handling, IAM, and infrastructure; produces prioritized findings with remediation.
    2. **Supply Chain Validation** — Validates dependencies, containers, builds, SBOMs, provenance, and licenses; enforces organizational policies.
    3. **Security Release Gate** — Evaluates unresolved findings and release evidence; returns approve, block, or human review required.
  - **Initial Platform Engineering Skills**
    1. **Platform Conformance Review** — Checks approved architecture, templates, infrastructure, and deployment patterns; detects divergence from the golden path.
    2. **Operational Readiness Review** — Evaluates reliability, observability, migrations, scaling, cost, and ownership; confirms the app can operate safely.
    3. **Deployment Readiness Gate** — Checks environment, rollout, rollback, and post-deployment validation; returns approve, block, or human review required.
- **Skills, agent files, agent configs, and processes to provide guardrails and policy enforcement.**
- **A maturity model for starting small and more human-driven, toward a mostly agent-driven lifecycle.**

## The App Creator Job Role

We think **AI App Creator, or just App Creator,** is the best fit. I hope it sticks; here's why:

This archetype is distinctly different from a professional software developer or even developer-adjacent roles like PMs, designers, operators, etc. **If you can read code, or sit through an engineering meeting without being completely confused, this new job role is not for you.**

**The App Creator staff role is much closer to previous roles like SharePoint site admins or WordPress admins.** Typical orgs have had these in every department for decades, lightly trained by IT, and largely self-sufficient at achieving business goals in platforms without knowing the SDLC. They aren't even akin to low-code users, because they can take on this new role without any coding concepts, which low-code and even some no-code tools require.

An App Creator in an org uses AI agents to build software for **their specific job roles, using their professional expertise** to guide project requirements. By contrast, professional developers mostly create software based on **other people's requirements**. **App Creators don't create apps for others outside their subject matter expertise.** These aren't moonlighters building side projects outside of work, these are people building software for themselves and those around them to help them do their job.

## Why not Vibe Coder, Citizen Developer, or Casual Developer?

**Why AI App Creator, or just App Creator?** - I like the word Creator rather than Developer if we're talking about a job role these non-developer staff are taking on. Using AI rather than Agentic is deliberate to avoid too much technical jargon. They create apps with AI. **Keeping developer/coder out of the name ensures these app creators aren't confused with someone who can speak developer terminology or do traditional developer things.** It's also short, because casual conversation in an org tends to shorten formal roles to 1-2 words or acronyms. "I got approved to be an App Creator today" sounds like something good and maybe even fun to do. **It's a creative act, and they are making apps, and it's not overloading an existing job role or career title. It's unique and self-describing in its purpose, and doesn't sound like an IT job.** They're like "Content Creators", only their content is code.

Other names I've heard for this new job role that I disagree with:

**Corporate Vibe Coder** - Sadly, vibe coder has too much negative sentiment around it, and qualifying it with something like "Corporate or Org" Vibe Coder will likely just get shortened back down to Vibe Coder around the office. In addition, this role doesn't fit the original definition of vibe coder: developers generating code they *could* read but choose not to. This archetype is for non-developers who rely on AI agents and IT governance to build solutions for their business needs, largely through automation provided by development staff.

**Citizen Developer** - Too confusing with existing volunteer programs like Code for America or U.S. Digital Response (USDR) volunteers that focus on local/state tech-worker volunteers. The word citizen contradicts this role's goals of solving business problems through prompting. They aren't developers, and they may not even be citizens of their host country. There is no second definition of citizen, so best to not overload it.

**Casual Developer** - This is what AWS uses internally, but the role doesn't quite fit that name. There's nothing casual about their intent to use this role to benefit their work, their team, and the org. Labeling them a developer is a slippery slope, as it suggests they are adjacent to "real" developers, yet they are nothing of the sort. This role doesn't expect them to know developer terminology, have any developer training beyond how to use their agent, or follow an established process for getting their ideas into software.

Ultimately, you can call this role what you want. I support your decision 😉. Because devs and IT will work with them regularly, I recommend including IT and potential App Creator staff in the naming process. Naming things is hard, so you might be surprised by the feedback.

# Business Requirements

Before taking on the ACF for implementation, some requirements should be met. Since the market around this solution is changing rapidly, and many tools are in their infancy, this isn't for everyone.

- **Focused on a single vertical agent stack.** Since this solution is currently dependent on multiple product integrations, strong tooling guardrails, and centralized agent skills and context, not every set of AI and code products will fit the ACF model. Claude + GitHub or GitHub Copilot are the currently focused AI tech stacks for implementation guidance.
- **Existing SDLC maturity.** An organization with an existing development group will need to have already heavily adopted patterns such as 12 Factor and distributed computing design (aka cloud native). SDLC automation is a heavy part of the ACF, and an organization that hasn't yet adopted modern patterns for accelerating their SDLC will lag far behind their ability to deploy the ACF vs. an org that already uses tech such as containers, Kubernetes, GitOps, fully automated testing, ephemeral preview environments, remote developer environments. AI-native development is built on those previous patterns and practices, and skipping them before deploying ACF will require many of them be implemented before ACF benefits can be realized. For example, A team doesn't have a process to provide db schema mgmt, automated db seeding for CI runs, automated e2e testing, or container-based deployment will need many of those just to get the first user to build and deploy apps in the ACF.
- **Generally, App Creator output should not be used by others outside the creators domain expertise.** Once an app becomes popular enough that it's used by X people weekly (X is up to you, start small, control growth somehow), or if the users of the app grow horizontally to other departments or up/down the org chart, be careful. App Creators can not create the same software as enterprise software teams that have access to PMs, full-time devs, DevOps, SRE's, user testing, managed feedback loops, etc. **Enterprise apps typically need a team or more of people to keep it stable, fast, and secure. The ACF platform (mostly guided by Agent Skills + automation) is not a complete substitute for the traditional SDLC.** The ACF is designed to produce a narrow subset of the SDLC through golden paths for the App Creator to produce "personal software" for themselves and the people around them. Once an app gets to a level of popularity or criticality for the business, there will need to eventually be a graduation process where the project moves to a formal IT project and the original app creator becomes one of many stakeholders. Their baby has grown up.

## Decision Points

- Deciding your minimum IT touch-points.
- **Is the vibe coded app just a prototype to be rebuilt by the dev-team?** This is a per-org decision, but possibly a flexible per-project decision. Based on the maturity of the ACF process, agent automation, and skill enforcement, the MVP could have enough guidance (agent and human guidance) to ensure the MVP can mature without a rewrite.
  - **Yes:** The prototype can be reverse engineering by dev's agent to create customer requirements, then eventually a spec to be reimplemented by IT. The vibe coding wasn't a wasted effort, it's just a more interactive way for the customer to describe their business requirements to IT. When agents write the code, it's cheaper to reproduce from spec's then it is to continually iterate on a bad first draft. As agents get better, this rewrite could simply be a single skill run to re-code a 10k MVP into something shippable.
  - **No:** This will assume that ACF (or something similar) has been implemented so that the App Creator had minimum training and used the agent skills and guidance to produce something that IT can start from.

# Research

## Unsolved problems of this framework

- **App Creators gaining access to business data for their various app features will likely be one of the most time-consuming ongoing parts of implementing this framework.** An org with a strong internal data/api portal design, where App Creators can "shop" for the relevant data they need in a unified and consistent way, will greatly reduce the amount of ongoing IT involvement in app creation and deployment. This will require strong data controls, API-first design as a existing dev culture, and established processes around dataset access requests and mock data access that many orgs haven't universally implemented across line-of-business data stores. With a complete data portal implementation, it's feasible for an agent to use a "Data Portal Skill" to search for relevant datasets, plan for the API access and data schema, and request access on behalf of the App Creator; All without IT's involvement. Without that unified data infrastructure, most App Creator projects will stall quickly and require multiple formal IT requests for data access and project assistance to help the agent implement features to use that data.
- **No local dev tooling. No local code.** One expectation of this framework is that App Creators never need local dev tooling or code checkouts. They only need AI chat. That agent needs access to ephemeral developer environments, but the staff member driving chat shouldn't need to understand how that works. Claude Code has cloud environments just for this purpose, which works from web, mobile, and Claude Desktop. Claude Cowork is not an option. GitHub Copilot can use its built-in cloud environments when invoked from [github.com/copilot/agents](http://github.com/copilot/agents) but it is far more technical since it lives in the GitHub UI.

## Articles on defining structured vibe coding in an org

[Vibe Coding: Karpathy's Term, Its Evolution, and What It Means in 2026](https://aiskill.market/blog/karpathy-vibe-coding-evolution-2026)

# Technical Implementations

## With Claude

- Claude Teams account for each App Creator.
- Claude Code via web or Claude Desktop (Not Claude Code TUI). [https://claude.ai/code](https://claude.ai/code)
- Claude cloud environments [Configure cloud environments - Claude Code Docs](https://code.claude.com/docs/en/cloud-environments)
- App Creators need to be contributors to the GitHub repos housing their projects.
  - Agents will do all GitHub interaction on their behalf, co-authoring commits.
- Claude GitHub App - install to App Creator users and Org/repos they will work in. [https://github.com/apps/claude](https://github.com/apps/claude)
  - This links Claude agents in chat to the org repos it can access in its cloud environments.
- Org managed plugin marketplace to deliver agent Skills and MCPs to App Creators Claude accounts.

## With Copilot

- GitHub Copilot account for each App Creator
- Copilot via web. No local non-dev Copilot tool exists [https://github.com/copilot](https://github.com/copilot)
  - Copilot web automatically uses cloud environments (not the same as codespaces, which are developer-specific). This may be different from the new preview of cloud sandboxes that's [a billable charge](https://docs.github.com/en/copilot/concepts/about-cloud-and-local-sandboxes) and may only be Copilot CLI/GUI for now.
- App Creators need to be contributors to the GitHub repos housing their projects.
  - Agents will do all GitHub interaction on their behalf, co-authoring commits.
- Skills need to be in-repo, as Copilot doesn't yet support centralized org skill markeplaces. Copilot *does* support centralized [custom-agent profiles](https://docs.github.com/en/copilot/how-tos/administer-copilot/manage-for-organization/prepare-for-custom-agents) that could fill part of that gap.

## With Notion (Using Claude or Cursor External Agents)

- Notion Business or Enterprise account for each App Creator.
- Notion AI is usable via web/mobile/desktop.
- App Creators need to be contributors to the GitHub repos housing their projects.
  - Agents will do all GitHub interaction on their behalf, co-authoring commits.
- In Notion, enable GitHub MCP for each App Creator, which requires a GitHub fine-grained PAT for the user to store in Notion.
- In Notion, Enable the Claude or Cursor [Custom Agent](https://www.notion.com/blog/introducing-custom-agents) for each App Creator. Connect it to the GitHub repos for their projects. Notion can have many Custom Agents, but the Claude/Cursor are special external Agents. The Claude ones uses [Claude Managed Agents](https://platform.claude.com/docs/en/managed-agents/overview) but is hosted by Notion and part of Notion AI credits ([more info](https://www.notion.com/help/guides/how-to-set-up-claude-agents-on-your-teams-notion-task-board#how-do-external-agents-work-in-notion)). The Cursor one is hosted by Cursor and requires a Cursor subscription. Both provide full development abilities via cloud sandboxes.
- Org managed Notion Skills and MCPs, enabled for App Creators Notion accounts.
