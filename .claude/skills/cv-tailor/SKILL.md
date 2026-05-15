---
name: cv-tailor
description: "Use when tailoring a CV for a specific saved job application, extracting key role requirements into insights.json, and updating cv_KARAMI.tex to better match the job while keeping all claims truthful. Trigger phrases: tailor CV, adapt resume, job-specific CV, ATS alignment, tailor application CV."
---

# CV Tailor Skill

## Purpose

Run a repeatable workflow for a saved application folder by:

- extracting role requirements from descriptions.md into insights.json
- tailoring cv_KARAMI.tex for that role
- keeping all claims accurate and evidence-based

## Input

Work on an application folder at:
applications/{company_title_datesaved}/

Expected files:

- descriptions.md: summary of the job description
- cv_KARAMI.tex: application-specific copy of the base CV

Condition:

- if insights.json is missing, create it before tailoring the CV
- if insights.json already exists, use it as the source of prioritised requirements

## Workflow

1. Create role insights
   Create applications/{company_title_datesaved}/insights.json with exactly these fields:

- important to have
- nice to have
- language requirements
- match score (0-100% alignment of CV to role requirements) this show waht percentage of the important to have requirements are met by the existing CV content, weighted by their prioritisation in insights.json. This score guides whether tailoring is worthwhile.

2. Tailor the CV if the match score is above 60% otherwise skip adaptation.
   Update cv_KARAMI.tex using both:

- descriptions.md
- insights.json

- create changes.json with a summary of changes made to the CV (for user review)
  - removed skills + why
  - added skills + why you included it

Tailoring rules:

- prioritise requirements listed in important to have
- include nice to have items only when supported by existing evidence in the CV
- reflect language requirements only when truthful and relevant
- improve phrasing, ordering, and emphasis without inventing new experience

## Output

A completed application folder containing:

- insights.json
- cv_KARAMI.tex tailored for the target role
- changes.json summarising CV updates for user review

## Guardrails

- Do not invent employers, job titles, dates, achievements, responsibilities, tools, or certifications.
- Do not add skills or keywords unless they are supported by the existing CV or source material.
- Keep measurable claims unchanged unless the user provides corrected numbers.
- Optimise for relevance and clarity, not exaggeration.
