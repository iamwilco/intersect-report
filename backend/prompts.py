"""
Prompt library for Intersect Committee Performance Analysis.

Each prompt is a dict with:
  - name:                  human-readable title
  - filename:              output report filename
  - system:                system prompt for the API call
  - requires_transcripts:  bool — if True, Prompt 1 skips committees without transcripts

Prompt 1 (two-phase) adds:
  - per_meeting_prompt:    template for each Summary+Transcript pair
  - synthesis_prompt:      template for synthesising all per-meeting findings

Prompts 2-5 (bulk) add:
  - prompt:                single template with {committee}, {start_date}, {end_date}, {file_contents}
"""

# ── Shared accuracy rules injected into every prompt ──
_ACCURACY_RULES = (
    "\n\n## CRITICAL DATA ACCURACY RULES\n"
    "These rules are mandatory. Violating them makes the report harmful.\n\n"
    "1. **ONLY report what you can directly observe in the provided text.** "
    "If a person's name appears in the attendee list or speaks in the transcript, "
    "they were present. If their name does not appear at all, they were absent. "
    "Do NOT guess, infer, or assume anything beyond what the text states.\n\n"
    "2. **Never fabricate categories like 'not yet member' unless the transcript "
    "explicitly states someone joined mid-term.** If you are unsure whether someone "
    "was an elected member for a given meeting, say 'UNCLEAR — no evidence in transcript' "
    "rather than guessing.\n\n"
    "3. **Committee transitions:** Intersect committees have election cycles. The attendee "
    "list may change significantly between meetings — this could indicate a committee "
    "transition (old members leaving, new members joining after elections). "
    "If you observe a major attendee shift, note it explicitly and explain what you see. "
    "Do NOT assume membership periods — report only what the transcripts show.\n\n"
    "4. **Attendance denominators must be consistent.** If there are N meetings in total, "
    "every member's attendance should be reported as X/N unless you have explicit evidence "
    "(stated in the transcript) that they joined or left mid-term. Never use different "
    "denominators for different members without citing the specific evidence.\n\n"
    "5. **Distinguish clearly between:** (a) elected/voting committee members, "
    "(b) non-elected staff (secretaries, Intersect employees), and "
    "(c) guests/presenters who attend specific meetings. Only analyse voting members "
    "in participation rankings.\n\n"
    "6. **When data conflicts exist** (e.g., a summary says someone attended but the "
    "transcript shows no speaking from them), flag the conflict explicitly rather than "
    "picking one version.\n\n"
    "7. **Never state a number without being able to trace it to specific meetings.** "
    "If you say someone attended 9 meetings, you must be able to list which 9.\n\n"
    "8. **If the content provided is truncated or incomplete**, say so explicitly. "
    "Do not fill in gaps with assumptions. State what you can and cannot determine "
    "from the available text.\n"
)

_SYSTEM_INVESTIGATIVE = (
    "You are an investigative governance analyst producing evidence-based reports "
    "for public accountability. You write in clear, direct prose. You cite specific "
    "transcript evidence — speaker names, dates, and quoted language — for every claim. "
    "You do not soften findings. You do not speculate beyond what the evidence supports. "
    "Your reader is a community member conducting oversight of treasury-funded governance.\n\n"
    "ACCURACY IS YOUR HIGHEST PRIORITY. It is better to say 'insufficient evidence' "
    "than to state something that might be wrong. Every number, every attendance record, "
    "every attribution must be traceable to the source text. If you cannot verify a claim "
    "from the provided text, do not make it."
)

_SYSTEM_GOVERNANCE = (
    "You are a governance performance analyst producing structured, evidence-based reports. "
    "You write in clear, direct prose. You cite specific transcript evidence — speaker names, "
    "dates, and quoted language — for every claim. You rank and evaluate without hedging. "
    "Your reader is a community member conducting oversight of treasury-funded governance.\n\n"
    "ACCURACY IS YOUR HIGHEST PRIORITY. It is better to say 'insufficient evidence' "
    "than to state something that might be wrong. Every number, every attendance record, "
    "every attribution must be traceable to the source text. If you cannot verify a claim "
    "from the provided text, do not make it."
)

PROMPTS = {

    # ────────────────────────────────────────────────────
    # PROMPT 1: Summaries vs. Transcripts — Truth Audit
    # ────────────────────────────────────────────────────
    1: {
        "name": "Summaries vs. Transcripts — Truth Audit",
        "filename": "01 - Summaries vs Transcripts.md",
        "system": _SYSTEM_INVESTIGATIVE,
        "requires_transcripts": True,

        "per_meeting_prompt": (
            "You have been given the official meeting summary and the raw transcript "
            "for the {committee} committee meeting on {date}.\n\n"
            "Produce a detailed comparison with three sections:\n\n"
            "1. **Fabricated / Misrepresented** — Anything in the summary that is factually "
            "wrong, significantly overstated, or misrepresents what actually happened. "
            "Pay special attention to:\n"
            "   - \"Decisions\" that were actually just proposals, suggestions, or ideas "
            "floated without a vote\n"
            "   - Action items that were never stated or agreed to\n"
            "   - Conflict, frustration, or disagreement that was sanitised or removed\n"
            "   - Attribution errors (wrong person credited, wrong context)\n"
            "   - Attendance lists that don't match who actually spoke in the transcript\n\n"
            "2. **Omitted** — Material discussions, confrontations, proposals, or context "
            "from the transcript that are completely absent from the summary but matter for "
            "understanding what actually happened. Flag:\n"
            "   - Extended debates or disagreements that were erased\n"
            "   - Guest contributions that were ignored\n"
            "   - Recurring issues raised by members that never appear in official records\n"
            "   - Context that changes the meaning of what IS included\n\n"
            "3. **Broadly Accurate** — What the summary gets right.\n\n"
            "Be forensic. Quote specific speaker names from the transcript. "
            "Do not soften findings.\n\n"
            "**Evidence standard:** End with a confirmation that all claims are supported "
            "by direct quotes from named speakers in the transcript."
            + _ACCURACY_RULES +
            "\n\n=== SUMMARY ===\n{summary}\n\n"
            "=== TRANSCRIPT ===\n{transcript}"
        ),

        "synthesis_prompt": (
            "You produced per-meeting truth audit findings for the {committee} committee. "
            "Now synthesise them into an **Overall Patterns** section identifying:\n\n"
            "- Systematic biases in summary production (tone laundering, proposal-to-decision "
            "inflation, invented action items, accountability sanitising)\n"
            "- Whether the official record can be trusted as a factual account\n"
            "- Who benefits and who is harmed by the distortions\n"
            "- A statistical summary: how many meetings had fabrications, omissions, etc.\n\n"
            "Be direct and cite the most compelling examples from the per-meeting findings.\n\n"
            "**Important:** Only reference findings that appear in the per-meeting analysis below. "
            "Do not introduce new claims.\n\n"
            "{all_findings}"
        ),
    },

    # ────────────────────────────────────────────────────
    # PROMPT 2: Member Participation Analysis
    # ────────────────────────────────────────────────────
    2: {
        "name": "Member Participation Analysis",
        "filename": "02 - Member Participation Analysis.md",
        "system": _SYSTEM_GOVERNANCE,
        "requires_transcripts": False,

        "prompt": (
            "You have the complete meeting records for the {committee} committee "
            "from {start_date} to {end_date}.\n\n"
            "Produce a comprehensive participation analysis.\n\n"

            "**FIRST: Identify the committee composition.**\n"
            "Before analysing participation, you MUST determine:\n"
            "1. How many meetings are in this dataset? List every meeting date.\n"
            "2. Did the committee membership change during this period? Look for:\n"
            "   - A sharp change in attendee names between consecutive meetings "
            "(indicates an election/transition)\n"
            "   - Explicit mentions of elections, new terms, handovers, or transitions\n"
            "   - People who appear in early meetings but never again (old committee)\n"
            "   - People who first appear mid-series and continue (new committee)\n"
            "3. Who are the ELECTED/VOTING members vs. staff (secretaries, Intersect employees) "
            "vs. guests/presenters?\n"
            "4. State clearly: 'The dataset contains N meetings. "
            "[If transition found: The committee transitioned around DATE — the first M meetings "
            "are the old committee, the remaining N-M are the new committee.] "
            "The current elected members are: [list].'\n\n"

            "**Part 1: Attendance Grid**\n"
            "Create a table showing each ELECTED member's attendance across ALL meetings "
            "in the dataset.\n"
            "- Column headers: meeting dates\n"
            "- Cells: 'P' (present — name appears in attendee list OR person speaks in transcript), "
            "'A' (absent — does not appear at all), or 'N/A' (not yet a member — ONLY if there is "
            "explicit evidence of a mid-term election, stated in a transcript)\n"
            "- Final column: attendance rate as X/{total_meetings}\n"
            "- ALL members use the SAME denominator ({total_meetings} total meetings) "
            "unless you have explicit transcript evidence they joined mid-term, in which case "
            "state the evidence and use X/Y where Y is their eligible meetings\n"
            "- Staff and guests should be listed separately, NOT in the elected member grid\n\n"

            "**Part 2: Per-Member Deep Analysis**\n"
            "For each elected/voting member:\n"
            "- **Attendance rate** — X/{total_meetings} meetings (or X/Y with cited evidence "
            "if they joined mid-term)\n"
            "- **Speaking frequency** — Heavy / Moderate / Light / Silent. "
            "Cite specific meetings where they spoke or were silent.\n"
            "- **Substantive contributions** — Every concrete proposal, document, "
            "presentation, or strategic idea WITH the meeting date. "
            "If they contributed nothing concrete, say so.\n"
            "- **Work between meetings** — Evidence of work done outside meetings. "
            "If no evidence, say so.\n"
            "- **Quality of engagement** — Adding value or filling space?\n"
            "- **Accountability** — Did they follow through on action items?\n"
            "- **Trajectory** — Improved, declined, or flat over the period?\n\n"

            "**Part 3: Power Dynamics**\n"
            "- Who dominates speaking time? Cite evidence.\n"
            "- Who is consistently sidelined? Cite evidence.\n"
            "- Visible alliances or voting blocs?\n"
            "- Who does actual work vs. who just shows up?\n\n"

            "**Part 4: Summary Rankings**\n"
            "Rank all elected members from most to least effective with transcript evidence. "
            "Members who show up, stay silent, and do no work should be called out.\n"
            + _ACCURACY_RULES +
            "\n\n---\n\n{file_contents}"
        ),
    },

    # ────────────────────────────────────────────────────
    # PROMPT 3: Leadership Assessment
    # ────────────────────────────────────────────────────
    3: {
        "name": "Leadership Assessment",
        "filename": "03 - Leadership Assessment.md",
        "system": _SYSTEM_GOVERNANCE,
        "requires_transcripts": False,

        "prompt": (
            "You have the complete meeting records for the {committee} committee "
            "from {start_date} to {end_date}.\n\n"

            "**FIRST: Identify the leadership team.**\n"
            "Before analysing, determine from the transcripts:\n"
            "- Who served as Chair? Did the Chair change during this period?\n"
            "- Who served as Vice Chair? Was the position vacant at any point?\n"
            "- Who served as Secretary? Did the Secretary change?\n"
            "- Cite the transcript evidence for each identification "
            "(e.g., how they were addressed, election results mentioned, role references).\n\n"

            "Analyse each identified leader individually:\n\n"
            "### Chair\n"
            "- **Meeting facilitation**: Effective? Time management? All voices heard? "
            "Or monologues, lost control, drift?\n"
            "- **Decision-making**: Clear votes? Proposals vs decisions distinguished? "
            "Action item follow-up?\n"
            "- **Preparation**: Agendas ready? Previous items followed up?\n"
            "- **Conflict management**: Mediate or avoid? Take sides?\n"
            "- **Strategic direction**: Vision and direction, or just processing items?\n"
            "- **Power usage**: Appropriate? Unilateral decisions, favouritism, "
            "suppression of dissent?\n\n"
            "### Vice Chair\n"
            "- **Support role**: Active support? Passive?\n"
            "- **Independent contributions**: What beyond supporting the Chair?\n"
            "- **Accountability**: Own commitments delivered?\n\n"
            "### Secretary\n"
            "- **Minutes accuracy**: How accurate based on evidence?\n"
            "- **Timeliness**: Documentation produced promptly?\n"
            "- **Administrative execution**: Tools, access, invites, logistics?\n"
            "- **Boundary respect**: Stay in lane (admin) or cross into governance "
            "(swaying votes, advocating positions, bringing guests without sanction)?\n"
            "- **Communication management**: Channels, posts, coordination?\n\n"
            "### Overall Leadership Assessment\n"
            "- Is the committee well-led?\n"
            "- Biggest leadership failure?\n"
            "- What would you change?\n\n"
            "Support every finding with specific transcript evidence (date, speaker, quote).\n"
            + _ACCURACY_RULES +
            "\n\n---\n\n{file_contents}"
        ),
    },

    # ────────────────────────────────────────────────────
    # PROMPT 4: Promises vs. Reality
    # ────────────────────────────────────────────────────
    4: {
        "name": "Promises vs. Reality — Achievement Audit",
        "filename": "04 - Promises vs Reality.md",
        "system": _SYSTEM_GOVERNANCE,
        "requires_transcripts": False,

        "prompt": (
            "You have the complete meeting records for the {committee} committee "
            "from {start_date} to {end_date}.\n\n"
            "Track every commitment, action item, decision, and promise made across "
            "all meetings and determine what was actually delivered.\n\n"

            "**Part 1: The Tracker**\n"
            "Create a table:\n"
            "| # | Promise/Commitment | Made by | First promised (date) | "
            "Repeated? | Status | Evidence |\n\n"
            "Status options:\n"
            "- DELIVERED — confirmed complete in a later transcript\n"
            "- PARTIAL — evidence of progress but not fully resolved\n"
            "- NOT DELIVERED — no evidence of completion in any subsequent transcript\n"
            "- RECURRING — promised in multiple meetings, never resolved\n\n"
            "**Rules for the tracker:**\n"
            "- Only include commitments that were ACTUALLY STATED by a named speaker in a transcript. "
            "Do not include items that only appear in summaries unless the transcript confirms them.\n"
            "- For each item, cite the specific meeting date and speaker.\n"
            "- 'NOT DELIVERED' means you checked all subsequent transcripts and found no evidence. "
            "It does NOT mean you assume it wasn't done.\n"
            "- Items from the final meeting cannot be assessed — mark as 'PENDING (final meeting)'.\n\n"

            "**Part 2: Concrete Deliverables**\n"
            "List everything the committee actually produced (with evidence):\n"
            "- Documents published\n- Programs launched\n- Votes completed\n"
            "- External-facing outputs\n- Budget proposals submitted\n"
            "- Partnerships established\n"
            "For each, cite the meeting where it was confirmed.\n\n"

            "**Part 3: Gap Analysis**\n"
            "- Total commitments vs delivered. Calculate delivery rate.\n"
            "- Biggest failures (repeated promises never kept).\n"
            "- Most/least reliable promise-keepers.\n"
            "- Patterns in what gets done vs. what doesn't.\n\n"

            "**Part 4: Overall Assessment**\n"
            "Given the committee's mandate, budget, and time period:\n"
            "- Is this committee delivering value to Cardano?\n"
            "- What would you tell a DRep asking about continued funding?\n\n"
            "Be brutally honest. The purpose is accountability.\n"
            + _ACCURACY_RULES +
            "\n\n---\n\n{file_contents}"
        ),
    },

    # ────────────────────────────────────────────────────
    # PROMPT 5: Critical Observations
    # ────────────────────────────────────────────────────
    5: {
        "name": "Critical Observations",
        "filename": "05 - Critical Observations.md",
        "system": _SYSTEM_INVESTIGATIVE,
        "requires_transcripts": False,

        "prompt": (
            "You have read every word of every transcript and summary for the "
            "{committee} committee from {start_date} to {end_date}.\n\n"
            "Write a free-form critical observations report covering anything notable "
            "that doesn't fit the other analysis categories:\n\n"
            "- **Governance red flags**: Conflicts of interest, self-dealing, "
            "inappropriate influence, procedural violations?\n"
            "- **Cultural dynamics**: Collaborative? Dysfunctional? Performative? "
            "Passive-aggressive?\n"
            "- **Information asymmetry**: Who knows more? Information withheld or "
            "gatekept?\n"
            "- **External influence**: Staff, founding entities, or other actors "
            "shaping decisions inappropriately?\n"
            "- **Tool and process dysfunction**: Helping or hindering work?\n"
            "- **Recurring themes**: Topics that return meeting after meeting "
            "without resolution. Why?\n"
            "- **Member dynamics**: Tensions, alliances, power plays?\n"
            "- **Cross-committee coordination**: Evidence of coordination or silos?\n"
            "- **Attendance patterns**: Absences clustering around important votes?\n"
            "- **Budget and resources**: How does the committee handle money?\n"
            "- **Community engagement**: Engaging the broader community or insular?\n\n"
            "Write as a narrative, not a checklist. Cite transcript evidence "
            "(date, speaker, quote) for every claim. "
            "The reader is conducting oversight of Intersect's committee governance.\n"
            + _ACCURACY_RULES +
            "\n\n---\n\n{file_contents}"
        ),
    },
}
