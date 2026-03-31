"""
Configuration for the Committee Analysis Pipeline.
Edit paths and model settings here.
"""

from pathlib import Path

# ─────────────────────────────────────────────
# Paths
# ─────────────────────────────────────────────

# Root of the Obsidian vault's Intersect folder
# Each committee should have: {VAULT_ROOT}/{COMMITTEE}/Transcripts/
VAULT_ROOT = Path.home() / "Desktop" / "Intersect Research" / "Intersect"

# ─────────────────────────────────────────────
# Committees
# ─────────────────────────────────────────────

COMMITTEES = ["TSC", "CPC", "OSC", "GMC", "CCC", "CBC", "ISC", "MCC"]

# ─────────────────────────────────────────────
# Model settings
# ─────────────────────────────────────────────

# Default model. Override with --model flag.
# Options:
#   claude-sonnet-4-20250514   — good balance of quality/cost ($3/$15 per M tok)
#   claude-opus-4-20250514     — highest quality, ~5x cost ($15/$75 per M tok)
MODEL = "claude-sonnet-4-20250514"

# Context window budget (leave headroom from the 200K limit)
MAX_CONTEXT_TOKENS = 180_000

# Max output tokens per API call
# Increase if outputs are getting truncated (watch for "max_tokens" stop reason)
MAX_OUTPUT_TOKENS = 16_000

# Conservative chars-per-token estimate for budget calculations
CHARS_PER_TOKEN = 4

# Seconds to wait between API calls (rate limit courtesy)
RATE_LIMIT_DELAY = 1.5
