"""
Configuration for Intersect Committee Performance Analysis Pipeline.
Edit these values to match your local environment.
"""

from pathlib import Path

# ─────────────────────────────────────────────
# Vault / data paths
# ─────────────────────────────────────────────

# Root of your Intersect vault. Each committee should have a subfolder here
# with a Transcripts/ directory containing dated .md files.
VAULT_ROOT = Path.home() / "Desktop" / "wilco-os" / "projects" / "intersect-reports" / "Intersect"

# Where the frontend site lives (for generate_site_data.py output)
SITE_DATA_DIR = Path.home() / "Desktop" / "wilco-os" / "projects" / "intersect-reports" / "site" / "data"

# ─────────────────────────────────────────────
# Committees
# ─────────────────────────────────────────────

COMMITTEES = [
    "MCC",   # Membership & Community Committee
    "TSC",   # Technical Steering Committee
    "CPC",   # Civics & Participation Committee
    "OSC",   # Open Source Committee
    "GMC",   # Growth & Marketing Committee
    "CCC",   # Constitution & Civics Committee
    "CBC",   # Community & Budget Committee
    "ISC",   # Intersect Steering Committee
]

COMMITTEE_FULL_NAMES = {
    "MCC": "Membership & Community Committee",
    "TSC": "Technical Steering Committee",
    "CPC": "Civics & Participation Committee",
    "OSC": "Open Source Committee",
    "GMC": "Growth & Marketing Committee",
    "CCC": "Constitution & Civics Committee",
    "CBC": "Community & Budget Committee",
    "ISC": "Intersect Steering Committee",
}

# ─────────────────────────────────────────────
# Model & API settings
# ─────────────────────────────────────────────

MODEL = "claude-opus-4-20250514"

# Context window budget (leave headroom below true limit)
MAX_CONTEXT_TOKENS = 180_000

# Maximum output tokens per API call
MAX_OUTPUT_TOKENS = 16_000

# Rough chars-per-token for estimation (Claude averages ~3.5-4)
CHARS_PER_TOKEN = 4

# Seconds to wait between API calls (rate-limit safety)
RATE_LIMIT_DELAY = 2

# Rate limit: max input tokens per minute for your API tier.
# Set to 0 to disable rate-based chunking (recommended — the retry logic
# handles 429s automatically). Only set a value if you want to proactively
# chunk below your tier's limit.
RATE_LIMIT_TPM = 0

# Max retries on 429 rate-limit errors
MAX_RETRIES = 5
