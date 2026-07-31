# Risks Scope

## Risks
- Without a native mobile app or offline logging in the MVP (both are LATER), field supervisors depend on stable connectivity on-site to record progress — an adoption risk if signal is intermittent.
- Without automatic notifications for overdue or upcoming milestones (LATER), supervisors must manually check statuses, which can delay detection of blockers.
- The "at-risk" criterion is not defined (UNKNOWN) — if each supervisor interprets it differently, the dashboard loses consistency across projects.

## Assumptions
- We assume "web application compatible with computers, tablets, and cell phones" is solved with responsive design, not native apps.
- We assume the Friday weekly summary is the only formal channel to the client in the MVP, since the client portal is LATER.
- We assume that, with no integrations (spreadsheets, email, cloud storage) in the MVP, all data entry happens directly in BuildTrack with no import/export.
- We assume "clients without editing permissions" implies they will have some form of read-only access, though the exact mode (login vs. receiving the summary) is still unconfirmed.

## Dependencies / Pending Decisions
- Define which specific role is authorized to modify a milestone's target date.
- Define the objective criterion for marking a milestone as "at risk" (e.g., days remaining vs. days elapsed).
- Define the delivery format of the weekly summary (on-screen, downloadable PDF, or email) and whether clients will have login access or only receive the summary.
