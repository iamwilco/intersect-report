# committee_analysis.py

Main analysis pipeline script. Save as `committee_analysis.py` in your scripts folder.

```python
#!/usr/bin/env python3
"""
Intersect Committee Performance Analysis Pipeline
==================================================
Processes committee transcripts and summaries through the Anthropic API
to produce critical, evidence-based performance reports.

Usage:
  python committee_analysis.py --committee MCC --prompt 1
  python committee_analysis.py --committee MCC --prompt all
  python committee_analysis.py --committee all --prompt all
  python committee_analysis.py --committee MCC --prompt 1 --dry-run
  python committee_analysis.py --committee MCC --prompt 1 --model claude-opus-4-20250514
"""

import os
import sys
import json
import time
import argparse
import hashlib
from pathlib import Path
from datetime import datetime

try:
    import anthropic
except ImportError:
    print("ERROR: pip install anthropic")
    sys.exit(1)

from config import (
    VAULT_ROOT, COMMITTEES, MODEL, MAX_CONTEXT_TOKENS,
    MAX_OUTPUT_TOKENS, CHARS_PER_TOKEN, RATE_LIMIT_DELAY
)
from prompts import PROMPTS


# ─────────────────────────────────────────────
# Token estimation
# ─────────────────────────────────────────────

def estimate_tokens(text: str) -> int:
    return len(text) // CHARS_PER_TOKEN


# ─────────────────────────────────────────────
# File loading
# ─────────────────────────────────────────────

def load_committee_files(committee: str) -> dict | None:
    """Load all Summary + Transcript files for a committee."""

    transcripts_dir = VAULT_ROOT / committee / "Transcripts"
    if not transcripts_dir.exists():
        print(f"  ERROR: {transcripts_dir} does not exist")
        return None

    files = sorted(transcripts_dir.glob("*.md"))
    summaries: dict[str, str] = {}
    transcripts: dict[str, str] = {}

    for f in files:
        content = f.read_text(encoding="utf-8").strip()
        if not content:
            continue

        parts = f.stem.split(" - ")
        if len(parts) < 2:
            continue
        date_str = parts[0].strip()
        file_type = parts[1].strip().lower()

        if "summary" in file_type:
            summaries[date_str] = content
        elif "transcript" in file_type:
            transcripts[date_str] = content

    all_dates = sorted(set(list(summaries.keys()) + list(transcripts.keys())))

    pairs = []
    for d in all_dates:
        pairs.append({
            "date": d,
            "summary": summaries.get(d),
            "transcript": transcripts.get(d),
        })

    # Build combined text block
    all_text_parts = []
    for d in all_dates:
        if d in summaries:
            all_text_parts.append(f"=== SUMMARY: {d} ===\n{summaries[d]}")
        if d in transcripts:
            all_text_parts.append(f"=== TRANSCRIPT: {d} ===\n{transcripts[d]}")
    all_text = "\n\n".join(all_text_parts)

    has_transcripts = any(v is not None for v in transcripts.values())
    start_date = all_dates[0] if all_dates else "unknown"
    end_date = all_dates[-1] if all_dates else "unknown"

    return {
        "summaries": summaries,
        "transcripts": transcripts,
        "pairs": pairs,
        "all_text": all_text,
        "dates": all_dates,
        "has_transcripts": has_transcripts,
        "start_date": start_date,
        "end_date": end_date,
        "total_tokens": estimate_tokens(all_text),
    }


# ─────────────────────────────────────────────
# API caller with audit logging
# ─────────────────────────────────────────────

def call_api(
    system: str,
    user_prompt: str,
    model: str,
    audit_dir: Path | None = None,
    audit_name: str = "call",
) -> str | None:
    """Call the Anthropic API. Returns response text or None on failure."""

    client = anthropic.Anthropic()

    input_tokens_est = estimate_tokens(system + user_prompt)
    print(f"    Est. input tokens: ~{input_tokens_est:,}")

    if input_tokens_est > MAX_CONTEXT_TOKENS:
        print(f"    ⚠ Input ({input_tokens_est:,}) exceeds limit ({MAX_CONTEXT_TOKENS:,})")
        return None

    # ── Audit: save input ──
    if audit_dir:
        audit_dir.mkdir(parents=True, exist_ok=True)
        meta = {
            "timestamp": datetime.now().isoformat(),
            "model": model,
            "system_hash": hashlib.md5(system.encode()).hexdigest(),
            "user_chars": len(user_prompt),
            "est_input_tokens": input_tokens_est,
        }
        (audit_dir / f"{audit_name}_meta_in.json").write_text(
            json.dumps(meta, indent=2)
        )
        (audit_dir / f"{audit_name}_full_input.txt").write_text(
            f"=== SYSTEM ===\n{system}\n\n=== USER ===\n{user_prompt}"
        )

    # ── API call ──
    t0 = time.time()
    try:
        resp = client.messages.create(
            model=model,
            max_tokens=MAX_OUTPUT_TOKENS,
            system=system,
            messages=[{"role": "user", "content": user_prompt}],
        )
    except anthropic.APIError as exc:
        print(f"    ✗ API error: {exc}")
        return None

    elapsed = time.time() - t0
    text = resp.content[0].text
    print(f"    ✓ {elapsed:.1f}s  in={resp.usage.input_tokens:,}  out={resp.usage.output_tokens:,}")

    if resp.stop_reason == "max_tokens":
        print(f"    ⚠ Output TRUNCATED — increase MAX_OUTPUT_TOKENS in config.py")

    # ── Audit: save output ──
    if audit_dir:
        out_meta = {
            "timestamp": datetime.now().isoformat(),
            "elapsed_s": round(elapsed, 2),
            "input_tokens": resp.usage.input_tokens,
            "output_tokens": resp.usage.output_tokens,
            "model": resp.model,
            "stop_reason": resp.stop_reason,
        }
        (audit_dir / f"{audit_name}_meta_out.json").write_text(
            json.dumps(out_meta, indent=2)
        )
        (audit_dir / f"{audit_name}_output.md").write_text(text)

    return text


# ─────────────────────────────────────────────
# Prompt 1 — per-meeting then synthesis
# ─────────────────────────────────────────────

def run_prompt_1(committee: str, data: dict, model: str):
    cfg = PROMPTS[1]
    reports_dir = VAULT_ROOT / committee / "Reports"
    audit_dir = reports_dir / "_audit" / "p1"
    reports_dir.mkdir(parents=True, exist_ok=True)

    if not data["has_transcripts"]:
        print(f"  SKIP: Prompt 1 requires transcripts. None found for {committee}.")
        return

    # Phase 1 — per-meeting
    findings: list[str] = []
    for pair in data["pairs"]:
        if not pair["summary"] or not pair["transcript"]:
            print(f"  skip {pair['date']} (missing file)")
            continue

        print(f"  ▸ Meeting {pair['date']}")
        prompt = cfg["per_meeting_prompt"].format(
            committee=committee,
            date=pair["date"],
            summary=pair["summary"],
            transcript=pair["transcript"],
        )
        result = call_api(cfg["system"], prompt, model, audit_dir, f"mtg_{pair['date']}")
        if result:
            findings.append(f"### {pair['date']}\n\n{result}")
        time.sleep(RATE_LIMIT_DELAY)

    if not findings:
        print("  ✗ No meeting analyses produced.")
        return

    # Phase 2 — synthesis
    print(f"  ▸ Synthesis ({len(findings)} meetings)")
    synth_prompt = cfg["synthesis_prompt"].format(
        committee=committee,
        all_findings="\n\n---\n\n".join(findings),
    )
    synthesis = call_api(cfg["system"], synth_prompt, model, audit_dir, "synthesis")

    # Assemble report
    report = _header(cfg["name"], committee, data)
    report += "\n\n---\n\n".join(findings)
    if synthesis:
        report += "\n\n---\n\n## Overall Patterns\n\n" + synthesis

    out = reports_dir / cfg["filename"]
    out.write_text(report, encoding="utf-8")
    print(f"  ✅ {out}")


# ─────────────────────────────────────────────
# Prompts 2-5 — single pass or chunked
# ─────────────────────────────────────────────

def run_prompt_bulk(prompt_num: int, committee: str, data: dict, model: str):
    cfg = PROMPTS[prompt_num]
    reports_dir = VAULT_ROOT / committee / "Reports"
    audit_dir = reports_dir / "_audit" / f"p{prompt_num}"
    reports_dir.mkdir(parents=True, exist_ok=True)

    if cfg.get("requires_transcripts") and not data["has_transcripts"]:
        print(f"  NOTE: No transcripts for {committee}. Running on summaries only (results will be limited).")

    file_contents = data["all_text"]
    overhead = estimate_tokens(cfg["prompt"]) + estimate_tokens(cfg["system"]) + 2000
    content_tokens = estimate_tokens(file_contents)
    total = content_tokens + overhead
    print(f"  Content ~{content_tokens:,} tok | overhead ~{overhead:,} tok | total ~{total:,}")

    if total <= MAX_CONTEXT_TOKENS:
        # ── Single call ──
        prompt = cfg["prompt"].format(
            committee=committee,
            start_date=data["start_date"],
            end_date=data["end_date"],
            file_contents=file_contents,
        )
        result = call_api(cfg["system"], prompt, model, audit_dir, "full")
    else:
        # ── Chunked ──
        result = _run_chunked(cfg, committee, data, model, audit_dir)

    if not result:
        print("  ✗ No result.")
        return

    report = _header(cfg["name"], committee, data) + result
    out = reports_dir / cfg["filename"]
    out.write_text(report, encoding="utf-8")
    print(f"  ✅ {out}")


def _run_chunked(cfg: dict, committee: str, data: dict, model: str, audit_dir: Path) -> str | None:
    """Split meetings into context-sized chunks, analyse each, then synthesise."""

    budget = MAX_CONTEXT_TOKENS - estimate_tokens(cfg["prompt"]) - estimate_tokens(cfg["system"]) - 5000

    chunks: list[str] = []
    cur_parts: list[str] = []
    cur_tok = 0

    for d in data["dates"]:
        block = ""
        if d in data["summaries"]:
            block += f"=== SUMMARY: {d} ===\n{data['summaries'][d]}\n\n"
        if d in data["transcripts"]:
            block += f"=== TRANSCRIPT: {d} ===\n{data['transcripts'][d]}\n\n"
        btok = estimate_tokens(block)

        if cur_tok + btok > budget and cur_parts:
            chunks.append("\n".join(cur_parts))
            cur_parts = [block]
            cur_tok = btok
        else:
            cur_parts.append(block)
            cur_tok += btok

    if cur_parts:
        chunks.append("\n".join(cur_parts))

    print(f"  Chunked into {len(chunks)} parts")

    results: list[str] = []
    for i, chunk in enumerate(chunks, 1):
        print(f"  ▸ Chunk {i}/{len(chunks)}")
        prompt = cfg["prompt"].format(
            committee=committee,
            start_date=data["start_date"],
            end_date=data["end_date"],
            file_contents=chunk,
        )
        r = call_api(cfg["system"], prompt, model, audit_dir, f"chunk_{i}")
        if r:
            results.append(r)
        time.sleep(RATE_LIMIT_DELAY)

    if len(results) == 1:
        return results[0]

    if len(results) > 1:
        print(f"  ▸ Synthesising {len(results)} chunks")
        merged = "\n\n---\n\n".join(
            f"=== PART {i+1} ===\n{r}" for i, r in enumerate(results)
        )
        synth_prompt = (
            f"You produced {len(results)} partial analyses of the {committee} committee. "
            "Synthesise them into a single cohesive report. Resolve contradictions, merge "
            "attendance data, deduplicate, and produce the final unified analysis.\n\n"
            + merged
        )
        return call_api(cfg["system"], synth_prompt, model, audit_dir, "synthesis")

    return None


# ─────────────────────────────────────────────
# Helpers
# ─────────────────────────────────────────────

def _header(title: str, committee: str, data: dict) -> str:
    return (
        f"# {title}\n\n"
        f"**Committee:** {committee}  \n"
        f"**Period:** {data['start_date']} → {data['end_date']}  \n"
        f"**Meetings:** {len(data['dates'])}  \n"
        f"**Transcripts available:** {'Yes' if data['has_transcripts'] else 'No — analysis based on summaries only (known to be unreliable)'}  \n"
        f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}  \n\n---\n\n"
    )


# ─────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────

def run(committee: str, prompt_num: int, model: str):
    print(f"\n{'━'*60}")
    print(f"  {committee} │ Prompt {prompt_num}: {PROMPTS[prompt_num]['name']}")
    print(f"{'━'*60}")

    data = load_committee_files(committee)
    if not data:
        return

    s = len(data["summaries"])
    t = len(data["transcripts"])
    print(f"  {s} summaries, {t} transcripts  │  {data['start_date']}→{data['end_date']}  │  ~{data['total_tokens']:,} tok")

    if prompt_num == 1:
        run_prompt_1(committee, data, model)
    else:
        run_prompt_bulk(prompt_num, committee, data, model)


def main():
    ap = argparse.ArgumentParser(description="Intersect Committee Performance Analysis")
    ap.add_argument("--committee", required=True, help=f"{', '.join(COMMITTEES)}, or 'all'")
    ap.add_argument("--prompt", required=True, help="1-5, comma-separated, or 'all'")
    ap.add_argument("--model", default=MODEL)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    model = args.model

    # Parse committees
    if args.committee.lower() == "all":
        committees = COMMITTEES
    else:
        committees = [c.strip().upper() for c in args.committee.split(",")]
        for c in committees:
            if c not in COMMITTEES:
                sys.exit(f"Unknown committee '{c}'. Valid: {', '.join(COMMITTEES)}")

    # Parse prompts
    if args.prompt.lower() == "all":
        prompts = [1, 2, 3, 4, 5]
    else:
        prompts = [int(p.strip()) for p in args.prompt.split(",")]
        for p in prompts:
            if p not in PROMPTS:
                sys.exit(f"Unknown prompt {p}. Valid: 1-5")

    # Dry run
    if args.dry_run:
        print("\n══ DRY RUN ══\n")
        for c in committees:
            data = load_committee_files(c)
            if not data:
                continue
            for p in prompts:
                skip = ""
                if p == 1 and not data["has_transcripts"]:
                    skip = " ⚠ SKIP (no transcripts)"
                chunk = ""
                if data["total_tokens"] > MAX_CONTEXT_TOKENS:
                    chunk = " → will chunk"
                print(f"  {c} / P{p} ({PROMPTS[p]['name']})"
                      f"  │  {len(data['summaries'])}S {len(data['transcripts'])}T"
                      f"  │  ~{data['total_tokens']:,} tok{chunk}{skip}")
        return

    print(f"\nModel: {model}")
    print(f"Committees: {', '.join(committees)}")
    print(f"Prompts: {', '.join(str(p) for p in prompts)}")
    print(f"Vault: {VAULT_ROOT}\n")

    for c in committees:
        for p in prompts:
            run(c, p, model)
            time.sleep(RATE_LIMIT_DELAY)

    print(f"\n{'━'*60}")
    print(f"  DONE")
    print(f"{'━'*60}")


if __name__ == "__main__":
    main()
```
