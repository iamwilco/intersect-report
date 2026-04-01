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
    from dotenv import load_dotenv
    # Load .env from the same directory as this script
    load_dotenv(Path(__file__).resolve().parent / ".env", override=True)
except ImportError:
    pass  # dotenv optional — fall back to shell env

try:
    import anthropic
except ImportError:
    print("ERROR: pip install anthropic")
    sys.exit(1)

from config import (
    VAULT_ROOT, COMMITTEES, MODEL, MAX_CONTEXT_TOKENS,
    MAX_OUTPUT_TOKENS, CHARS_PER_TOKEN, RATE_LIMIT_DELAY,
    RATE_LIMIT_TPM, MAX_RETRIES, ELECTION_START,
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
    """Load all Summary + Transcript files for a committee.

    Filters out meetings before the committee's ELECTION_START date
    (if configured) so only the current election period is analysed.
    """

    transcripts_dir = VAULT_ROOT / committee / "Transcripts"
    if not transcripts_dir.exists():
        print(f"  ERROR: {transcripts_dir} does not exist")
        return None

    election_start = ELECTION_START.get(committee)

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

        # Skip pre-election meetings
        if election_start and date_str < election_start:
            continue

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

_client: anthropic.Anthropic | None = None

def _get_client() -> anthropic.Anthropic:
    """Reuse a single client across calls for connection pooling."""
    global _client
    if _client is None:
        _client = anthropic.Anthropic()
    return _client


def call_api(
    system: str,
    user_prompt: str,
    model: str,
    audit_dir: Path | None = None,
    audit_name: str = "call",
    cache_user_prefix: str | None = None,
) -> str | None:
    """Call the Anthropic API with prompt caching. Returns response text or None.

    Args:
        cache_user_prefix: Large text (e.g. file_contents) to cache as a prefix
            in the user message. Placed BEFORE user_prompt so the model reads
            data first, then the analysis instructions. Cached across calls
            that share the same system prompt + prefix.
    """

    client = _get_client()

    all_user_text = (cache_user_prefix or "") + user_prompt
    input_tokens_est = estimate_tokens(system + all_user_text)
    print(f"    Est. input tokens: ~{input_tokens_est:,}")

    if input_tokens_est > MAX_CONTEXT_TOKENS:
        print(f"    WARNING: Input ({input_tokens_est:,}) exceeds limit ({MAX_CONTEXT_TOKENS:,})")
        return None

    # ── Build messages with cache breakpoints ──
    system_msg = [
        {"type": "text", "text": system, "cache_control": {"type": "ephemeral"}},
    ]

    if cache_user_prefix:
        user_content = [
            {"type": "text", "text": cache_user_prefix, "cache_control": {"type": "ephemeral"}},
            {"type": "text", "text": user_prompt},
        ]
    else:
        user_content = user_prompt

    # ── Audit: save input ──
    if audit_dir:
        audit_dir.mkdir(parents=True, exist_ok=True)
        meta = {
            "timestamp": datetime.now().isoformat(),
            "model": model,
            "system_hash": hashlib.md5(system.encode()).hexdigest(),
            "user_chars": len(all_user_text),
            "est_input_tokens": input_tokens_est,
            "caching": cache_user_prefix is not None,
            "cache_prefix_chars": len(cache_user_prefix) if cache_user_prefix else 0,
        }
        (audit_dir / f"{audit_name}_meta_in.json").write_text(
            json.dumps(meta, indent=2)
        )
        (audit_dir / f"{audit_name}_full_input.txt").write_text(
            f"=== SYSTEM ===\n{system}\n\n=== USER ===\n{all_user_text}"
        )

    # ── API call with retry on 429 (streaming for Opus compatibility) ──
    t0 = time.time()
    text = None
    input_tokens = 0
    output_tokens = 0
    cache_read_tokens = 0
    cache_creation_tokens = 0
    stop_reason = None
    resp_model = model

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            collected = []
            with client.messages.stream(
                model=model,
                max_tokens=MAX_OUTPUT_TOKENS,
                system=system_msg,
                messages=[{"role": "user", "content": user_content}],
            ) as stream:
                for event_text in stream.text_stream:
                    collected.append(event_text)
                final = stream.get_final_message()
                input_tokens = final.usage.input_tokens
                output_tokens = final.usage.output_tokens
                cache_read_tokens = getattr(final.usage, "cache_read_input_tokens", 0) or 0
                cache_creation_tokens = getattr(final.usage, "cache_creation_input_tokens", 0) or 0
                stop_reason = final.stop_reason
                resp_model = final.model
            text = "".join(collected)
            break
        except anthropic.RateLimitError as exc:
            wait = min(30 * attempt, 120)
            print(f"    Rate limited (attempt {attempt}/{MAX_RETRIES}). Waiting {wait}s...")
            time.sleep(wait)
        except anthropic.APIError as exc:
            print(f"    FAIL: API error: {exc}")
            return None

    if text is None:
        print(f"    FAIL: Exhausted {MAX_RETRIES} retries.")
        return None

    elapsed = time.time() - t0

    # ── Log with cache info ──
    cache_info = ""
    if cache_read_tokens:
        cache_info = f"  cache_read={cache_read_tokens:,}"
    elif cache_creation_tokens:
        cache_info = f"  cache_write={cache_creation_tokens:,}"
    print(f"    OK {elapsed:.1f}s  in={input_tokens:,}  out={output_tokens:,}{cache_info}")

    if stop_reason == "max_tokens":
        print(f"    WARNING: Output TRUNCATED — increase MAX_OUTPUT_TOKENS in config.py")

    # ── Audit: save output ──
    if audit_dir:
        out_meta = {
            "timestamp": datetime.now().isoformat(),
            "elapsed_s": round(elapsed, 2),
            "input_tokens": input_tokens,
            "output_tokens": output_tokens,
            "cache_read_input_tokens": cache_read_tokens,
            "cache_creation_input_tokens": cache_creation_tokens,
            "model": resp_model,
            "stop_reason": stop_reason,
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

        print(f"  > Meeting {pair['date']}")
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
        print("  FAIL: No meeting analyses produced.")
        return

    # Phase 2 — synthesis
    print(f"  > Synthesis ({len(findings)} meetings)")
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
    print(f"  DONE: {out}")


# ─────────────────────────────────────────────
# Prompts 2-5 — single pass or chunked
# ─────────────────────────────────────────────

def run_prompt_bulk(prompt_num: int, committee: str, data: dict, model: str):
    cfg = PROMPTS[prompt_num]
    reports_dir = VAULT_ROOT / committee / "Reports"
    audit_dir = reports_dir / "_audit" / f"p{prompt_num}"
    reports_dir.mkdir(parents=True, exist_ok=True)

    if cfg.get("requires_transcripts") and not data["has_transcripts"]:
        print(f"  NOTE: No transcripts for {committee}. Running on summaries only.")

    file_contents = data["all_text"]
    overhead = estimate_tokens(cfg["prompt"]) + estimate_tokens(cfg["system"]) + 2000
    content_tokens = estimate_tokens(file_contents)
    total = content_tokens + overhead
    print(f"  Content ~{content_tokens:,} tok | overhead ~{overhead:,} tok | total ~{total:,}")

    # Chunk only if content exceeds context window
    needs_chunking = total > MAX_CONTEXT_TOKENS
    if RATE_LIMIT_TPM and total > RATE_LIMIT_TPM:
        needs_chunking = True

    if not needs_chunking:
        # ── Single call with cached file contents ──
        instructions = cfg["prompt"].format(
            committee=committee,
            start_date=data["start_date"],
            end_date=data["end_date"],
            total_meetings=len(data["dates"]),
            file_contents="",
        )
        result = call_api(
            cfg["system"], instructions, model, audit_dir, "full",
            cache_user_prefix=file_contents,
        )
    else:
        # ── Chunked ──
        result = _run_chunked(cfg, committee, data, model, audit_dir)

    if not result:
        print("  FAIL: No result.")
        return

    report = _header(cfg["name"], committee, data) + result
    out = reports_dir / cfg["filename"]
    out.write_text(report, encoding="utf-8")
    print(f"  DONE: {out}")


def _run_chunked(cfg: dict, committee: str, data: dict, model: str, audit_dir: Path) -> str | None:
    """Split meetings into context-sized chunks, analyse each, then synthesise."""

    prompt_overhead = estimate_tokens(cfg["prompt"]) + estimate_tokens(cfg["system"]) + 5000
    context_budget = MAX_CONTEXT_TOKENS - prompt_overhead
    if RATE_LIMIT_TPM:
        rate_budget = RATE_LIMIT_TPM - prompt_overhead
        budget = min(context_budget, rate_budget)
    else:
        budget = context_budget

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

    # Build the instructions once (without file_contents)
    instructions = cfg["prompt"].format(
        committee=committee,
        start_date=data["start_date"],
        end_date=data["end_date"],
        total_meetings=len(data["dates"]),
        file_contents="",
    )

    results: list[str] = []
    for i, chunk in enumerate(chunks, 1):
        print(f"  > Chunk {i}/{len(chunks)}")
        r = call_api(
            cfg["system"], instructions, model, audit_dir, f"chunk_{i}",
            cache_user_prefix=chunk,
        )
        if r:
            results.append(r)
        # Wait between chunks — shorter if relying on retry logic for rate limits
        if i < len(chunks):
            time.sleep(RATE_LIMIT_DELAY)

    if len(results) == 1:
        return results[0]

    if len(results) > 1:
        print(f"  > Synthesising {len(results)} chunks")
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
# Batch API mode (50% off)
# ─────────────────────────────────────────────

def _make_system_msg(system_text: str) -> list[dict]:
    return [{"type": "text", "text": system_text, "cache_control": {"type": "ephemeral"}}]


def _make_user_content(prompt: str, cache_prefix: str | None = None):
    if cache_prefix:
        return [
            {"type": "text", "text": cache_prefix, "cache_control": {"type": "ephemeral"}},
            {"type": "text", "text": prompt},
        ]
    return prompt


def _build_bulk_chunks(cfg: dict, data: dict) -> list[str]:
    """Build chunk list for a bulk prompt. Returns a list of 1+ content strings."""
    file_contents = data["all_text"]
    overhead = estimate_tokens(cfg["prompt"]) + estimate_tokens(cfg["system"]) + 2000
    content_tokens = estimate_tokens(file_contents)
    total = content_tokens + overhead

    needs_chunking = total > MAX_CONTEXT_TOKENS
    if RATE_LIMIT_TPM and total > RATE_LIMIT_TPM:
        needs_chunking = True

    if not needs_chunking:
        return [file_contents]

    # Chunk by meeting date
    prompt_overhead = estimate_tokens(cfg["prompt"]) + estimate_tokens(cfg["system"]) + 5000
    context_budget = MAX_CONTEXT_TOKENS - prompt_overhead
    if RATE_LIMIT_TPM:
        budget = min(context_budget, RATE_LIMIT_TPM - prompt_overhead)
    else:
        budget = context_budget

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

    return chunks


def run_batch(committees: list[str], prompts: list[int], model: str):
    """Submit all analysis requests via the Batch API (50% off)."""
    from anthropic.types.message_create_params import MessageCreateParamsNonStreaming
    from anthropic.types.messages.batch_create_params import Request

    client = _get_client()

    # ── Phase 1: build all independent requests ──
    phase1_requests: list[Request] = []
    # Track what we need to assemble reports later
    job_meta: dict[str, dict] = {}  # custom_id -> metadata

    all_data: dict[str, dict] = {}
    for committee in committees:
        data = load_committee_files(committee)
        if not data:
            continue
        all_data[committee] = data
        s = len(data["summaries"])
        t = len(data["transcripts"])
        print(f"  {committee}: {s}S {t}T | ~{data['total_tokens']:,} tok")

        for pnum in prompts:
            cfg = PROMPTS[pnum]

            if pnum == 1:
                if not data["has_transcripts"]:
                    print(f"    P1: SKIP (no transcripts)")
                    continue
                for pair in data["pairs"]:
                    if not pair["summary"] or not pair["transcript"]:
                        continue
                    prompt = cfg["per_meeting_prompt"].format(
                        committee=committee,
                        date=pair["date"],
                        summary=pair["summary"],
                        transcript=pair["transcript"],
                    )
                    cid = f"{committee}_p1_mtg_{pair['date']}"
                    phase1_requests.append(Request(
                        custom_id=cid,
                        params=MessageCreateParamsNonStreaming(
                            model=model,
                            max_tokens=MAX_OUTPUT_TOKENS,
                            system=_make_system_msg(cfg["system"]),
                            messages=[{"role": "user", "content": prompt}],
                        ),
                    ))
                    job_meta[cid] = {
                        "committee": committee, "prompt": pnum,
                        "phase": "meeting", "date": pair["date"],
                    }
                print(f"    P1: {sum(1 for k in job_meta if k.startswith(f'{committee}_p1_mtg'))} meeting requests")
            else:
                chunks = _build_bulk_chunks(cfg, data)
                instructions = cfg["prompt"].format(
                    committee=committee,
                    start_date=data["start_date"],
                    end_date=data["end_date"],
                    total_meetings=len(data["dates"]),
                    file_contents="",
                )
                for i, chunk in enumerate(chunks):
                    suffix = "full" if len(chunks) == 1 else f"chunk_{i+1}"
                    cid = f"{committee}_p{pnum}_{suffix}"
                    phase1_requests.append(Request(
                        custom_id=cid,
                        params=MessageCreateParamsNonStreaming(
                            model=model,
                            max_tokens=MAX_OUTPUT_TOKENS,
                            system=_make_system_msg(cfg["system"]),
                            messages=[{"role": "user",
                                       "content": _make_user_content(instructions, chunk)}],
                        ),
                    ))
                    job_meta[cid] = {
                        "committee": committee, "prompt": pnum,
                        "phase": "full" if len(chunks) == 1 else "chunk",
                        "chunk_index": i, "total_chunks": len(chunks),
                    }
                print(f"    P{pnum}: {len(chunks)} request(s)")

    if not phase1_requests:
        print("No requests to submit.")
        return

    # ── Submit phase 1 ──
    print(f"\nSubmitting {len(phase1_requests)} requests to Batch API...")
    batch = client.messages.batches.create(requests=phase1_requests)
    print(f"  Batch ID: {batch.id}")

    # ── Poll for completion ──
    phase1_results = _poll_batch(client, batch.id)
    if phase1_results is None:
        return

    # ── Collect results and build synthesis requests ──
    results_by_id: dict[str, str] = {}
    for result in phase1_results:
        cid = result.custom_id
        if result.result.type == "succeeded":
            text = result.result.message.content[0].text
            results_by_id[cid] = text
            usage = result.result.message.usage
            cache_read = getattr(usage, "cache_read_input_tokens", 0) or 0
            cache_info = f" cache_read={cache_read}" if cache_read else ""
            print(f"    OK {cid}: in={usage.input_tokens:,} out={usage.output_tokens:,}{cache_info}")
        else:
            print(f"    FAIL {cid}: {result.result.type}")

    # ── Phase 2: synthesis requests ──
    phase2_requests: list[Request] = []
    phase2_meta: dict[str, dict] = {}

    for committee in committees:
        if committee not in all_data:
            continue
        data = all_data[committee]

        for pnum in prompts:
            cfg = PROMPTS[pnum]

            if pnum == 1:
                # Collect per-meeting findings
                findings = []
                for pair in data["pairs"]:
                    cid = f"{committee}_p1_mtg_{pair['date']}"
                    if cid in results_by_id:
                        findings.append(f"### {pair['date']}\n\n{results_by_id[cid]}")

                if not findings:
                    continue

                synth_prompt = cfg["synthesis_prompt"].format(
                    committee=committee,
                    all_findings="\n\n---\n\n".join(findings),
                )
                cid = f"{committee}_p1_synthesis"
                phase2_requests.append(Request(
                    custom_id=cid,
                    params=MessageCreateParamsNonStreaming(
                        model=model,
                        max_tokens=MAX_OUTPUT_TOKENS,
                        system=_make_system_msg(cfg["system"]),
                        messages=[{"role": "user", "content": synth_prompt}],
                    ),
                ))
                phase2_meta[cid] = {
                    "committee": committee, "prompt": pnum, "phase": "synthesis",
                }
            else:
                # Check if this prompt was chunked
                chunk_cids = [k for k in results_by_id
                              if k.startswith(f"{committee}_p{pnum}_chunk_")]
                if len(chunk_cids) > 1:
                    chunk_results = [results_by_id[k] for k in sorted(chunk_cids)]
                    merged = "\n\n---\n\n".join(
                        f"=== PART {i+1} ===\n{r}" for i, r in enumerate(chunk_results)
                    )
                    synth_prompt = (
                        f"You produced {len(chunk_results)} partial analyses of the "
                        f"{committee} committee. Synthesise them into a single cohesive "
                        "report. Resolve contradictions, merge attendance data, "
                        "deduplicate, and produce the final unified analysis.\n\n"
                        + merged
                    )
                    cid = f"{committee}_p{pnum}_synthesis"
                    phase2_requests.append(Request(
                        custom_id=cid,
                        params=MessageCreateParamsNonStreaming(
                            model=model,
                            max_tokens=MAX_OUTPUT_TOKENS,
                            system=_make_system_msg(cfg["system"]),
                            messages=[{"role": "user", "content": synth_prompt}],
                        ),
                    ))
                    phase2_meta[cid] = {
                        "committee": committee, "prompt": pnum, "phase": "synthesis",
                    }

    # Submit phase 2 if needed
    if phase2_requests:
        print(f"\nSubmitting {len(phase2_requests)} synthesis requests...")
        batch2 = client.messages.batches.create(requests=phase2_requests)
        print(f"  Batch ID: {batch2.id}")
        phase2_results = _poll_batch(client, batch2.id)
        if phase2_results:
            for result in phase2_results:
                if result.result.type == "succeeded":
                    results_by_id[result.custom_id] = result.result.message.content[0].text
                    print(f"    OK {result.custom_id}")
                else:
                    print(f"    FAIL {result.custom_id}: {result.result.type}")

    # ── Assemble and write reports ──
    print("\nAssembling reports...")
    for committee in committees:
        if committee not in all_data:
            continue
        data = all_data[committee]
        reports_dir = VAULT_ROOT / committee / "Reports"
        audit_dir = reports_dir / "_audit"
        reports_dir.mkdir(parents=True, exist_ok=True)

        for pnum in prompts:
            cfg = PROMPTS[pnum]

            if pnum == 1:
                findings = []
                for pair in data["pairs"]:
                    cid = f"{committee}_p1_mtg_{pair['date']}"
                    if cid in results_by_id:
                        findings.append(f"### {pair['date']}\n\n{results_by_id[cid]}")
                if not findings:
                    continue

                report = _header(cfg["name"], committee, data)
                report += "\n\n---\n\n".join(findings)
                synth_cid = f"{committee}_p1_synthesis"
                if synth_cid in results_by_id:
                    report += "\n\n---\n\n## Overall Patterns\n\n" + results_by_id[synth_cid]
            else:
                # Check for single result or synthesised chunks
                full_cid = f"{committee}_p{pnum}_full"
                synth_cid = f"{committee}_p{pnum}_synthesis"

                if full_cid in results_by_id:
                    result_text = results_by_id[full_cid]
                elif synth_cid in results_by_id:
                    result_text = results_by_id[synth_cid]
                else:
                    # Single chunk, no synthesis needed
                    chunk_cids = sorted(k for k in results_by_id
                                        if k.startswith(f"{committee}_p{pnum}_chunk_"))
                    if len(chunk_cids) == 1:
                        result_text = results_by_id[chunk_cids[0]]
                    else:
                        print(f"  {committee} P{pnum}: no results")
                        continue

                report = _header(cfg["name"], committee, data) + result_text

            out = reports_dir / cfg["filename"]
            out.write_text(report, encoding="utf-8")
            print(f"  DONE: {out}")

            # Save batch results as audit
            pdir = audit_dir / f"p{pnum}"
            pdir.mkdir(parents=True, exist_ok=True)
            for cid, text in results_by_id.items():
                if cid.startswith(f"{committee}_p{pnum}_"):
                    (pdir / f"{cid.split(f'_p{pnum}_')[1]}_output.md").write_text(text)

    print(f"\n{'=' * 60}")
    print("  BATCH DONE")
    print(f"{'=' * 60}")


def _poll_batch(client, batch_id: str, poll_interval: int = 30):
    """Poll a batch until completion. Returns results or None."""
    while True:
        batch = client.messages.batches.retrieve(batch_id)
        counts = batch.request_counts
        total = counts.succeeded + counts.errored + counts.expired + counts.canceled
        pending = counts.processing
        print(f"  Status: {batch.processing_status} | done={total} processing={pending}")

        if batch.processing_status == "ended":
            if counts.errored:
                print(f"  WARNING: {counts.errored} requests errored")
            if counts.expired:
                print(f"  WARNING: {counts.expired} requests expired")
            return list(client.messages.batches.results(batch_id))

        time.sleep(poll_interval)


# ─────────────────────────────────────────────
# Helpers
# ─────────────────────────────────────────────

def _header(title: str, committee: str, data: dict) -> str:
    return (
        f"# {title}\n\n"
        f"**Committee:** {committee}  \n"
        f"**Period:** {data['start_date']} -> {data['end_date']}  \n"
        f"**Meetings:** {len(data['dates'])}  \n"
        f"**Transcripts available:** {'Yes' if data['has_transcripts'] else 'No — analysis based on summaries only (known to be unreliable)'}  \n"
        f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}  \n\n---\n\n"
    )


# ─────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────

def run(committee: str, prompt_num: int, model: str):
    sep = "=" * 60
    print(f"\n{sep}")
    print(f"  {committee} | Prompt {prompt_num}: {PROMPTS[prompt_num]['name']}")
    print(f"{sep}")

    data = load_committee_files(committee)
    if not data:
        return

    s = len(data["summaries"])
    t = len(data["transcripts"])
    print(f"  {s} summaries, {t} transcripts  |  {data['start_date']}->{data['end_date']}  |  ~{data['total_tokens']:,} tok")

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
    ap.add_argument("--batch", action="store_true",
                    help="Use Batch API (50%% off, results in ~1h)")
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
        print("\n== DRY RUN ==\n")
        for c in committees:
            data = load_committee_files(c)
            if not data:
                continue
            for p in prompts:
                skip = ""
                if p == 1 and not data["has_transcripts"]:
                    skip = " [SKIP: no transcripts]"
                chunk = ""
                if data["total_tokens"] > MAX_CONTEXT_TOKENS:
                    chunk = " -> will chunk"
                print(f"  {c} / P{p} ({PROMPTS[p]['name']})"
                      f"  |  {len(data['summaries'])}S {len(data['transcripts'])}T"
                      f"  |  ~{data['total_tokens']:,} tok{chunk}{skip}")
        return

    mode = "batch" if args.batch else "streaming"
    print(f"\nModel: {model}")
    print(f"Mode: {mode}")
    print(f"Committees: {', '.join(committees)}")
    print(f"Prompts: {', '.join(str(p) for p in prompts)}")
    print(f"Vault: {VAULT_ROOT}\n")

    if args.batch:
        run_batch(committees, prompts, model)
        print(f"\n{'=' * 60}")
        print(f"  DONE")
        print(f"{'=' * 60}")
        return

    for c in committees:
        for p in prompts:
            run(c, p, model)
            time.sleep(RATE_LIMIT_DELAY)

    print(f"\n{'=' * 60}")
    print(f"  DONE")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
