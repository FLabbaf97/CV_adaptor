# Using Cursor AI for Job Applications

This guide explains how to use Cursor's AI agent to tailor your CV, write motivation letters, and manage your job applications — all within this workspace.

---

## How it works

Cursor reads a set of **rules** from `.cursor/rules/` every time you chat with it. These rules give the AI detailed, step-by-step instructions for each workflow. You don't need to paste instructions or explain the project — it already knows the file structure, conventions, and guardrails.

There are four rules:

| Rule file | Always on? | Triggers |
|---|---|---|
| `00-project.mdc` | Yes — loaded every chat | Project context, conventions |
| `cv-tailor.mdc` | Auto when application files are open | "tailor CV", "adapt resume" |
| `motivation-letter.mdc` | Auto when application files are open | "write motivation letter", "cover letter" |
| `career-ops.mdc` | Agent-requested or manual | "report", "tracker", "evaluate job", "export" |

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

### See all application statuses
> "Show me an overview of all my applications"

Cursor will list every folder under `applications/` and show which files are present (tailored CV, letter, report).

### Evaluate a new job (without saving it yet)
Paste a job description directly and say:
> "Evaluate this job against my CV"

Cursor will give you a quick A–F grade and role fit score.

### Compare two jobs
> "Compare the GSK and EthonAI applications — which is the better fit?"

### Update the motivation letter
> "Update the motivation letter for GSK to add more emphasis on MLOps"

---

## Pro tips

- **Reference the folder directly** in your message — e.g. `applications/GSK_...` — to help Cursor identify the right context without ambiguity.
- **Open the application files** in the editor before chatting; Cursor auto-attaches the cv-tailor and motivation-letter rules when those files are visible.
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
