---
name: interview-prep
description: >-
  Interview preparation for a saved application folder. Researches the company
  or lab (not the parent university/corp alone), maps CV fit, and writes 10–20
  hard role-specific interview questions probing CV gaps and unclear experience.
  Use whenever the user asks to prepare for an interview, interview prep,
  practice questions for a position, research a role for interview, application
  fit for interview, or similar — even if they only name a folder under
  applications/. Trigger phrases: prepare me for interview, interview prep,
  interview questions for, get ready for interview with.
---

# Interview Prep Workflow

## Purpose

Prepare interview materials for one application folder under `applications/`:

1. `position_research.md` — company/lab/product + what the role looks like online
2. `application_fit.md` — fit highlights, motivation, why they would choose you, gaps
3. `interview_qa.md` — 10–20 challenging, role-specific questions with empty answer slots

All outputs stay inside the target application folder. Never invent credentials.

## Step 0 — Resolve the folder

1. Locate `applications/{folder}/` from the user's request (path or company name).
2. If ambiguous, list candidates and ask.
3. Require a job description file: prefer `descriptions.md`, else `description.md`.
4. Prefer reading the per-job `CV_farzaneh_labbaf.tex` if present; also read `base_cv/cv.md` and `base_cv/context_for_cover_letter.md`.
5. Optionally load `insights.json` if it exists.

## Step 1 — Position research → `position_research.md`

**Reuse rule:** If `position_research.md` already exists and the user did not ask to refresh, load it and skip recreation.

Otherwise research online (lab/team pages, product docs, collaboration pages, recent hiring posts) and write CV-relevant research. Focus on the **team, lab, or product unit** that owns the role — not only the parent brand (e.g. Mathis Lab, not generic EPFL).

### Required sections

```markdown
# Position research — {Role} ({Org / Lab})

**Role source:** …
**Org / lab:** …
**Last checked online:** {date}

## The lab / company / product in one paragraph
…

## What this specific opening is about
…

## Products / platforms / research outputs (most CV-relevant)
| Asset | What it does | Why it matters for this role |
…

## What the job likely looks like day to day
1. …
…

## CV-relevant themes to emphasize when preparing
| Role need | Credible angles from CV |
…

## Gaps to address honestly
…

## Useful links
…
```

Keep content actionable for interview prep. Cite URLs. Note posting status if the live ad differs from the saved JD.

## Step 2 — Application fit → `application_fit.md`

**Reuse rule:** If `application_fit.md` exists and the user did not ask to refresh, load it and skip recreation (unless research was refreshed — then update fit).

Write a personal, evidence-only fit brief:

```markdown
# Application fit — {Role}

## Experience most aligned with this role
### 1. … (strongest)
### 2. …
…

## Why this position is appealing (motivation)
…

## Why they would strongly consider you
1. …
…

## Honest positioning (gaps and how to frame them)
| Gap | Frame positively |
…

## Suggested one-liner for interviews / letters
…
```

Ground every claim in CV or `context_for_cover_letter.md`. Prefer concrete outcomes over slogans.

## Step 3 — Interview Q&A sheet → `interview_qa.md`

Write **10–20** questions. Default to **12–15** unless the role is unusually broad.

### Interviewer persona

Write as a senior interviewer with HR process skills **and** domain knowledge of the role (ML engineering, research software, product, etc.). Goal: test whether the candidate is a real fit — not coach softball questions.

### Question design rules

- **Not generic.** Avoid “Tell me about yourself”, “Where do you see yourself in 5 years”, “What are your strengths?” unless tightly bound to a specific CV claim.
- **Probe gaps and fog.** Prefer topics that are:
  - Required in the JD but weak/missing on the CV
  - Mentioned on the CV but vague (ownership, metrics, stack depth, team size, failure modes)
  - Easy to overclaim (PyTorch vs JAX, “worked with scientists”, “scaled systems”, “CI/CD”)
- **Be specific.** Name tools, projects, employers, or claims from *this* CV and *this* JD.
- **Mix types:** technical depth, system design, collaboration with scientists/PMs, production reliability, trade-offs, failure/debug stories, honesty about gaps.
- Order roughly: warmer specifics → harder gap probes → closing depth.

### Exact Q&A template (per question)

```markdown
# Interview Q&A — {Role} ({Org})

**Instructions for you:** Fill **Your answer** under each question before running the interview-feedback skill. Leave Feedback / Score / Improve empty.

**Sources used:** position_research.md, application_fit.md, job description, CV.

---

## Q1. {Specific challenging question}

**Why this question:** {1–2 sentences: which JD requirement or CV fog this probes}

**Your answer:**
<!-- Write your answer below this line -->


**Feedback:** _(skill 2)_
**Score:** _/10
**Improve:** _(skill 2)_

---
```

Repeat through QN. After the last question, add:

```markdown
## Prep notes (optional)

- Gaps to practice aloud: …
- Stories to have ready (STAR): …
```

### Do not

- Invent CV facts to make questions easier.
- Fill in answers for the user.
- Put feedback/scores in this step (that is `interview-feedback`).

## Step 4 — Summarize for the user

Report:
- Paths written/updated
- Whether research/fit were reused or refreshed
- Question count and the 2–3 hardest themes to practice
- Next step: fill `interview_qa.md`, then ask for interview answer feedback
