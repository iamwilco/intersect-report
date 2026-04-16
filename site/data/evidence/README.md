# Evidence Overlay

Human-curated overlay applied on top of AI-derived promise statuses. Each file is keyed by committee code (lowercase): `mcc.json`, `gmc.json`, etc.

## Workflow

1. Submission arrives via GitHub Issue (`evidence-submission` label) or email to chat@wilco.space.
2. Reviewer (Wilco) verifies the artifact actually delivers on the promise.
3. If accepted: add an entry to the committee's overlay file in this directory and merge the PR. The site rebuild picks it up automatically.
4. If rejected: close the issue with a reason. No file change.

## Schema

```json
{
  "promises": {
    "<promise_num>": {
      "verified_status": "verified-delivered" | "disputed",
      "submissions": [
        {
          "url": "https://...",
          "type": "recording" | "doc" | "pr" | "screenshot" | "other",
          "submitted_by": "Name — Role",
          "submitted_at": "2026-04-15",
          "note": "optional reviewer note",
          "accepted": true
        }
      ]
    }
  }
}
```

Only submissions with `"accepted": true` are rendered on the site. Rejected submissions can be kept in the file for audit trail (set `accepted: false`) or omitted entirely.

## Example

```json
{
  "promises": {
    "7": {
      "verified_status": "verified-delivered",
      "submissions": [
        {
          "url": "https://youtube.com/watch?v=...",
          "type": "recording",
          "submitted_by": "Wilco — MCC observer",
          "submitted_at": "2026-04-15",
          "note": "ClickUp 101 workshop, run 2026-02-10. Satisfies promise #7.",
          "accepted": true
        }
      ]
    }
  }
}
```
