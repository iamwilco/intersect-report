# Agent Documentation Index

> **For AI Agents:** Read this file first to understand the project and available documentation.

## Quick Navigation

| Folder | Purpose | When to Read |
|--------|---------|--------------|
| [`/system`](./system/) | Architecture, schemas, API endpoints | **First**, for any architectural decisions |
| [`/plans`](./plans/) | PRDs and implementation history | When implementing new features |
| [`/SOPs`](./SOPs/) | Standard Operating Procedures | When encountering known issues |
| [`/skills`](./skills/) | Reusable agent playbooks | When a task matches a skill |
| [`/workflows`](./workflows/) | Step-by-step dev workflows | When executing specific dev tasks |
| [`/learning`](./learning/) | Lessons learned, patterns | Before starting work (avoid past mistakes) |

---

## Project Overview

**Name:** Intersect Reports
**Description:** PROJECT_DESCRIPTION

### Technology Stack

| Layer | Technology |
|-------|-----------|
| **Frontend** | |
| **Backend** | |
| **Database** | |
| **Auth** | |
| **Deploy** | |

### Module Structure

```
project-root/
├── src/
└── ...
```

---

## System Documentation

- [Architecture](system/architecture.md) — System overview, modules, data flow
- [Database Schema](system/database-schema.md) — Entities, relationships, migrations
- [API Endpoints](system/api-endpoints.md) — REST/GraphQL contracts

## Workflows

| Workflow | Trigger | Description |
|----------|---------|-------------|
| [Build](workflows/build.md) | `/build` | Build the project |
| [Test](workflows/test.md) | `/test` | Run test suites |
| [Deploy](workflows/deploy.md) | `/deploy` | Deploy to staging/production |
| [Update docs](workflows/update-doc.md) | `/update-doc` | Sync documentation with code |

## Learning

- [Lessons](learning/lessons.md) — Rules from past mistakes
- [Plans history](plans/) — Past PRDs and implementations

## Quick Commands

```bash
# Fill in your project's common commands
npm install        # Install dependencies
npm run dev        # Development server
npm run build      # Production build
npm test           # Run tests
```
