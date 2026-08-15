#!/usr/bin/env python3
"""Generate the case-study index and website data from report frontmatter."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CASE_DIR = ROOT / "learnings" / "case-studies"
README = CASE_DIR / "README.md"
JSON_OUTPUT = CASE_DIR / "case-studies.json"
START_MARKER = "<!-- generated-case-studies:start -->"
END_MARKER = "<!-- generated-case-studies:end -->"
REPOSITORY_URL = "https://github.com/wakamex/autoresearch"
COLLECTION_TITLE = "Autoresearch case studies"
LINK_RE = re.compile(r"\[([^]]+)\]\((https?://[^)]+)\)")
TOKEN_CONFIDENCE = {"high", "medium", "low"}


@dataclass(frozen=True)
class CaseStudy:
    number: int
    filename: str
    title: str
    started: str
    ended: str
    summary_markdown: str
    summary_text: str
    links: list[dict[str, str]]
    word_count: int
    featured_rank: int | None
    token_estimate: dict[str, int | str]

    @property
    def slug(self) -> str:
        return self.filename.removesuffix(".md")

    @property
    def report_url(self) -> str:
        return f"{REPOSITORY_URL}/blob/master/learnings/case-studies/{self.filename}"

    @property
    def raw_url(self) -> str:
        return (
            "https://raw.githubusercontent.com/wakamex/autoresearch/"
            f"master/learnings/case-studies/{self.filename}"
        )


def parse_report(path: Path) -> CaseStudy:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"{path}: missing JSON frontmatter")

    try:
        raw_metadata, body = text[4:].split("\n---\n", 1)
    except ValueError as error:
        raise ValueError(f"{path}: unterminated JSON frontmatter") from error

    try:
        metadata = json.loads(raw_metadata)
    except json.JSONDecodeError as error:
        raise ValueError(f"{path}: invalid JSON frontmatter: {error}") from error

    required = {"case", "title", "started", "ended", "summary_markdown"}
    allowed = required | {"featured_rank", "token_estimate"}
    missing = required - metadata.keys()
    extra = metadata.keys() - allowed
    if missing or extra:
        raise ValueError(f"{path}: metadata keys missing={sorted(missing)} extra={sorted(extra)}")

    number = metadata["case"]
    if not isinstance(number, int) or path.name[:3] != f"{number:02d}-":
        raise ValueError(f"{path}: case number does not match filename")

    for field in ("title", "started", "ended", "summary_markdown"):
        if not isinstance(metadata[field], str) or not metadata[field].strip():
            raise ValueError(f"{path}: {field} must be a non-empty string")

    featured_rank = metadata.get("featured_rank")
    if featured_rank is not None and (
        isinstance(featured_rank, bool) or not isinstance(featured_rank, int) or featured_rank < 1
    ):
        raise ValueError(f"{path}: featured_rank must be a positive integer")

    token_estimate = metadata.get("token_estimate")
    if not isinstance(token_estimate, dict):
        raise ValueError(f"{path}: token_estimate must be an object")
    expected_token_fields = {"processed_tokens", "effective_tokens", "confidence"}
    if set(token_estimate) != expected_token_fields:
        raise ValueError(
            f"{path}: token_estimate keys must be {sorted(expected_token_fields)}"
        )
    for field in ("processed_tokens", "effective_tokens"):
        value = token_estimate[field]
        if isinstance(value, bool) or not isinstance(value, int) or value < 0:
            raise ValueError(f"{path}: token_estimate.{field} must be a non-negative integer")
    if token_estimate["effective_tokens"] > token_estimate["processed_tokens"]:
        raise ValueError(f"{path}: effective token estimate exceeds processed token estimate")
    if token_estimate["confidence"] not in TOKEN_CONFIDENCE:
        raise ValueError(
            f"{path}: token_estimate.confidence must be one of {sorted(TOKEN_CONFIDENCE)}"
        )

    started = date.fromisoformat(metadata["started"])
    ended = date.fromisoformat(metadata["ended"])
    if ended < started:
        raise ValueError(f"{path}: ended date precedes started date")

    expected_heading = f"# Case {number:02d} - {metadata['title']}"
    if body.lstrip().splitlines()[0] != expected_heading:
        raise ValueError(f"{path}: heading must be {expected_heading!r}")

    expected_window = f"Observation window: {metadata['started']} through {metadata['ended']}"
    observation_lines = re.findall(r"^Observation window:.*$", body, flags=re.MULTILINE)
    if observation_lines != [expected_window]:
        raise ValueError(f"{path}: observation window must be {expected_window!r}")

    summary_markdown = metadata["summary_markdown"]
    links = [
        {"text": match.group(1), "url": match.group(2)}
        for match in LINK_RE.finditer(summary_markdown)
    ]
    summary_text = LINK_RE.sub(lambda match: match.group(1), summary_markdown)

    return CaseStudy(
        number=number,
        filename=path.name,
        title=metadata["title"],
        started=metadata["started"],
        ended=metadata["ended"],
        summary_markdown=summary_markdown,
        summary_text=summary_text,
        links=links,
        word_count=len(body.split()),
        featured_rank=featured_rank,
        token_estimate=token_estimate,
    )


def load_cases() -> list[CaseStudy]:
    cases = [parse_report(path) for path in sorted(CASE_DIR.glob("[0-9][0-9]-*.md"))]
    numbers = [case.number for case in cases]
    expected = list(range(1, len(cases) + 1))
    if numbers != expected:
        raise ValueError(f"case numbers must be contiguous: found {numbers}, expected {expected}")
    featured_ranks = sorted(
        case.featured_rank for case in cases if case.featured_rank is not None
    )
    expected_featured_ranks = list(range(1, len(featured_ranks) + 1))
    if featured_ranks != expected_featured_ranks:
        raise ValueError(
            "featured ranks must be unique and contiguous: "
            f"found {featured_ranks}, expected {expected_featured_ranks}"
        )
    return cases


def format_effective_tokens(tokens: int) -> str:
    if tokens >= 1_000_000_000:
        value = f"{tokens / 1_000_000_000:.2f}".rstrip("0").rstrip(".")
        return f"~{value}B"
    if tokens >= 1_000_000:
        value = f"{tokens / 1_000_000:.1f}".rstrip("0").rstrip(".")
        return f"~{value}M"
    if tokens >= 1_000:
        value = f"{tokens / 1_000:.1f}".rstrip("0").rstrip(".")
        return f"~{value}K"
    return f"~{tokens}"


def render_table(cases: list[CaseStudy]) -> str:
    rows = [
        "| Case | What happened | Effective tokens | When |",
        "|---|---|---:|---|",
    ]
    for case in cases:
        rows.append(
            f"| [`{case.filename}`]({case.filename}) | {case.summary_markdown} "
            f"| {format_effective_tokens(case.token_estimate['effective_tokens'])} "
            f"| {case.started} to {case.ended} |"
        )
    return "\n".join(rows)


def render_readme(current: str, cases: list[CaseStudy]) -> str:
    if current.count(START_MARKER) != 1 or current.count(END_MARKER) != 1:
        raise ValueError(f"{README}: expected exactly one generated marker pair")
    before, remainder = current.split(START_MARKER, 1)
    _, after = remainder.split(END_MARKER, 1)
    return f"{before}{START_MARKER}\n{render_table(cases)}\n{END_MARKER}{after}"


def render_json(cases: list[CaseStudy]) -> str:
    processed_tokens = sum(case.token_estimate["processed_tokens"] for case in cases)
    effective_tokens = sum(case.token_estimate["effective_tokens"] for case in cases)
    payload = {
        "schema_version": 2,
        "title": COLLECTION_TITLE,
        "description": (
            f"{len(cases)} chronological field reports on using autoresearch in applied projects, "
            "including what worked, what failed, and how the research infrastructure evolved."
        ),
        "updated": max(case.ended for case in cases),
        "repository_url": REPOSITORY_URL,
        "token_estimates": {
            "processed_tokens": processed_tokens,
            "effective_tokens": effective_tokens,
            "method": (
                "Rounded estimates from retained local session records. Processed tokens include "
                "input, output, cache-write, and cache-read tokens. Effective tokens are an "
                "uncached-equivalent proxy calculated as processed tokens minus 90% of cache-read "
                "tokens. Reconstructed provider records and day-level attribution introduce "
                "uncertainty."
            ),
        },
        "cases": [
            {
                "case": case.number,
                "slug": case.slug,
                "filename": case.filename,
                "title": case.title,
                "started": case.started,
                "ended": case.ended,
                "summary_markdown": case.summary_markdown,
                "summary_text": case.summary_text,
                "links": case.links,
                "word_count": case.word_count,
                "featured_rank": case.featured_rank,
                "token_estimate": case.token_estimate,
                "report_url": case.report_url,
                "raw_url": case.raw_url,
            }
            for case in cases
        ],
    }
    return json.dumps(payload, indent=2, ensure_ascii=False) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="fail if the generated README table or JSON is stale",
    )
    args = parser.parse_args()

    try:
        cases = load_cases()
        current_readme = README.read_text(encoding="utf-8")
        expected_readme = render_readme(current_readme, cases)
        expected_json = render_json(cases)
    except (OSError, ValueError) as error:
        print(error, file=sys.stderr)
        return 1

    if args.check:
        stale = []
        if current_readme != expected_readme:
            stale.append(str(README.relative_to(ROOT)))
        if not JSON_OUTPUT.exists() or JSON_OUTPUT.read_text(encoding="utf-8") != expected_json:
            stale.append(str(JSON_OUTPUT.relative_to(ROOT)))
        if stale:
            print(f"stale generated files: {', '.join(stale)}", file=sys.stderr)
            print("run: python3 scripts/generate_case_studies.py", file=sys.stderr)
            return 1
        print(f"case-study data is current ({len(cases)} cases)")
        return 0

    README.write_text(expected_readme, encoding="utf-8")
    JSON_OUTPUT.write_text(expected_json, encoding="utf-8")
    print(f"generated {README.relative_to(ROOT)} and {JSON_OUTPUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
