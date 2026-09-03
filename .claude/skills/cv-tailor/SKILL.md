---
name: cv-tailor
description: >-
  CV tailoring workflow. Use when the user asks to tailor, adapt, or customize a
  CV for a specific job application folder under applications/. Extracts role
  requirements into insights.json, scores CV–JD alignment, and edits
  CV_farzaneh_labbaf.tex for the target role. Use context_for_cover_letter.md
  to guide tailoring. Trigger phrases: tailor CV, adapt resume, job-specific CV,
  ATS alignment, tailor application CV, customize CV.
---

# CV Tailor Workflow

## Purpose

Run a repeatable, evidence-only tailoring workflow for a saved application folder:

1. Extract role requirements from `descriptions.md` → `insights.json`
2. Score the existing CV against those requirements
3. Edit `CV_farzaneh_labbaf.tex` to better match the role
4. Record all changes in `changes.json` for user review

## Step 0 — Resolve the target folder

- If the user specified a folder path or company name, locate the matching folder under `applications/`.
- If ambiguous, list the available folders and ask the user to confirm.
- Verify both `descriptions.md` and `CV_farzaneh_labbaf.tex` exist in that folder before proceeding.

## Step 1 — Create or load insights.json

**If `insights.json` already exists:** load it and skip to Step 2.

**If `insights.json` is missing:** read `descriptions.md` and create `applications/{folder}/insights.json` with exactly this structure:

```json
{
  "role": "<job title and company>",
  "important_to_have": [
    "<requirement 1 — most critical>",
    "<requirement 2>",
    "..."
  ],
  "nice_to_have": [
    "<nice-to-have skill or experience>",
    "..."
  ],
  "language_requirements": [
    "<language and level if stated, e.g. English C1>"
  ],
  "domain_focus": "<e.g. MLOps, NLP, clinical AI, etc.>",
  "seniority": "<e.g. mid-level, senior, PhD required>",
  "match_score": <integer 0–100>,
  "match_verdict": "<one sentence: is tailoring worthwhile?>"
}
```

### How to compute match_score

- For each `important_to_have` item, check whether `CV_farzaneh_labbaf.tex` contains clear supporting evidence.
  - Full match = 1.0
  - Partial / buried evidence = 0.5
  - Missing = 0.0
- `match_score = round(sum(weights) / len(important_to_have) * 100)`
- State the score and verdict clearly to the user.

## Step 2 — Decide whether to tailor

- If `match_score < 60`: inform the user, explain what is missing, and **stop**. Do not edit the CV.
- If `match_score >= 60`: proceed with Step 3.

## Step 3 — Tailor CV_farzaneh_labbaf.tex

Read **both** `descriptions.md` and `insights.json`. Edit `applications/{folder}/CV_farzaneh_labbaf.tex`:

### What to change

- **Reorder bullet points** within sections to surface the most relevant evidence first.
- **Rephrase bullets** to mirror the language and keywords in the job description (without fabricating new facts).
- **Emphasise** tools, frameworks, and domain concepts that appear prominently in the JD.
- **De-emphasise or remove** bullet points that are irrelevant or low-signal for this specific role.
- **Include `nice_to_have` items** only if they are already present and evidenced in the CV.
- **Reflect language requirements** only when truthful and relevant.

### What NOT to change

- Do not invent new employers, job titles, dates, projects, achievements, tools, metrics, or certifications.
- Do not add skills or keywords that are not backed by existing CV content.
- Do not alter measurable numbers (e.g. "86% accuracy", "50% reduction") unless the user explicitly provides corrections.
- Do not edit `base_cv/CV_farzaneh_labbaf.tex`.

## Step 4 — Write changes.json

Save `applications/{folder}/changes.json` with this structure:

```json
{
  "role": "<job title and company>",
  "date": "<today's date ISO 8601>",
  "added_emphasis": [
    {"item": "<bullet or skill>", "reason": "<why it was surfaced>"}
  ],
  "removed_or_deprioritised": [
    {"item": "<bullet or skill>", "reason": "<why it was removed or moved down>"}
  ],
  "rephrased": [
    {"original": "<original text>", "updated": "<new text>", "reason": "<why>"}
  ],
  "gaps_not_closable": [
    "<requirement that could not be addressed without fabrication>"
  ]
}
```

## Step 5 — Report to user

After completing all edits, respond with:

0. render the tex file to create a pdf. and check number of pages in cv_farzaneh_labbaf.pdf and report it. 
1. The final `match_score` and verdict.
2. A brief summary of the most impactful changes (top 3).
3. Any gaps that could not be closed.
4. Confirmation of all files written: `insights.json`, `CV_farzaneh_labbaf.tex`, `changes.json`.

## Guardrails (repeat for emphasis)

- NEVER invent employers, job titles, dates, achievements, responsibilities, tools, or certifications.
- NEVER add skills or keywords unless they are supported by the existing CV.
- Keep measurable claims unchanged unless the user provides corrected numbers.
- Optimise for relevance and clarity, not exaggeration.
