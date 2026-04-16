#!/usr/bin/env python3
"""
Generate structured JSON data from committee reports for the frontend site.

Reads the generated markdown reports from each committee's Reports/ directory,
parses their structure, and outputs JSON files that the frontend can consume.

Usage:
  python generate_site_data.py                    # All committees
  python generate_site_data.py --committee MCC    # Single committee
  python generate_site_data.py --list             # Show available data
"""

import re
import json
import argparse
from pathlib import Path
from datetime import datetime

from config import (
    VAULT_ROOT, COMMITTEES, COMMITTEE_FULL_NAMES, SITE_DATA_DIR, ELECTION_START,
)
try:
    from config import SITE_DATA_MIRRORS
except ImportError:
    SITE_DATA_MIRRORS = []

EVIDENCE_DIR = SITE_DATA_DIR / "evidence"


def load_evidence_overlay(committee: str) -> dict:
    """Load human-curated evidence overlay for a committee.

    File shape: { "promises": { "<num>": {
        "verified_status": "verified-delivered" | "disputed",
        "submissions": [ { url, type, submitted_by, submitted_at, note, accepted } ]
    } } }
    """
    path = EVIDENCE_DIR / f"{committee.lower()}.json"
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        print(f"  WARN: invalid JSON in {path}, skipping overlay")
        return {}


def apply_evidence_overlay(promises: list[dict], overlay: dict) -> list[dict]:
    by_num = overlay.get("promises", {})
    for p in promises:
        entry = by_num.get(str(p["num"]))
        if not entry:
            continue
        if "verified_status" in entry:
            p["verified_status"] = entry["verified_status"]
        subs = [s for s in entry.get("submissions", []) if s.get("accepted")]
        if subs:
            p["evidence_submissions"] = subs
    return promises


def parse_report_header(text: str) -> dict:
    """Extract metadata from the standard report header."""
    meta = {}
    for line in text.split("\n")[:10]:
        if line.startswith("**Committee:**"):
            meta["committee"] = line.split("**Committee:**")[1].strip()
        elif line.startswith("**Period:**"):
            meta["period"] = line.split("**Period:**")[1].strip()
        elif line.startswith("**Meetings:**"):
            meta["meetings_count"] = int(line.split("**Meetings:**")[1].strip())
        elif line.startswith("**Transcripts available:**"):
            meta["has_transcripts"] = "Yes" in line
        elif line.startswith("**Generated:**"):
            meta["generated"] = line.split("**Generated:**")[1].strip()
    return meta


def parse_promises_report(text: str) -> list[dict]:
    """Extract promise tracker items from Prompt 4 report."""
    promises = []
    # Match table rows: | # | Promise | Made by | Date | Repeated? | Status | Evidence |
    row_re = re.compile(
        r"\|\s*(\d+)\s*\|"       # number
        r"\s*(.+?)\s*\|"          # promise
        r"\s*(.+?)\s*\|"          # made by
        r"\s*(.+?)\s*\|"          # date
        r"\s*(.+?)\s*\|"          # repeated
        r"\s*(.+?)\s*\|"          # status
        r"\s*(.+?)\s*\|"          # evidence
    )
    for match in row_re.finditer(text):
        num, promise, made_by, date, repeated, status, evidence = match.groups()
        # Skip header separator rows
        if set(num.strip()) <= {"-", " "}:
            continue
        status_clean = status.strip().upper()
        status_key = "failed"
        if "DELIVERED" in status_clean and "NOT" not in status_clean:
            status_key = "delivered"
        elif "PARTIAL" in status_clean:
            status_key = "partial"
        elif "RECURRING" in status_clean:
            status_key = "recurring"

        promises.append({
            "num": int(num.strip()),
            "promise": promise.strip(),
            "made_by": made_by.strip(),
            "first_promised": date.strip(),
            "repeated": repeated.strip(),
            "status": status_key,
            "evidence": evidence.strip(),
        })
    return promises


RATIO_RE = re.compile(r"^\s*(\d+)\s*/\s*(\d+)\s*$")


def parse_attendance_section(text: str) -> list[dict]:
    """Extract member attendance data from Prompt 2 report.

    Handles multiple table formats:
      | Name | 11/25 | 12/02 | ... | 11/11 |      (MCC: ratio in LAST cell)
      | Name | 6/6   | 100%  |                   (TSC: ratio in SECOND cell)
    Picks the last cell that is a clean "N/M" ratio. Columns that look like
    dates (e.g. "11/25") in the header region are not candidates because we
    only inspect body cells and take the ratio furthest to the right.
    """
    members = []
    by_name: dict[str, dict] = {}
    lines = text.split("\n")
    in_table = False

    for line in lines:
        stripped = line.strip()
        if not stripped.startswith("|"):
            if in_table:
                in_table = False
            continue

        cells = [c.strip() for c in stripped.strip("|").split("|")]

        if all(set(c) <= {"-", " ", ":"} for c in cells):
            in_table = True
            continue

        if not in_table or len(cells) < 2:
            continue

        name = cells[0]
        if not name or set(name) <= {"-", " "}:
            continue

        ratio_cell = None
        for c in reversed(cells[1:]):
            m = RATIO_RE.match(c)
            if m:
                ratio_cell = m
                break
        if not ratio_cell:
            continue

        try:
            attended = int(ratio_cell.group(1))
            total_meetings = int(ratio_cell.group(2))
        except ValueError:
            continue
        if total_meetings == 0:
            continue

        existing = by_name.get(name)
        if existing:
            existing["attended"] += attended
            existing["total"] += total_meetings
            existing["rate"] = round(existing["attended"] / existing["total"] * 100)
        else:
            entry = {
                "name": name,
                "attended": attended,
                "total": total_meetings,
                "rate": round(attended / total_meetings * 100),
            }
            by_name[name] = entry
            members.append(entry)

    return members


def split_report_sections(text: str) -> list[dict]:
    """Split a report into H2 sections for frontend rendering."""
    sections = []
    current_title = None
    current_body = []

    for line in text.split("\n"):
        if line.startswith("## "):
            if current_title:
                sections.append({
                    "title": current_title,
                    "body": "\n".join(current_body).strip()
                })
            current_title = line[3:].strip()
            current_body = []
        else:
            current_body.append(line)

    if current_title:
        sections.append({
            "title": current_title,
            "body": "\n".join(current_body).strip()
        })

    return sections


def build_committee_data(committee: str) -> dict | None:
    """Build a complete data structure for one committee."""

    reports_dir = VAULT_ROOT / committee / "Reports"
    transcripts_dir = VAULT_ROOT / committee / "Transcripts"

    if not reports_dir.exists() and not transcripts_dir.exists():
        return None

    # Count source files (filtered by election start date)
    election_start = ELECTION_START.get(committee)
    summary_count = 0
    transcript_count = 0
    dates = []

    if transcripts_dir.exists():
        for f in sorted(transcripts_dir.glob("*.md")):
            parts = f.stem.split(" - ")
            if len(parts) < 2:
                continue
            date_str = parts[0].strip()
            file_type = parts[1].strip().lower()
            if election_start and date_str < election_start:
                continue
            if "summary" in file_type:
                summary_count += 1
            elif "transcript" in file_type:
                transcript_count += 1
            if date_str not in dates:
                dates.append(date_str)

    dates.sort()

    # Load reports
    reports = {}
    report_files = {
        "summaries_vs_transcripts": "01 - Summaries vs Transcripts.md",
        "member_participation": "02 - Member Participation Analysis.md",
        "leadership_assessment": "03 - Leadership Assessment.md",
        "promises_vs_reality": "04 - Promises vs Reality.md",
        "critical_observations": "05 - Critical Observations.md",
    }

    for key, filename in report_files.items():
        report_path = reports_dir / filename
        if report_path.exists():
            text = report_path.read_text(encoding="utf-8")
            header = parse_report_header(text)
            sections = split_report_sections(text)

            report_data = {
                "available": True,
                "header": header,
                "sections": sections,
                "raw_text": text,
            }

            # Add structured data for specific reports
            if key == "promises_vs_reality":
                promises = parse_promises_report(text)
                overlay = load_evidence_overlay(committee)
                report_data["promises"] = apply_evidence_overlay(promises, overlay)
            elif key == "member_participation":
                report_data["members"] = parse_attendance_section(text)

            reports[key] = report_data
        else:
            reports[key] = {"available": False}

    # Compute summary stats
    total_promises = 0
    delivered = 0
    partial = 0
    failed = 0
    recurring = 0
    if reports["promises_vs_reality"].get("available"):
        for p in reports["promises_vs_reality"].get("promises", []):
            total_promises += 1
            effective = "delivered" if p.get("verified_status") == "verified-delivered" else p["status"]
            if effective == "delivered":
                delivered += 1
            elif effective == "partial":
                partial += 1
            elif effective == "recurring":
                recurring += 1
            else:
                failed += 1

    data = {
        "committee": committee,
        "full_name": COMMITTEE_FULL_NAMES.get(committee, committee),
        "period": {
            "start": dates[0] if dates else None,
            "end": dates[-1] if dates else None,
        },
        "meetings_count": len(dates),
        "summary_count": summary_count,
        "transcript_count": transcript_count,
        "has_transcripts": transcript_count > 0,
        "dates": dates,
        "reports": reports,
        "stats": {
            "total_promises": total_promises,
            "delivered": delivered,
            "partial": partial,
            "failed": failed,
            "recurring": recurring,
            "delivery_rate": round(delivered / total_promises * 100) if total_promises else 0,
        },
        "generated": datetime.now().isoformat(),
    }

    return data


def build_index(all_data: list[dict]) -> dict:
    """Build the master index JSON with summary info for all committees."""
    committees = []
    for d in all_data:
        report_count = sum(
            1 for r in d["reports"].values() if r.get("available")
        )
        committees.append({
            "id": d["committee"],
            "name": d["full_name"],
            "period": d["period"],
            "meetings_count": d["meetings_count"],
            "has_transcripts": d["has_transcripts"],
            "report_count": report_count,
            "stats": d["stats"],
        })

    return {
        "generated": datetime.now().isoformat(),
        "committees": committees,
    }


def main():
    ap = argparse.ArgumentParser(description="Generate site data from committee reports")
    ap.add_argument("--committee", help="Single committee code, or omit for all")
    ap.add_argument("--list", action="store_true", help="List available data and exit")
    args = ap.parse_args()

    SITE_DATA_DIR.mkdir(parents=True, exist_ok=True)

    if args.committee:
        target = [args.committee.upper()]
    else:
        target = COMMITTEES

    all_data = []
    for c in target:
        print(f"Processing {c}...")
        data = build_committee_data(c)
        if data:
            # Strip raw_text from reports to keep JSON manageable
            for key in data["reports"]:
                if data["reports"][key].get("available"):
                    data["reports"][key].pop("raw_text", None)

            payload = json.dumps(data, indent=2)
            out_path = SITE_DATA_DIR / f"{c.lower()}.json"
            out_path.write_text(payload, encoding="utf-8")
            print(f"  -> {out_path}")
            for mirror in SITE_DATA_MIRRORS:
                mirror.mkdir(parents=True, exist_ok=True)
                (mirror / f"{c.lower()}.json").write_text(payload, encoding="utf-8")
            all_data.append(data)
        else:
            print(f"  No data found for {c}")

    if args.list:
        for d in all_data:
            rc = sum(1 for r in d["reports"].values() if r.get("available"))
            print(f"  {d['committee']}: {d['meetings_count']} meetings, {rc}/5 reports")
        return

    # Build index
    index = build_index(all_data)
    index_payload = json.dumps(index, indent=2)
    index_path = SITE_DATA_DIR / "index.json"
    index_path.write_text(index_payload, encoding="utf-8")
    print(f"\nIndex -> {index_path}")
    for mirror in SITE_DATA_MIRRORS:
        mirror.mkdir(parents=True, exist_ok=True)
        (mirror / "index.json").write_text(index_payload, encoding="utf-8")
    print(f"Done. {len(all_data)} committee(s) exported.")


if __name__ == "__main__":
    main()
