# cv-adapter

An agentic workflow for tailoring CVs to specific job applications, extracting key requirements, and updating CVs while maintaining truthfulness and evidence-based claims.

## Setup

```bash


$env:UV_LINK_MODE='copy'; uv sync

# Windows workaround for uv hardlink errors (os error 396)
# this should be run by the user
uv run python scripts/export_saved_jobs.py


# tailor CVs
copilot -p "please tailor the CVs"

# compile PDFs
.\gen-pdfs.ps1
```
