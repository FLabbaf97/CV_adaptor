# cv-adapter

Agentic workflow to pull saved job listings from Notion, scaffold per-job application folders, and tailor CVs to each role without inventing credentials.

## Purpose

Keep a clean pipeline from job capture to application readiness:

- Export saved roles from Notion into `applications/` folders.
- Store each job description alongside a per-job copy of the CV.
- Tailor the CV and (optionally) generate a motivation letter with strict truthfulness guardrails.

## Skills

Workflow skills live under `.cursor/skills/` (Cursor) and `.claude/skills/` (Claude Code):

- `cv-tailor`: extract requirements into `insights.json` and adapt `CV_farzaneh_labbaf.tex` for a saved job folder.
- `motivation-letter`: generate a concise, role-aligned `motivation.tex` after CV tailoring.
- `job-ranking`: score and prioritize saved applications by fit.
- `interview-prep` / `interview-feedback`: prepare for interviews and review practice answers.

## Setup

1. Create a Notion database named "Job Applications".
2. Create a Notion integration and share the database with it.
3. Set required environment variables (see `.env.example`):
   - `NOTION_DATABASE_ID`
   - `NOTION_TOKEN`
4. Use the "Export to Notion" Chrome extension to create a template for consistent job entries.

## Usage

Run this periodically to pull saved roles and write them into `applications/`:

```bash
uv run python scripts/export_saved_jobs.py
```
