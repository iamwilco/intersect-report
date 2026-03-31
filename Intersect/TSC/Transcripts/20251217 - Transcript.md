**

## Technical Steering Committee - 2025/12/17 08:28 CST - Transcript

# Attendees

Alexander Moser, Benjamin Hart, Bosko Majdanac, Duncan Coutts, James Meidinger, Kevin Hammond, leandros bsp, Neil Davies, Nicolas Biri, read.ai meeting notes, Ryan (Cerkoryn), Ryan Williams, Sebastian Nagel, Terence McCutcheon

# Transcript

Kevin Hammond: Hi Tex. Hi Ryan.

Ryan (Cerkoryn): How's it going?

Kevin Hammond: Good. Thank you. I'll just paste the agenda into the chat. Hi Ros.

Bosko Majdanac: Hi. Yeah,…

Kevin Hammond: Hi. You're looking very Christmassy.

Bosko Majdanac: I'm looking very bored already with all these pop huntress,…

Bosko Majdanac: whatever is happening on my TV right now for my kids because they are listening to all of that.

James Meidinger: Morning guys.

Kevin Hammond: Hi, James.

James Meidinger: How's it going?

Kevin Hammond: Good to see you.

James Meidinger: Yeah, you as well. Kevin, I want to apologize. I know we meant to chat a couple different times at the summit and…

James Meidinger: I didn't end up get to chat with you. So, I do apologize for that.

Kevin Hammond: I've tried to ping you on LinkedIn,…

Kevin Hammond: James. So, if we could,…

Kevin Hammond: if you don't mind following up by LinkedIn after the call, that would be great. is there anything you wanted to raise with this group?

James Meidinger: Yep. …

James Meidinger: no, I was just kind of hang out and see what you guys had going on and then if I had something to add, I potentially have some information here and there that could be potentially helpful what have you. But I just love to learn really and what you guys are doing is interesting to me as well. and of course it all applies to everything that I do since I work in and live in this space basically. So absolutely. How's it going Good to see Hey Ryan.

Bosko Majdanac: Good. Hi

Ryan (Cerkoryn): Hey, how's it going, Good to see you.

James Meidinger: You too So, everybody recovered from the midnight summit.

James Meidinger: Kevin, you were there, correct? You didn't make that one.

Kevin Hammond: No, I didn't make that one.

Kevin Hammond: I can't remember the timing, but

James Meidinger: I'm not much for so I don't go to at the Rare Evo, they have that event where they go into the big dance, area, right, and have this whole big party. I typically avoid those. I don't mind concerts and middle shows and all that kind of good stuff, but for whatever reason, it's either too late or something. I went to the midnight event that night and from start to finish, it was killer. they took out all stops to make sure everybody had a lot of fun. and made the night very I could actually talk in there.

James Meidinger: Which typically you can't talk. It makes no sense to me going into a place where there's super loud music and trying to have conversations.

Kevin Hammond: What? Right.

James Meidinger: I just don't get it. but at least there you could. so yeah, just the event was well managed the entire time. and the neon light hoop girls really kind of added to the event as well. That was kind of unusual and cool. So definitely enjoyed it. So next year you got to go.

Kevin Hammond: I'll bear in mind depending where it is of course may be difficult to get to.

James Meidinger: Sometimes it is. I think yeah we'll see. They haven't announced yet. I know for Cardono Summit that's going to be in Singapore. So I've never been there. excited for that.

James Meidinger: 

Kevin Hammond: Yeah, that looks interesting and…

Kevin Hammond: it's token 2049.

James Meidinger: No question. Right. Yeah. I've never actually been in that region at all. I am looking forward to going onto that. I'm not sure if you can get onto that building. Basically it's like an island in the sky is what it looks like to me.  They got those three buildings that are pillars and then on top of that there's this whole area just above where it's just that one building that they have. It's absolutely amazing. So would love to go check that out and just see the enormity of it and then you know how it was built, right? So I love that stuff.

Kevin Hammond: We should probably start the meeting. so boss, do we have apologies from anyone or…

Kevin Hammond: we waiting for anyone to join us? Okay,…

Bosko Majdanac: only just give me I mean I wasn't it yeah Nicholas Biri said he will be late…

Bosko Majdanac: because he attends Leos Mley and Alexander Moser said he will be late as  Okay.

Kevin Hammond: So then I would propose that we start. I'm counting five voting members, but we're expecting others to welcome to the technical steering committee meeting of the 17th December 2025. This will be the last TSC meeting of the year.

### 00:05:00

Kevin Hammond: As usual, I've posted the agenda into the chat. I'm expecting this to be relatively light and Hex has posted his affiliation into the chat. So, first item the agenda, Bosco, was to actions arising from the previous meeting.

Kevin Hammond: I suggest we keep this lightweight, especially if we're going to cover items later in the agenda.

Bosko Majdanac: Mhm. Yeah.

Bosko Majdanac: So, hi overview of the action items last week. So, it was basically to borcho to complete initial population and updates to the hard forest tracking repository this week. Yeah. So, that was done.  And we had heartful meeting yesterday. So we'll have something more about that later in the meeting. we have finalized the TSC official response on nested transactions and it was sent to Mel Ni. I suppose I pronounced it and it was sent as an email. Kevin was in then Sebastian to confirm and share the specific conversion and I think that was done in the threads.

Bosko Majdanac: I think Kevin DSC to work with the product committee on 2030 vision and…

Kevin Hammond: Yes. Great.

Bosko Majdanac: 2026 road map that was also something that you have provided a pull request Kevin the files and then nominations and this for the vice chair role to be out of bend and I've asked people to step in and nominate themselves Yeah.

Kevin Hammond: So, we'll catch up on most those items later on the week. So, thank you very much for doing all that, Bosco. A lot of work going on in the background.

Bosko Majdanac: 

Bosko Majdanac: And it's good. All six of

Kevin Hammond: So, you've covered the response to the message transaction.

Kevin Hammond: So the response we passed on to Michaela Nutsy the chain instant partition working group update I was going to propose that Ryan or Neil gave us an update and I will fill in with any missing details. Is that okay Ryan? Yeah. sorry not Ry right Kakorin.

Ryan (Cerkoryn): Yeah, I can pull up the chats and stuff. Just trying to find my tabs. when did we last meet for this? it was hard for working group yesterday. Sorry, I have too many calendars. yeah, it was in Monday. I know we're looking at different types of basically trying to figure out when the previous longest chain fork how many contiguous orphan blocks occurred. So I was doing a little bit of research into that. not entirely sure where that data would best be stored because by definition it's not included on the canonical chain.

Ryan (Cerkoryn): so what I ended up doing is just having two different AI tried to do some deep research on stuff. Basically searching social media posts and articles and whatnot written about it. And I found the best I could find was that there are two contiguous blocks was the longest area of orphan blocks that was prior to this event. so we definitely overshot that by quite a bit. what other things were we covering?  Yeah, there were talk about double spends u basically some terminology stuff basically because mechanical to the chain itself they can't really have been a double spend because all the UTXOs are accounted for.

Ryan (Cerkoryn): So the question is there how does that account for off-chain types of stuff for any kind of centralized exchange or bridge transactions whereas it could have been spent from that other chain or that bridge and then that part of the fork rolled back and then it looks as if those assets were either never spent or they were spent twice. so that's I think more of a terminology question because we can say that there's double spends occurred on the Cardono blockchain itself. so I think getting our terminology Right.

Kevin Hammond: Yeah, I think that's quite a positive result, Ryan, because the blockchain is still consistent, the ledger is still consistent, and we don't have to put in any balancing transactions to make it consistent, but obviously there could be offchain effects as a result of the transactions that weren't processed. on the chain.

### 00:10:00

Ryan (Cerkoryn): Mhm. Right.

Kevin Hammond: But it's very hard to assess what those impacts might be without further information.

Ryan (Cerkoryn): yeah, other than that I'm not sure other major stuff u I haven't mentioned. Am I missing anything?

Kevin Hammond: So yeah, thank thanks Ryan. So I think the state state play is that we're getting towards having a pretty complete draft of a report which we can prepare to pass on to the community.  We've got Ryan Williams here. So Ryan, you can maybe tell us a bit more about the detail and maybe show some of the draft report. the goal, as I said, is to present that to the community by the end of the year. the Insect board have asked for access to look at a draft of that.

Kevin Hammond: So hopefully there'll be enough time to process any comments they provide before the end of the year before people start to go on holiday. Ryan W is there anything you wanted to raise or Neil Yes,…

Ryan Williams: Nothing in particular. I'd say, yeah, the report has come together quite nicely. So, yeah, thank you for your contributions and contributions from other people in this group. there isn't I don't believe and someone could correct me I don't think we found any nasties or anything too surprising. which is good. I think that's nice.  baby. Yeah.

Kevin Hammond: I think the chain of events that instant has become clearer as a result of writing the report that's been clarified over the last week or so.

Kevin Hammond: and we also identified that not all of the transactions that appeared on the non-preferred chain was submitted to the preferred chain. About 20 I believe 20 is it 2029 were not the ones which appeared in the bad block.  So those were not resubmitted onto the preferred chain during the instant response and there's also been some movement on the timeline. So Carlos Dope from IO has provided us with an outline timeline just as an initial timeline.

Kevin Hammond: You.

Neil Davies: I'm just saying that, all of this is sounding like, very good news. And my point is if it's only 29 transactions and they were in the bad blog, that's pretty good, right? Right.

Kevin Hammond: Yeah. I'm sorry.

Neil Davies: And the fact but the other thing is if that  Given the nature of this space, if anyone had had any major problem, any problems, it would have been shouted from the rooftops. Yeah. Mhm.

Kevin Hammond: So in total it was about 500 transactions Neil that appeared only on the non-preferred chain. it was 20 from the block which we hadn't previously accounted for. So they've been overlooked in the previous analysis. So we've corrected the number of transactions submitted.

Kevin Hammond: But I think we're getting to a situation where we have a pretty clear technical view of what happened and we've got some insight into the reasons…

Neil Davies: What is this?

Kevin Hammond: why the incident happened and why it unfolded the way it unfolded and so there's been some analysis of lessons learned but the report as we said this is only intended to be a preliminary factf finding report. is not intended to draw conclusions and though there are conclusions to be drawn and lessons to be Thank you Neil for being involved in that process and everyone else of course. so moving on hard fork working group update.

Kevin Hammond: I was Leandros, you were there. Would you like to take this?

leandros bsp: Hey there.

Kevin Hammond: Hi Dan.

leandros bsp: Yeah. I didn't get any major updates. we resulted on naming for Max. I feel sorry that we lost him. not too much going on. Caligus keys don't seem to be able to be implemented during this hard fork. Probably going to take a lot of time. I'm not sure if I'm missing anything else. didn't seem like anything critical that goes into this committee.

### 00:15:00

Kevin Hammond: Ryan, go ahead.  That's

leandros bsp: Might be wrong. I don't know.

Ryan (Cerkoryn): also mentioned there was discussion about how to earmark items for scope for the dickra era hard work going forward. So I guess there was kind of back and forth in that. It looks like kind of coming to the consensus that there should be kind of a four-step process. you go to the full SIP process somewhere there's going to be a short list of those SIPs maintained basically things that could be considered for the hard work it'll be periodically reviewed by diversity workshops and…

Ryan (Cerkoryn): then presumably once or twice a year the list will be presented to DREPs to be voted on for inclusion so that was one of the other things we talked

Kevin Hammond: Yeah, that's great.

Kevin Hammond: And Ryan, you've agreed to put together a repository so that Ryan W. you're putting together a repository so this can be recorded.

Ryan Williams: Yeah. Yeah. I've been speaking to Adam Dean who I think might make the repo.

Kevin Hammond: Brilliant. Yeah.

Ryan Williams: But we'll move. We were keen to start this process going.

Kevin Hammond: So the proposal is that any item that's going to be put forward to a future hard fork be first of all should have a CPS colano problem statement and that all items should be recorded in this list and subject to discussion develop teams during the node diversity workshops as well as by the community and by the GRE.

Kevin Hammond: So we'll aim to open up the scope of the future hard forks to make it easier to make contributions there. And the summary of the development status is we still don't have a node which is a release candidate at this point in time. we're expecting that to become available probably at the start of the new year because expecting it to be integrated early in the new year and then to be rolled out first on Sanionet and then subsequently on preview and prepro.  So, we'll be aiming not to disrupt preview too early in the process and to make sure it's recovered from the recent incident there.

Kevin Hammond: So the naming of the hard fork. So the proposal are that the working group has come up with is to name the hard fork after Max Vanam Rosson who is a prominent community member of Cardano ambassador who passed away very recently and very unexpectedly. so the group voted with 15 out of 20 votes for that naming. do we have a majority here of voting members? I'm not sure we have a quorum here to gratify that yet.

Bosko Majdanac: One, two, three.

Terence McCutcheon: But not majority

Kevin Hammond: So let's wait for any late comers to join us. and we can come back to that otherwise we'll take it out of band but in my…

Bosko Majdanac: What's up?

Kevin Hammond: but I personally voted in favor on the half working group it seemed to me to be a very positive thing to do and…

Kevin Hammond: Max's family was pleased to have him honored in this way so it's a fitting tribute to Max,…

James Meidinger: Can't think of a better person to be named.

Bosko Majdanac: Just a small typo in the agenda.

Bosko Majdanac: …

Kevin Hammond: what's the typo? Basket. …

Bosko Majdanac: It should be ending with an M, not an N.

Kevin Hammond: yes. Okay.

Kevin Hammond: in the agenda. I see in the chat I'm seeing Max Rosson. Is there a mistake there?

Bosko Majdanac: Yes, in the agenda on Slack you put those and…

Bosko Majdanac: Yeah. Yeah. It should be rough,…

Kevin Hammond: Ross. Okay.

Bosko Majdanac: I think. Yeah. Yeah.

### 00:20:00

Kevin Hammond: Let's make sure we get that correct. Yeah. Thank you.

Bosko Majdanac: 

Bosko Majdanac: Yeah. Yeah. Okay.

Kevin Hammond: Thank you. fraction cost. so the next two items on the agenda we'd put for Alex, but we need to wait for Alex to join us to process them.

Kevin Hammond: so what I would then propose to do is to come on to the TSC operational budget 20 discussion on the 2030 vision and then to go back to the items that we've skipped over and all the vice chair discussion obviously. so TSC operational budget we had a outline discussion last week.  I've not had time to progress that because I've been focusing on things like getting this instant report completed. I've been putting some effort into editing that. there is movement Intersect is realizing that it needs more technical coordination in 2026.

Kevin Hammond: there are ways that we should be being involved in that technical coordination. my understanding from Jack is first of all that they're pushing internally the role of an instant manager to support instance like the chain partition instant that we saw.  So we've secure and in the security council we felt the lack of someone who's dedicated to that role for some time. and so that's in progress at the moment and that's an important thing to do for 26. but also intersect is I'm trying to remember the title a head of technology coordination I think it is boss.

Kevin Hammond: so the proposal is to have a dedicated person within intersect to support that and to support work that we're doing within the TSC and Jack mentioned a number of other areas other important so things like hard coordination node diversity coordination all things where we'd expect the TFC to be involved in a heavy weight.  So that of course is going to feed into an operational budget discussion because what we'll need to determine with intersect boss is what of these activities can be picked up from existing intersect budget which should be put forward to a dedicated TSC budget. We had a discussion last week about items that we could include. Did anyone have any thoughts following the meeting last week on that?

Kevin Hammond: So I gave a list of things that were included last time. one of the things that we had been proposing was to support other community members more getting them involved in various ways in the committees and other organizations providing support for SIP editors analogists to the OSC support for maintainer retainers. So I'll open the floor for discussion.

James Meidinger: Mr. Kevin, I'm curious so as far as the discussion goes specifically, how's it meant to incite regular community members in to get engaged?

Kevin Hammond: So the proposal is James there are a number of technical organizations committees and…

Kevin Hammond: other structures which basically relying on volunteer support. And what we're proposing was to recognize the contribution that the members were making to these committees by giving them some reward on the lines of the stipens that are being provided for other committees. also there are places where we're looking for technical input.

Kevin Hammond: for example, the DREApp Slack technical input on the budget proposals that are being submitted.  And one of the proposals was to pay technically aware individuals to provide feedback on the proposal submissions, new independent feedback on the proposals that could inform the DREAP decisions. That would be one thing to do. then in addition the TSC would like to be able to engage more directly with the community. so already these meetings of course are open to anyone.

### 00:25:00

Kevin Hammond: technical working groups we have open to anyone. We're aware that we could be doing more in the way of attending various events if we had the funding to do so and running running and or bringing as well as organizing workshops that are currently being paid by individual projects.

Kevin Hammond: For example, the no diversity workshop is being paid from the Amaru budget and it makes sense to have that as a community organized effort, not for it to just come under a single project. So various items like that we were proposing.

James Meidinger: That's a great idea.

Kevin Hammond: Yeah,…

James Meidinger: How are you disseminating the information having to do with people you've tapped that have been given this reward, let's say, for example, for their volunteer work that they're doing, right? They're not expecting it, but they're then being tapped going, "Hey, thank you." how are you actually putting that information out into the public? as far as letting people know this is actually a thing and also those who are actually getting tapped with this particular reward.

Kevin Hammond: at the moment this is just an idea James.

Kevin Hammond: So what we do we would obviously need to promote it we need to say as part of the rewards process …

James Meidinger: I see

Kevin Hammond: if you participate in the following things then you'll be eligible for the following reward okay and we imagine that as b this is what I was discussing with proposal evaluation technical evaluation this is what's typically done in public bodies who are managing who

Kevin Hammond: administering large sums of money. you pay for expert advice to inform the decisions and to ratify to help with the decision making. it's a token amount. but it makes difference.

James Meidinger: No. Yeah,…

James Meidinger: it's great idea. and engages quite a few people that we have in our community that are exceedingly good at what they do. they work in a professional space basically and some of the things that they're doing obviously have PhDs, masters and a lot of times we don't even know who they are. until you meet them of course you're in a meeting with them which I have a lot of those and yeah that would be there's a wealth of people you would tap into … if you started to do something like that.  So for me personally is a great idea.

James Meidinger: 

Kevin Hammond: And obviously this needs to engage properly with the other parts of intersect including the private committee including the budget committee 2026 budget process.

Kevin Hammond: What we're thinking James is that we need to set this up in the short term so we're prepared for 26. So what we're thinking is that we need to get together a relatively small budget proposal that could be for 26 just for the TSC separate from the main intersect budget proposal and obviously whenever the insect puts in its 2026 budget proposal then we would tag along with that as well.

Kevin Hammond: we're seeing a number of things where we're not able to engage as much as we would like and we're seeing issues arising because we're not able to engage from that perspective.

James Meidinger: Yeah, makes sense. this abs for me personally, I'm not a voting member. I'm just in the dialogue, but at the same time, I think this would be very good. And also in essence it's kind of an outreach for the TSC and others because there's such a high level when you're listening to some of the conversations that you guys have but there is a spot here and there where people could actually add cot or value right and they just don't know it yet and if you start to highlight people or spotlight people then they'll go hey I know that guy and…

Kevin Hammond: Very welcome,…

James Meidinger: maybe I could do that right and then from there it'll snowball we'll get more community involvement which would be great I got to jump out of here I appreciate everything you guys are doing but thanks for letting me sit  in and just observe.

Kevin Hammond: And do contact me on LinkedIn. We'll set up a conversation. Great. Yeah. in one of the other roles that we had discussed was indeed a technical coordinator someone who can translate technical information for the community and this may be the role that insect is putting forward but I don't know the details of that yet Jack sorry bossy Jack hasn't yet given us the details of that

Bosko Majdanac: She didn't.

Kevin Hammond: So what I would propose doing here if nobody feels particularly motivated yeah we can come back to items.

### 00:30:00

Bosko Majdanac: Kevin, sorry. Alex is here. So if you want to  over back

Kevin Hammond: So what I'm going to propose if nobody wants to have any other discussion now I can put together an outline document where we're covering some of these issues and then we can debate them coming back into 2026 and we obviously aim to expand the set of things that we're doing and to align them with the insect goals

Kevin Hammond: and activities for 2026. Great. So, I'll aim to get an outline draft out to this group by the end of the week, assuming all the other things are sufficiently under control. Great.  So, let's go back to some of the items that we hadn't previously covered. we're expecting Nicholas and possibly Sebastian join us later, Bosow. So, let's delay the vote on the hard name until they have an opportunity to join us. But I put two items on the agenda that you'd asked to be covered.

Kevin Hammond: So the first of these was the ideal number of constitution committee members and the second was the timing of governance actions. Would you like to take the floor?

Alexander Moser: Yes, the first one actually both are just observations and it's worth noting them here in this setting that we're aware of the potential risks or the changes which are not obvious. First one is about the rogue add CC member governance action which increases to members to eight if it passes.  That by itself isn't particularly bad. The threshold for CC approval is still 2/3. But given math, two3 2/3 of eight rounded up is six CC members needing to be in unison of their opinion of the constitution to let a governance action pass.

Alexander Moser: while with seven that's only five. So even though we're getting one additional CC member the threshold increases as well. Security is slightly better but the risk of things not passing because of nonparticipation as we've unfortunately seen a bit in the past half year is there.  I really don't think that this should change anything about the threshold parameter, but if anybody has a comment on that, please do.

Kevin Hammond: I so trying to think what action we could take, Alex. So, this is an onchain governance action.

Alexander Moser: Yes, the EDC member Christina I'd argue that it's not as positive as it seems…

Kevin Hammond: And that would expire. the supposed to add one additional constitution committee member the v the voting threshold is retained at 2/3. so the issue is that when this was proposed the proposals didn't consider that they were increasing the number of CC members who would need to be in favor of a vote.

Kevin Hammond: So increasing from seven to eight is positive especially given the current mincc setting. But if we were and…

Alexander Moser: because 2/3 of 8 is one more CC member than 2/3 of seven …

Kevin Hammond: and if we were to drop to the proposed MCC level of five, then we'd be in a situation where even if all the committee no. No. we would only have five. Yeah.

Kevin Hammond: I think if we ended up with five voting members on the CC, they wouldn't be able to ratify any action is that true?

### 00:35:00

Alexander Moser: yes, because it's below the mean CC value.

Kevin Hammond: Because Yeah.

Alexander Moser: I've made a little table with potential total sizes and…

Alexander Moser: what that 2/3 means.  Bosco, if you happen to be on Slack and find that sheet, be appreciated. I'm on mobile at the moment.

Kevin Hammond: So Alex,…

Kevin Hammond: I say what I think the best thing to do here might be this is information to make the community aware of. it's is factual information. we do have an ex account, a Twitter account.

Kevin Hammond: So what we could do be to put together a small blog and say do you realize that dot okay because it's not obvious who otherwise to pass this information on to and then the community at least is aware of the issue and can discuss it. But I don't think we should be saying don't make the change because the change is at worst neutral and does provide some additional resilience. so there are more people…

Kevin Hammond: who can be drawn on the CC. Alex, I think it's a positive step to have more members on the constitutional committee even if the threshold doesn't change.

Alexander Moser: Yep. Oops.

Kevin Hammond: So would you be willing to write a short blog post post that we could then distribute from the TSC account?

Alexander Moser: Yes, my blog post might be too much for that little fact. But I think what is more important to communicate openly would be the second point…

Alexander Moser: since there is a real risk of things not working out.

Kevin Hammond: Yeah, when I say blog post,…

Kevin Hammond: I'm thinking possibly a paragraph or two in the form of two or three tweets. So, nothing very complicated. Right, Ryan, you posting something in the chat?

Ryan (Cerkoryn): No, I was just saying that I think the ideal number of committee members is kind of tied to how many applicants there are that have committee support. so in this latest election that Intersect held, it was very close between Cardono, Huria, and Christina. So it makes sense to add both from my perspective. I'm not sure…

Ryan (Cerkoryn): how far off the third person would be. but I think if we want more redundancy past that point, it makes more sense to just change the committee min size or…

Alexander Moser: It's crazy.

Ryan (Cerkoryn): or even alter the voting thresholds based on that.

Kevin Hammond: Yeah, absolutely.

Kevin Hammond: So, there's the proposal which has been put to the parameter committee to reduce committee min size.

Kevin Hammond: That was approved at the last meeting, Alex. Correct. so we have supported that recommendation. it was a proposal that UT was putting forward. so we'd expect him to submit that, but there's a delay because this is a governance security related parameter. There needs to be a three-month delay between it being debated, being proposed, and being enacted on chain.

Alexander Moser: Yes, but I'm not proposing to change The threshold is fine. It just doesn't work as good with eight as it would with 709. That's all I had to say.

Kevin Hammond: And the second item was to do with the timing of the governance actions.

Alexander Moser: Matias has identified any risk that if that add CC member governance action for Christina would pass too late. It clashes with the ratification of the treasury withdrawal.  And you can't, as far as understood, change the CC and withdraw from the treasury at the same epoch boundary. It would have the result of the treasure withdrawal just being dropped even though it's approved.

Kevin Hammond: So there are some hazards in the governance system. Alex, I need to go back and…

Alexander Moser: Watch this.  Exactly.

Kevin Hammond: check the precise ratification logic in this case. but I think the community has to accept that occasion because there are changes in the governance system. that means that some actions might have to be resubmitted. And the particular case where it can happen is with a no confidence vote, then the committee of course can't ratify any actions and you might have to resubmit ones that would otherwise have passed.

### 00:40:00

Kevin Hammond: So again I think it's something to be aware of. but the community has to take its own decisions and to be honest I don't see any great rush for a Treasury withdrawal.

Alexander Moser: You don't.

Kevin Hammond: What's the rush?

Alexander Moser: I'm asking myself the same question, but you're not talking to the same people as I do. Everybody is hyper stressed about that treasure withdrawal and…

Kevin Hammond: I see.

Kevin Hammond: Okay. But…

Alexander Moser: the NCL, too. Apparently,…

Kevin Hammond: but it's not as if the Treasury is going to go away, Alex. It's still going to be there in 202 And there will be a sensibly set NCL in 2026, I would assume.

Kevin Hammond: So this treasury withdrawal can happen against 2026 NCL.

Alexander Moser: some of those discussions that group has is dependent on a sum of available money,…

Kevin Hammond: Okay.

Alexander Moser: which is why they're being DS.

Kevin Hammond: We don't need to go into that space. I think if you're at a stage where you're worrying about a particular sum of money being made available then you've probably left things by a particular date then you've probably left things too late. Right. Right. Okay.

Alexander Moser: The two of us agree it doesn't change the fact of where we are right now.

Kevin Hammond: But as I saying the fact is depending on how things work out either the constitution committee member is elected and…

Kevin Hammond: the withdrawal goes through and again we would need to check the ratification logic to see whether that makes a difference to the ordering. maybe what needs to happen is the new member is elected and they immediately need to confirm the constitutionality. So it might be some quick shuffle happening like that. Yes.

Alexander Moser: that anyway needs to happen after the first CC member governance action goes through in the beginning of January, but the fact that there is a second CC member somewhat jeopardizes that treasure withdrawal again is just curious fact and…

Kevin Hammond: Okay. Yep.

Alexander Moser: I guess nothing much that we can do about it but I'd rather tweet this than the threshold situation because that's not as critical. It's just an observation and I think Neil put it correctly. that's how I meant it within this context of the call could be considered a little bit of a doss attack.

Alexander Moser: seen her submitting that governance action with perfect timing to block the treasure withdrawal. But obviously she didn't do that on purpose, but it is undesired.

Kevin Hammond: Right. Okay.

Kevin Hammond: So some accidental effect. So what we're saying is people should be informed of the connces the possible consequences of particular government actions the sequencing of particular government sanctions I think the recommendation we'd made to intersect was to increase the committee size and…

Alexander Moser: Merry Christmas.

Kevin Hammond: not just to appoint one person anyway

Kevin Hammond: So this is consistent with that but of course in sections only to retain the existing number following the elections that they held.

Alexander Moser: That was it for my end. Thank you.

Kevin Hammond: Thanks. Thanks So just following that Consequential interle. Yeah. it's becoming quite complicated, Neil. So we're observing this with the parameter updates that are going to need to be processed. so we have the main committee size.

### 00:45:00

Kevin Hammond: We have the increased Plutous memory unit limits and we have the Plutous cost model upgrades which are all going to need to happen early in 26 and we need to make sure that they get processed in the right order.  So Ryan, I think you've got a table that's tracking that and those are particularly critical because the ledger enforces a chain of dependencies on parameter updates to make sure that they are sensible.

Kevin Hammond: So if one of them gets rejected then all three could fail for example or we might have multiple equivalent proposals floating around which will be confusing to the GRAPS right state target number yeah that it's going to get very interesting Ryan because almost certainly something is going to fail simply…

Ryan (Cerkoryn): What do you mean by that?

Kevin Hammond: because we'll be having three or four parameter proposals and you have to put in the hash of the preceding one to create chain.

Ryan (Cerkoryn): Okay.

Kevin Hammond: Okay, we'll need to work out to make sure that there's a sensible ordering or…

Ryan (Cerkoryn): Yeah, we'll have to work it out. So, yeah.

Kevin Hammond: we'll have to duplicate some of the proposals which said it's potentially confusing to DRS. Why should they vote yes or no twice?

Ryan (Cerkoryn): That makes sense.

Kevin Hammond: Okay. Yeah.

Ryan (Cerkoryn): Yo, you'll have to work that up.

Ryan (Cerkoryn): We just finished basically putting together a draft of…

Ryan (Cerkoryn): how that proposal will look early this week, but I was going to bring it up to you guys at the next parameter committee meeting so I mention more about it then.

Kevin Hammond: Yes. And Neil,…

Kevin Hammond: yes, it is the preceding successful has We're brought into the situation because the parameter update we were proposing was scheduled pretty well when the constitution committee had its little hiatus. So it's created a bit of timing pressure on those updates which is so you're going to put together a blog post on the second point as I understand it.

Alexander Moser: Yeah. CF also will post it.

Kevin Hammond: Great. Yeah.

Alexander Moser: We could just probably retweet it.

Kevin Hammond: We're think TSC is happy to retweet that or you can tweet it from the TSC whichever you prefer.

Kevin Hammond: Brilliant. Should we come back to The halfalk naming. so Nicola, you weren't here when we were announc you weren't here when we were discussing this, but the proposal is to name the protocol version 11 hard fork after Max Van Rossm who is a prominent member of the Colano community. happy to answer more questions, but I would propose that we move to a vote otherwise. So, boss, if you'd like to set up a poll for that, that would be great.

Bosko Majdanac: What should we put as a question? So, should we name just a simple one? Write yes and no. Okay,…

Kevin Hammond: Yes, I think so.

Bosko Majdanac: 

Bosko Majdanac: just give me a minute. Your vent.

Kevin Hammond: Go ahead.

Nicolas Biri: Yeah. I was just wondering, do we know if we have their family approval for it?

Kevin Hammond: Yeah. Yes, we do. we asked during the meeting on Tuesday and…

Nicolas Biri: Okay. Okay, perfect. Yeah,…

Kevin Hammond: the response came back on.

Nicolas Biri: 

Nicolas Biri: That's great. I think it was actually what was required on my side to have an educated guess on my vote.

Kevin Hammond: So, we have that I passed that in the TSC Slack channel and…

Nicolas Biri: I didn't notice it. Sorry.

Kevin Hammond: Let me see. I can read out what the family said because it's quite moving. so Ken Eric asked question the family and…

Alexander Moser: Bosk please add abstain as option.

Kevin Hammond: the answer came back.

### 00:50:00

Kevin Hammond: So the answer from the family came back that Max would be tickled pink to have a hard fork named after him. Please thank the Cardano community. He so enjoyed his involvement with Cardano and the people he met in that space.

Bosko Majdanac: Vote is open.

Bosko Majdanac: I mean pawn is open.

Kevin Hammond: So we'll leave the poll open to allow people chance to vote.

Kevin Hammond: I'm seeing seven votes recorded.

Bosko Majdanac: Yes. Six.

Bosko Majdanac: And one abstain so far.

Kevin Hammond: And I think we have seven voting members in the call.

Kevin Hammond: Is that correct? Has anyone not voted?

Bosko Majdanac: Who is missing? You die, And then close. Sebastian is here.

Kevin Hammond: You and Sebastian are missing. So we Sebastian's here.

Sebastian Nagel: I joined was late.

Kevin Hammond: I didn't see you join Sebastian. So, we've got eight votes recorded. Seven one.

Bosko Majdanac: Yeah. Seven. Yes. And one abstain. So all of the voting members did it.

Kevin Hammond: Great. We can end the v the poll and…

Bosko Majdanac: So we can end the poll I

Kevin Hammond: we can confirm the proposed name. we'll need to figure out the process for doing that. Boss, I think historically what we did was we ratified the decision.

Kevin Hammond: We made the proposal and we put it out to the DREPs via an info.

Bosko Majdanac: So, you're speaking about infection, right? Okay.

Kevin Hammond: That's what we did I think for the plowman hard fork. So we should follow the same process consult the community as well.

Bosko Majdanac: Yes, we can do that relatively quickly. Ryan, do you have something to add on that? Ryan Williams,…

Bosko Majdanac: younger Ryan.

Ryan Williams: Yeah, we can do that…

Ryan Williams: if that's the request.

Bosko Majdanac: Okay, just a question. Are we going to have a hard fork? Are we sure about that before we put Okay.

Kevin Hammond: There will definitely be a hard fork. Bosco to the protocol version 11 is named after okay we can't be sure that the hard fork that we're proposing is going to be the one…

Bosko Majdanac: Okay, sure.

Kevin Hammond: which will be protocol version 11 we hope that the will confirm that and the directs will confirm Yeah.

Bosko Majdanac: That was my point. Yeah, but that is the kind of potential friction. Okay. we have seven more minutes.  It should just be mine for

Kevin Hammond: So, I think we can move on. so 203 coming back to this the product committee is going to submit anaction on chain for discussion by the GRAPS.

Kevin Hammond: I've posted a link to the latest version of the vision. this includes KPIs. I would suggest that we look at these KPIs now and provide comments or feedback. it's good to have KPIs. but if they're not achievable, and then we've got a problem, of course.  So we should certainly make sure that any feedback on those is given to the product committee. So I'll give you a chance to look at that item is I'll just paste it again in the chat.

Nicolas Biri: Excellent.

### 00:55:00

Kevin Hammond: So, the KPIs, they're coming under the section called strategy. I'll just paste the link to that. I think we're going to need to go into those in some detail. Does anyone have any quick thoughts now? So we're seeing KPIs are under adoption,…

Kevin Hammond: reliability, operational resilience,…

Nicolas Biri: Yeah. Thanks.

Kevin Hammond: revenue, governance and scalability. Neil

Neil Davies: I'm just trying to work out typically in an organization a KPI is something that you have control over the knobs for doing these aren't KPIs in the sense that they're aspirations right are they…

Neil Davies: because we have no control nobody in the community has any direct control over making these numbers happen as the community itself so they're aspirations not performance indicators right I'm just saying it's yeah…

Kevin Hammond: Y A performance indicator,…

Kevin Hammond: it's an indication of how well you've achieved the goal.

Neil Davies: so these are aspirations. And yeah one thing I would do because it's very disappointing not to reach something is I would split these into target threshold and a threshold target and scratch. We'd like to get this many. We'd love to get and this would be fantastic. I get a spread because that's get a spread in front of numbers then you could talk about being on target and just that would create more dialogue and better dialogue as opposed to we got two billion aid and we failed.

Kevin Hammond: I mean the question is what happens if you don't reach these targets?

Neil Davies: Exactly I mean, and there's no sanction mechanism, which there would be in a company, There's no sanction mechanism at all. so actually, all you're doing is setting yourself up for collective disappointment or collective success or whatever, right? You want to This doesn't seem like a good way of interacting with the community.

Neil Davies: That's all I'm saying.

Kevin Hammond: Yeah, I think this probably came…

Kevin Hammond: because they're asked to quantify the outcomes set quantifiable targets.

Neil Davies: That's different. these are our aspirations.

Neil Davies: We should do at least this. All right. what you've got here is this feels like numbers pulled out of somebody's I'm going to be polite by stopping.

Kevin Hammond: Be polite.

Neil Davies: Because if you're going to put a number like 3 billion, why is that better than 2 billion worse than 4 billion?

Sebastian Nagel: probably in comparison to other competitors.

Neil Davies: That would be a good but the point is you're guessing, it's a document. You shouldn't have to guess in the most responsible way. they should say in comparison with other chain a number between this and this seems reasonable, We choose these two numbers. And I'm just saying I'm just being corporate about this, right?

Neil Davies: that's my comment.

Kevin Hammond: And any comments on any of the particular aspirations?

Kevin Hammond: I think we should look at these and then individually or collectively determine whether they are feasible plausible or not. Visibility is hard to assess on a fiveyear time scale, but there may be. Okay.

Neil Davies: All rationale of unreliability right is wrong because they talk about up the point is we will have blockless intervals of more than 5 minutes by the normal operation of the protocol and…

Neil Davies: I don't know what they mean by up time yeah,…

### 01:00:00

Kevin Hammond: Yeah. …

Kevin Hammond: it's conventional. Yeah.

Neil Davies: they've taken this, but this assumes 100% property thing, and they assume that I'm just saying the current status is 99.898. I really are. So they have folded the normal behavior of the system as a negative li reliability.

Kevin Hammond: Right. length of time during…

Sebastian Nagel: What would be a better me measure of reliability?

Neil Davies: I don't know. I mean I mean Yeah,…

Ryan (Cerkoryn): It be different depending on the depth.

Kevin Hammond: which transactions could not be processed on the chain. Number

Sebastian Nagel: By whom? not

Neil Davies: it's not a simple Okay, you're asking me to do their work for them Number number two it's not a simple problem because actually what are are you interested in lack of forks or then because nonprogress is better than duplicate progress in some way. So I mean if you're going to have a reliability metric

Kevin Hammond: there's maybe the more specific things I mean some measure of chain density might be useful no.

Neil Davies: then what I'm saying is this is not the right way to go about it but I don't know What do you want is reliability the right word?

Neil Davies: Yeah, because this implies right there's a sort of implication here that basically if it's working you will get your transaction in which isn't true either right yeah

Sebastian Nagel: Yeah. Yeah. Chain density and chain quality only say is metrics of block production, right? If everyone is censoring all the transactions,…

Neil Davies: Right. Exactly.

Sebastian Nagel: you would have them high. But yeah,

Neil Davies: What's the observable behavior you want to see?

Neil Davies: And I mean my guess is that the probability of me submitting something and…

Kevin Hammond: Yeah.% of transactions that are submitted appear on chain within X blocks.

Neil Davies: it getting on chain is better than 99.9% or something. Yeah. that's what businesses want. Yeah. …

Kevin Hammond: But that's not exactly reliability. that's a load metric.

Neil Davies: It depends if you look at it from a systemic point of view or from an end user perspective. So these are mixing up the reliability metrics and it's an ontological I don't know if Dun Duncan you ready to down the point you go it's an onlogical epistemological difference here right every time we said that during the Shelly design alcohol was consumed okay…

Duncan Coutts: Yeah. Yeah.

Kevin Hammond: Yeah, Ryan's raising a point about the Canary transactions CF business.  Perfect.

Neil Davies: because it was standing it was like the red shirted man getting killed in Star Trek it was bound to happen as a composition  Yeah. Yeah.

Duncan Coutts: I think it's clear that they're going to need some, advice and support here on trying to frame their question properly because, it's a probabilistic thing. It doesn't quite work in the way that, whoever wrote this imagines. and they need some help in framing the but yeah,…

Duncan Coutts: as Neil says, it's more than a 30 second here's the right answer exercise.

Sebastian Nagel: And it's a bit different than the others,…

Sebastian Nagel: So there's very user focused things which personally I think is good, it's not very technical u metrics which are how it today works. It's more about what the users get or how many active users monthly and these kinds of things. So in reliability it should also as I think I'm not sure who said it just before but getting transactions in the system is kind of maybe a one aspect of reliability maybe but block production users don't care about the blocks they care about getting their transactions in I guess and…

Kevin Hammond: Yeah. Yeah.

Sebastian Nagel: exa exactly right so really the block schedule is not a metric in a similar  level of user focus as this document otherwise

Neil Davies: they care about when they can use the result of that transaction again.

Neil Davies: That's what they really care about.

Kevin Hammond: And then you got to look at the different kinds of user, Sebastian. So an app user will have a different expectation from someone who's submitting a transaction using a wallet perhaps.

### 01:05:00

Neil Davies: So basically as you say there's system metrics, there's end user metrics. yes, you're right. The Canavar Carl put together that the Canaries and the really interesting thing is that for example, that hiatus where no Canary was lost and all canaries got into block in less than three blocks. that's what actually happened in the system. So it turns out if this is just to show you how bad metrics can be. If you were using the foundation's canary during that sporking event, the chamber put you here perfectly,…

Neil Davies: which you did for the canaries, right?

Kevin Hammond: …

Kevin Hammond: so I previously suggested to the product committee that we have a joint session. We've not had them take us up on that. I propose to go back to Kyle and Sam and either we can go to one of their sessions or they can come to one of ours or we set up some special working group to cover this. How would you like to proceed? it's going to be 26 boss. We're not going to do it before the end of the year. Shall we invite the private committee to a discussion once we've had a chance to look at this?

Kevin Hammond: Do we could I'm trying to work out whether people will have had a chance to read through it.

Bosko Majdanac: To the next one.

Neil Davies: It's not that it's a 10-minute read.

Kevin Hammond: It's a temporary So let's invite the product committee to join the first call of 2026 and we can discuss that.

Bosko Majdanac: And the first call is going to be 7th of January.

Kevin Hammond: Yeah, I think Sam might be away,…

Bosko Majdanac: Okay. Me too.

Kevin Hammond: but we'll miss you,…

Bosko Majdanac: But yeah, could be that I will be there perhaps in the evening.

Kevin Hammond: We'll miss So,…

Bosko Majdanac: You won't

Kevin Hammond: we've got a way to proceed on this. and if the product committee isn't able to meet on the 7th, we'll push back to a later meeting. we'll issue a formal invitation to them and we'll take an action.

Kevin Hammond: We'll dedicate the meeting to discussion with them or a large part of it. Bos, I think it sounds like a positive thing to do.

Bosko Majdanac: loaded.

Kevin Hammond: Final item on the agenda was vice chair position. So, thank you everyone for who voted for me in the position as chair, but we are missing a vice chair position which would be useful to have. It's not a very ownorous position. happy to discuss the details with people but it's essentially acting in the chair's absence for example and taking on the direction of any meetings which the vice chair feels are important. so we had any nominations for vice chair boss yet?

Bosko Majdanac: No, that's why I posted the reminder so we can wait…

Bosko Majdanac: until 202 There seems to be no candidates for it except last week Sebastian said he is excluding himself from the list with the right reasons and that's fine.  No, I don't know. Nobody else pointed out whether they are in favor of, nothing.

Sebastian Nagel: We have anti-candidates or kind of non-candidates.

Kevin Hammond: We could nominate you anyway,…

Kevin Hammond: Sebastian. Okay.

Benjamin Hart: I mean,…

Sebastian Nagel: Not going to

Benjamin Hart: I could just nominate everyone other than Sebastian right now. I'm not sure they would accept, but

Kevin Hammond: So, I think it's definitely a good move to have a vice chair. if we don't have a vice chair, then in the absence of the chair, someone would have to be nominated to take the role. it's good to have someone who's dedicated to that who's familiar with the business. So, please do think about whether you might do that.

Kevin Hammond: It's good position to take up and it's not particularly ownorous. We can even have multiple vice chairs if more than one person steps forward. The intersect is putting together a policy on chair and vice chair's elections. so we need to follow whatever they're doing there.

Kevin Hammond: I've been involved in some of the discussions. It didn't look very ownorous to me. so when we were discussing this I was trying to avoid try locking us in to overly rigorous procedures.

### 01:10:00

Kevin Hammond: So hopefully they've taken that on board in the policy spot.

Bosko Majdanac: Do you have any specific aspect of that document that you can point me too.

Bosko Majdanac: That doesn't feel So, I can check as well. You can do it on Slack.

Kevin Hammond: Let's do it out of band. I don't think there's anything specific, boss, but we just have to be aware of it when we're electing members. so one thing was the frequency of elections. So you need to make sure that works. And my position was very much well the committee should have the right to hold an election whenever it wants, right? So you shouldn't say a chair is elected for a certain period. I mean that may normally be the case. but I don't think it's good to have a hard and fast rule.

Kevin Hammond: If the committee wants to hold a chair election, it should have the level to be able to do that without necessarily someone, this could only happen if there's a vote of no confidence in the chair and that seems to me to be a bit so some details about the policy that we need to be careful with, but hopefully it's not too restrictive. So, everyone have a think about that the role. I encourage you to have a good break. have a good holiday everyone.

Kevin Hammond: And I'll catch you in the new year if not before.

Sebastian Nagel: Merry Christmas. Right.

Kevin Hammond: Take off time off and see your family.

Bosko Majdanac: Thank you.

Alexander Moser: Merry  Interest.

Bosko Majdanac: Have a great Christmas everybody. Bye-bye.

Kevin Hammond: Merry Christmas. Bye.

Ryan (Cerkoryn): Take care everyone.

### Meeting ended after 01:12:10 👋

This editable transcript was computer generated and might contain errors. People can also change the text after it was created.

  
**