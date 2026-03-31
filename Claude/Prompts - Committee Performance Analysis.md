# Committee Performance Analysis — Prompt Library

These prompts are designed to be used with the full set of Summary + Transcript files for each committee. Feed them the complete folder contents (all transcripts and all summaries for a single committee) in a single context window, then run each prompt sequentially.

---

## Prompt 1: Summaries vs. Transcripts — Truth Audit

```
You are an investigative analyst. You have been given the complete set of meeting summaries and raw transcripts for the [COMMITTEE NAME] of Intersect MBO.

Your task: systematically compare every summary against its corresponding transcript and produce a detailed report.

For EACH meeting, provide three sections:

1. **Fabricated / Misrepresented** — Anything in the summary that is factually wrong, significantly overstated, or misrepresents what actually happened in the transcript. Pay special attention to:
   - "Decisions" listed in summaries that were actually just proposals, suggestions, or ideas floated without a vote
   - Action items that were never stated or agreed to in the meeting
   - Conflict, frustration, or disagreement that was sanitized or removed
   - Attribution errors (wrong person credited, wrong context)

2. **Omitted** — Material discussions, confrontations, proposals, or context from the transcript that are completely absent from the summary but matter for understanding what actually happened. Specifically flag:
   - Extended debates or disagreements that were erased
   - Guest contributions that were ignored
   - Recurring issues raised by members that never appear in official records
   - Context that changes the meaning of what IS included

3. **Broadly Accurate** — What the summary gets right.

After all meetings, provide an **Overall Patterns** section identifying:
- Systematic biases in summary production (tone laundering, proposal-to-decision inflation, invented action items, accountability sanitizing)
- Whether the official record can be trusted as a factual account
- Who benefits and who is harmed by the distortions

Be forensic. Quote specific timestamps and speaker names from transcripts. Do not soften findings. The purpose is accountability.
```

---

## Prompt 2: Member Participation Analysis

```
You are a governance analyst. You have the complete transcripts for all meetings of the [COMMITTEE NAME] of Intersect MBO from [START DATE] to [END DATE].

Produce a comprehensive participation analysis for every elected/voting member.

**Part 1: Attendance Grid**
Create a table showing each member's attendance across all meetings. Mark: Present, Absent, Late/Audio Issues. Calculate attendance rate.

**Part 2: Per-Member Deep Analysis**
For each voting member, provide:

- **Attendance rate** (X/Y meetings)
- **Speaking frequency** — Classify as: Heavy (speaks in most agenda items), Moderate (speaks on 2-3 topics), Light (1-2 brief contributions), Silent (present but barely speaks)
- **Substantive contributions** — List every concrete proposal, document, presentation, or strategic idea this member brought to any meeting. Be specific. If they contributed nothing substantive, say so.
- **Work between meetings** — Evidence from transcripts that this member did actual work outside of meetings (documents prepared, tasks completed, follow-ups done). If no evidence exists, say so.
- **Quality of engagement** — When they speak, are they adding value (new ideas, critical questions, constructive pushback) or just filling space (agreement sounds, repetitive points, off-topic tangents)?
- **Accountability** — Did they follow through on action items assigned to them? Track promises made vs. delivered across the full series.
- **Trajectory** — Did their participation improve, decline, or stay flat over the period?

**Part 3: Power Dynamics**
- Who dominates speaking time? Estimate percentage of member speech per meeting.
- Who is consistently sidelined or ignored?
- Are there voting blocs or alliances visible in the transcripts?
- Who does actual work vs. who just shows up?

**Part 4: Summary Verdict**
Rank all members from most to least effective. Justify each ranking with transcript evidence. Be direct and critical. Members who show up, stay silent, and do no work between meetings should be called out explicitly.
```

---

## Prompt 3: Leadership Assessment (Chair, Vice Chair, Secretary)

```
You are evaluating the performance of the leadership team of the [COMMITTEE NAME] of Intersect MBO based on the complete meeting transcripts from [START DATE] to [END DATE].

Analyse the following roles individually:

### Chair
- **Meeting facilitation**: Do they run meetings effectively? Do they manage time, keep discussions on track, ensure all voices are heard? Or do they monologue, lose control, or let meetings drift?
- **Decision-making**: Do they call clear votes? Do they distinguish between proposals and decisions? Do they push for accountability on action items?
- **Preparation**: Do they come prepared with agendas? Do they follow up on previous meeting items?
- **Conflict management**: How do they handle disagreements? Do they mediate or avoid? Do they take sides?
- **Strategic direction**: Are they providing vision and direction for the committee? Or just processing agenda items?
- **Power usage**: Do they use their position appropriately? Any evidence of unilateral decisions, favoritism, or suppression of dissent?

### Vice Chair
- **Support role**: Do they actively support the Chair? Step in when needed? Or are they passive?
- **Independent contributions**: What do they bring beyond supporting the Chair?
- **Accountability**: Do they deliver on their own commitments?

### Secretary
- **Minutes accuracy**: Based on the Summary vs. Transcript analysis, how accurate are their minutes?
- **Timeliness**: Is documentation produced promptly?
- **Administrative execution**: Are tools, access, invites, and logistics handled properly?
- **Boundary respect**: Does the secretary stay in their lane (administration) or cross into governance (swaying votes, advocating positions, bringing guests without committee sanction, shaping agendas)?
- **Communication management**: Are channels, posts, and coordination handled effectively?

### Overall Leadership Assessment
- Is the committee well-led?
- What is the leadership team's biggest failure?
- What would you change if you were advising the ISC on this committee's performance?

Support every finding with specific transcript evidence. Be direct and critical.
```

---

## Prompt 4: Achievement Audit — Promises vs. Reality

```
You are a performance auditor. You have the complete meeting transcripts and summaries for the [COMMITTEE NAME] of Intersect MBO from [START DATE] to [END DATE].

Your task: Track every commitment, action item, decision, and promise made across all meetings and determine what was actually delivered.

**Part 1: The Tracker**
Create a table with columns:
| # | Promise/Commitment | Made by | First promised (date) | Repeated? | Status | Evidence |

Status options:
- ✅ Delivered — completed within a reasonable timeframe
- ⚠️ Partial — some progress but not fully resolved
- ❌ Never delivered — no evidence of completion
- 🔁 Recurring — promised multiple times, never resolved

Be exhaustive. Include EVERY action item from EVERY meeting — both those in the summaries AND those visible in the transcripts but missing from summaries.

**Part 2: Concrete Deliverables**
List everything this committee actually produced during the period:
- Documents published
- Programs launched
- Votes completed
- External-facing outputs
- Budget proposals submitted
- Partnerships established

For each, assess quality and impact: was it meaningful or performative?

**Part 3: The Gap Analysis**
- How many total commitments were made? How many delivered? Calculate the delivery rate.
- What are the biggest failures (promises made repeatedly but never kept)?
- Who is the most reliable promise-keeper? Who is the least?
- Is there a pattern in what gets done vs. what doesn't?

**Part 4: Overall Assessment**
Given the committee's stated mandate, budget, and the time period covered:
- Is this committee delivering value to the Cardano ecosystem?
- What would you tell a DRep who asks whether this committee deserves continued funding?

Be brutally honest. The purpose is accountability to treasury-funded governance.
```

---

## Prompt 5: Critical Observations — What Stood Out

```
You are an experienced governance observer who has just read every word of every transcript and summary for the [COMMITTEE NAME] of Intersect MBO from [START DATE] to [END DATE].

Write a free-form critical observations report covering anything notable that doesn't fit neatly into the other analysis categories. Consider:

- **Governance red flags**: Any evidence of conflicts of interest, self-dealing, inappropriate influence, or procedural violations?
- **Cultural dynamics**: What is the committee's culture? Collaborative? Dysfunctional? Performative? Passive-aggressive?
- **Information asymmetry**: Who knows more than others? Is information being withheld or gatekept?
- **External influence**: Are Intersect staff, founding entities, or other actors shaping committee decisions inappropriately?
- **Tool and process dysfunction**: Are the committee's tools and processes helping or hindering their work?
- **Recurring themes**: What topics come up meeting after meeting without resolution? Why?
- **Member dynamics**: Any interpersonal tensions, alliances, or power plays visible in the transcripts?
- **The committee's relationship with other committees**: Evidence of coordination or silos?
- **Attendance patterns**: Do absences cluster around important votes or controversial topics?
- **Budget and resource discussions**: How does the committee handle money? Any concerns?
- **Community engagement**: Is the committee actually engaging with the broader Cardano community, or is it an insular club?

Write this as a narrative report, not a checklist. Be specific, cite transcript evidence, and don't pull punches. The reader is someone conducting oversight of Intersect's committee governance.
```

---

## Usage Instructions

1. **One committee at a time.** Feed all transcripts + summaries for a single committee into one context window.
2. **Run prompts sequentially.** Start with Prompt 1 (truth audit), then 2 (members), then 3 (leadership), then 4 (achievements), then 5 (observations).
3. **Replace placeholders.** Fill in [COMMITTEE NAME], [START DATE], [END DATE] for each committee.
4. **For committees without transcripts** (only summaries): Skip Prompt 1 and modify Prompts 2-5 to note that analysis is based on summaries only (which are known to be unreliable based on MCC findings).
5. **Save outputs** in a `Reports/` folder under each committee, matching the MCC structure.

### Committee-Specific Notes

- **TSC**: Highly detailed summaries with discussion notes tables. Weekly meetings = lots of data. Look for IOE contract oversight patterns.
- **CPC**: Light summaries (no discussion tables). Focus will be on Prompts 2-5 since there's less to cross-reference.
- **OSC**: Very detailed summaries with full discussion tables. Treasury-funded programs = high accountability stakes. Look for procurement process issues.
- **GMC**: New committee, still bootstrapping. Look for whether they're producing anything beyond meetings.
- **CCC**: Governance/civics mandate. Look for whether they're actually stewarding the constitution or just meeting.
- **CBC**: Massive volume. Weekly meetings + AMAs. Focus on whether budget oversight is actually happening.
- **ISC**: Meta-committee overseeing all others. Look for whether they're exercising oversight or rubber-stamping.
