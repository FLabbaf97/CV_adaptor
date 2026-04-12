---
name: motivation-letter
description: "Use when creating a job-specific motivation letter (cover letter) after CV tailoring. Trigger phrases: create motivation letter, write cover letter, motivation.tex, application letter, one-page letter, adapt motivation letter. Uses adapted cv_KARAMI.tex, descriptions.md, and base_cv/context_for_cover_letter.md to produce truthful, role-aligned motivation.tex."
argument-hint: "application folder path under applications/..."
---

# Motivation Letter Skill

## Purpose

Generate a concise, role-specific LaTeX motivation letter for a saved application folder.

The letter must:

- be based on existing evidence from the adapted CV and job description
- follow a clear 4-5 paragraph structure
- fit on a single page
- not repeat the CV line-by-line; it must argue role fit using selected evidence
- be saved as `motivation.tex` in the application folder

## When to Use

Use this skill after CV adaptation is complete for a target folder under `applications/...`.

Typical triggers:

- "create motivation letter"
- "write cover letter"
- "generate motivation.tex"
- "tailor application letter"

## Inputs

Target application folder:

- `applications/{Job_Title_Company_Source_YYYY-MM-DD}/`

Required files:

- `descriptions.md` (job requirements and context)
- `cv_KARAMI.tex` (adapted, job-specific CV)
- `base_cv/context_for_cover_letter.md` (master narrative and template language)

Optional but useful:

- `insights.json` (priority requirements already extracted during CV tailoring)

## Preconditions and Branching

1. Confirm the application folder exists.
2. Confirm `descriptions.md` exists.
3. Confirm `cv_KARAMI.tex` exists.
4. If `cv_KARAMI.tex` is missing or clearly untailored, stop and ask to run `cv-tailor` first.
5. If `motivation.tex` already exists, update it in place unless the user asks for a second variant.

## Workflow

1. Extract role priorities

- Identify 2-3 core requirements from `descriptions.md`.
- Prefer requirements that appear in must-have sections, responsibilities, or repeated keywords.
- If `insights.json` exists, use it to prioritize requirement mapping.

2. Map evidence from the adapted CV

- Pull only supported evidence from `cv_KARAMI.tex` (projects, methods, domain experience, internship work, outcomes).
- Build a requirement-to-evidence mapping before drafting.
- Exclude claims that are not explicitly supported in the CV.

3. Draft the letter in this structure (4-5 paragraphs)

- Paragraph 1: Opening - positioning and intent (3-4 lines)
  - Who you are, specialization, and why this role/company specifically.
- Paragraph 2: Why you - relevant experience (6-10 lines)
  - Match 2-3 job requirements to concrete CV-backed work.
- Paragraph 3: Why this - motivation and fit (4-6 lines)
  - Explain why the company/problem setting fits your goals and experience.
- Paragraph 4: How you think - your edge (optional but recommended)
  - Emphasize evaluation mindset, practical rigor, and cross-domain thinking.
- Paragraph 5: Closing (2-3 lines)
  - Reaffirm interest and contribution intent.

4. Keep it one page

- Target approximately 260-380 words.
- Keep sentences tight and remove redundant phrases.
- Prefer one concrete example per requirement instead of broad lists.
- Do not restate the CV chronologically; synthesize only the most relevant evidence.

5. Write output file

- Create or update `applications/{...}/motivation.tex`.
- Keep style professional, specific, and concise.
- Reuse language patterns from `base_cv/context_for_cover_letter.md` where appropriate.

## Output

- `applications/{...}/motivation.tex` (single-page, role-aligned letter)

## Quality Checks

Before finalizing, verify all checks pass:

1. Evidence integrity

- Every technical claim is traceable to `cv_KARAMI.tex`.
- No invented employers, titles, dates, publications, tools, metrics, or language skills.

2. Relevance

- At least 2 priority job requirements are explicitly addressed.
- Company-specific motivation is present (not generic).

3. Structure

- Uses 4-5 paragraphs with clear role progression.
- Includes opening, relevant experience, motivation/fit, and closing.

4. Length

- Content is likely to compile to one page in standard letter formatting.

## Guardrails

- Do not invent or exaggerate facts.
- Do not copy the job description verbatim; synthesize and map to evidence.
- Do not dump all CV content; select only what matches the role.
- Do not repeat the CV line-by-line; the letter should explain fit and motivation.
- Do not edit `base_cv/cv_1225_KARAMI.tex`.
- Avoid using em dashes in the letter text.

## Example Invocations

- `/motivation-letter applications/Proton_2026-03-29_Machine_Learning_Engineer`
- "Create a one-page motivation.tex for this adapted application folder"
- "Write a role-specific cover letter using descriptions.md and cv_KARAMI.tex"
