# Using Cursor AI for Job Applications

This guide explains how to use Cursor's AI agent to tailor your CV, write motivation letters, and manage your job applications — all within this workspace.

---

## How it works

Cursor loads **project context** from `.cursor/rules/` and **workflow skills** from `.cursor/skills/` when you ask for a task. You don't need to paste instructions or explain the project — it already knows the file structure, conventions, and guardrails.

| File | Type | When loaded | Triggers |
|---|---|---|---|
| `00-project.mdc` | Rule — always on | Every chat | Project context, conventions |
| `cv-tailor/SKILL.md` | Skill | When tailoring a CV | "tailor CV", "adapt resume" |
| `motivation-letter/SKILL.md` | Skill | When writing a cover letter | "write motivation letter", "cover letter" |
| `job-ranking/SKILL.md` | Skill | When ranking applications | "rank jobs", "sort by fit" |
| `interview-prep/SKILL.md` | Skill | When preparing for interviews | "prepare for interview" |
| `interview-feedback/SKILL.md` | Skill | When reviewing answers | "feedback on my interview answers" |

---

## Step 0 — Export saved jobs from Notion

Before doing anything, make sure your application folders exist.

**Say to Cursor:**
> "Export my saved jobs from Notion"

Or run it yourself:
```bash
python scripts/export_saved_jobs.py
```

This creates folders like:
```
applications/
  GSK_2026-05-15_AIML_Engineer_AI_for_Science/
    descriptions.md
    CV_farzaneh_labbaf.tex
  EthonAI_2026-05-15_Applied_Research_Scientist_Causal_AI/
    descriptions.md
    CV_farzaneh_labbaf.tex
```

---

## Step 1 — Tailor the CV

**Open** the application folder you want to work on (click into it in the file explorer so Cursor picks it up as context), then say:

> "Tailor my CV for the GSK application"

or

> "Adapt my CV for `applications/GSK_2026-05-15_AIML_Engineer_AI_for_Science`"

**What Cursor will do:**
1. Read `descriptions.md` to understand the role
2. Read `CV_farzaneh_labbaf.tex` (the per-job copy)
3. Create `insights.json` with must-have requirements and a match score (0–100)
4. If match score ≥ 60%: rewrite and reorder bullets in the CV to emphasise relevant experience — without inventing anything
5. Create `changes.json` summarising every edit made

**You will see:**
- The match score and a verdict
- Top 3 changes made
- Any requirements that couldn't be addressed

**Tip:** If you want Cursor to re-analyse from scratch, delete `insights.json` first and ask again.

---

## Step 2 — Write the motivation letter

After CV tailoring is done, say:

> "Write a motivation letter for the GSK application"

or

> "Create motivation.tex for `applications/GSK_2026-05-15_AIML_Engineer_AI_for_Science`"

**What Cursor will do:**
1. Read the tailored `CV_farzaneh_labbaf.tex`
2. Read `descriptions.md` and `insights.json`
3. Read `base_cv/context_for_cover_letter.md` for your personal narrative and project context
4. Draft a one-page LaTeX cover letter in 4–5 paragraphs
5. Save it as `motivation.tex` in the application folder

**You will see:**
- Word count and paragraph summary
- Which CV evidence was used for each job requirement
- Confirmation of the file written

---

## Step 3 — Get a match report

To get a detailed breakdown of how your CV matches a role before tailoring:

> "Give me a report on the EthonAI application"

or

> "How well does my CV match `applications/EthonAI_2026-05-15_Applied_Research_Scientist_Causal_AI`?"

Cursor will create `report.md` in that folder with:
- A scored table of must-have requirements (Met / Partial / Missing)
- Missing keywords to add
- CV content to de-emphasise
- Prioritised action list

---

## Additional commands

### Rank applications by fit
> "Rank my jobs" / "Sort applications by fit"

### See all application statuses
> "Show me an overview of all my applications"

Cursor will list every folder under `applications/` and show which files are present (tailored CV, letter, report).

### Update the motivation letter
> "Update the motivation letter for GSK to add more emphasis on MLOps"

### Interview prep
> "Prepare me for interview with the GSK application"

---

## Pro tips

- **Reference the folder directly** in your message — e.g. `applications/GSK_...` — to help Cursor identify the right context without ambiguity.
- **Name the workflow** in your message (e.g. "tailor CV for …") so Cursor loads the right skill.
- **Use `@` to include files** if needed: type `@applications/GSK_.../descriptions.md` in your message to pin it to context.
- The base CV at `base_cv/CV_farzaneh_labbaf.tex` is **never modified** by any workflow. Per-job copies live in each application folder.
- `insights.json` is only created once per folder. To re-analyse the role (e.g. the JD was updated), delete the file and tailor again.

---

## File outputs per workflow

| Workflow | Files created/modified |
|---|---|
| Export jobs | `applications/{folder}/descriptions.md`, `CV_farzaneh_labbaf.tex` |
| Tailor CV | `insights.json`, `CV_farzaneh_labbaf.tex` (edited), `changes.json` |
| Motivation letter | `motivation.tex` |
| Match report | `report.md` |
