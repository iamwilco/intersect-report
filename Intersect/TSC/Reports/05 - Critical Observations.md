# Critical Observations

**Committee:** TSC  
**Period:** 20251119 -> 20260415  
**Meetings:** 20  
**Transcripts available:** Yes  
**Generated:** 2026-04-16 17:36  

---

# Technical Steering Committee Analysis: A Study in Governance Dysfunction
## November 2025 - April 2026

### Executive Summary

The Technical Steering Committee (TSC) of Intersect operates as a technically competent body systematically undermined by organizational dysfunction. Analysis of meeting transcripts from November 2025 through April 2026 reveals a committee that provides technical oversight without corresponding authority, struggles with basic operational support, and discovers critical governance changes after they occur. Most alarmingly, constitutional amendments removing treasury safeguards passed without the knowledge of committees chartered to oversee such changes.

### The Constitutional Crisis: Governance Blindsided

The most severe governance failure centers on Constitution v2.4. On February 11, 2026, Kevin Hammond revealed that both the TSC and Civics Committee were unaware of constitutional changes:

> "So, one of the reasons why we were slightly blindsided is we're expecting the civics committee to tell us, And to ask us to do a technical review. So I was a bit surprised they didn't do that, but the reason they didn't was apparently they didn't know either." (20260211, Kevin Hammond)

The changes, proposed by a single DRep (Yuta) and voted through while oversight committees remained uninformed, included potentially removing treasury spending restrictions. Kevin Hammond's discovery sparked alarm:

> "apparently if my reading is correct you can now spend the Cardano Treasury on anything you like without having to justify it... that does raise definite alarm bells" (20260204, Kevin Hammond)

By February 18, technical review revealed the document was "technically 'a mess,' with 90 pages of diffs that are nearly impossible to audit." Specific problems included:
- Guardrail labels not updated as required
- Metadata required to be "immutable" without defining immutability
- No clarity on implementation timing or impact on pending proposals

### The Chain Incident: Authority Without Power

The November 2025 chain partition incident exposed fundamental tensions between technical expertise and organizational control. When the board demanded legal review of the incident report after the working group completed its technical analysis, Neil Davies erupted:

> "I wish to go on record for saying that I wish to censure the board for changing the terms and conditions of the committee after it was agreed at the beginning... changing the remit at the last minute because you haven't thought things through is just such bad form and just shows incompetence" (20251210, Neil Davies)

This incident established a pattern: technical committees perform work, but control remains elsewhere.

### Budget and Compensation: Professional Work at Amateur Rates

The committee's operational budget discussions reveal systematic undervaluation of technical expertise. The proposed $150 rate for reviewing multi-million dollar proposals prompted consistent objections:

> "if you're going to review a two or three or $5 million project... which is actually supposed to deliver and has delivery criteria... to say you can do that for $150 is absolutely bloody laughable." (20260325, Neil Davies)

Nicolas Biri characterized the $200 milestone review rate as "unprofessional" (20260128). The committee eventually secured $250 - still below professional standards for technical due diligence.

### Committee Attendance and Participation

Meeting attendance data shows generally strong participation with notable patterns:

**Regular Attendees (>80% attendance):**
- Kevin Hammond (Chair)
- Neil Davies 
- Bosko Majdanac
- Udai Solanki
- Nicolas Biri

**Variable Attendance:**
- Alexander Moser: Present for proposals he championed, absent during critical discussions
- Duncan Coutts: Sporadic attendance at seemingly strategic moments
- Sebastian Nagel: Regular when present but gaps in attendance

The persistent inability to fill the Vice Chair position from November through April speaks to deeper issues. Even Neil Davies, who regularly stepped in to chair, explicitly refused the formal role citing "other commitments" (20260128).

### Information Asymmetry and Vendor Dominance

Transcript analysis reveals clear information asymmetry between vendor-employed members and independents. Discussions frequently feature:

- Kevin Hammond: "I discussed that with Ryan with Ziang..." 
- Nicolas Biri: "I chatted with Carlos..."
- Sebastian Nagel: "having talked to Nick Clark..."

Independent members struggle to participate meaningfully in vendor-dominated technical discussions, creating an implicit hierarchy within the committee.

### Cross-Committee Dysfunction

The committee operates in isolation from other governance bodies, creating dangerous gaps:

1. **Product Committee**: Sets KPIs without technical validation; TSC spent months in "back and forth" discussions that "literally looks like every single week" (20260415, Bosko Majdanac)

2. **Parameter Committee**: Not informed of constitutional changes affecting their remit

3. **Civics Committee**: Failed to notify TSC of constitutional amendments requiring technical review

4. **Budget Committee**: Imposed templates "geared to community proposals" requiring artificial alignment with "five pillars" that "sounds very weird... I will say stupid" (20260311, Nicolas Biri)

### Communication Infrastructure Failures

Basic communication mechanisms remain broken despite repeated identification:

- No RSS feed for parameter updates after months of requests
- Discord channels behind membership paywalls, creating barriers to technical collaboration
- SPOs learning critical updates through Twitter campaigns rather than formal channels
- Calendar conflicts and Google Meet failures delaying meetings

Sebastian Nagel's observation about Discord gatekeeping captures the tension: "paywalling that working group channel is probably not the best idea to get the maximum reach" (20260225).

### The Permissionless Paradox

A philosophical divide persists about the TSC's role in Cardano's "permissionless" ecosystem:

**Passive Position** (Nicolas Biri, Alexander Moser): "it's a permissionless system. Everybody can propose something... if they're going to reach out to us, it may be a TSC problem, not the community problem" (20260318, Nicolas Biri)

**Active Position** (Kevin Hammond): "Then we have to live with inconsistency and potentially failure, Alex, when we could have prevented it" (20260318)

This unresolved tension creates ongoing friction about proactive versus reactive engagement.

### Technical Crisis Management: The 10.7.0 Near-Disaster

The handling of node version 10.7.0 reveals both competence and systemic issues. Post-release discovery found:
- 50% CPU increase during synchronization
- 6GB memory leak over 1-2 weeks  
- Rare consensus failure conditions

Kevin Hammond's assessment: "10.7.0 is not mainnet ready and we are not going to recommend that it become mainnet ready" (20260401). The crisis emerged through post-release discovery rather than pre-release testing, with benchmarking infrastructure failing when "AWS fell over."

### Nested Transactions: Technical Judgment Overridden

Despite Michele Nuzzi's detailed technical objections about complexity and MEV exposure (20251119), the TSC abdicated decision-making authority:

> "TSC is not taking a decision or making a decision... it's not TSC can recommend but the product should decide" (20251210, Bosko Majdanac)

This pattern - technical analysis followed by deference to product decisions - exemplifies the committee's limited actual authority.

### Conclusion

The Technical Steering Committee demonstrates high technical competence systematically undermined by:

1. **Authority Without Power**: Can recommend but not decide, even on technical matters
2. **Systematic Under-resourcing**: Professional responsibilities with volunteer-level support
3. **Information Asymmetry**: Vendor employees dominate with insider knowledge
4. **Communication Failures**: Basic infrastructure remains broken after months
5. **Governance Blindsiding**: Critical changes occur without committee knowledge

The committee provides a veneer of technical oversight while real decision-making occurs elsewhere - in vendor development meetings, board rooms, and constitutional processes that bypass technical review. The TSC's inability to prevent removal of treasury safeguards, secure adequate review funding, or ensure basic communication infrastructure reveals the reality: technical governance at Intersect remains largely performative while actual control resides with funded entities and their employees.