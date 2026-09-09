# Golden Paths

<!--
  IT / PLATFORM TEAM: a golden path is a pre-approved, pre-built way to create an app in your org.
  It bundles a tech stack, hosting, data storage, and integration rules into one shape that your
  platform can build, test, deploy, and secure with little human involvement. An App Creator whose
  idea fits a golden path gets a faster, smoother, more likely approved project.

  Describe each path twice: once technically (for Part 2 of the brief) and once as plain-language
  signals the agent can match against what the App Creator says. Edit, add, or remove paths to
  match what your platform actually supports. Use the `customize` skill in skills/platform/ for a
  guided version of this.

  The example below is a starting point, not a recommendation for your org.
-->

## How the app-idea skill uses this file

During discovery, compare what the App Creator describes against the **signals** of each path. When a path matches, record it in Part 2 under "Golden path match" with the reasons, and tell the App Creator in plain language that their idea fits the standard way apps get built here, which means fewer approvals and a faster start. When nothing matches, record why in Part 2 so IT can decide whether to extend a path or route the project differently. Never mention the technical stack to the App Creator.

---

## Path: Internal Web App

**Status:** {{Approved / Pilot / Deprecated}}
**Owner:** {{platform team}}

### Technical shape (for Part 2)

| Layer | Choice |
|---|---|
| App type | Browser-based web application, responsive for desktop and mobile |
| Runtime | Node.js |
| Packaging | Container image built from the org base image |
| Hosting | Kubernetes, org shared cluster, one namespace per app |
| Owned data | PostgreSQL, one database per app, managed by the platform |
| External data | Read via approved internal APIs only; no direct database connections to other systems |
| Login | Org SSO |
| Notifications | Email via the org relay; no SMS |
| Files | Object storage bucket per app, if needed |
| Background jobs | Scheduled jobs inside the cluster; no long-running external workers |

### Plain-language signals that an idea fits (for matching during discovery)

Fits when the App Creator describes something that:

- People use from a browser, at a desk or on a phone
- Keeps track of its own records (requests, lists, statuses, notes, schedules)
- Looks up information from other systems but doesn't need to change those systems
- Works with the normal work login
- Sends the occasional email but doesn't need texts or instant alerts
- Has fewer than {{max_users}} users in one team or department

### Signals that an idea does NOT fit this path

- Needs to write data back into another system of record
- Needs a native mobile app, offline use, or hardware (scanners, badges, sensors)
- Needs real-time features (live chat, live dashboards updating every second)
- Handles regulated data as its core purpose
- Needs to be reached by people outside the org

---

## Path: {{Add another path}}

**Status:**
**Owner:**

### Technical shape (for Part 2)

### Plain-language signals that an idea fits

### Signals that an idea does NOT fit this path
