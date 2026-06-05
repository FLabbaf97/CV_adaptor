---
name: career-ops
description: AI job search command center -- evaluate offers, generate CVs, scan portals, track applications
arguments: mode # Claude Code specific
user-invocable: true
argument-hint: "[report <folder> | scan | deep | pdf | oferta | ofertas | apply | batch | tracker | pipeline | contacto | training | project | interview-prep | update]"
license: MIT
---

# career-ops -- Router

## Mode Routing

Determine the mode from `$mode`:

| Input                           | Mode                             |
| ------------------------------- | -------------------------------- |
| (empty / no args)               | `discovery` -- Show command menu |
| JD text or URL (no sub-command) | **`auto-pipeline`**              |
| `oferta`                        | `oferta`                         |
| `ofertas`                       | `ofertas`                        |
| `contacto`                      | `contacto`                       |
| `deep`                          | `deep`                           |
| `interview-prep`                | `interview-prep`                 |
| `pdf`                           | `pdf`                            |
| `training`                      | `training`                       |
| `project`                       | `project`                        |
| `tracker`                       | `tracker`                        |
| `pipeline`                      | `pipeline`                       |
| `apply`                         | `apply`                          |
| `scan`                          | `scan`                           |
| `batch`                         | `batch`                          |
| `patterns`                      | `patterns`                       |
| `followup`                      | `followup`                       |
| `report <folder>`               | `report`                         |
| folder path (no sub-command)    | `report`                         |

**Folder-path detection:** If `$mode` is not a known sub-command AND looks like a folder path (contains `/`, starts with `applications/`, or matches an existing directory under the repo root), execute `report` with that path as the target folder.

**Auto-pipeline detection:** If `$mode` is not a known sub-command AND contains JD text (keywords: "responsibilities", "requirements", "qualifications", "about the role", "we're looking for", company name + role) or a URL to a JD, execute `auto-pipeline`.

If `$mode` is not a sub-command AND doesn't look like a JD or a folder path, show discovery.

---

## Discovery Mode (no arguments)

Show this menu:

```
career-ops -- Command Center

Available commands:
  /career-ops {folder}  → REPORT: analyze CV against job description, save report.md in folder
  /career-ops {JD}      → AUTO-PIPELINE: evaluate + report + PDF + tracker (paste text or URL)
  /career-ops pipeline  → Process pending URLs from inbox (data/pipeline.md)
  /career-ops oferta    → Evaluation only A-F (no auto PDF)
  /career-ops ofertas   → Compare and rank multiple offers
  /career-ops contacto  → LinkedIn power move: find contacts + draft message
  /career-ops deep      → Deep research prompt about company
  /career-ops interview-prep → Generate company-specific interview prep doc
  /career-ops pdf       → PDF only, ATS-optimized CV
  /career-ops training  → Evaluate course/cert against North Star
  /career-ops project   → Evaluate portfolio project idea
  /career-ops tracker   → Application status overview
  /career-ops apply     → Live application assistant (reads form + generates answers)
  /career-ops scan      → Scan portals and discover new offers
  /career-ops batch     → Batch processing with parallel workers
  /career-ops patterns  → Analyze rejection patterns and improve targeting
  /career-ops followup  → Follow-up cadence tracker: flag overdue, generate drafts

Inbox: add URLs to data/pipeline.md → /career-ops pipeline
Or paste a JD directly to run the full pipeline.
```

---

## Context Loading by Mode

After determining the mode, load the necessary files before executing:

### Modes that require `_shared.md` + their mode file:

Read `modes/_shared.md` + `modes/{mode}.md`

Applies to: `auto-pipeline`, `oferta`, `ofertas`, `pdf`, `contacto`, `apply`, `pipeline`, `scan`, `batch`

### Standalone modes (only their mode file):

Read `modes/{mode}.md`

Applies to: `tracker`, `deep`, `interview-prep`, `training`, `project`, `patterns`, `followup`

### Modes delegated to subagent:

For `scan`, `apply` (with Playwright), and `pipeline` (3+ URLs): launch as Agent with the content of `_shared.md` + `modes/{mode}.md` injected into the subagent prompt.

```
Agent(
  subagent_type="general-purpose",
  prompt="[content of modes/_shared.md]\n\n[content of modes/{mode}.md]\n\n[invocation-specific data]",
  description="career-ops {mode}"
)
```

Execute the instructions from the loaded mode file.

---

## Report Mode (inline)

**Trigger:** argument is a folder path, or `report <folder>`.

### Step 1 — Resolve inputs

- Resolve the folder path relative to the repo root if not absolute.
- Verify the folder exists; if it does not, tell the user and stop.
- Find the job description file: prefer `description.md`, fall back to `descriptions.md`. If neither exists, tell the user and stop.
- Find the CV file: `CV_farzaneh_labbaf.tex`. If it does not exist, tell the user and stop.

### Step 2 — Extract role requirements

Read the job description and produce a structured summary:

- **Must-have skills / qualifications** (listed in order of priority from the JD)
- **Nice-to-have skills**
- **Language requirements**
- **Seniority and years of experience expected**
- **Domain focus** (e.g. NLP, computer vision, MLOps, etc.)

### Step 3 — Analyse the CV

Read `CV_farzaneh_labbaf.tex` and evaluate it against the requirements above:

- For each must-have requirement: mark as **Met**, **Partial**, or **Missing**, citing the specific CV section/line where evidence exists (or noting absence).
- For each nice-to-have: mark as **Met** or **Missing**.
- Identify keywords prominent in the JD that are absent from the CV.
- Identify CV content that is irrelevant or low-signal for this role.

### Step 4 — Compute match score

Overall match score (0–100) = weighted coverage of must-have requirements:
- Each must-have **Met** = full weight
- **Partial** = half weight
- **Missing** = zero

State the score and a one-sentence verdict on whether tailoring is worthwhile (threshold: ≥ 60%).

### Step 5 — Recommendations

Provide a concrete, prioritised action list:

1. Sections/bullet points to rewrite or reorder to surface buried evidence.
2. Keywords to add (only where truthful — backed by existing experience).
3. Content to de-emphasise or remove for this role.
4. Any gaps that cannot be closed without inventing experience (flag clearly).

### Step 6 — Write report.md

Save the full report to `{folder}/report.md` using this structure:

```markdown
# CV–JD Match Report
**Role:** <job title and company from JD>
**Date:** <today>
**Match Score:** <score>%  (<verdict>)

## Must-Have Requirements
| Requirement | Status | Evidence in CV |
|-------------|--------|---------------|
| ...         | Met / Partial / Missing | ... |

## Nice-to-Have Requirements
| Requirement | Status |
|-------------|--------|
| ...         | Met / Missing |

## Missing Keywords
<comma-separated list>

## Low-Signal CV Content for This Role
<bullet list>

## Recommended Actions (prioritised)
1. ...
2. ...

## Gaps That Cannot Be Closed Without Fabrication
<bullet list or "None">
```

After writing the file, confirm the path to the user and display the match score and top 3 recommended actions inline.
