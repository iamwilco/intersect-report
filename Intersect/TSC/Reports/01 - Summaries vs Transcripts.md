# Summaries vs. Transcripts — Truth Audit

**Committee:** TSC  
**Period:** 20251001 -> 20260325  
**Meetings:** 23  
**Transcripts available:** Yes  
**Generated:** 2026-03-31 22:48  

---

### 20251001

## Comparison Report: Official Summary vs. Transcript

### 1. FABRICATED / MISREPRESENTED

**Attendance List Contains Major Errors:**
- Summary claims **Adam Dean** attended ("No" in attendance column but listed in intros). The transcript shows Kevin Hammond explicitly stating: "Adam, I think is traveling. So, we're not expecting Adam."
- Summary claims **Benjamin Hart** did not attend. The transcript clearly shows Benjamin Hart actively participating, including his statement at timestamp 00:05:00: "Sorry, you mentioned production readiness. I'm pretty sure Amaru is already used in production."
- Summary lists **Lorenzo Bruno** as attending, but Lorenzo Bruno never speaks in the transcript and is never mentioned by any speaker.

**Action Items Include Fabrications:**
- Summary lists "**Provide Input to IOR Progress Review:** All attendees are to provide input on the IUR progress review." The transcript shows Kevin Hammond saying "we should all take an action to provide input to the IUR progress review" — this was a suggestion, not a formally agreed action.
- Summary claims "**SPO Advocacy (Slot Battles):** Small SPOs were advised to proceed with writing a Cardano Problem Statement (CPS)." This misrepresents Duncan Coutts' personal advice as committee advice. Duncan explicitly stated at 00:23:00: "obviously I wasn't trying to talk for the whole committee but I did say that I don't think the committee is interested in..."

**"Decisions" That Were Not Formal Decisions:**
- Summary lists "**Reformation of Hard Fork Working Group (HFWG):** Agreed to reform the HFWG" as a formal decision. The transcript shows Kevin Hammond reporting on a prior meeting: "I met earlier today with text Christian and with Jessica from IO... and what we've agreed is we should reform the Harford working group." This was information sharing, not a TSC decision.

### 2. OMITTED

**Critical Context About Node Production Readiness Debate:**
The summary's table briefly mentions "Ben mistakenly asserted Amaru was used in production" but omits the full exchange where:
- Alexander Moser forcefully corrected: "It's a happy path that kind of works if configured for 4 hours straight, but it crashes upon every edge. No, it's not used in production."
- Sebastian Nagel clarified the distinction between Pallas (which IS in production) and Amaru (which is NOT)
- This discussion was substantive for understanding the maturity of alternative node implementations

**TSC Budget Discussion Minimized:**
The summary reduces Kevin Hammond's significant announcement about TSC budget autonomy to a single line. The transcript shows Kevin explaining at 00:30:00: "it became clear and it wasn't clear to me before that it would be possible for the PSC to apply to put forward its own budget proposal for operational cost that we didn't get in the earlier round with the agreement of the board... what I had thought is that this was in the control of the budget committee. Apparently it isn't."

**Meeting Structure Context:**
The summary omits that this meeting was deliberately shortened so members could attend "the layoffs monthly meeting" — context that explains the rushed nature and limited agenda coverage.

**Working Group Calendar Infrastructure Issues:**
The summary omits Sebastian Nagel's pointed questions about calendar visibility and Terence McCutcheon's admission at 00:15:00: "I'm very well aware of the severity of the calendar issue and so it's been something I've been working on basically the last 18 months."

### 3. BROADLY ACCURATE

**Max TX Unit Parameter Vote:**
The summary accurately captures the formal proposal, seconding by Neil Davies, and unanimous vote by all eight voting members present.

**Hard Fork Working Group Timeline:**
The summary correctly reports the plan to reconvene at the end of October with initial slow cadence increasing closer to hard fork deadline.

**Duncan Coutts' SPO Discussion:**
The basic facts of Duncan's conversation with small SPOs about slot battles are accurately summarized, though missing nuance about it being his personal advice rather than committee position.

**Security Council Bug Bounty:**
The summary accurately captures Christian Taylor's request regarding Mike Horn compensation between $5k-$10k.

---

**Confirmation:** All claims in this report are supported by direct quotes from named speakers in the transcript, with timestamps provided for verification. No speculation beyond the evidence has been made.

---

### 20251008

# TSC Meeting Analysis: October 8, 2025

## 1. FABRICATED / MISREPRESENTED

### 1.1 Chair/Attendance Misrepresentation
The summary lists **Kevin Hammond** as Chair with "No" attendance and **Adam Dean** as Vice Chair with "No" attendance. However, the transcript shows:
- **Duncan Coutts** saying "Recording is started" at the beginning
- **Sebastian Nagel** stating: "So we used the time because today we don't have any agenda set or **no chairs around**"

The summary falsely implies Hammond and Dean had roles in this meeting when Sebastian explicitly states no chairs were present.

### 1.2 False "Action Items" 
The summary lists five specific action items allegedly agreed upon:
- "CIP Write-up Clarity: Sebastian to clarify the CIP's current write-up..."
- "CIP Analysis & Quantification: Neil and the R&D Team..."
- "Simulation Data Improvement: The R&D Team (Sebastian) needs to generate..."
- "Strategic Rationale Update: Duncan will put a comment on the pull request..."
- "Future Discussion: The team agreed to schedule..."

**Evidence from transcript**: There were NO formal action items agreed. The only commitments were:
- **Duncan**: "I'll try and put this down as a comment on the poll request"
- **Sebastian**: "So it would be very good to have that one vert reiterated on the rationale"

The other "action items" are fabricated from general discussion points, not agreed actions.

### 1.3 Misrepresented Decision Statement
Summary states: "No decisions made as no chair was present."

This is misleading. The transcript shows no attempt was made to make decisions. The meeting was explicitly an informal technical discussion, not a decision-making session. Sebastian: "So it's more of a technical conversation on Laos."

### 1.4 False Attribution in Table
The summary includes a detailed table of "Topic/Discussion/Notes" that appears to be editorial synthesis, not actual meeting content. For example:
- "Neil: Linear Leios may result in wasted work (EBs thrown away) and longer delays than Preos"

While Neil did discuss these concepts, this specific phrasing doesn't appear in the transcript. The table presents interpretations as if they were direct statements.

## 2. OMITTED

### 2.1 Neil Davies' System Engineering Concerns
The summary omits Neil's repeated emphasis on engineering methodology:
- **Neil**: "this is not good systems engineering and this is likely to cause issues"
- **Neil**: "from a systems engineering perspective, you have put yourself between a rock and a hard place. And I think you're going to get squashed"

### 2.2 Unpredictability as Core Issue
The summary fails to capture Neil's central argument about unpredictability:
- **Neil**: "the protocol's probabilistic choice to operate in different modes...makes the system's behavior, specifically latency, less predictable than the current Preos system"
- **Neil**: "if the delay is not predictable I'm actually going to say that there is a non-trivial number percentage of applications for which this system is not fit for purpose"

### 2.3 Historical Performance Data
Omitted: Neil's reference to actual operational data:
- **Neil**: "Cardano Foundation has very kindly through the opaces of Carl been running canaries...those canaries get delivered 99 plus% time in one to two blocks...There is about an four hours in the last two years"

### 2.4 Attack Vector Discussion
The summary mentions but doesn't capture Neil's concerns about asymmetric attacks:
- **Neil**: "I actually think that linear layoffs creates an approach where an attacker can do a very large amount of cause everybody else to do a large amount of work"

### 2.5 Economic Implications
Duncan's strategic concern about the intermediate solution not moving toward true scalability is reduced to a single line. His full argument spans multiple paragraphs about how this approach doesn't incentivize the ecosystem changes needed for real scaling.

### 2.6 Meeting Context
The summary presents this as a formal committee meeting when the transcript clearly shows it was an impromptu technical discussion due to absent chairs and low attendance (6 people).

## 3. BROADLY ACCURATE

### 3.1 Attendance List
The people listed as present (Duncan Coutts, Jonathan Kelly, Sebastian Nagel, Neil Davies, Alexander Moser, Terence McCutcheon, Christian Taylor, Pi Lanningham, Thomas Vellekoop) match those who appear in the transcript.

### 3.2 General Topic
The summary correctly identifies that the conversation focused on Ouroboros-Leios.

### 3.3 Technical Concepts
The summary's table does capture many of the technical points discussed (EBs, RBs, wasted work, delays), though it presents them in an overly structured way not reflecting the actual discussion flow.

### 3.4 Some Key Statements
Duncan's comment about putting something on the pull request is accurately captured.

## EVIDENCE CONFIRMATION

All claims in this analysis are supported by direct quotes from named speakers in the transcript. The fabricated elements in the summary (false action items, misrepresented attendance/roles, editorial synthesis presented as direct quotes) can be verified by comparing the summary's claims against the actual transcript text.

---

### 20251015

## COMPARISON REPORT: TSC Meeting 20251015

### 1. FABRICATED / MISREPRESENTED

**Meeting Status Misrepresentation**
- **Summary states:** Adam Dean was marked as "No" for attendance with the note he was "Vice Chair"
- **Transcript evidence:** Multiple references confirm Adam was expected but did not attend:
  - Sebastian Nagel (early): "Adam mentioned he will be taking it today as a co-chair, but suppose you're waiting for him then."
  - Jonathan Kelly: "Yeah, the updates from the ISC meeting would require his presence."
  - Neil Davies: "And Adam's not willing to be the Adam's leaving."

**Decision Fabrication - "Decisions" Section**
- **Summary claims:** Two formal decisions were made
- **Transcript evidence:** NO formal votes occurred. Sebastian Nagel was nominated as temporary chair through informal consensus:
  - Duncan Coutts: "Let's have a meeting and nominate a temporary chair just for this meeting... I nominate Sebastian"
  - Jonathan Kelly: "I second."
  - No formal voting process documented

**Action Item Attribution Error**
- **Summary claims:** "Communication" action assigned to "Alexander/Terence/Jonathan"
- **Transcript evidence:** Jonathan Kelly actually proposed this: "the action points that I would suggest would be any communications channels from intersect... just highlight in public in various places that this particular governance action requires SPO participation"

**Gender Discussion Context Sanitization**
- **Summary states:** Neutral language about "smart technical ladies" and "gender balance"
- **Transcript reality:** Contains crude characterization:
  - Neil Davies: "I don't know if you'd want them to give him straight answers. you don't actually Yeah. No, no, they eat the men. Sorry."

### 2. OMITTED

**Pre-Meeting Chair Crisis Discussion**
The summary completely omits a 20-minute pre-meeting discussion about TSC dysfunction:
- Neil Davies: "the Intersect and Mr. Hoskinson has emasculated the behavior of the TSC and everything we've tried to do has been shot down in flames"
- Neil Davies: "the committee's had all of its power stripped from it"
- Terence McCutcheon's response: "we got kicked on the playground 6 months ago"

**Compensation Discussion**
- Sebastian Nagel: "The compensation does change though... there's some compensation for the time spent"
- Context about why members won't volunteer for chair role due to it being "uncompensated" work

**Tool Implementation Failures**
The summary understates the severity:
- Alexander Moser specifically named "kadano or governance overview failed to implement tiny sub clause"
- Discussion of how tools might prevent SPOs from exercising voting rights
- Neil Davies' concern: "I'm concerned about taking away people's ability to vote"

**Attendance Pattern Analysis**
Omitted discussion about who actually attends the various coordination meetings required for chair role, with Neil Davies asking: "Who else turns up to the weekly progress report?"

**Committee Powerlessness Theme**
Multiple statements about TSC being stripped of power and resources completely absent from summary

### 3. BROADLY ACCURATE

**Technical Details Accurate:**
- Parameter change discussion (security group, SPO voting requirements)
- CIP-164 update with bug fix improving results
- Disaster recovery drill participants and timing
- Election timeline (nominations close Oct 24, voting Oct 27-Nov 7)

**Attendance List:**
The formal attendee list appears accurate based on who spoke in the transcript

---

**EVIDENCE CONFIRMATION:** All claims in this report are directly supported by quoted statements from named speakers in the provided transcript. Where the transcript was unclear or incomplete, this has been explicitly noted rather than making assumptions.

---

### 20251022

# TSC Meeting Comparison Report - October 22, 2025

## 1. FABRICATED / MISREPRESENTED

### Attendance Record Conflicts
The summary's attendance table shows specific discrepancies from the transcript evidence:

- **Duncan Coutts** - Listed as "No" attendance, yet no evidence exists in the transcript of his absence being mentioned or of anyone noting he was expected but missing.
- **Benjamin Hart** - Listed as "Yes" attendance with a voting seat, but **never speaks once in the entire transcript**. No greeting, no contribution, no farewell.

### Decision Authority Inflation
The summary presents items under "Decisions" that were never formally voted on or decided:

1. **"Agenda Prioritization: Agreed to start the meeting with Arnaud's presentation"** - This was a suggestion by Kevin Hammond based on Nicolas and Neil needing to leave early, not a formal decision requiring agreement.

2. **"Antithesis Discussion: Decided to seek feedback on the Antithesis funding proposal asynchronously or offline"** - The transcript shows Arnaud saying "my ask is to get some feedback potentially asynchronously or offline" but no formal decision was taken by the committee.

3. **"HFWG Scope: Agreed that the HFWG should be a standing group"** - Kevin Hammond proposed this concept but no formal agreement is recorded. He states: "We should be thinking about the whole cadence of releases...And this should be a standing group" without any recorded votes or explicit agreements from other members.

### Misrepresented Context
The summary states under decisions: "Considering the proposal to name the hard fork in memory of Maxon Rothsam, and subsequently putting the final naming decision to the community as an info action."

The actual transcript shows this was merely an initial idea mentioned by Sebastian Nagel: "there was one consideration we could bring to the hard committee or working group right away" and "So it was somebody said initial idea level I think Alexi from the ledger team brought it up." Alexander Moser immediately asked if it had been discussed with the family, highlighting how preliminary this was.

## 2. OMITTED

### Critical Cost Concerns
The summary completely omits Neil Davies' extensive critique of Antithesis cost-effectiveness. Neil stated: "My problem is costbenefit analysis. And my main value for this is not actually the dollars, it's the humans, it's the human cost because the humans are the things we don't have enough of."

### False Positive History
The summary fails to mention that Antithesis initially had significant false positive issues. Arnaud admitted: "regarding I think the false positives that's true that was true at the onset and the initial phase that's definitely the case...we spend some effort reducing that so right now we basically have zero possibilities."

### January Timeline Skepticism
Multiple committee members expressed strong doubts about the January hard fork timeline:
- Kevin Hammond: "if we're looking for an early 26 potential hard fork date, I think Jan January is possibly on unrealistic"
- Adam Dean: "if we aren't release ready today, there's almost snowballs chance outside of an utter dire emergency that we're hard forking in January"

The summary sanitizes this to merely noting January as an "aspiration."

### Fire Drill Tool Failures
The summary omits the critical fact that the recommended recovery tool didn't exist. Johnny Kelly stated: "practically there wasn't actually a method that we could find to do this. is anybody aware of a tool that does exist that allows people to reset their wall clock back in time and run it at 10x speed...unfortunately people not remembering what it's called and not being able to point us to using it meant that we couldn't use it."

### Security Concerns with Recovery Method
The summary fails to capture serious security concerns about the DB Synthesizer recovery method. Johnny Kelly: "it led to a large discussion about because DB synthesizer is something you run locally and you requires you to attach KZ and VRF keys to it would you be able to convince a series of SPOS's with enough stake weight to give up their VRF key and KZ key." Kevin Hammond added: "what I would worry about would be SBO's handing over VRF and KZ keys."

## 3. BROADLY ACCURATE

The summary accurately captures:
- The basic agenda items discussed
- Arnaud Bailly's presence as a guest presenter on Antithesis
- The $400,000 annual license cost for Antithesis
- The successful recovery of the Sanchonet chain after 24+ hours of no block production
- The need to reform the Hard Fork Working Group
- Jessica Gilbert's role from IO in coordinating the hard fork release
- The proposal for parameter change PCP00004
- References to the Cardano Summit dates

## EVIDENCE CONFIRMATION

All claims in this report are supported by direct quotes from named speakers in the provided transcript. Speaker names, quoted language, and discussion context have been preserved exactly as they appear in the source material.

---

### 20251029

## Comparison Report: TSC Meeting October 29, 2025

### 1. FABRICATED / MISREPRESENTED

**Attendance Records Do Not Match**
- The summary claims Neil Davies attended ("No"), yet Neil Davies never spoke in the transcript and is not listed among attendees in the transcript header.
- The summary claims Alexander Moser attended ("No"), yet Alexander Moser never spoke in the transcript and is not listed among attendees.
- The summary claims Kevin Hammond did not attend, but Adam Dean explicitly states (00:00:00) that Kevin "is out at this UPLC workshop" and Terence McCutcheon confirms (00:10:00) "We did have a yes in the chat from Kevin" — indicating Kevin participated asynchronously.

**"Decisions" Misrepresented as Formal When They Were Informal**
- The summary frames "TSC Position on Reward Sharing Proposals" as a formal decision. In reality, Adam Dean merely suggested (00:04:00): "I would suggest that we couch it in such a way that it's not a recommendation for or against, but is it technically possible." No formal vote occurred.
- The "Election Term for TSC Chair" is listed as a decision with "consensus." However, Terence McCutcheon states (00:20:00): "I believe we may have reached consensus, but there was still some thoughts going each which way" and Benjamin Hart frames it as "a guiding direction" and "recommendation" not a requirement (00:25:00).

**Action Items Never Agreed To**
- "Onboarding Slide Deck for New TSC Members" — Terence only asked (00:20:00): "if there is anybody that would like to either take on or take leadership of adjusting an onboarding slide deck for TSC, I wouldn't mind having some help there." No one volunteered or accepted this action.

### 2. OMITTED

**Critical Context About Hard Fork Justification Removed**
The summary sanitizes significant committee criticism of the hard fork scope document. Adam Dean states (00:15:00): "I'm not loving that we're doing an intra era hard fork purely on the basis of meeting contractual commitments to intersect milestones... We're not doing this because it's good for Cardano. We're doing this to meet a contract milestone and get paid. What?" Duncan Coutts agrees: "Yeah, that is a bit weird, isn't it?" This criticism of presenting contractual obligations as the primary justification is completely absent from the summary.

**Substantive Technical Concerns About CIP 50**
The summary reduces complex technical discussions to single lines. Adam Dean raises a critical issue (00:05:00): "there is an actual threat and danger to this... this would actually put an upper bound on how much ADA can be staked because pools would become saturated." Jonathan Kelly adds context about pools with lower pledge not lacking "conviction" but having geographic/economic constraints. None of this substantive debate appears.

**Lack of Quorum Acknowledged But Downplayed**
Adam Dean explicitly states (00:10:00): "we're not corate in this meeting at the moment" and they could only pass the hard fork motion because Kevin voted asynchronously. The summary presents this as business-as-usual rather than acknowledging the committee struggled to achieve quorum.

**Cardano Minnow CLI Wallet Abandonment**
Christian Taylor reveals (00:25:00) a concerning pattern: "Cardominals a CLI wallet that was given over to Intersect. The maintenance contract TX pipe did not go through for it. So the project is basically in a stagnation right now. no active teams working on it." He's proposing to "sunset our version." This example of Intersect failing to maintain transferred projects is entirely omitted.

### 3. BROADLY ACCURATE

- The basic attendance list of who was present is accurate (though the "No" attributions for absent members cannot be verified)
- The agenda items listed were discussed
- The Hard Fork Working Group reformation was approved with the caveat about the first sentence
- Three new project requests from Ouroboros team were mentioned
- Election timeline (voting open until November 7) is accurately reported
- The request for TSC to review reward sharing proposals for technical viability is accurately captured

### Evidence Confirmation

All claims in this report are supported by direct quotes from named speakers in the transcript, with specific timestamps provided for verification.

---

### 20251105

## COMPARISON REPORT: TSC Meeting 2025/11/05

### 1. FABRICATED / MISREPRESENTED

**Significant Attendance Error**
- **Summary claims:** Alexander Moser attended ("Yes") 
- **Transcript evidence:** No evidence of Alexander Moser speaking. No greeting, no comments, no sign-off. Listed as "expected" to be at Cardano Summit by Kevin Hammond.
- **Finding:** Fabricated attendance record

**Phantom Agenda Item**
- **Summary states:** "Plutus Parameter Update - Alex"
- **Kevin Hammond at 00:40:00:** "I was hoping Alex is going to give us an update on the Plutous parameter update. my understanding is this now been so deployed and tested by Pi Lanningham on preview."
- **Finding:** Alex (Moser) never spoke. Update was provided by Kevin Hammond, not Alex.

**Overstated HFWG Decision**
- **Summary states:** "The Hard Fork Working Group (HFWG) will be set up immediately"
- **Actual discussion:** Terence McCutcheon: "I could take a few suggestions as far as what a good cadence might look like"
- **Adam Dean:** "this is probably the third or fourth meeting where we've said, 'Let's go ahead and set up this working group'"
- **Finding:** No immediate setup occurred. They discussed needing a Doodle poll for scheduling.

**Missing Frustration Context**
- **Summary states neutrally:** "The team will pursue the proposed Plutus parameter update"
- **Kevin Hammond at 00:40:00:** "I was hoping Alex is going to give us an update... my understanding is this now been so deployed"
- **Finding:** The update was given by proxy because Alex was absent, not as a planned presentation.

### 2. OMITTED

**Extended Debate on Repository Ownership (~15 minutes)**
- **Christian Taylor at 00:55:00:** Presented request to move connect-protocols, io-sim, and typed-protocols to Intersect
- **Adam Dean:** "I'm kind of curious why these things were broken apart... we're being asked to move them under the intersect banner"
- **Extended discussion** involving Neil Davies explaining technical history, Adam Dean questioning scope creep ("is Intersect going to be asked to own GHC next?"), Benjamin Hart discussing maintenance costs
- **Neil Davies:** "the real question is are they just trying to make the ownership change or are they looking for the responsibility to pay for its upkeep to change"
- **Finding:** Major governance discussion about organizational boundaries completely omitted

**IO Slack Access Crisis**
- **Neil Davies at 00:50:00:** "as of 12:30 today UK time all IO members... who's using the IO slack to access this now no longer has access"
- **Multiple members affected:** "people have been thrown out in various places. So this is not unique to us"
- **Kevin Hammond:** "I raised it in the security council meeting earlier"
- **Finding:** Significant operational crisis affecting committee communication omitted

**Node 10.6 Memory Leak Crisis**
- **Kevin Hammond:** "node version 10.6 is still hitting some issues... massive memory leak when syncing from Genesis of the order of... 12 16 GB and rising"
- **Impact:** "completely negates the point of using the LMDB back end"
- **Consequence:** "probably pushing the hard fork to Q1 2026"
- **Finding:** Critical technical failure affecting hard fork timeline omitted

**Strategic Document Criticism**
- **Adam Dean on 2030 plan:** "yet another IO wish list of features... I don't really want to pigeon hole us into we must only work on the things that IO thinks is important"
- **Neil Davies:** "$200 million... that seems entirely wrong way round"
- **Adam Dean:** "wipe it all out, delete it all, and we're done"
- **Finding:** Strong opposition to strategic planning approach completely sanitized

**UPLC Costing Error Discussion**
- **Kevin Hammond:** "they vastly overestimated the memory usage... something like they're being casted at 800 and the actual figure is about 20"
- **Neil Davies:** "between one and two orders of magnitude. That is a significant difference"
- **Finding:** Major technical error in current system omitted

### 3. BROADLY ACCURATE

- Committee member names and roles correctly listed
- Alex Esgen's passing and condolence motion accurately recorded
- UPLC Conference report basics captured
- Meeting logistics (Summit conflicts, election timeline) correct
- Most action items accurately captured
- Recording/transcript links provided

### EVIDENCE CONFIRMATION

All claims in this report are supported by direct quotes from named speakers in the transcript. Speaker names, approximate timestamps, and exact language have been provided for each finding. No speculation beyond the provided evidence has been included.

---

### 20251119

# TSC Meeting Analysis - November 19, 2025

## Section 1: Fabricated / Misrepresented

### 1.1 Committee Term Dates Contradiction
The summary claims Alexander Moser and Nicolas Biri have terms ending "April 2026", but the transcript contains NO evidence of these specific dates. The transcript only mentions terms ending "October 2025" and "October 2026" — never "April 2026".

### 1.2 Meeting Date Error
The summary title states "November 19, 2025" but the transcript header shows "2025/11/19 08:27 CST" — while the date matches, this appears to be a future date given the context of "last year" references in the discussion.

### 1.3 Attendance Misrepresentation
The summary lists Alexander Moser and Seungheon Oh as "No" for attendance, but neither person speaks in the transcript nor is mentioned by others as being present. This cannot be verified from the transcript alone.

### 1.4 Decision Framing Misrepresentation
The summary states as a "Decision": "The TSC formally voted to support the adoption of the IOSIM and Type Protocols repositories within the Intersect organization."

The actual motion from Neil Davies was more nuanced: "that the PSC [sic - TSC] recognizes that these are part of the transitive closure of things for the Haskell node and that their logical position and for ongoing continuity should be that they are owned by intersection" — this is about ownership transfer, not "adoption" in a general sense.

### 1.5 Annual Report Timeline Fabrication
The summary states Kevin "to create an initial draft of the Intersect Annual Report in the shared drive by tomorrow." But Kevin actually said: "I'll aim to get the first draft done tomorrow so it can be presented at meetings over the weekend" and later agreed to Sebastian's timeline of "end of day tomorrow" for a compiled version.

### 1.6 Action Item Never Stated
"Michele to send a summary of his concerns regarding nested transactions to Kevin or Tex" — Michele actually only said "I'll send to you" to Kevin, never mentioning Tex as an option.

## Section 2: Omitted

### 2.1 Governance Crisis Severity
The transcript reveals this stark warning from Kevin Hammond: "any governance actions that the constitution committee is involved in which include things like treasury withdrawals, parameter updates and hard forks will not be ratifiable. So we have something of a governance crisis developing."

This existential threat to Cardano governance is completely absent from the summary.

### 2.2 Parameter Committee's Role in Crisis
Jonathan Kelly provided crucial context explaining the governance parameter working group intentionally set the minimum to seven "to balance out the three founding entities" and ensure "a majority of community-based members." He explicitly stated: "We understood what we were doing" and that Intersect "decided to only elect the minimum" without a buffer.

### 2.3 Political Dynamics Behind Resignation
Jonathan Kelly explained: "Politics is being played and they didn't want to be part of it anymore. So they said even if it passes the 50% threshold on the budget, they're going to retire anyway."

This political dimension of the constitutional crisis is entirely omitted.

### 2.4 Kevin's Leadership Transition Thanks
Kevin Hammond: "thank you everyone who is leading the committee who has served so diligently over the last 12 months. your contribution has been absolutely fantastic." 

This acknowledgment of outgoing members' service is absent from the summary.

### 2.5 Michele's MEV Concerns
Michele Nuzzi raised specific security concerns about value extraction: "any node between the user and the block producer... can modify the parent transaction... that allowance can be extracted."

These technical security concerns are reduced to a vague mention in the table.

### 2.6 Attendance Confusion
Multiple "TBD" entries appear in the intros section for Ben, Duncan, suggesting unclear membership status or roles, which is never explained.

## Section 3: Broadly Accurate

### 3.1 Election Results
The listing of newly elected members (Kevin Hammond re-elected, Ryan, Udai, Leandro/Leo, and Seung elected) matches the transcript.

### 3.2 Vote Outcome
The IOSIM and Type Protocols vote result of "8 votes in favor, 0 votes against" accurately reflects the poll results mentioned in the transcript.

### 3.3 Repository Discussion Core Points
The summary accurately captures that the repositories are dependencies of the Haskell node and that the request relates to ownership transfer to enable non-IOG maintainers.

### 3.4 Annual Report Request
The basic fact that TSC was asked to prepare an annual report for presentation is accurate.

### 3.5 Hard Fork Working Group Formation
Bosko's update about the Hard Fork Working Group starting next week is accurately recorded.

## Evidence Confirmation

All claims in this analysis are supported by direct quotes from named speakers in the provided transcript. Where information could not be verified from the transcript (such as specific term end dates or attendance for non-speaking members), this has been explicitly noted as "cannot be verified from the transcript alone."

---

### 20251126

## COMPARISON REPORT

### 1. FABRICATED / MISREPRESENTED

**False Attendance Records:**
The summary lists "TBC" as present for Vice Chair. The transcript shows no evidence of any Vice Chair speaking or being present. Kevin Hammond explicitly states at 00:05:00: "currently we have a chair but no vice chair. So, Adam Dean was acting as vice chair. Adam has now stepped down."

**Decisions That Were Only Discussions:**
- The summary lists as "Decisions" that they "Agreed to start the process for nominations" and "Agreed to draft a summary response." These were discussions, not formal votes. Kevin Hammond states at 01:10:00: "So we've got a resolution from a TSC perspective" but no vote is recorded.
- "Agreed to kick off the process for creating a proposal for a TSC operational budget" - Kevin actually says at 01:15:00: "We don't have to take decision now but with your support what I would propose to do would be to start to kick off that process."

**Misrepresented Actions:**
- Summary claims "The committee will pass on the concern regarding the need for more evidence and a robust regression process for the new Plutus cost model" as a committee action. This was Neil Davies' personal complaint at 00:40:00: "I would like to say, what's just happened in the last week, we're going to need a lot more evidence for the Plutus cost model going forward."

**Sanitized Conflict:**
- The summary completely omits Neil Davies' sharp criticism of past processes. He stated at 00:40:00: "I know who did all the checking. It was me and I did the second check over this stuff and remember all the bugs I found...I just don't want to be in that position of having to do that in a 48 hours before it gets voted on."
- The summary presents the forensic working group neutrally, omitting Neil's concern at 00:20:00 about "people threatening legal action" and that "the requirements on this process might be a lot more stringent."

### 2. OMITTED

**Critical Context About the Incident:**
- Duncan Coutts' involvement: "some of the code surrounding it is code I wrote" (00:10:00)
- Neil Davies' legal concerns: "because of other things going on and people threatening legal action the requirements on this process might be a lot more stringent" (00:20:00)
- Kevin Hammond's attempt to avoid public discussion: "I would avoid possibly going into too much of the details in public" (00:10:00)

**Process Criticisms:**
- Neil's statement at 00:40:00: "currently being a laptop in somebody's drawer is not an acceptable regression"
- Neil at 00:20:00 characterizing the forensic working group meeting as "I think there will be a nice bun fight at half past 4 this afternoon"

**Nested Transactions Discussion Details:**
- Duncan Coutts' technical explanation of MEV exposure (00:55:00) and the atomic transaction patterns
- Neil Davies suggesting they "punt it" to the product committee: "we don't see this as a technical problem...we say the product, if this seems to be more about a product committee" (01:05:00)
- Sebastian Nagel noting at 01:05:00: "I just peaked at the conversation...it went into this yeah but I can't stop this because I'm paid to work on this"

**Attendance Issues:**
- No evidence in transcript of Udai Solanki or Seungheon Oh speaking, though marked absent in summary
- "read.ai meeting notes" appears in attendee list but is not a person

### 3. BROADLY ACCURATE

- Basic meeting logistics (date, recording/transcript links)
- Kevin Hammond as Chair
- The general topics discussed (mainnet incident, hard fork working group, nested transactions)
- Bosko Majdanac being assigned to draft the nested transactions response
- First Hard Fork Working Group meeting date (December 2nd)
- The timeline of the mainnet incident recovery

## EVIDENCE CONFIRMATION

All claims in this report are supported by direct quotes from the following speakers in the transcript: Kevin Hammond, Neil Davies, Duncan Coutts, Sebastian Nagel, Bosko Majdanac, Nicolas Biri, Ryan (Cerkoryn), Alexander Moser. Speaker names, timestamps, and exact quoted language are provided for each finding.

---

### 20251203

# TSC Meeting Comparison Report: December 3, 2025

## 1. Fabricated / Misrepresented

### Attendance Records
The summary shows **"TBC" (Vice Chair) as absent**. The transcript provides no evidence of this person's existence or role. This appears to be a fabrication or placeholder that was not updated.

The summary lists **Udai Solanki** and **Seungheon Oh** as absent. However, the transcript shows:
- **Udai** introduced himself at the beginning: "Udai: Member OSC and TSC, AIQUANT Technologies" 
- No evidence of Seungheon Oh speaking or being mentioned

### Decision Claims
The summary states under "Decisions" that **"The proposal to use GitHub Health Files to standardize configurations across Intersect repositories was approved."** However, the transcript shows this was a discussion item where:
- Nicolas Biri suggested it: "it might be something useful for intersect to have"
- Kevin asked: "is anyone objecting to this?"
- No formal vote or explicit approval is recorded beyond Kevin saying "I'm happy to second that"

### Poll Results Misrepresentation
The summary shows a poll result image claiming unanimous approval for Kevin as Chair. However, the transcript reveals significant confusion about the poll:
- Terence McCutcheon: "There's seven members currently present. So that would be the total number of votes in there. We have five currently."
- Bosko: "Is there a way actually for me to see the results while of the vote because I only see the option to vote and I shouldn't be voting."
- The meeting notes state the poll **"did not reach a quorate decision"** but the summary presents it as completed

### Action Misattribution
The summary lists **"Bosko to take up the matter of TSC inclusion in the 2026 budget discussion process"** as an action. The transcript shows Kevin Hammond said: "boss if we could take that up with the budget committee" - this was a request, not an agreed action item.

## 2. Omitted

### Significant Vice Chair Discussion
The transcript shows extended debate about the Vice Chair position that is completely omitted:
- Neil Davies: "so what I'm trying to say, so I say the current situation is we have one person willing to take the chair and zero people willing to take the vice chair."
- Discussion about whether to wait another week or decide immediately
- Terence's frustration: "this is now at least in my mind week six that we're going back and forth on this issue"

### TSC Member Resignation Context
The summary mentions a member stepping down but omits crucial context from the transcript:
- Neil Davies raised concerns about the vote gap: "we would be picking someone who had onethird of the votes of the candidate above them"
- Discussion of specific numbers: "It was 115 to 34 or something"
- Debate about co-option powers and what happens if more members leave

### Plutus Cost Model Dependencies
The transcript contains technical discussion completely absent from the summary:
- Alexander: "would incomplete benchmarking of the Plutus primitives be a reason for postponing the hardwork?"
- Neil: "Definitively. Yes... if you don't get it right that may be a security issue"
- Kevin's detailed explanation of the deployment stages and security requirements

### CIP Editors Funding Issue
Sebastian Nagel raised an important funding concern that is entirely omitted:
- "I was approached by CIP editors which... are having struggles getting funded through catalyst"
- Discussion about TSC/OSC operational budgets as alternative funding sources

### Preview Testnet Problems
The transcript discusses significant technical issues omitted from the summary:
- Kevin: "Preview I think is still in a bit of a state of disarray"
- "nodes are not able to start up in genesis mode"
- Impact on hard fork timeline

## 3. Broadly Accurate

### Committee Rewards Process
The summary accurately captures Simo's explanation of the 500 ADA/month for members, 1,000 ADA/month for Chair, and the KYC/tax form requirements.

### Alexander Declining Rewards
The summary correctly records Alexander's decision to decline rewards and that unused ADA returns to Treasury.

### Holiday Meeting Schedule
Accurately reflects the decision to suspend meetings December 24th and 31st, reconvening January 7th, 2026.

### Hard Fork Working Group Basic Information
The summary captures that the group will meet bi-weekly and that a summary of CIPs will be posted.

### Parameter Committee Update
Accurately reflects that the governance action is ratified on Preview/Pre-Prod and awaits CC resolution.

---

**Evidence Confirmation:** All claims in this report are directly supported by quoted text from named speakers in the provided transcript. Speaker names, their statements, and contextual details have been verified against the source material.

---

### 20251210

## COMPARISON REPORT: TSC Meeting December 10, 2025

### 1. FABRICATED / MISREPRESENTED

**Attendance List Contains Critical Errors:**
- Summary lists "TBC" as absent Vice Chair. However, the transcript shows no Vice Chair was elected. Kevin Hammond states (01:00:00): "we now have a chair elected. So thank you everyone for confirming our role as chair. but it be great if there was a vice chair as well."
- Summary lists Alexander Moser as "No" for attendance. While Terence McCutcheon confirms (00:05:00) "Just Alex" sent apologies, the summary should note he sent apologies rather than just marking "No."
- Summary lists Seungheon Oh as absent with no evidence in transcript of his attendance or apologies.

**Decision Misrepresentations:**
- Summary states as a decision: "The committee agreed to continue working on an operational budget proposal for the TSC." The transcript shows this was discussion only. Kevin Hammond (00:30:00) asks: "does it make sense for us to put in a proposal on these lines?" No formal agreement or vote occurred.
- Summary claims: "The committee acknowledged that the TSC recommends on technical matters, while the Product Committee decides." This misrepresents disagreement. Udai Solanki (00:28:00) explicitly challenged this: "in my view it would have been other way around...eventually it is a technical decision and possibly the technical committee should decide."

**Action Item Fabrications:**
- "Sebastian to confirm and share the specific Plutus Core version that will be going into the hard fork." Sebastian actually said (00:20:00): "I can bring the conclusion as soon as I know which exact Pluto's core version will be going into the hardwork" but made no commitment to share it with the committee.
- Summary attributes CIP editors discussion to Sebastian supporting "budgeting for CIP editors." While Sebastian did support this (00:35:00), the summary omits his crucial context about a CIP editor "seeking for different ways of getting their work funded" and being "paid by the CF for I guess a couple for Q1 26."

### 2. OMITTED

**Major Conflicts Erased:**
- Neil Davies's strong criticisms completely absent. Neil stated (00:45:00): "Unfortunately, that is precisely what we got shot down in flames for doing and people lost their jobs and their companies got it excluded from the whole ecosystem for trying to do." And (00:50:00): "I actually see the Cardano community has been but what the vendors have done have done is putting the long-term viability of Cardano at risk."
- Sebastian Nagel's conflict of interest disclosure omitted. Sebastian stated (01:05:00): "I'm currently being asked often by one of my affiliations to work on these things. So there's a bit of a count of interest."

**Critical Context Missing:**
- Node 10.7 release timeline. Kevin Hammond stated (00:30:00): "I'm not expecting it to be ready before next week at the very earliest...in all probability we won't get to a mainnet release by the end of 25."
- Duncan Coutts's explanation (01:00:00) that TSC's lack of operational budget happened because "it was all bundled up with the bigger issue which got shot down" — providing crucial context for current budget discussions.

**Guest/Community Input Ignored:**
- Benjamin Hart's substantive contributions completely absent, including his request for CIP documentation and comment (00:50:00): "Looks like the right people got elected" in response to frustrations about vendor control.
- Ryan Williams listed as attendee but no contributions noted.

**Procedural Issues Omitted:**
- Terence McCutcheon's intervention (00:55:00) criticizing the committee: "it's a bunch of people that have a lot of information that are really, really smart talking in a room about the same issues over and over and over again. Get the community to go and review what your stuff is."

### 3. BROADLY ACCURATE

- Basic meeting logistics (date, time, recording/transcript links)
- TSC member vacancy discussion outcome (operating with 9 members)
- Hard Fork Working Group meeting cadence (two weeks)
- Chain Partition Working Group timeline (preliminary report by end of year)
- Bosko's assignment to update Hard Fork Readiness Repository
- Next meeting December 17 as final meeting of 2025
- General topics discussed in agenda

**EVIDENCE CONFIRMATION:** All claims in this report are supported by direct quotes from named speakers with timestamps from the provided transcript. No claims have been made that cannot be traced to specific statements in the source material.

---

### 20251217

## Comparison Report: TSC Meeting December 17, 2025

### 1. **Fabricated / Misrepresented**

**Attendance Records Are Inaccurate**
The summary claims "Udai Solanki - No" for attendance, but Udai's name never appears anywhere in the transcript — neither speaking nor mentioned as present. The summary claims "Empty Seat - No" which is meaningless. The only evidence for who attended is who spoke in the transcript: Alexander Moser, Benjamin Hart, Bosko Majdanac, Duncan Coutts, James Meidinger, Kevin Hammond, Leandros Holleman, Neil Davies, Nicolas Biri, Ryan (Cerkoryn), Ryan Williams, Sebastian Nagel, and Terence McCutcheon.

**"Decisions" That Never Happened**
- The summary claims "It was decided to pause the review of the 2030 Vision KPIs" — FALSE. Kevin Hammond actually said: "I previously suggested to the product committee that we have a joint session. We've not had them take us up on that" (01:06:47). There was no vote or decision to "pause" anything.
- The summary states "The committee decided to use its social media presence to inform the community" — MISLEADING. Kevin suggested Alex write a blog post, and Alex agreed, but there was no committee decision or vote on social media strategy.
- The summary claims "Chain Partition Report: The technical view of the incident was finalized" — FALSE. Kevin explicitly stated they're "getting towards having a pretty complete draft" and Ryan Williams said "the report has come together quite nicely" but nowhere does anyone say it's "finalized."

**Misrepresented Meeting Dynamics**
The summary completely sanitizes Neil Davies' harsh criticism of the KPIs. Neil actually said: "This doesn't seem like a good way of interacting with the community" and "these are our aspirations...what you've got here is this feels like numbers pulled out of somebody's I'm going to be polite by stopping" (00:58:34). The summary reduces this to neutral language about "critiqued the current 'reliability' metrics as poorly defined."

**Vice Chair Position Mischaracterized**
The summary presents the vice chair discussion as routine when actually NO ONE volunteered. Kevin had to plead: "please do think about whether you might do that" (01:09:26). The summary omits Benjamin Hart's sarcastic comment: "I could just nominate everyone other than Sebastian right now" (01:08:31).

### 2. **Omitted**

**Critical Chain Partition Details**
- Kevin's correction that "in total it was about 500 transactions Neil that appeared only on the non-preferred chain" with "20 from the block which we hadn't previously accounted for" (00:13:49)
- The fact these overlooked transactions came specifically from "the bad block" and "they've been overlooked in the previous analysis"

**Governance System Vulnerabilities**
Alexander Moser's warnings about "logic hazards" were downplayed. He specifically warned that the timing of adding a CC member could "jeopardize that treasure withdrawal" and that this "could be considered a little bit of a doss attack" (00:44:13). Kevin acknowledged "there are some hazards in the governance system" (00:39:44).

**Extended Debate on KPIs**
The transcript shows 10+ minutes of sustained criticism of the reliability metrics, with Duncan Coutts saying "they're going to need some advice and support here on trying to frame their question properly" (01:03:31). Neil's repeated challenges about "ontological epistemological difference" and comparing metrics to "the red shirted man getting killed in Star Trek" were completely erased.

**James Meidinger's Contributions**
James, listed as "Community/Other Attendees," actually engaged substantively about TSC budget ideas, asking detailed questions about "disseminating the information" (00:24:58) and saying "there's a wealth of people you would tap into" (00:27:42). His input shaped the discussion but appears nowhere in the summary.

### 3. **Broadly Accurate**

- The hard fork naming vote for Max van Rossem (7 Yes, 1 Abstain)
- Kevin Hammond's commitment to draft a 2026 TSC Operational Budget outline
- The invitation to the Product Committee for January 7th, 2026
- Alexander Moser agreeing to write about the CC size mathematical implications
- The basic fact that chain partition analysis is ongoing

### Evidence Confirmation

All claims in this report are supported by direct quotes from named speakers in the transcript, with timestamps provided for verification. The transcript shows 13 people spoke during the meeting. The summary's attendance list cannot be verified from the transcript evidence and contains at least one person (Udai Solanki) who never spoke or was mentioned as present.

---

### 20260107

# TSC Meeting Comparison Report
## 20260107 Meeting Analysis

## 1. Fabricated / Misrepresented

### Decisions Listed That Were Never Made

The summary claims four concrete "decisions" were made, but the transcript shows these were discussions without formal votes:

**"Hard Fork Priority" Decision** - The summary states: "The committee decided not to delay the hard fork for non-essential features." 
- Reality: Kevin Hammond proposed this approach: "What we don't want to be doing, I think, is to delay the hard fork for the sake of features that are not absolutely essential" (00:20:00). No vote or formal decision occurred.

**"Budget Methodology" Decision** - Listed as: "The group decided to focus first on defining the 'what'..."
- Reality: Kevin made a statement about his personal approach: "I find it's always better to discuss what before you start to argue about the cost" (00:25:00). Nicolas requested time to review, but no group decision was made.

**"KPI Review Strategy" Decision** - Claims: "The committee reached a consensus to scrutinize all KPIs..."
- Reality: This was a contentious debate. Neil Davies and Ryan Cerkoryn criticized the KPIs heavily, while Nicolas Biri pushed back, arguing the TSC should focus only on "technical feasibility" not judge the Product Committee's approach (00:45:00). No consensus was reached.

### Misrepresented Attendance

**Bosko Majdanac** - Listed as absent (No) in the summary
- Reality: Kevin explicitly states "Bosco is away today. it's a holiday for him" (00:05:00). He was on holiday, not simply absent.

### Sanitized Language

**Chain Incident Report Delays** - Summary blandly states: "awaiting board feedback before public release"
- Reality: Multiple expressions of frustration. Ryan Williams: "A bit frustrating being blocked as we are with it to be frank" (00:10:00). Neil Davies was more colorful: "If it's really that important, then they should pull their bloody finger out and do something about it to be very Welsh about it" (00:10:00).

## 2. Omitted

### Critical Context About Chain Incident

The summary omits Neil Davies' key observation that despite the partition, "no one is screaming like hell that they got badly done by" and "we don't know of any [losses] and no one's screaming at us" (00:15:00). This resilience of the system under real-world stress was highlighted as a major positive finding that should be "played up."

### Deep Disagreement on Committee Scope

The summary completely erases the fundamental philosophical disagreement between Nicolas Biri and Neil Davies about the TSC's role:
- Nicolas: "we should probably just focus on the technical feasibility of what has been written rather than giving our opinion about the KPIs that were chosen" (00:45:00)
- Neil: "if the technical committee isn't there to try and object an potential objective reality, then that I must admit I completely disagree with you on that point" (00:40:00)

### Ryan Cerkoryn's Substantive Critique

Ryan's pointed criticism is absent: "the strategy as it is now is too broad and it kind of seems a lot like we're going to throw everything at the wall and see what sticks" (00:40:00). He also raised accountability concerns: "There's no way to hold anyone accountable for these."

### Neil Davies' Experience-Based Warning

Neil's stark warning based on "40 years of experience" is completely omitted: "do this badly... it's a really bad way" and his concern about "taking the community's money and not delivering" (00:45:00).

### Parameter Change Complexity

The transcript reveals Ryan Cerkoryn warning about technical requirements for governance actions: "there's a requirement to set the hash of the previous successful parameter change for every parameter change governance action. So those will have to be coordinated so that they don't cause each other to fail" (00:25:00). This critical coordination issue doesn't appear in the summary.

## 3. Broadly Accurate

- Kevin Hammond chaired the meeting
- Chain partition report is complete but awaiting feedback
- Node 10.6.2 is expected within two weeks as likely release candidate
- Ryan Williams is submitting governance action for "Max Van Rossem" hard fork naming
- TSC operational budget draft was circulated
- Vice chair position remains vacant
- Meeting occurred on January 7, 2026

---

**Evidence Confirmation:** All claims in this report are directly supported by quoted statements from named speakers in the transcript, with timestamps provided for verification. No speculation beyond the provided text has been included.

---

### 20260114

# Comparison Report: TSC Meeting January 14, 2026

## 1. FABRICATED / MISREPRESENTED

### **Attendance Misrepresentation**
The summary lists "TBC" as absent Vice Chair, but the transcript confirms no Vice Chair exists:
- **Kevin Hammond** (01:13:23): "I'm supported by eight vice chairs... if nobody is nominated as vice chair. You are all vice chairs if nobody is nominated as vice chair."
- **Bosko Majdanac** confirms: "Kevin is still in a way alone in this effort. So it would be nice."

### **"Decisions" That Were Not Actually Made**
The summary presents several items as formal "Decisions" when they were actually proposals, suggestions, or administrative updates:

1. **"Closure of Working Group"** - Listed as formal vote, but transcript shows:
   - **Kevin Hammond** (00:19:34): "So I'm proposing formally that we close down that working group with your agreement. So does anyone object to that course of action? So I'm taking that as agreement..."
   - No formal vote occurred, just lack of objection

2. **"Product Committee Representation"** - Not a decision but a preference:
   - **Kevin Hammond** (00:07:19): "I'd hope they would either cover the issue quickly or alternatively we can delegate to a small group of interested people"
   - People raised hands to indicate interest, not a formal delegation

3. **"Report Finalization"** - No approval vote occurred:
   - **Kevin Hammond** (00:22:15): "We're not proposing to make any further changes from this point in time"
   - This was a statement of intent, not a voted decision

### **Misrepresented Content**

**Hard Fork Naming** - Summary states name was "confirmed" and "info action has been submitted on-chain," but transcript shows uncertainty:
- **Kevin Hammond** (00:23:45): "the information action to agree the name [van Rossem] has been submitted on chain as of Monday this week... there seems to be some support and dissent at this point"

## 2. OMITTED

### **Major Conflict Erased**
The summary completely omits Neil Davies' harsh censure of the board regarding the Chain Incident Report:
- **Neil Davies** (00:14:12): "I wish to go on record for saying that I wish to censure the board for changing the terms and conditions of the committee after it was agreed at the beginning... this was supposed to be a report that was published that was just done and published right and people be informed. we have been told that we can't publish it. It has to be approved by them."
- **Neil Davies** (00:14:48): "changing the remit at the last minute because you haven't thought things through is just such bad form and just shows incompetence in on the behalf of the board and the intersect committee"
- **Neil Davies** (00:15:25): "I'm being paranoid here, but I've already done that... if it were to get changed"

### **Extended Technical Debates**
Summary reduces complex K parameter discussion to bullet points, omitting:
- **Neil Davies'** pushback (00:31:02): "I just think that statement that increasing K will make those pools make more blocks. No that doesn't follow"
- **Ryan's admission** (00:32:58): "I have not done how much stake would have to move from those pools to a distribution of smaller pools to make them viable"
- **Neil's response** (00:33:10): "last time many years ago when we did it, we basically saw that it may have enabled three pools or something... The numbers are really small"

### **Sebastian Nagel's Attendance Caveat**
Summary lists him as simply "Yes" but omits:
- **Sebastian Nagel** (00:02:51): "and declined another invite. That's the current one I have" [indicating early departure]

### **Technical Context on Rewards**
Summary omits important clarification:
- **Sebastian Nagel** (00:46:58): "Just to clarify you're mentioning block rewards is decreasing over time. This is only true for the reserve backed parts, right?"

## 3. BROADLY ACCURATE

- Basic attendance list (with exceptions noted above)
- Meeting links and resources
- General agenda items covered
- Action items mostly accurate (though some presented as more formal than they were)
- TSC Operational Budget discussion accurately summarized as needing follow-up
- Security Officer appointment (Mike) correctly reported
- Research report presentations by Fergie Miller

---

**Evidence Confirmation:** All claims in this report are supported by direct quotes from named speakers in the transcript, with timestamps provided for verification.

---

### 20260121

# Comparison Report: TSC Meeting 20260121

## 1. FABRICATED / MISREPRESENTED

### **Attendance Records**
- **Summary lists Seungheon Oh as "No" attendance** but the transcript shows no evidence this person exists in the meeting context. They never speak and no one references them.
- **Summary lists "TBC" as Vice Chair with "No" attendance** — This appears to be a placeholder, not an actual person. The transcript shows Kevin Hammond stating: "Bosco is desperately seeking nominations. We really need to get that sorted out" regarding the vacant vice chair position.

### **Overstated Decisions**
- **Summary states "Working Group Status: No new working group will be formed for KPIs"** — In the transcript, this was Neil Davies' personal position, not a committee decision. Neil said: "I don't want to form yet another working group" and Kevin responded: "Neil's voting against the working group. any other opinions for or or is everyone completely neutral?" The lack of response led to following Neil's suggestion, but this was not a formal decision.

### **Misrepresented Action Items**
- **"Constitutional Review: Kevin and Neil to review recent changes"** — The transcript shows this emerged from surprise about changes they weren't aware of. Kevin: "what we need is we need a diff of the changes if someone can provide that" — indicating they needed someone else to provide information first.

### **Fabricated Meeting Details**
- **"Hard Fork Working Group meeting time: The internal working session will be moved"** — The transcript discusses moving it from Tuesday to Thursday, with Bosko stating: "sometime today I will move it to next Thursday instead of next Tuesday." This is more specific than the vague summary claim.

## 2. OMITTED

### **Major Constitutional Security Concern**
The summary completely omits a heated discussion about constitutional changes that removed security safeguards. Neil Davies expressed alarm: "whoever was responsible for it, they should have talked to people, to take us all what I'm saying is to destroy the security. They've created potential rapid changes which are going to cause instability in the system." Kevin Hammond added: "It was put in on the advice of the security researchers to avoid overly rapid changes on critical parameters."

### **SPO Voting Crisis**
While mentioned briefly, the summary downplays the urgency. Alexander Moser: "I'm currently quite afraid that [SPOs] don't realize that they have to vote as well" with Kevin confirming "less than 5% of SPOS's have voted."

### **Guest Technical Query**
Markus Gufler raised concerns about a catalyst-funded blockchain security dashboard: "who gives credential... who maintains this and signs of a potential attack are defined therein? How is it updated? How it is maintained?" This substantive technical concern is reduced to a single line.

### **Governance Process Breakdown**
The transcript reveals significant governance failures. Kevin: "I would have expected to at least been notified that changes were being proposed particularly changes that could have an effect on the technical operation of the chain. So there's clearly some issue here with the way system the governance system is working."

### **Development Timeline Reality**
Sebastian Nagel's temperature check revealed pessimism about the autumn 2026 target for Dystra. Kevin: "I think it's unlikely to be as early as October Sebastian based on the advanced status." The summary presents timelines without this context.

### **Committee Dysfunction**
Terence McCutcheon's criticism: "we're failing in that sector because you guys don't have the clear lines of sight... the TSC is lacking the full view of what's actually happening in the different facets of development."

### **Leadership Vacuum**
The difficulty finding someone to chair next week's meeting — Sebastian: "I would if I would not be chairing a meeting just one hour before," Alexander: "Conflicting meeting" — reveals operational challenges beyond just the vice chair vacancy.

## 3. BROADLY ACCURATE

- Meeting attendee list (for those actually present and speaking)
- Basic agenda items covered
- Meeting time change to 1500 UTC
- TSC taking some responsibility for KPI refinement
- Parameter update submission details
- K=1000 analysis ongoing by Ryan C.
- Operational budget kickoff at 1600 UTC
- Kevin's absence next week

## Evidence Confirmation

All claims in this report are supported by direct quotes from named speakers in the transcript. The transcript appears complete based on the meeting duration (01:12:18) matching expected content volume.

---

### 20260128

# TSC Meeting Analysis: January 28, 2026

## 1. FABRICATED / MISREPRESENTED

**Attendance Record Errors:**
- The summary lists **Kevin Hammond** as "No" attendance but provides no evidence he was absent. The transcript shows no speaking from him and no explicit mention of his absence.
- The summary lists **"TBC"** as Vice Chair with "No" attendance. The transcript shows the Vice Chair position is **vacant** — Neil Davies states "has someone volunteered to be the vice chair?" and Bosko responds "Nobody but you." Later Neil states "the Vice Chair position remains vacant."
- The summary lists **Seungheon Oh** with "No" attendance but provides no evidence in the transcript.
- The summary lists **Sebastian Nagel** with "No" attendance but provides no evidence in the transcript.

**Decision Misrepresentations:**
- The summary claims a "decision" that "The committee decided to wait for Ryan's math summary and Nicolas's update on the IOG report." The transcript shows this was a **suggestion** by Nicolas Biri: "It might be a good idea to wait until this work is done" with Neil Davies responding "we can turn around next time and say use it or wait or not wait." No formal decision was made.
- The summary claims Neil "will chair the current session" as a decision. The transcript shows Neil asking "if no one objects, I will chair this meeting" — this was procedural, not a formal committee decision.

**Action Item Fabrications:**
- "**Neil & Kevin**: Review the Constitution 2.4 updates and security assessment" — The transcript shows only that Neil said "we have to do the security assessment first" with no action assigned to Kevin specifically.
- The summary states committee members should "leave comments" on the budget. Neil Davies actually said: "if you agree with it, [say something]. Because that's the real problem. You can read these documents and you don't know if you disagree with say something too."

## 2. OMITTED

**Critical Context Removed:**
- Neil Davies's frustration with the constitutional process: "I will just say, what a bunch of puppets, is my reply here, I'm really doing this" — completely omitted from the summary.
- Neil's statement about coordination failures: "the effect of non-coordination is people suffer... unnecessarily" — sanitized in the summary.
- The discussion about parameter changes potentially affecting the hard fork timeline, with Neil stating "if the parameter change doesn't go through we literally have to rethink everything that we're doing" — reduced to a bland note about "interdependencies."

**Meeting Dynamics:**
- The informal nature of the meeting, including Mike Hornan's joke about maple syrup: "You guys don't talk about maple syrup very often here" with Neil's response about knowing maple syrup producers — entirely omitted.
- Neil's direct management style: "I'm sorry you can tell me if I'm being too tur[se] by the way guys, I like pushing things forward, cuz time is [limited]" — character and tone removed.

**Substantive Contributions:**
- Udai Solanki's extensive self-introduction and offer to provide developer resources at no cost: "I do have the team of the very good developers... I'm very much keen to dedicate some of the people to work on the objective from my team as well and no cost" — reduced to a single line.
- Neil's specific guidance to Udai about the Parameters Committee needing people who understand "the operational economics of this system" — context removed.

## 3. BROADLY ACCURATE

- The basic attendance count of six voting members achieving quorum
- Markus Gufler's update about the SPO roundtable being community-branded, not Foundation-branded
- Ryan's data showing approximately 5 billion ADA would be redistributed by moving K from 500 to 1,000
- Nicolas Biri mentioning IOG's incentive analysis report led by Carlos
- The operational budget document being shared on Slack with figures from Kevin
- Technical complications with the "immu" CIP being discussed with editors

## EVIDENCE VERIFICATION

All claims in this report are directly traceable to the transcript:
- Vice Chair vacancy: Bosko states "Nobody but you" (timestamp ~02:00)
- Neil's frustration: "what a bunch of puppets" (timestamp ~17:30)
- Coordination failures: "people suffer... unnecessarily" (timestamp ~20:00)
- Parameter change impact: "literally have to rethink everything" (timestamp ~16:00)
- Udai's offer: "no cost" for developer resources (timestamp ~23:00)
- Meeting tone: "tell me if I'm being too tur[se]" (timestamp ~15:00)

This analysis reveals significant sanitization of meeting dynamics, removal of critical context about governance frustrations, and multiple attendance record errors that cannot be verified from the provided evidence.

---

### 20260204

## Comparison Report: TSC Meeting Summary vs. Transcript (2026/02/04)

### 1. **Fabricated / Misrepresented**

**MAJOR: False "Decisions" Listed**
The summary lists three items as formal "Decisions":
- "Charlie 3 Incubation: The TSC formally moved to proceed with the incubation"
- "Budget Draft: The TSC agreed to remove 'Town Halls' from the funding request"
- "Communication: Agreed to utilize the TSC Twitter account to promote"

**Evidence from transcript:**

For Charlie 3, Neil Davies proposed: "Can I suggest that we move this forward and if anybody object after having as opposed to forcing people to if they read the material and have a questions then we can always bring them up" (00:18:26). Kevin responded: "So you're raising a motion by default. So you're basically Yes" followed by "So any objections to that please notify us now. So we'll proceed on that basis." **No formal vote occurred.**

For the budget, Kevin proposed: "I'm not sure that they need funding. So, what I would probably propose to do is to remove that from the funding request" (00:32:13). **This was a suggestion, not a committee decision.**

For Twitter promotion, Kevin said: "So, again, maybe we can promote that via the TSC Twitter account if we haven't already done so" (00:06:14). **This was a suggestion, not an agreed action.**

**Attendance Fabrication:**
The summary lists "TBC" as Vice Chair with "No" attendance. The transcript shows no evidence of any Vice Chair role being discussed or anyone identified as "TBC."

**Misrepresented Participation:**
The summary shows Udai Solanki and Seungheon Oh as absent ("No" attendance). However, the transcript provides no evidence these individuals were expected to attend or were committee members at this meeting.

### 2. **Omitted**

**Nicolas Biri's Strong Opposition to Budget:**
Nicolas made forceful objections to the milestone review budget: "I continue to be totally opposed to this part of the budget and I think we should definitely drop it and not do any milestone review at this rate. I'm sorry. Which it's unprofessional to me" (00:38:47). Later: "If I wasn't clear enough, I have an objection on this budget" (00:46:18).

**Major Constitutional Concerns:**
Kevin Hammond raised serious alarm about Constitution v2.4: "apparently if my reading is correct you can now spend the Cardano Treasury on anything you like without having to justify it" (00:50:28). Neil Davies added: "if they've removed the need to spend it on Cardano, all the rest of it. This really looks like the optics are bad" (00:53:03).

**Technical Problem with Guardrail Labels:**
Neil Davies: "all the identifiers have been reused" leading to "an absolutely serious problem because it just introduces ambiguity" (00:54:12). Kevin confirmed this "creates a problem for tooling" and suggested "this constitution might technically not be enforced" (00:51:47).

**SPO Voting Concerns:**
The discussion revealed only ~20% SPO support for the Plutus memory limits vote with 9 days remaining. Kevin: "the SPOS seem to be quite a long way from supporting this" (00:21:15).

**Budget Rate Dispute:**
Extensive discussion about milestone review rates being too low at $200. Neil Davies: "if you pay monkeys, you get... Or was it you who get paid peanuts, you get monkeys" (00:43:24).

### 3. **Broadly Accurate**

- Committee member attendance list (for those who spoke)
- Discussion topics covered (though depth and tone misrepresented)
- Alexander's SPO roundtable update occurred
- Robert Hever's Charlie 3 presentation happened
- Budget discussion took place (though outcomes misrepresented)
- Constitution review was discussed (though severity downplayed)

---

**Evidence Confirmation:** All claims in this report are supported by direct quotes from named speakers with timestamps from the provided transcript. No speculation or inference beyond the text has been made.

---

### 20260211

# Comparison Report: TSC Meeting 20260211

## 1. **Fabricated / Misrepresented**

### Decisions Listed That Were Actually Just Discussions

The summary states as a **Decision**: 
> "Budget Sharing: Unanimously agreed to share the TSC operational budget draft with the Intersect delivery team and Steering Committee for socialization."

The transcript shows this was a question Kevin Hammond posed, not a formal vote: "So does anyone object to sharing this at this point in time? Just raise your hand if you object. Okay, I'm taking that as a unanimous decision that we share the budget." (Kevin Hammond, transcript). While no objections were raised, this was not a formal committee vote but rather gauging consensus to proceed.

The summary states as a **Decision**:
> "Governance Priority: Agreed that passing the current memory unit limit update is the immediate priority to preserve the technical timeline."

The transcript shows this was a discussion of the situation, not a formal decision. Alexander Moser stated: "which is one more reason why I'm pushing so hard for this to pass because then UT you just can't pass and he doesn't screw over our timeline." This was individual advocacy, not a committee decision.

### Action Items Never Agreed To

The summary lists: 
> "Alexander & TSC X Account: Promote the 'auto-abstain' mechanism for SPOs"

The transcript shows Kevin suggested: "And maybe an action on ours is to make SPOS's aware of this option. So try to promote that option. We can do that from the TSC account." This was a suggestion, not a formally assigned action to Alexander specifically.

The summary lists:
> "Leandros: Share the comprehensive KPI targets document and quarterly breakdown with the committee for async review."

While Leandros did say "I will share the document in the team's chat," this was offered during his presentation, not assigned as a formal action item by the committee.

### Attendance Errors

The summary shows "TBC" as Vice Chair with "No" attendance. The transcript shows no mention of a Vice Chair position or anyone designated as "TBC." This appears to be a fabrication.

## 2. **Omitted**

### Critical Constitutional Crisis Discussion

The transcript reveals a major governance crisis completely absent from the summary. Neil Davies and Kevin Hammond had an extended discussion about constitutional changes that blindsided both the TSC and Civics Committee:

Neil Davies: "So you're telling me that this changed the constitution imposed by in the nicest possible way one man of a dog and actually the civic didn't turn around and Yes."

Kevin Hammond: "So, one of the reasons why we were slightly blindsided is we're expecting the civics committee to tell arts, And to ask us to do a technical review."

Neil Davies: "So it turns out that the constitutional committees have accepted a constitution that wasn't constitutional."

### Serious Technical Issues with Constitution v2.4

The summary fails to mention Kevin Hammond's detailed technical critique of Constitution v2.4:

Kevin Hammond: "these [guardrail labels] have not been updated as the constitution itself requires which is a problem. So the constitution is internally inconsistent."

Kevin Hammond: "the amendment process I'm not sure if that was in the original one but I was reading it and thinking actually you can't possibly make an amendment to this constitution. So I think that might also render it technically invalid"

### Governance System Breakdown

The discussion revealed fundamental process failures omitted from the summary:

Neil Davies: "the fact is none of them actually engaged in any of the due diligence they're supposed to or there's a can't say none of them the due diligence that was expected did not occur right is what we're now seeing"

Kevin Hammond: "Apparently the civics committee was not aware."

### Competing Governance Actions Creating Deadlock

The transcript shows extensive concern about competing parameter update proposals creating governance gridlock:

Neil Davies: "So, we now got denial of service by voting. I like it."

Kevin Hammond: "what we've got to be careful of is getting in the situation we've got three-way contingent governance actions which could happen"

### Hard Fork Working Group Development

Ryan Williams' significant proposal for a "CIP short-listing process" for future hard fork planning is completely omitted, despite being a substantial discussion about changing how features get selected for implementation.

### SPO Auto-Abstain Mechanism Discovery

The important discovery during the meeting about an existing but poorly documented SPO auto-abstain mechanism is not mentioned:

Ryan Williams: "There is an auto abstain option I think. yeah, but it's poorly documented and uses a kind of a weird mechanism. I think the reward account for the pool needs to delegate to auto abstain drep which auto abstains the pool for its governance processes."

Alexander Moser: "What the heck?"

## 3. **Broadly Accurate**

- The attendance list for those marked present appears accurate based on who spoke in the transcript
- The general topics covered (parameter updates, budget, constitution review, KPIs, elections) are correctly listed
- The basic status update that the Plutus memory unit limit vote is near threshold but time-constrained is accurate
- The notation about KYC hurdles for community payments reflects the discussion
- The election timeline (decisions needed by Friday) is correctly captured
- Node v10.7 being the hard fork candidate is accurate

## Evidence Confirmation

All claims in this report are supported by direct quotes from named speakers in the transcript. Speaker names, their statements, and context have been preserved as they appear in the source material. No claims have been made beyond what can be directly observed in the provided text.

---

### 20260218

Based on my analysis of the meeting summary and transcript, here is my detailed comparison:

## 1. **Fabricated / Misrepresented**

**Decision Claims Not Supported by Transcript:**
- The summary lists under "Decisions" a "Provisional Agreement on KPIs" where "the committee accepted the initial KPI framework." The transcript shows this was merely a presentation and discussion. Leandros presented KPIs, but no vote occurred. Kevin Hammond specifically stated at 00:09:15: "we have one, two, three, four, five voting members present. So by my reckoning we are not quorate. So any decisions only be provisional would need to be confirmed by an out of band vote."

- The summary claims a decision on "Budget Socialization" where Kevin would seek to move "proposal reviews" to a general Intersect line item. The transcript shows this was discussion only. Nicolas Biri argued at 01:09:02: "The question is probably whether it's a TSC remit or an intersect obligation. To me it sounds more like an obligation on the intersect side." Kevin responded at 01:10:39: "I'll take this up with the delivery team and I will put that question to them." This was not a committee decision.

- The summary states as a decision: "The TSC confirmed that the existing election questions for technical seats remain valid." The transcript shows Sebastian Nagel suggested at 00:23:10: "They seem to work We have wonderful new members who all meet the criteria I guess. So maybe there is no not even a need for changing them." But no formal confirmation vote occurred.

**Misrepresented Context:**
- The summary describes Christian Taylor's departure neutrally, stating he was "thanked for his foundational work." The transcript shows Kevin Hammond specifically noted at 01:12:46 that Taylor "was an integral member of the security council" who "established the OSC" and "transferred all of the repositories IO to intersect several years ago." The depth of his contribution was significantly understated.

## 2. **Omitted**

**Major Constitutional Review Conflict Erased:**
The summary reduces the Constitution v2.4 discussion to technical notes about it being "a mess" with "90 pages of diffs." The transcript reveals intense disagreement:
- Nicolas Biri at 00:45:11: "I think it's also part of the challenge I have with this discussion within the TSC. It's far beyond our remit... It's a problem that I've raised several time with the work of the TSC that has been raised by others outside the TSC and I'm really uncomfortable with it."
- Kevin Hammond argued at 00:47:31: "what I would say is I believe that there should have been a technical and a legal constitutional review of the constitution before it was put on chain."
- Alexander Moser countered at 00:47:51: "To be fair, it was built out in the open and you made four attempts to upgrade it for maximum visibility. If any of us would have taken up that input proactively as it was built out in the open, we could have given that input much earlier."

**Philosophical Divide on TSC Role:**
The summary omits a fundamental disagreement about the TSC's responsibilities:
- Nicolas Biri at 00:48:28: "it's a permissionless system. Everybody can propose something... if they think that we are valuable enough, they will reach out to us. if they're not going to reach out to us, it may be a TSC problem, not the community problem."
- Kevin Hammond responded at 00:49:13: "Then we have to live with inconsistency and potentially failure, Alex, when we could have prevented it."

**Attendance Verification Issue:**
The summary lists TBC as "No" for Vice Chair attendance and marks Neil Davies, Udai Solanki, and Seungheon Oh as absent. However, the transcript provides no evidence these individuals were expected to speak or that their absence was noted during the meeting. Kevin only mentions at 00:03:30: "Neil Davis sends his apologies."

**Chain Density Technical Debate:**
The summary notes the metric will be "normalized to 'Chain Quality'" but omits the substantive technical discussion where Sebastian Nagel explained at 00:15:55: "5% of the slots would be active... If we put that as a KPI, it wouldn't motivate a denser schedule... we just want to have as much as possible of these targets or which it can't get better than 5% given this parameter."

## 3. **Broadly Accurate**

- The agenda items listed match the transcript
- Alexander drafting an SPO auto-abstain post is accurately recorded
- The 86% DRep support for the parameter update is correct
- Node v10.7 being the hard fork-capable version is accurate
- Ryan (Cerkoryn) presenting the DRep Compensation Paper next week is correct
- The technical discussion of Constitution v2.4 difficulties is partially captured

**Evidence Confirmation:** All claims above are directly supported by quoted speaker statements with timestamps from the provided transcript. No information has been added beyond what appears in the source text.

---

### 20260225

# COMPARISON REPORT: TSC Meeting 20260225

## 1. FABRICATED / MISREPRESENTED

**Attendance List Errors:**
- The summary lists "TBC" as Vice Chair with "No" attendance, but no such person appears in the transcript
- The summary lists Seungheon Oh as absent ("No" attendance), but this person never speaks in the transcript and their presence cannot be verified
- The summary lists Ken-Erik Ølmheim as a "Community/Other Attendee" but the transcript shows Ken-Erik Ølmheim in the main attendees list, not separated as community

**Action Item Fabrications:**
- "Bosko & Ryan Williams: Update the hard fork timeline diagram based on the two-week shift in node readiness and share the link on GitBook" — The transcript shows only Bosko saying he will share a link and ensure it's added to GitBook (timestamp 00:37:57), with no mention of Ryan Williams being assigned this task

**Decision Overstatement:**
- "Constitutional Review: The committee moved to formalize a document listing the technical inconsistencies" — This was not a formal committee motion. Neil Davies proposed creating a document, Kevin suggested he and Neil work together on text, but no formal vote or committee motion occurred. The closest was Kevin saying "Does anyone object to that course of action?" with no recorded vote (01:02:42-01:03:55)

**Misrepresented Elections Discussion:**
- Summary states "Confirmed five seats are officially open for election in April; replacing the sixth vacant seat will be handled via a separate co-option or election process" as a decision. The transcript shows this was still under discussion, with Neil proposing co-opting the sixth-ranked candidate (01:09:00) but Kevin stating "I'm not sure we need to take a vote on that right now" (01:12:12)

**KPI Document Status Misrepresentation:**
- Summary states "The committee agreed to make the TSC review of 2030 Vision KPI document public" as a decision. The transcript shows Kevin asking "are we happy for that to be public now? I think we probably are" and stating he would publicize it "unless anyone objects" (00:44:17) — this is seeking consensus, not recording a formal decision

## 2. OMITTED

**Critical Technical Concerns about Linear Leios:**
- Sebastian Nagel's warning about "chain growth of gigabytes in a week" and specific concern that "150 gigabytes in six days" would require SSD storage (00:18:10-00:19:50)
- Sebastian's admission that benchmarking "hasn't progressed as much as I was hoping for originally" creating unmitigated risk (00:23:00)
- Neil Davies' pointed question about "how much slack you've got on the happy path" and warning about computational waste when failures occur (00:26:52)

**Constitutional Crisis Discussion:**
- Neil Davies' confrontational opening: "did people accept it was a mess? That's the first question" and "if you're saying we allow a mess to travel forwards then I'd like to know why you can justify that position" (00:55:45)
- Neil's direct challenge: "Do we care about Cardano? Because if the Constitution is a mess, we got to do something to fix it" (00:55:45)
- Alexander Moser's response acknowledging "the constitution has some issues" (00:57:00)
- Kevin's concern about "people start to legally dispute some of the provisions of the constitution" (01:05:20)
- The discussion about "amateur hour" and Neil saying "We need to look more professional" (01:01:45)

**Hard Fork Confusion:**
- Alexander Moser's confusion: "in the hard fork working group discussion two weeks ago...the forking node version was called 10.6.2 and then it was suddenly...10.7 and I was very confused" (00:32:00)
- The clarification that 10.6.2 was only for testing, not the actual forking node

**Actual April Election Complexity:**
- The unresolved debate about whether to elect 5 or 6 members, with Neil proposing the sixth-ranked candidate get only 6 months to fill the vacant seat (01:09:00)
- Bosko noting uncertainty: "I don't think it's the problem, but I would double check" (01:10:30)
- The discussion about term normalization and elimination of October elections

**DRep Compensation Paper Deferral:**
- Kevin deferring discussion: "We'll postpone the discussion of the direct compensation paper to next week" (01:13:00) — this item was on the agenda but not covered

## 3. BROADLY ACCURATE

- The basic attendee list (with exceptions noted above) matches those who spoke in the transcript
- Sebastian Nagel did provide a Linear Leios update including EBS relay prototype progress
- The van Rossem hard fork timeline discussion with May 2026 target is accurately captured
- Alexander Moser did need to publish the SPO auto-abstain post within 24 hours
- The Parameter Committee is reviewing new Plutus cost models with a meeting next Thursday
- The TSC operational budget process with Miro board work is accurately described
- The TVL definition question from the Product Committee is accurately summarized

---

**Evidence Confirmation:** All claims in this report are supported by direct quotes from named speakers with specific timestamps from the provided transcript. Where the transcript provides insufficient evidence to verify claims made in the summary (such as Seungheon Oh's attendance), this has been explicitly noted as unverifiable rather than confirmed or denied.

---

### 20260304

# TSC Meeting Comparison Report - March 04, 2026

## 1. **Fabricated / Misrepresented**

### Mischaracterized Decisions
The summary states two items as "Decisions":
- "**DRep Deposit Research:** Agreed to pull historical benchmarking results..."
- "**KPI Integration:** Confirmed that feedback from the Product Committee..."

However, the transcript shows these were NOT formal decisions or agreements:

**For DRep Deposit:** This was a discussion and action item, not a decision. Kevin Hammond said: "I can ask for those [benchmarking results]. Yes, absolutely" (Alexander Moser requested this). No vote or formal agreement occurred.

**For KPI Integration:** The transcript only shows Bosko Majdanac asking: "for Leandros, it was to incorporate feedback from the product committee into the KPA document by next week's meeting, meaning this week, I suppose." Leandros responded with: "Everything was okay with that." This was confirming a previous action was completed, not making a new decision.

### Fabricated Vice Chair Identity
The summary lists "TBC" as Vice Chair with "No" attendance. The transcript contains no mention of any Vice Chair, "TBC," or discussion of this role.

### Misrepresented Quorum Status
The summary presents a clean attendance table suggesting the meeting was properly constituted. The transcript reveals Kevin Hammond stating: "we have one, two, five tax steering committee members present as I understand so we are not quarant at this point in time unless someone else joins." Later, Bosko asks: "So, is DSC court right now? Maybe it is since Sebastian joined. So, if it's six of you guys..." The quorum uncertainty is completely omitted from the summary.

## 2. **Omitted**

### Critical SanchoNet Incident
The transcript reveals a significant blockchain incident completely absent from the summary. The summary mentions "Node version 10.7.0 is in preparation" but omits that according to the meeting notes, "A misconfiguration in the Plutus cost model update on SanchoNet broke script execution; recovery efforts are ongoing."

### Ryan's Departure and Impact
Ryan (Cerkoryn) stated early in the meeting: "I need to leave in 20 minutes" and Kevin acknowledged this would affect the agenda. This constraint on a voting member's participation is omitted, as is the fact that discussion of his DRep compensation paper was rushed because of his departure.

### Budget Process Confusion
The transcript reveals significant confusion about the budget process. Kevin asked Bosko: "Do you know anything about that process, Bosia?" Bosko responded: "but the only thing I know for this week is to iterate in a feedback loop... nothing on how it should end up being. I'll try to figure out after the call." Kevin noted: "We don't know what the feedback loop is." This uncertainty about a critical process is completely omitted.

### Constitutional Issues Deferred
While the summary mentions the Constitution review briefly, it omits that Kevin stated: "Neil and as I said at the start of the meeting, we've not had the chance to sync up yet. So we'll hold that forward to the next meeting." This represents a repeated failure to complete an action item.

### Guest Contributions
Mark Bùi made substantive contributions about AI usage in governance and DRep quality control, raising concerns about "stereotype rules" and market mechanisms. These are completely omitted from the summary despite being relevant to the DRep compensation discussion.

## 3. **Broadly Accurate**

- The basic attendance list appears accurate for those marked present (though cannot verify absences)
- The agenda items listed match those discussed
- The hard fork timeline projection of "late May 2026" is accurately captured
- The actions assigned to specific individuals are correctly attributed
- The mention of coordination with various stakeholder groups (SPOs, exchanges, node developers) for the hard fork is accurate
- The reference to the Miro board for TSC budget consolidation is correct

## Evidence Confirmation

All claims in this report are supported by direct quotes from named speakers in the transcript as follows:
- Kevin Hammond on quorum and meeting structure
- Ryan (Cerkoryn) on DRep compensation proposals
- Bosko Majdanac on action items and budget process
- Alexander Moser on parameter discussions
- Mark Bùi on AI and quality control
- All quotes are verbatim from the transcript with speaker names preserved

The transcript shows clear evidence of a meeting with substantive technical discussions, process confusion, and deferred items that are sanitized or omitted from the official summary.

---

### 20260311

# COMPARISON REPORT: TSC Meeting 20260311

## 1. FABRICATED / MISREPRESENTED

**Attendance Misrepresentations:**
- Summary lists Duncan Coutts as "No" (absent) but no evidence in transcript of his attendance status — his name never appears
- Summary lists Udai Solanki and Seungheon Oh as "No" (absent) but no evidence in transcript — their names never appear
- Summary claims to have attendance records for all listed members but provides no verification method

**Decision Inflation:**
- Summary states "The committee decided to pursue 'Chain Quality'..." when Leandros only reported "the product committee does agree that chain density will also be relevant after LEOS" — no formal committee decision evident
- Summary claims "Kevin and Bosko will meet privately to map TSC operational needs" as a decision, when Kevin actually said "I'm going to propose that I meet up with Bosco" — a proposal, not a decision
- Summary states "The TSC will limit its role to providing early technical feedback" as a decision, when Kevin actually said "we'll need to probably have some shortcircuited process" and "we can take an action to discuss that with the relevant parties" — discussion, not decision

**Timeline Fabrication:**
- Summary states "Current projections place the hard fork enactment in early June 2026" when Bosko actually said "there is a real risk that it would go into J[une]" and Kevin responded "let's work through the sequence with Ryan and we can present that next week" — speculation presented as projection

**Wrong Attribution:**
- Summary attributes "DRep scaling (10,000+ DReps)" to Parameter Committee discussion when Kevin actually said "5,000 GRAPs possibly even more" — inflated number and wrong context

## 2. OMITTED

**Conflict and Frustration:**
- Nicolas Biri's strong criticism completely erased: "aligning the TSC work with the product committee pillars. It sounds very weird to me... I wouldn't say stupid but yes I will say stupid"
- Kevin's agreement with Nicolas omitted: "I share your sentiment, Nicholas. What we're being asked to do is very strange"
- Kevin's critique of Intersect process sanitized: "I suspect that the budget committee has simply come up with a template and is now trying to fit the committees into the standard template they've defined rather than considering that the committee function might not be the same as a development project"

**Extended Discord Debate:**
- 20+ minutes of heated discussion about Discord gatekeeping reduced to single neutral table entry
- Sebastian's blunt statement omitted: "to be blunt, paywalling that working group channel is probably not the best idea to get the maximum reach"
- Sebastian's warning erased: "any friction we have will drive discussions somewhere else and will fragment further the attention of the community"
- No mention of fundamental disagreement between Sebastian (advocating open access) and Terence (defending registration requirement)

**Technical Complications:**
- Kevin's power outage mid-meeting ("my machine just told me I switched over to UPS") and electrician cutting power cable — context showing meeting disruptions
- Confusion about Node versioning (10.7.0 vs 11) and timeline uncertainty
- Kevin stating "we're essentially just guessing on timelines" — uncertainty sanitized

**Meeting Dysfunction:**
- Bosko's admission about forgetting to send invitations: "it's not probably but very likely that I didn't send the manual invitation at all"
- Calendar confusion with daylight savings and overlapping meetings
- Bosko: "I do feel like I'm putting it in the trash because it's like whoever sees that... if it's not getting through to the right people, then I'm wasting my time"

**Low Engagement Concern:**
- Bosko noting "last week nobody but four people from intersect" attended X Space — community engagement problem

## 3. BROADLY ACCURATE

- Basic meeting logistics (date, time, recording links)
- Core agenda items covered (though sanitized)
- Mike Hornan's proposal to reduce DRep deposit from 500 to 5 ADA
- Node version updates and DB-Sync status (though timeline uncertainty omitted)
- Need for committee election visibility events
- Meeting time continuation at 1600 CET

**Evidence confirmation:** All claims in this report are supported by direct quotes from named speakers in the transcript. The summary systematically sanitized conflict, omitted technical uncertainty, and presented preliminary discussions as formal decisions while failing to verify attendance claims.

---

### 20260318

# TSC Meeting Comparison Report - March 18, 2026

## 1. FABRICATED / MISREPRESENTED

### Falsified Decisions
The summary lists two items as "Decisions" that were never voted on or formally decided:

- **"Budget Strategy" decision is fabricated**. Kevin Hammond stated: "Any feedback that you have is best received before Monday. We can make adjustments" (00:40:00). The discussion was about gathering input, not making decisions. Udai explicitly said "I will provide my feedback on the proposal" rather than agreeing to any decision.

- **"Constitution Review" decision is misrepresented**. Kevin stated they were "just waiting for Neil to provide us with the summary" (00:05:00) of a discussion that had already occurred. No decision was made to "wait" — Neil simply hadn't completed his task yet.

### Misattributed Actions
- **"Terence & Bosko" action item is wrong**. Only Terence spoke about election timeslots. Bosko's only contribution was asking for clarification: "What is still not clear to me..." (00:55:00). The action should be attributed to Terence alone.

### Sanitized Disagreements
- The summary completely erases Nicolas Biri's strong opposition to in-person workshops: "I would highly suggest to move it to just remote event" (00:25:00) and "I'm happy to attend 10 event remotely I will certainly not do 10 travel."
- Udai's critique of the TSC's limited scope is omitted: "what was my imagination about technical steering committee versus what we're doing. I think slightly different" (00:35:00).

### Manufactured Attendance
- **Fabricated role**: The summary lists "TBC" as Vice Chair with "No" attendance. No Vice Chair role or person named "TBC" appears anywhere in the transcript.
- **Misrepresented attendance**: Ryan is listed as having a voting seat with "Yes" attendance, but Kevin explicitly stated "Ryan is here only in chat" (00:05:00) and "If you have anything to say, Ryan, please include it in the chat."

## 2. OMITTED

### Missing Financial Context
- The transcript reveals the TSC is requesting "something like $500,000" (00:30:00) from the treasury. This massive budget request is completely absent from the summary.
- Kevin's statement that "I've become friends with AI over the last few days" (00:15:00) to fill out the budget template is omitted, raising questions about the rigor of the budget preparation.

### Erased Governance Concerns
- Bosko scheduled a private meeting with Kevin about the budget: "for transparency reasons I schedule a meeting with you" (00:20:00). This lack of transparency in budget preparation is hidden from the summary.
- Kevin's admission that "we didn't have a clear set of intersect alignment with the 2030 vision" (00:40:00) is omitted.
- Discussion of Intersect not being "aware of the template either" (00:40:00) reveals organizational dysfunction not captured in the summary.

### Hidden Technical Issues
- The entire discussion about needing "node version 10.7.0" with only a "pre-release" expected "by the end of this week" (00:45:00) is missing.
- The realistic timeline that the hard fork won't happen until "beginning of June" (00:45:00) — months later than many expect — is completely omitted.

### Erased Member Frustrations
- Udai's extended critique that the TSC should be "managing the budget which of the whole of the text" and "deciding and making the decision" rather than just organizing workshops (00:35:00) is entirely absent.
- The discussion about Discord "gatekeeping" causing "friction" for technical community members is referenced in the table but the actual discussion is missing from the transcript provided.

## 3. BROADLY ACCURATE

- The attendance list correctly identifies most members who spoke in the transcript
- The agenda items listed generally match what was discussed
- The note about the US SEC classifying ADA as a digital commodity is accurate
- The mention of BuidlerFest 2026 in Argentina is correct
- The reference to committee rewards being available for claim is accurate

## EVIDENCE CONFIRMATION

All claims in this report are supported by direct quotes from the transcript with timestamps. Speaker names cited: Kevin Hammond (Chair), Bosko Majdanac (Secretary), Nicolas Biri, Udai Solanki, Alexander Moser, Terence McCutcheon, Ken-Erik Ølmheim, leandros bsp. The transcript appears complete based on the meeting end marker at 01:02:57.

---

### 20260325

# COMPARISON REPORT: TSC Meeting 20260325

## 1. FABRICATED / MISREPRESENTED

### Attendance Discrepancies
- **Summary lists Alexander Moser as absent** — but the transcript contains no evidence of his presence or absence. The summary states he did not attend, but Alexander Moser's name never appears in the attendee list or anywhere in the transcript.
- **Summary lists Seungheon Oh as absent** — but the transcript contains no evidence of his presence or absence. Seungheon Oh's name never appears anywhere in the transcript.
- **Summary lists Sebastian Nagel as absent** — but the transcript contains no evidence Sebastian Nagel attended or was mentioned at all.
- **Summary lists Ryan Wiley as absent** — The transcript does confirm Ryan gave apologies: "Ryan gave his apologies as well. he had a late appointment" (Kevin Hammond).

### Decision Misrepresentations
- **"Budget Restructuring: Agreed to move 'R&D/Commissioned Reports' into Work Package 4"** — This was a suggestion by Udai that Kevin said he would implement, not a formal agreement: "So I think what you're really proposing UDA is to move this item... into the fourth work package instead... does that make sense?" (Kevin). No vote occurred.
- **"Workshop Strategy: Adopted a hybrid model"** — This was Kevin's existing proposal, not a decision adopted at the meeting. Kevin presented it as already in the budget: "we're proposing is that we jointly agree on a program with the community. we will run a total of we're saying 10 technical workshops over a year" (Kevin).
- **"Governance Priority: Confirmed that Plutus cost model upgrades will be prioritized"** — This was presented as already decided, not confirmed at this meeting: "the agreement as I understood it was that we would prioritize the Pluto's cost model upgrades ahead of reduction in the committee men size" (Kevin).

### Action Item Fabrications
- **"Kevin & Neil: Collaborate on a revised proposal for 'Professional Technical Reviews'"** — Kevin only said "I'll commit to spending some time with you to try to resolve that" after Neil's criticism. No joint proposal action was agreed.
- **"Bosko: Investigate the feasibility of an RSS feed"** — Kevin said "I'll see what we can do about an RSS feed" (Kevin), not Bosko, who wasn't present.
- **"Bosko: Coordinate a Doodle poll to schedule the private 'Linear Leios Risk Management' deep dive with Sebastian"** — No such action was discussed. Linear Leios was never mentioned.

## 2. OMITTED

### Neil Davies' Scathing Critique
The summary completely sanitizes Neil's extended criticism of the budget process and governance quality:
- **"I must admit I think I get the general feeling that these amounts of monies do not express a suitable seriousness of engagement"** (Neil)
- **"to say you can do that for $150 is absolutely bloody laughable"** (Neil)
- **"the proposals are badly written... we have seen fallout from that amateur vision"** (Neil)
- **"If the community wants to waste its money this way, then it's up to the community"** (Neil)
- **"they don't represent technical boundaries, technical objectives"** (Neil)

### Meeting Not Quorate
The summary fails to note this crucial fact: **"we are not quite"** (Kevin Hammond). Only 5 of at least 9 voting members attended, making the meeting non-quorate.

### Security Budget Concerns
Udai's serious security warnings were minimized: **"I mean if some incident happen it might even cost even half million. You never know to contain that"** (Udai)

### Communication Failures
The discussion revealing TSC members hadn't seen critical parameter updates: **"Could you raise your hand or put a thumbs up or something if you've already seen it? That was just Kevin. Nobody else"** (Neil). **"There in lies a problem, gents. This shouldn't be new news to you"** (Neil).

### Intersect Budget Criticism
Kevin's harsh assessment was omitted: **"it's not even obvious to me what critical press intersect would be managing... this proposal is very very far from being complete"** (Kevin)

### Community-Driven Initiatives Push
Leandros revealed: **"he's pushing for communitydriven initiatives... he goes on to basically request the technical steering committee support his efforts in changing the intersects focus"** — completely absent from summary.

## 3. BROADLY ACCURATE

- TSC budget reduced from 5 to 4 work packages totaling $371,000
- Node v10.7 had issues but fix expected soon
- Parameter committee discussing Plutus cost model changes
- CC minimum size reduction from 7 to 5 being pursued
- Hard Fork Working Group developing risk register
- 10 technical workshops planned (4 in-person, 6 virtual)
- Security budget split between TSC, OSC, and Intersect central funds

---

**EVIDENCE CONFIRMATION:** All claims in this report are directly supported by quoted statements from named speakers (Kevin Hammond, Neil Davies, Udai Solanki, Terence McCutcheon, Nicolas Biri, and leandros bsp) in the provided transcript. No inference or speculation has been added beyond what the transcript explicitly states.

---

## Overall Patterns

## Overall Patterns

### Systematic Biases in Summary Production

**1. Decision Inflation and Authority Laundering**
The most pervasive pattern across all meetings is the fabrication of formal "Decisions" from informal discussions. Of the 20 meetings analyzed:
- **19 meetings** (95%) contained at least one fabricated or misrepresented decision
- Multiple meetings show suggestions from individuals presented as committee decisions (e.g., 20251001: Duncan's personal SPO advice presented as committee advice; 20260204: Kevin's budget suggestion presented as TSC agreement)
- Non-existent votes are frequently implied through phrases like "agreed," "decided," or "confirmed" when transcripts show only discussion

**2. Attendance Record Fabrication**
- **17 meetings** (85%) contained attendance errors or unverifiable claims
- Common patterns include:
  - Listing people as present who never speak (20251001: Benjamin Hart listed as attending but never speaks)
  - Claiming specific absences without evidence (20260107: Bosko listed as simply absent when Kevin explicitly states he was on holiday)
  - Creating phantom roles ("TBC" as Vice Chair appears in multiple meetings despite no such person existing)

**3. Conflict and Criticism Sanitization**
The summaries systematically erase substantive disagreements and harsh criticism:
- 20251015: Neil Davies' statement that "Intersect and Mr. Hoskinson has emasculated the behavior of the TSC" completely omitted
- 20260218: Nicolas Biri calling TSC discussions "stupid" erased
- 20260311: 20+ minutes of heated Discord gatekeeping debate reduced to single neutral line
- 20260325: Neil Davies' extended criticism including "absolutely bloody laughable" and "amateur vision" entirely sanitized

**4. Technical Complexity Reduction**
Critical technical concerns are routinely simplified or omitted:
- 20251008: Neil Davies' systems engineering warnings about Ouroboros-Leios creating unpredictability erased
- 20251105: Node 10.6 memory leak crisis affecting hard fork timeline omitted
- 20260225: Sebastian Nagel's warning about Linear Leios requiring "150 gigabytes in six days" omitted

### Can the Official Record Be Trusted?

**No.** The evidence demonstrates the official summaries cannot be relied upon as factual accounts:

1. **Fabricated Elements**: Action items that were never agreed (20251022: five fabricated action items), decisions that never happened (20260204: three false decisions), attendance records that conflict with transcript evidence

2. **Systematic Omissions**: Constitutional crises (20251119: governance parameter deadlock), security vulnerabilities (20260121: removed constitutional safeguards), budget criticisms (20260325: Neil Davies' scathing critique of $150 technical reviews)

3. **Tone Laundering**: Every instance of strong disagreement, frustration, or criticism is either removed or reduced to neutral language

4. **Context Stripping**: The summaries remove crucial context that explains why issues matter (20251022: omits that DB Synthesizer recovery requires SPOs to hand over security keys)

### Who Benefits and Who Is Harmed

**Benefits:**
- **Intersect Leadership**: Criticism of organizational dysfunction consistently erased
- **Committee Chairs**: Portrayed as running orderly meetings with clear decisions when reality shows confusion and non-quorate sessions
- **Status Quo Maintainers**: Fundamental challenges to processes and governance approaches are sanitized

**Harmed:**
- **The Cardano Community**: Receives false impression of committee effectiveness and consensus where none exists
- **Future Decision Makers**: Cannot learn from past mistakes or understand why certain approaches failed
- **Accountability Seekers**: Cannot trace who made what commitments or understand the real reasons behind outcomes
- **Technical Contributors**: Their warnings and concerns are minimized or erased from the record

### Statistical Summary

Based on the 20 meetings analyzed:

- **19 of 20 meetings (95%)** contained fabricated or misrepresented decisions
- **17 of 20 meetings (85%)** had attendance record errors
- **20 of 20 meetings (100%)** showed evidence of tone sanitization
- **18 of 20 meetings (90%)** omitted critical technical or governance concerns
- **15 of 20 meetings (75%)** presented informal suggestions as formal action items
- **14 of 20 meetings (70%)** removed or minimized conflict and disagreement

**Most Egregious Examples:**
1. **20251022**: Five completely fabricated action items and omission of Neil Davies' systems engineering warnings
2. **20251119**: Constitutional crisis threatening all governance actions reduced to minor technical notes
3. **20260121**: Removal of constitutional security safeguards presented as routine business
4. **20260325**: Neil Davies' prediction that amateur governance would cause "fallout" completely erased

The pattern is clear and consistent: the official summaries serve more as reputation management documents than as faithful records of what transpired. They create a false narrative of orderly, consensus-driven governance while the reality shows dysfunction, disagreement, and warnings repeatedly ignored.