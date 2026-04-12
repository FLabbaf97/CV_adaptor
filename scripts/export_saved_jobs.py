import argparse
import json
import os
import re
import shutil
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit, urlunsplit

from dotenv import load_dotenv
from notion_client import Client
from notion_client.errors import APIResponseError


_WINDOWS_RESERVED_NAMES = {
    "con",
    "prn",
    "aux",
    "nul",
    "com1",
    "com2",
    "com3",
    "com4",
    "com5",
    "com6",
    "com7",
    "com8",
    "com9",
    "lpt1",
    "lpt2",
    "lpt3",
    "lpt4",
    "lpt5",
    "lpt6",
    "lpt7",
    "lpt8",
    "lpt9",
}


def _rich_text_to_plain(rich_text_items: list[dict[str, Any]]) -> str:
    return "".join(item.get("plain_text", "") for item in rich_text_items)


def _normalize_url(value: str | None) -> str | None:
    if not value:
        return value

    parsed = urlsplit(value)
    host = parsed.netloc.lower()

    if "linkedin.com" in host:
        match = re.match(r"^/jobs/view/(\d+)/?", parsed.path)
        if match:
            canonical_path = f"/jobs/view/{match.group(1)}/"
            return urlunsplit(
                (parsed.scheme, parsed.netloc, canonical_path, "", "")
            )

    return value


def _extract_property_value(prop: dict[str, Any]) -> Any:
    prop_type = prop.get("type")

    if prop_type == "title":
        return _rich_text_to_plain(prop.get("title", []))
    if prop_type == "rich_text":
        return _rich_text_to_plain(prop.get("rich_text", []))
    if prop_type == "url":
        return _normalize_url(prop.get("url"))
    if prop_type == "status":
        status = prop.get("status")
        return status.get("name") if status else None
    if prop_type == "select":
        selected = prop.get("select")
        return selected.get("name") if selected else None
    if prop_type == "multi_select":
        return [
            item.get("name")
            for item in prop.get("multi_select", [])
            if item.get("name")
        ]
    if prop_type == "date":
        date_value = prop.get("date")
        return date_value.get("start") if date_value else None
    if prop_type == "checkbox":
        return prop.get("checkbox")
    if prop_type == "number":
        return prop.get("number")
    if prop_type == "email":
        return prop.get("email")
    if prop_type == "phone_number":
        return prop.get("phone_number")

    return None


def _get_title(properties: dict[str, dict[str, Any]]) -> str:
    for prop in properties.values():
        if prop.get("type") == "title":
            return _extract_property_value(prop) or ""
    return ""


def _has_saved_tag(
    properties: dict[str, dict[str, Any]],
    tag_value: str,
) -> bool:
    target = tag_value.strip().lower()

    for prop in properties.values():
        prop_type = prop.get("type")

        if prop_type in {"status", "select"}:
            value = _extract_property_value(prop)
            if isinstance(value, str) and value.strip().lower() == target:
                return True

        if prop_type == "multi_select":
            values = _extract_property_value(prop)
            if isinstance(values, list) and any(
                str(v).strip().lower() == target for v in values
            ):
                return True

    return False


def _fetch_database_pages(
    notion: Client,
    database_id: str,
) -> list[dict[str, Any]]:
    db_info = notion.databases.retrieve(database_id=database_id)
    data_sources = db_info.get("data_sources", [])

    if data_sources:
        pages: list[dict[str, Any]] = []
        for source in data_sources:
            source_id = source.get("id")
            if not source_id:
                continue
            pages.extend(_fetch_data_source_pages(notion, source_id))
        return pages

    if not hasattr(notion.databases, "query"):
        raise RuntimeError(
            "No queryable data source found for this Notion database."
        )

    pages: list[dict[str, Any]] = []
    cursor: str | None = None

    while True:
        payload: dict[str, Any] = {
            "database_id": database_id,
            "page_size": 100,
        }
        if cursor:
            payload["start_cursor"] = cursor

        response = notion.databases.query(**payload)
        pages.extend(response.get("results", []))

        if not response.get("has_more"):
            break
        cursor = response.get("next_cursor")

    return pages


def _fetch_data_source_pages(
    notion: Client,
    data_source_id: str,
) -> list[dict[str, Any]]:
    pages: list[dict[str, Any]] = []
    cursor: str | None = None

    while True:
        payload: dict[str, Any] = {
            "data_source_id": data_source_id,
            "page_size": 100,
        }
        if cursor:
            payload["start_cursor"] = cursor

        response = notion.data_sources.query(**payload)
        pages.extend(response.get("results", []))

        if not response.get("has_more"):
            break
        cursor = response.get("next_cursor")

    return pages


def _to_job_json(page: dict[str, Any]) -> dict[str, Any]:
    properties = page.get("properties", {})

    normalized: dict[str, Any] = {
        "id": page.get("id"),
        "created_time": page.get("created_time"),
        "last_edited_time": page.get("last_edited_time"),
        "title": _get_title(properties),
        "properties": {},
    }

    for name, prop in properties.items():
        normalized["properties"][name] = _extract_property_value(prop)

    return normalized


def _slugify(value: str) -> str:
    # Remove characters not allowed in Windows path segments.
    cleaned = re.sub(r"[<>:\"/\\|?*\x00-\x1F]", "", value)
    # Remove punctuation and symbols (including emoji), keep letters/digits.
    cleaned = re.sub(r"[^\w\s-]", "", cleaned, flags=re.UNICODE)
    cleaned = re.sub(r"[-\s]+", "_", cleaned).strip("_. ")

    if not cleaned:
        return "untitled"

    if cleaned.lower() in _WINDOWS_RESERVED_NAMES:
        cleaned = f"{cleaned}_job"

    return cleaned


def _extract_role_from_title(title: str, company_name: str) -> str:
    if not title:
        return "untitled"

    parts = [part.strip() for part in title.split("|") if part.strip()]
    if not parts:
        return title

    role = parts[0]
    if (
        company_name
        and role.lower() == company_name.lower()
        and len(parts) > 1
    ):
        return parts[1]

    return role


def _format_date(value: str | None) -> str:
    if not value:
        return "unknown_date"

    normalized = value.replace("Z", "+00:00")
    try:
        dt = datetime.fromisoformat(normalized)
    except ValueError:
        return _slugify(value)

    return dt.date().isoformat()


def _build_application_dirname(job: dict[str, Any]) -> str:
    props = job.get("properties", {})
    company_name = str(props.get("Company") or "")
    role_name = _extract_role_from_title(
        str(job.get("title") or ""),
        company_name,
    )

    company = _slugify(company_name or "unknown_company")
    date_saved = _format_date(job.get("created_time"))
    role = _slugify(role_name)

    return f"{company}_{date_saved}_{role}"


def _write_job_description(job_dir: Path, job: dict[str, Any]) -> None:
    lines = [
        f"# {job.get('title') or 'Untitled job'}",
        "",
        f"- ID: {job.get('id')}",
        f"- Created: {job.get('created_time')}",
        f"- Last edited: {job.get('last_edited_time')}",
        "",
        "## Properties",
        "",
    ]

    for key, value in sorted(job.get("properties", {}).items()):
        if isinstance(value, list):
            rendered = ", ".join(str(item) for item in value)
        else:
            rendered = "" if value is None else str(value)
        lines.append(f"- {key}: {rendered}")

    (job_dir / "descriptions.md").write_text(
        "\n".join(lines) + "\n",
        encoding="utf-8",
    )


def _scaffold_application(
    job: dict[str, Any],
    base_cv_path: Path,
    applications_dir: Path,
) -> bool:
    job_dir = applications_dir / _build_application_dirname(job)

    if job_dir.exists():
        return False

    job_dir.mkdir(parents=True, exist_ok=False)
    _write_job_description(job_dir, job)
    shutil.copy2(base_cv_path, job_dir / "cv_KARAMI.tex")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Fetch jobs from Notion database and output entries "
            "tagged as Saved in JSON format."
        )
    )
    parser.add_argument(
        "--saved-tag",
        default=os.getenv("SAVED_TAG", "Saved"),
        help=(
            "Tag/status value that marks a job as saved "
            "(default: Saved or env SAVED_TAG)."
        ),
    )
    parser.add_argument(
        "--output",
        default=None,
        help=(
            "Optional path to write JSON output file. "
            "If omitted, prints to stdout only."
        ),
    )
    args = parser.parse_args()

    load_dotenv()

    notion_token = os.getenv("NOTION_TOKEN")
    database_id = os.getenv("NOTION_DATABASE_ID")

    if not notion_token:
        raise SystemExit("Missing NOTION_TOKEN in environment.")
    if not database_id:
        raise SystemExit("Missing NOTION_DATABASE_ID in environment.")

    notion = Client(auth=notion_token)

    try:
        pages = _fetch_database_pages(notion, database_id)
    except APIResponseError as error:
        raise SystemExit(
            f"Failed to query Notion database: {error}"
        ) from error

    saved_jobs = [
        _to_job_json(page)
        for page in pages
        if _has_saved_tag(page.get("properties", {}), args.saved_tag)
    ]

    root_dir = Path(__file__).resolve().parents[1]
    applications_dir = root_dir / "applications"
    base_cv_path = root_dir / "base_cv" / "cv_1225_KARAMI.tex"

    if not base_cv_path.exists():
        raise SystemExit(f"Base CV not found: {base_cv_path}")

    created_count = 0
    for job in saved_jobs:
        if _scaffold_application(job, base_cv_path, applications_dir):
            created_count += 1

    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "saved_tag": args.saved_tag,
        "count": len(saved_jobs),
        "applications_created": created_count,
        "jobs": saved_jobs,
    }

    json_text = json.dumps(payload, indent=2, ensure_ascii=False)
    print(json_text)

    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(json_text + "\n", encoding="utf-8")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
