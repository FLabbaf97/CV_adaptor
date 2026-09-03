---
name: job-ranking
description: "Rank and compare all saved job applications by CV fit, interest alignment, and experience level. Reads applications/*/descriptions.md plus base_cv/cv.md and context_for_cover_letter.md, scores each role 1–5, and outputs a sorted table with per-role reasoning. Trigger phrases: rank jobs, rank applications, sort jobs by fit, job priority, which jobs should I apply to, application ranking, compare all applications."
---

# Job Ranking Skill

## Purpose

Scan every active application folder, compare each role against the candidate's CV and stated interests, and produce a **ranked priority list** with numeric scores and reasoning.

## Scope

- **Include:** all folders directly under `applications/` except `0_Archived`
- **Optional filter:** if the user names specific folders or a subset (e.g. "only Zurich roles"), rank only those
- **Exclude:** `0_Archived` and any subfolders inside it unless the user explicitly asks

## Required inputs (read all before scoring)


| File | Purpose |
|------|---------|
| `base_cv/cv.md` | Plain-text CV — primary evidence for experience fit |
| `base_cv/context_for_cover_letter.md` | Motivation, transferable skills, ideal environment, domain interests |
| `applications/{folder}/descriptions.md` | Job description per role (fallback: `description.md`) |
| `applications/{folder}/CV_farzaneh_labbaf.tex` | Optional — use if tailored; otherwise rely on `base_cv/cv.md` |

## Workflow

### 1. Discover application folders

List `applications/`. Skip `0_Archived`. For each remaining folder, confirm `descriptions.md` (or `description.md`) exists; note missing JDs and exclude from ranking.

### 2. Build candidate profile summary

From `base_cv/cv.md` and `context_for_cover_letter.md`, extract:

- Core technical strengths (languages, ML/MLOps, domains)
- Years and depth of relevant experience
- Domain preferences (healthcare, med-tech, regulated AI, startups, R&D, etc.)
- Location / language constraints if stated in context files
- Known gaps relative to common JD themes (e.g. LLM research, mass spectrometry, Copilot Studio)

### 3. Analyse each job

For each folder, read the JD and extract:

- Company name, job title, location (or "Not specified")
- 3–5 **job keywords** (domain, stack, role type)
- 2–4 **company keywords** (sector, mission, org type)
- Seniority / years expected
- Must-have vs nice-to-have themes
- language requirements (if stated)

### 4. Score each role (1–5 integers only)

Use **whole numbers from 1 to 5**. Do not use stars, percentages, or letter grades in the summary table.

| Score | Fit (experience & skills) | Interest (motivation & alignment) |
|-------|---------------------------|-----------------------------------|
| **5** | Strong overlap; meets most must-haves with direct evidence | Strong match to stated mission, domain, and work style |
| **4** | Good overlap; minor gaps or one moderate stretch | Clearly aligned; one secondary mismatch (e.g. location) |
| **3** | Partial overlap; credible but several gaps | Mixed — some alignment, role or sector not ideal |
| **2** | Weak overlap; major skill or seniority mismatch | Low alignment with healthcare/R&D/mission preferences |
| **1** | Poor match; core requirements largely unmet | Misaligned sector, stack, or career direction |

**Fit** weights: technical skills, domain experience, seniority, production/research evidence in CV.

**Interest** weights: `context_for_cover_letter.md` preferences — healthcare/med-tech, regulated AI, startups, mission-driven work, scientific collaboration.

**Overall rank** = sort primarily by `(2*Fit + Interest)/3` descending; 

### 5. Output report

#### A. Summary table (required)

```markdown
| Rank | Company | Location | Job keywords | Company keywords | Fit (1–5) | Interest (1–5) | Combined |
|:---:|---|---|---|---|---:|---:|---:|
| 1 | ... | ... | ... | ... | 5 | 5 | 10 |
```

- **Job keywords:** 3–5 comma-separated terms (role domain, stack, focus)
- **Company keywords:** 2–4 comma-separated terms (sector, org type, mission)
- Sort rows by rank (1 = highest priority)

#### B. Scoring methodology (brief)

One short paragraph explaining the three factors: experience fit, interest alignment, seniority match.

#### C. Per-role reasoning (required)

For **every** ranked role, a subsection:

```markdown
### {Rank}. {Company} — {Job title}

**Fit: {n}/5 · Interest: {n}/5**

**Why high / medium / low:** 2–4 sentences citing specific CV evidence and JD requirements.

**Main strengths:** bullet list (max 3)

**Main gaps:** bullet list (max 3)
```

#### D. Practical takeaway (optional, 2–4 bullets)

- Top 3–4 to prioritize for tailoring / applying
- Roles to deprioritize unless pivoting
- Any location or language blockers

### 6. Optional file output

If the user asks to save the report, write:

`applications/job_ranking_{YYYY-MM-DD}.md`

Use the same structure as sections A–D. Do not overwrite prior ranking files unless the user asks.

## Guardrails

- Never invent CV experience to inflate scores.
- Scores must reflect **evidence in `cv.md` / context files**, not aspirational skills.
- If a JD is missing or empty, exclude that folder and list it under **Skipped folders**.
- Be explicit about stretch roles (e.g. "Research Scientist" vs applied ML engineer).
- Location "Not specified" is acceptable when the JD omits it.
- the final answer should be precise. 

## Trigger examples

- "Rank my jobs"
- "Sort applications by fit and interest"
- "Which saved jobs should I prioritize?"
- "Job ranking — use numbers 1 to 5"
