# Statement Of Work

A Statement of Work (SOW) is a narrative description of the required work. It
stipulates the deliverables or services required to fulfill the contract, and it
defines the task to be accomplished or services to be delivered in clear,
concise and meaningful terms. Examples are by ChatGPT.

Contents:

- [Introduction](#introduction)
- [Statement of work template](#statement-of-work-template)
  - [Title](#title)
  - [Abstract](#abstract)
  - [Value](#value)
  - [Scope](#scope)
  - [Payment](#payment)
- [Purpose](#purpose)
  - [Objectives](#objectives)
  - [Performance](#performance)
- [Who does what](#who-does-what)
  - [People](#people)
  - [Roles](#roles)
  - [Responsibilities](#responsibilities)
- [Context](#context)
  - [Present](#present)
  - [Future](#future)
- [Planning](#planning)
  - [Requirements](#requirements)
- [Other terms and conditions](#other-terms-and-conditions)
  - [Client's obligations](#clients-obligations)
- [Schedule](#schedule)
  - [Expected start date and completion date](#expected-start-date-and-completion-date)
  - [Sign-off](#sign-off)


## Statement of work template


### Title

BuildTrack

### Abstract

This Statement of Work (SOW) outlines the objectives, scope, deliverables, roles, and timeline for the development and implementation of a web-based Construction Project Progress Tracker for BuildRight Contractors. The project aims to centralize project updates, milestone tracking, task progress, issue reporting, and weekly summaries for commercial renovation projects. BuildRight Contractors currently faces difficulties because project information is spread across messages, spreadsheets, and photo folders, making it hard for managers to understand the real status of each project and prepare client reports efficiently. The proposed solution will provide a dashboard where supervisors can update progress, operations managers can monitor project status, and client report preparers can generate weekly summaries. 

### Value

The main value of this project lies in improving the management and oversight of construction projects by centralizing information on a single platform. The application will reduce the time spent preparing weekly reports, make it easier to track milestones and tasks, and improve the ability to respond to potential delays. The cost should include software development services, user interface design, database setup, dashboard development, testing, documentation, and initial support after deployment.


### Scope

The project involves the development of a web application that allows users to create projects, define milestones, update the status of tasks or activities, log incidents, and view a weekly summary via a dashboard. The system will be intended for project supervisors, operations managers, and those responsible for preparing reports for clients. It will not include features for budget control, procurement management, BIM, advanced geolocation, or native mobile development.

**Scope of Work:**
- Creating and configuring projects.
- Setting up and tracking milestones.
- Updating the status of tasks or activities.
- Logging and tracking issues.
- Weekly progress summary view.
- Dashboard to view project status.
- Access for the different user roles defined in the project.

**Out of Scope:**
- Budget control.
- Purchasing or procurement management.
- BIM (Building Information Modeling) features.
- Advanced geolocation.
- Native mobile app.
- Offline data entry, as this is considered a future enhancement.


### Payment

Payments may be divided according to project milestones to ensure alignment between progress and compensation. A suggested payment schedule is 20% upon contract signing, 25% after requirements analysis and system design approval, 25% after completion of the main project tracking modules, 20% after dashboard, weekly summary, and issue tracking functionality are completed, and 10% after final testing, deployment, and client acceptance.


## Purpose


### Objectives

The main objectives of the project are:

- To centralize the monitoring of multiple construction projects.
- To facilitate the management of milestones and tasks.
- To enable the recording and tracking of incidents.
- To improve visibility into project status.
- To support the generation of weekly reports for clients via a dashboard.
- To detect delays in project execution in a timely manner.

### Performance

The success of the project will be evaluated using both **business** and **technical** performance indicators. These metrics will help determine whether the system achieves its operational objectives while meeting the expected technical quality standards.

Performance will be assessed through:

- Functional and integration testing
- User feedback sessions
- Project status meetings
- Acceptance of each project deliverable


### Business Performance Metrics

These metrics evaluate the impact of the system on the organization's project management processes.

| Metric | Description | Expected Outcome |
|---------|-------------|------------------|
| **Project Visibility** | Operations managers can monitor the status of all active projects from a centralized dashboard. | Improved visibility and decision-making across projects. |
| **Reporting Efficiency** | Weekly project summaries reduce the manual effort required to prepare client reports. | Faster report generation with less administrative work. |
| **Issue Tracking** | Project supervisors can record, update, and monitor project issues. | Managers can identify schedule risks and resolve problems earlier. |
| **User Satisfaction** | Key users evaluate the system compared to the current process of using messages, spreadsheets, and photo folders. | Users consider the new system easier, more organized, and more efficient. |


### Technical Performance Metrics

These metrics evaluate the quality, reliability, and usability of the application.

| Metric | Description | Target |
|---------|-------------|--------|
| **System Availability** | The web application is accessible during agreed business hours, excluding scheduled maintenance. | High availability during operating hours. |
| **Response Time** | Common actions (opening projects, updating tasks, viewing dashboards) execute within an acceptable time. | Ideally under **3 seconds** under normal usage. |
| **Data Accuracy** | Information related to projects, milestones, tasks, and issues is stored and displayed correctly. | Accurate and consistent data across the system. |
| **Role-Based Access** | Each user role only has access to the features required for its responsibilities. | Secure and appropriate access control. |
| **User Adoption** | Operations managers, project supervisors, and report preparers can effectively use the system after basic onboarding. | Successful adoption with minimal training. |


### Success Criteria

The project will be considered successful if it:

- Improves project visibility through a centralized dashboard.
- Reduces the time required to prepare weekly client reports.
- Enables effective tracking of project issues and schedule risks.
- Receives positive feedback from key users.
- Meets the defined availability and performance expectations.
- Maintains accurate and consistent project information.
- Enforces secure role-based access.
- Is successfully adopted by the intended users after basic training.

## Who does what


### People

The identified participants are:

- BuildRight Contractors (client).
- Project supervisor.
- Operations manager.
- Person responsible for preparing reports for clients.
- System development team (BuildTrack).

### Roles

**Project Supervisor**
- Updates the progress of tasks and activities.
- Logs incidents.
- Manages project milestones.

**Operations Manager**
- Oversees all projects.
- Checks the dashboard.
- Monitors adherence to the schedule.

**Reporting Manager**
- Uses information from the system to prepare reports for clients.

### Responsibilities

| Activity | Supervisor | Manager | Reporting Lead |
|---|---|---|---|
| Create projects | R | A | I |
| Update tasks | R | C | I |
| Log incidents | R | C | I |
| Review the dashboard | C | R | C |
| Prepare weekly reports | I | C | R |

R: Responsible · A: Approves / Final approver · C: Consulted · I: Informed

## Context


### Present

**Identified Obstacles:**
- Project information is currently scattered across messages, spreadsheets, and folders containing photos.
- There is no clear overview of the status of tasks or milestones.
- Reports for clients are prepared manually each week.
- The lack of visibility makes it difficult to detect project delays in a timely manner.

Currently, project information is scattered across messages, spreadsheets, and separate folders of photos. Managers must manually compile the information at the end of each week to prepare reports for clients, which makes it difficult to determine the actual status of projects and respond quickly to potential delays.


### Future

With the implementation of the system, BuildRight Contractors will have a centralized platform to manage the progress of its projects. Managers will be able to view the status of tasks, milestones, and issues in real time, as well as generate weekly summaries more efficiently. As a potential future improvement, the RFP includes the ability to capture information from mobile devices without an internet connection.



## Planning


### Requirements

The system shall provide the following functional capabilities as part of the Minimum Viable Product (MVP):

### FR-01: Project Management
The system shall allow authorized users to create, configure, edit, and manage projects.

### FR-02: Milestone Management
The system shall allow users to create, update, and monitor project milestones.

### FR-03: Task Status Management
The system shall allow users to update the status and progress of project tasks.

### FR-04: Issue Management
The system shall allow project supervisors to register, update, and track issues that may affect project schedules or deliverables.

### FR-05: Weekly Summary View
The system shall provide a weekly project summary that consolidates project progress and supports client reporting.

### FR-06: Project Dashboard
The system shall provide a centralized dashboard where operations managers can monitor the status and progress of all active projects.

### FR-07: User and Role Management
The system shall manage users and enforce role-based permissions, ensuring each user can only access the features corresponding to their responsibilities.

### FR-08: Web-Based Access
The system shall be deployed as a web application, allowing authorized users to access it through a standard web browser.

### FR-09: Project Progress Tracking
The system shall allow authorized users to record project progress and consult the current status of projects in real time.

### FR-10: Report Generation
The system shall allow users to generate project reports according to their assigned role and permissions.


The project deliverables include:

- Web application for project tracking.
- Project configuration and management module.
- Milestone management module.
- Task status update functionality.
- Issue registration and tracking module.
- Weekly project summary view.
- Project monitoring dashboard.
- User and role management module.

### Acceptance Criteria

The project will be accepted when:

- All functional requirements are fully implemented.
- Each module operates correctly within the defined MVP scope.
- Role-based access control functions as specified.
- Authorized users can successfully manage projects, milestones, tasks, issues, dashboards, and reports through the web application.
- The system is accessible through a web browser and performs according to the defined acceptance criteria.


## Other terms and conditions


### Client's obligations

BuildRight Contractors must:

- Provide the necessary information about current projects.
- Facilitate the validation of system requirements.
- Designate the users who will participate in testing.
- Review and approve the deliverables developed.
- Provide feedback during the course of the project.


## Schedule


### Expected start date and completion date

The proposed duration is approximately 16 weeks, organized into phases of analysis, design, development, testing, and implementation.

- **Estimated start date:** July 23, 2026
- **Estimated completion:** November 20, 2025
**Timeline / Milestones:**

| Milestone | Report | Deadline |
|---|---|---|
| Requirements gathering | Requirements document | Week 1 |
| System design | Interface and database design | Week 2 |
| Development of the projects and milestones module | Development progress report | Week 6 |
| Development of the Tasks and Issues Module | Development Progress Report | Week 10 |
| Development of the Dashboard and Weekly Summary | Development Progress Report | Week 14 |
| Testing and Debugging | Test Report | Week 15 |
| Final System Delivery | Implementation and Presentation | Week 16 |


### Sign-off

The following phrase will appear at the end of each Statement of Work:

NOTE: Before signing the Statement of Work, if you have any questions or
concerns, please call the Work Authority indicated above to negotiate any
issues.

If you agree to the requirements of this Statement of Work, please sign and date
the document which will be accepted as your proposal by Client, and return to my
attention.

Please return an original signature copy by mail.


Printed Name:

__________________________________________


Signature:

__________________________________________


Date:

__________________________________________
