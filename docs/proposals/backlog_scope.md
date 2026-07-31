# Backlog Scope

Refined backlog based on the GitHub issues already open in the repository. Technical/infrastructure issues (#1, #2, #10) are kept as technical tasks rather than user stories, since they don't map to a specific user-facing goal. Issues #3–#9 are expressed as user stories derived from their existing description and acceptance criteria.

## #1 — Configure project repository and development environment
**Type:** Technical task (infrastructure)
**Acceptance criteria:**
- Repository structure is available (frontend and backend folders, .gitignore, environment template).
- README explains how to run the project.
- Team members can clone and start the project.

## #2 — Design database schema for projects, milestones, tasks, and issues
**Type:** Technical task (infrastructure)
**Acceptance criteria:**
- ER diagram is completed.
- Schema supports all MVP functional requirements (projects, milestones, tasks, issues, users, roles).
- Migrations run successfully.

## #3 — User story: Secure login and role-based access
**As a** user of any role (Project Supervisor, Operations Manager, Reporting Manager), **I want** to log in securely and only see what my role allows, **so that** unauthorized access to other roles' functionality is blocked.
**Acceptance criteria:**
- Users can log in securely.
- Permissions are enforced by role.
- Unauthorized access is blocked.

## #4 — User story: Manage projects
**As an** Operations Manager, **I want** to create, edit, view, and manage projects, **so that** I can keep an accurate record of all active projects.
**Acceptance criteria:**
- Projects can be created, edited, listed, and deleted.
- Validation messages are returned when needed.
- Only authorized users can manage projects.

## #5 — User story: Manage milestones
**As a** Project Supervisor, **I want** to create, update, and monitor milestones linked to a project, **so that** progress toward key dates is tracked accurately.
**Acceptance criteria:**
- Milestones are linked to projects.
- Status updates are saved correctly.
- Milestones can be viewed by authorized users.

## #6 — User story: Update task status
**As a** Project Supervisor, **I want** to create tasks and update their progress and status, **so that** day-to-day work is reflected in the system.
**Acceptance criteria:**
- Tasks can be created and updated.
- Progress is stored correctly.
- Assigned users are displayed.

## #7 — User story: Log and track issues
**As a** Project Supervisor, **I want** to report and update issues with a severity level linked to a project, **so that** risks to the schedule are visible early.
**Acceptance criteria:**
- Issues can be registered and updated.
- Severity is visible.
- Issue history is stored.

## #8 — User story: Dashboard and weekly summary
**As an** Operations Manager, **I want** a dashboard showing project status, milestone progress, and open issues, **so that** I can monitor all active projects from one place.
**As a** Reporting Manager, **I want** to view and export a weekly summary, **so that** I can send it to the client on time.
**Acceptance criteria:**
- Dashboard loads active projects.
- Progress indicators are visible.
- Weekly summary can be viewed and exported.

## #9 — User story: Responsive interface across MVP modules
**As any** authorized user, **I want** a responsive interface for projects, milestones, tasks, issues, and reports, **so that** I can use the system consistently on desktop and tablet.
**Acceptance criteria:**
- Interface is responsive.
- Forms are usable.
- Navigation is consistent across modules.

## #10 — Perform system testing and prepare final deployment
**Type:** Technical task (QA/release)
**Acceptance criteria:**
- All critical tests pass.
- Major defects are resolved.
- Deployment guide is available.
- System is ready for final presentation.
