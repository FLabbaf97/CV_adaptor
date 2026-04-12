# cv_adapter — Project Guidelines

## Purpose

Fetches job listings tagged "Saved" from a Notion database, scaffolds per-job application folders with a copied LaTeX CV, and provides a skill to tailor that CV for the role—without inventing any credentials.

## Architecture

```
base_cv/cv_1225_KARAMI.tex          ← master ATS-compatible LaTeX CV (never edit directly for a job)
scripts/export_saved_jobs.py        ← Notion → applications/ scaffolding script
applications/{slug}_{YYYY-MM-DD}/  ← one folder per job application
    descriptions.md                 ← raw job description (from Notion)
    cv_KARAMI.tex                   ← per-job copy to tailor
    insights.json                   ← extracted requirements (created by cv-tailor skill)
    build/                          ← latexmk compilation artefacts
.github/skills/cv-tailor/SKILL.md  ← skill for CV tailoring workflow
```

## Conventions

- **Application folder naming**: `{Job_Title_Company_Source_YYYY-MM-DD}` — created automatically by `export_saved_jobs.py`.
- **Never edit `base_cv/cv_1225_KARAMI.tex` for a specific job.** Always tailor the per-job copy at `applications/.../cv_KARAMI.tex`.
- **insights.json lifecycle**: created once by the cv-tailor skill; if it already exists, the skill uses it directly — don't delete it unless re-analysis is intended.

## cv-tailor Skill

Use the `cv-tailor` skill (trigger: "tailor CV", "adapt resume", "job-specific CV") to extract role requirements into `insights.json` and update `cv_KARAMI.tex`. The skill enforces strict guardrails: never invent employers, titles, dates, achievements, tools, or skills not already in the CV.

## Known Pitfalls

- The `\graphicspath` in the base CV is hardcoded to `C://DATA//Tasks//cv_adapter//photo/`. Renaming or moving the workspace breaks LaTeX compilation — update the path in the `.tex` file if needed.
- There is no installed CLI entry point; run scripts directly with `python scripts/...`.
- Notion credentials (`NOTION_TOKEN`, `NOTION_DATABASE_ID`) must be set in `.env` before running the export script.
