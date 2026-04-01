# Intersect Committee Reports

Independent, evidence-based analysis of **Intersect MBO committee governance** — examining whether official records accurately reflect what was discussed, how elected members participated, whether commitments were followed through, and whether non-elected staff stayed within their defined roles.

## Live site

**[https://iamwilco.github.io/intersect-report/](https://iamwilco.github.io/intersect-report/)**

## Committees analysed

| Committee | Meetings | Transcripts | Reports | Key finding |
|---|---|---|---|---|
| **TSC** — Technical Steering Committee | 23 | Yes | 5/5 | ~54% delivery rate; strong technical output undermined by administrative dysfunction |
| **MCC** — Membership & Community Committee | 11 | Yes | 5/5 | 36% delivery rate; committee vote overridden, secretary boundary violations |
| **GMC** — Growth & Marketing Committee | 14 | Yes | 5/5 | 14.5% delivery rate; marketing white paper and KPI framework never delivered |
| CCC — Constitution & Civics Committee | 12 | Partial | Pending | |
| OSC — Open Source Committee | 14 | Yes | Pending | |
| CBC — Community & Budget Committee | 18 | No | Pending | |
| CPC — Civics & Participation Committee | 13 | No | Pending | |
| ISC — Intersect Steering Committee | 21 | No | Pending | |

## The five reports

Each committee is analysed through five structured prompts:

1. **Summaries vs. Transcripts** — Forensic comparison of official summaries against raw transcripts. Identifies fabricated decisions, invented action items, tone laundering, and omitted conflicts. Requires transcripts.
2. **Member Participation** — Attendance grid for every elected member, speaking frequency, substantive contributions, between-meeting work, and ranked effectiveness.
3. **Leadership Assessment** — Chair, Vice Chair, and Secretary evaluated on facilitation, decision-making, preparation, conflict management, boundary respect, and strategic direction.
4. **Promises vs. Reality** — Every commitment tracked from source to outcome. Delivery rate calculated. Most and least reliable promise-keepers identified.
5. **Critical Observations** — Free-form governance report covering red flags, cultural dynamics, information asymmetry, power plays, recurring failures, and community engagement.

## How it works

Committee meeting transcripts and summaries are processed through a Python pipeline using the Anthropic API (Claude Opus). Each committee's source material is fed through the five analysis prompts, producing independent reports with full audit trails.

The pipeline supports:
- **Prompt caching** — identical content across prompts is cached, reducing cost by up to 90% on repeated input
- **Auto-chunking** — large committees that exceed the context window are automatically split, analysed in parts, and synthesised
- **Batch API** — `--batch` flag for 50% off all token costs (results in ~1 hour)
- **Audit logging** — every API call logged with exact input, output, and token counts

### Running the pipeline

```bash
cd backend/
pip install anthropic python-dotenv
export ANTHROPIC_API_KEY="sk-ant-..."

# Dry run (no API calls)
python committee_analysis.py --committee TSC --prompt all --dry-run

# Run all prompts for one committee
python committee_analysis.py --committee TSC --prompt all

# Batch mode (50% cheaper, ~1 hour)
python committee_analysis.py --committee TSC --prompt all --batch

# Single prompt
python committee_analysis.py --committee MCC --prompt 2
```

### Regenerating site data

```bash
cd backend/
python generate_site_data.py
```

## Repository structure

```
docs/                    # Static site (GitHub Pages serves from here)
  index.html             # Main dashboard with all committees
  style.css              # Shared stylesheet
  data/                  # JSON data files per committee
  tsc/                   # TSC report pages (7 pages)
  mcc/                   # MCC report pages (9 pages)
  gmc/                   # GMC report pages (7 pages)

backend/                 # Analysis pipeline
  committee_analysis.py  # Main pipeline script
  prompts.py             # The five analysis prompts
  config.py              # Configuration (paths, model, limits)
  generate_site_data.py  # Generates JSON from reports for the site

Intersect/               # Source data & generated reports
  TSC/Transcripts/       # 23 summaries + 23 transcripts
  MCC/Transcripts/       # 11 summaries + 11 transcripts
  GMC/Transcripts/       # 14 summaries + 14 transcripts
  */Reports/             # Generated markdown reports (5 per committee)
```

## Methodology

All reports are based on official meeting transcripts and summaries sourced from Intersect's public documentation channels. Every factual claim is traceable to a specific transcript passage. Participation data is derived from transcript evidence — attendance lists in summaries are cross-referenced against actual speaking records.

These reports represent independent community analysis and are not affiliated with Intersect or any official body.

## Cost

With prompt caching and batch API, the full five-report analysis costs approximately:
- **Small committee** (11 meetings, ~70K tokens): ~$2-3
- **Large committee** (23 meetings, ~350K tokens): ~$5-10
- **All 8 committees**: ~$30-50

All costs are for Claude Opus via the Anthropic API at batch pricing.
