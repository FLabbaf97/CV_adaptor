---
name: interview-feedback
description: >-
  Grades filled interview Q&A answers for a job application folder. Skips
  unanswered questions. Adapts scoring and feedback to interview type (HR,
  general, or technical) using recruiter vs hiring-manager rubrics. Reads
  interview_qa.md, scores answered questions, writes Feedback / Score / Improve
  in place using JD, research, fit, and CV. Use when the user asks to review
  interview answers, grade interview Q&A, give feedback on prep answers, score
  my answers, or assess interview_qa.md. Trigger phrases: feedback on interview
  answers, grade my Q&A, review interview_qa, assess interview answers.
---

# Interview Feedback Workflow

## Purpose

Assess **answered** questions in `applications/{folder}/interview_qa.md` and write **Feedback**, **Score**, and **Improve** for those questions only.

Never invent career facts. Judge answers against the JD, research/fit files, and the CV. Adapt the lens to the **interview type** (HR / general / technical).

## Step 0 — Resolve folder, interview type, and inputs

1. Locate `applications/{folder}/` from the user request.
2. Require `interview_qa.md`. If missing, tell the user to run **interview-prep** first.
3. **Determine interview type** (required before grading). Use this priority:
   - Explicit user request (“HR feedback”, “technical interview”, “general screen”, etc.)
   - A **Call type** / interview-type note already in `interview_qa.md`
   - If still unclear, ask once and wait — do not assume:
     - **HR** — recruiter / talent acquisition screen (risk reduction, motivation, culture)
     - **General** — mixed first/second call (fit + light technical judgment)
     - **Technical** — hiring manager / Head of AI / CEO / engineering deep-dive
4. Read supporting context (as available):
   - job description (`descriptions.md` or `description.md`)
   - `position_research.md`
   - `application_fit.md`
   - per-job `CV_farzaneh_labbaf.tex` and/or `base_cv/cv.md`
   - `base_cv/context_for_cover_letter.md`
   - `insights.json` if present

### Answered vs unanswered (hard rule)

- **Grade only** questions with a non-empty **Your answer** (more than whitespace / placeholder comments like `<!-- Write your answer... -->`).
- **Skip** unanswered questions entirely: do **not** fill Feedback / Score / Improve for them; leave those fields blank or untouched.
- If **no** questions are answered, stop and tell the user to fill answers first.
- If some are answered, grade those and note in the summary how many were skipped.

## Step 1 — Grade answered questions with the type-specific rubric

Every answer still passes this mental checklist (any interview type):

1. Did they answer the question (not dodge or go off-topic)?
2. Was it structured and easy to follow?
3. Did they use a real example rather than generic statements?
4. Was their personal contribution clear (vs the team’s)?
5. Did they explain *why* they decided what they did?
6. Did they describe outcome and/or what they learned?
7. Would you trust them to work independently?
8. Would you enjoy having them on the team?

For **0–3 years AI software engineering** roles: prefer careful reasoning, clarifying questions, tradeoffs, and honest gaps over confident memorized definitions.

Map dimension scores (1–5) into an overall **0–10** per answer (see conversion below). Write feedback in the voice of that interviewer’s priorities.

---

### Type A — HR interview

**Interviewer mindset:** Recruiter at a large company (Google, Roche, Microsoft, ABB, UBS). They may not judge transformers or Kubernetes. Core question: *If I pass this candidate to the hiring manager, is there a high chance they succeed and represent the company well?*

**What to measure (primary dimensions, score each 1–5):**

| Dimension | 1 | 3 | 5 |
|-----------|---|---|---|
| Communication | Confusing, rambling | Understandable | Extremely clear; complex ideas made simple |
| Motivation & role fit | Generic (“I like AI”) | Somewhat convincing | Specific, believable, tied to experience and *this* job |
| Career consistency | Scattered / no arc | Partial arc | Clear Education → experience → today → future with reasons |
| Ownership | Always passive (“my manager asked…”) | Mixed | “I noticed / proposed / implemented / coordinated / learned…” |
| Teamwork | Vague niceness | Some collaboration | Real disagreement, feedback, collaboration stories |
| Self-awareness | “No weaknesses” or blame | Mild awareness | Honest weakness + how they manage it |
| Authenticity | Canned adjectives | Mix of real + polish | Specific experiences over buzzwords |
| Professionalism / culture fit | Concerning | Acceptable | Someone you’d want on the team |

**Weight heavily:** communication, motivation, ownership, authenticity, culture fit.  
**Weight lightly:** deep technical accuracy, architecture tradeoffs (do not fail HR answers for missing system-design depth).

**Reward structure:** Context → Problem → Actions → Result → Reflection (STAR+).  
**Penalize:** buzzword salads, fake passion adjectives, passive phrasing, life-story dumps without a career point, dodging “why *this* job.”

**Perfect HR answer pattern:** short story, clear ownership, concrete result, one reflection line.

---

### Type B — Technical interview

**Interviewer mindset:** CEO / Head of AI / Engineering Manager. Core question: *If I hire this person tomorrow, can they solve our problems?* They evaluate how the candidate **thinks**, not whether they recite definitions.

**What to measure (primary dimensions, score each 1–5):**

| Dimension | 1 | 3 | 5 |
|-----------|---|---|---|
| Technical understanding | Mostly incorrect | Fundamentals OK | Expert / role-appropriate depth |
| Problem-solving process | Jumps to conclusions | Reasonable process | Systematic: clarify → assumptions → options → tradeoffs → decision → risks |
| Engineering thinking | Tool name-drop only | Some practicality | Requirements, scalability, maintainability, testing, monitoring, reliability |
| Decision making | One technology, no alternatives | Mentions options weakly | Compares alternatives; “it depends…” with criteria |
| Communication | Hard for an engineer to follow | Followable | Clear thinking aloud; facts vs assumptions separated |
| Business awareness | Ignores users/cost/risk | Occasional nod | Users, cost, maintenance, risk, time prioritized |
| Ownership | Escalates immediately / passive | Mixed | Owns triage, customer impact, rollback, root cause, prevention |
| Learning mindset & honesty | Bluffs or hides gaps | Admits gaps thinly | “I haven’t used X; based on Y I’d approach it like…” |

**Weight heavily:** problem-solving process, engineering thinking, technical accuracy, tradeoffs, ownership.  
**Weight moderately:** communication, business awareness, learning honesty.  
**Weight lightly:** culture-fit fluff and generic motivation speeches (still note if motivation is incoherent).

**Reward structure:** Clarify requirements → state assumptions → options → tradeoffs → decision → risks. Slowing down and asking “Can I clarify…?” is a **positive** signal.  
**Penalize:** rushing to buzzwords (Kubernetes/Docker/AWS lists), no requirements questions, absolute “best solution” claims, bluffing, zero business/customer priority on incidents.

**Hidden positives:** admitting uncertainty, thinking aloud, separating facts from assumptions, pragmatic prioritization (MVP vs perfect).

---

### Type C — General interview

**Interviewer mindset:** Mixed screen (often first or second call). Both “will they represent us well?” and “can they think like an engineer?” matter.

**What to measure:** Blend of HR and technical dimensions. Score all that apply; weight by question content:

- Behavioral / motivation / “tell me about yourself” → use **HR** primary dimensions.
- System design / debugging / “how would you…” → use **Technical** primary dimensions.
- Ambiguous questions → expect a short story **plus** light reasoning (ownership + one tradeoff or decision).

Use the shared dimension emphasis table:

| Dimension | HR emphasis | Technical emphasis | General |
|-----------|-------------|--------------------|---------|
| Clear communication | Critical | Critical | Critical |
| Logical structure | Critical | Critical | Critical |
| Ownership | Critical | Critical | Critical |
| Evidence from real experience | Critical | High | Critical |
| Motivation & role fit | Critical | Medium | High |
| Teamwork | Critical | Medium | High |
| Problem-solving process | Low–Medium | Critical | High when question is technical |
| Technical accuracy | Low | Critical | High when question is technical |
| Tradeoff analysis | Low | Critical | Medium–High |
| Business awareness | Medium | High | High |
| Learning mindset | High | Critical | High |
| Honesty about limitations | Critical | Critical | Critical |

---

### Overall score conversion (all types)

After scoring relevant dimensions 1–5, convert to **Score: N/10**:

| Overall /10 | Meaning |
|------------:|---------|
| 9–10 | Excellent for this interview type; interviewer checklist mostly “yes” |
| 7–8 | Strong; minor gaps for this type’s priorities |
| 5–6 | Partial; generic, incomplete, or misses what this interviewer cares about most |
| 3–4 | Weak evidence / high risk to advance |
| 0–2 | Off-topic, contradictory, fabricated-sounding, or empty of substance |

Do **not** use a single generic rubric for all types. An excellent technical deep-dive that is unstructured may score high on Technical Understanding but mid on Communication — reflect that in Feedback. An excellent HR story with no architecture detail must **not** be penalized for missing Kubernetes.

## Step 2 — Write feedback into the same file

Update **only graded (answered)** questions in place. Preserve question text and the user’s answer.

```markdown
**Feedback:** {2–4 sentences in the voice of this interview type: what worked, what this interviewer still doubts}
**Score:** {N}/10
**Improve:** {2–4 concrete bullets or a short rewrite hint — typed to what HR vs technical interviewers reward}
```

Optional: add a one-line dimension snapshot when useful, e.g.  
`Dimensions (HR): Communication 4/5 · Motivation 3/5 · Ownership 5/5`

If a previous feedback block exists on an answered question, replace it (unless the user asked to keep history — then append a dated `## Feedback pass {date}` section at the end instead).

**Unanswered questions:** leave Feedback / Score / Improve empty; do not invent scores or coaching that pretends they answered.

### After grading

Append or refresh a summary at the bottom of `interview_qa.md`:

```markdown
## Feedback summary

**Interview type:** {HR | General | Technical}
**Graded:** {k}/{n} questions ({skipped} unanswered skipped)
**Average score:** {x.x}/10 (answered only)

### Strongest answers
- Q… — {why this interviewer liked it}

### Weakest answers (practice first)
- Q… — {what to fix for this interview type}

### Cross-cutting recommendations
1. … {aligned to interview type}
2. …
3. …
```

## Step 3 — Report to the user

State interview type used, average score (answered only), count skipped, weakest 2–3 answered questions, and the path to `interview_qa.md`. Offer type-specific next steps (e.g. tighten STAR for HR; practice clarify→tradeoffs for technical).

## Guardrails

- Skip unanswered questions — no score, no fake feedback.
- Do not invent employers, metrics, tools, or publications when suggesting improvements — phrase **existing** experience or honestly admit a gap.
- Do not delete the user’s answers.
- Keep feedback direct and actionable; avoid generic praise.
- Match rigor to seniority implied by the JD (junior: reward process and honesty over encyclopedic recall).
