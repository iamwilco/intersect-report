**

## Technical Steering Committee - 2025/10/01 08:29 CDT - Transcript

# Attendees

Alexander Moser, Benjamin Hart, Christian Taylor, Duncan Coutts, Jonathan Kelly, Kevin Hammond, Markus Gufler, Neil Davies, Nicolas Biri, Sebastian Nagel, Terence McCutcheon

# Transcript

Terence McCutcheon: Sure. He

Kevin Hammond: tax time to get a coffee.

Kevin Hammond: Hi, Johnny. good discussion yesterday at the competitors meeting.

Jonathan Kelly: Yeah, It was actually quite fun.

Kevin Hammond: Yeah. Yeah.

Jonathan Kelly: Although a bit different for them, to be focused only on one topic for a long period of time and to not cover I mean, I think Phil was a bit annoyed because it meant that they were covering less other sips.

Kevin Hammond: So a separator's meeting isn't really the place to do a technical review, But the

Kevin Hammond: because all you're do or so SIP editors shouldn't be taking account as Duncan tells us of the technical validity of the set. They should rather they're confirming does the SIP follow the yeah that's…

Jonathan Kelly: I think we just square peg round hold this so that there was some form of discussion somewhere yesterday. But yeah,…

Kevin Hammond: what the community wanted.

Jonathan Kelly: 

Jonathan Kelly: There'll be better places.

Kevin Hammond: Yeah, but It was good discussion people and we'll carry it on later. Right. Okay.

Sebastian Nagel: Yeah, I hope we'll have some time for discussion or open Q&A later. it's not probably will be 15 to 20 minutes or so time for that.

Kevin Hammond: So, what we might need to do is to organize some sort of follow on

Sebastian Nagel: Yeah. Yeah. If you want to really go into details I think we can have another session somewhere else.

Sebastian Nagel: It was the idea of Chris to start on a zip editor's meeting not just to do it only there

Kevin Hammond: Yeah. …

Kevin Hammond: sounds sensible to me. Alex. Hi. Hi. Welcome everyone. So, Adam, I think is traveling. So, we're not expecting Adam. so we have seven of us. Mark Marcus is not here.

Kevin Hammond: and Ben is not here yet. we've got a relative. So, the proposal was to keep this meeting short so we could go to the layoffs monthly meeting. rather than waiting several minutes for people to join us, what I'd probably propose is we get on with the agenda and then fill people in if they join us late. Is everyone okay with that? Great.

Kevin Hammond: So I'll just Hi Marcus,…

Markus Gufler: Hello.

Kevin Hammond: so I'll just quickly paste the agenda into the channel. But I think the first item I put up was the minutes from the last meeting and any actions that we needed to carry out. So I think one of the actions that I was aware of was to provide feedback on the IUR progress report.

Kevin Hammond: Was the link with that shared with us tax or Christian. is there anything critical from the list?

Terence McCutcheon: Yeah, the links were emailed directly to all members of that were invited to or…

Terence McCutcheon: part of the meeting last week. so those were linked there and I don't remember but they were in the chat that they were shared accordingly. I also have the other actions in a list if you not that I'm seeing. Obviously, we're meeting now. You shared metadata already. you have hard fork, which may not be on the agenda. There's, Carlos with invited to the parameter committee, recruitment input for security incident manager role.

Kevin Hammond: Yeah. Yeah.

Terence McCutcheon: And then obviously the slot paddle discussion was postponed. So,

Kevin Hammond: So I think we've covered up all the actions then but we should all take an action to provide input to the IUR progress review. so got several items on the agenda which I've put in the chat and pinned. is there anything anyone wants to add to that? Anything anyone wants to remove from that?  Given the time we probably won't get through all the items in detail, but we can carry anything that we don't cover, we can carry over to the next meeting. so first thing is half working group update.

### 00:05:00

Kevin Hammond: so I met earlier today with text Christian and with Jessica from IO to discuss this and Matt Davis from Intersect and what we've agreed is we should reform the Harford working group. We had a discussion about the procedures for that. we discuss the timebased release proposal that Nicola and Adam were promoting that seemed to be met favorably with so positively but we need to work out how that would work out in practice and what we would propose is to reconvene the meeting starting of this month from the end of October.

Kevin Hammond: So today's meeting is the 1 of October 2025. and start with a relatively small core group initially and a relatively slow cadence probably about a four-week cadence and then to increase the frequency of the meetings as we approached the actual hard fork deadline as usual. Hi hi Ben welcome.  So, we're just discussing the hardworking group update and He's gone. No, you're still there. And the proposal is to reconvene the hardworking group starting from with meeting at the end of this month. so, several items to be covered.

Kevin Hammond: the most important are going to be initially the scope of the next hard fork and subsequent hard forks. So we want to get this on the agenda and make sure community has buy in. So it's not developers telling the community this is what's going to be in the hard fork.  There's got to be an open discussion about whether these are the right things and if there is additional scope what it should be some discussion about what assessment timelines are and discussion about what all the steps are that we need to go through to enact a hard because the process has got longer more complicated now than it was historically.

Kevin Hammond: But luckily Zamat has prepared an outline timeline to that we can look at and that the group can look at. One of the things that we do have to start thinking about is including not only tool developers, exchanges etc. but also those developing other node versions.  So even though it's probably too early to have production ready nodes for the next hard fork and getting the node developers involved in the process at least aware of the process early on I think is very sensible because they're going to have to be part of this process going forward and also making the node developers aware of the existence of these other nodes need to coordinate technically with them is going to be very important

Kevin Hammond: then okay…

Benjamin Hart: Sorry, you mentioned production readiness. I'm pretty sure Amaru is already used in production.

Kevin Hammond: but it's not a blockage…

Benjamin Hart: Anyone using scrolls is using Amaru,…

Kevin Hammond: then okay So that

Benjamin Hart: I believe.

Alexander Moser: It is not used.

Alexander Moser: It's a happy path that kind of works if configured for 4 hours straight, but it crashes upon every edge. No, it's not used in production.

Benjamin Hart: Okay, my mistake. Maybe it's not Amaroo, but I believe scrolls uses a different node, in production. Let me just pull that up.

Kevin Hammond: That's interesting information.

Sebastian Nagel: So scrolls would be based on palas right this is the rust library for blockchain primitives and few network protocols and that might be used by scrolls for example yeah it is also the same foundation used for maro and…

Benjamin Hart: Yeah, palace is the one.

Sebastian Nagel: so the palace is in production it is used in several infrastructure pieces similar like okamio and…

Sebastian Nagel: koopo and other indexers and so are all used in production  But these are

Kevin Hammond: Yeah. Yeah.

Kevin Hammond: So this is not really so this is in the category of tools chain followers.

Kevin Hammond: So not really any different from what we've experienced before but absolutely we should include palace in the discussion and on and othering great thanks thanks then so that's the current state of play I think a number of the TSC members have volunteered to attend the meeting. the proposed what we discussed earlier was having an open meeting or at least recording it so that anyone who can't attend can catch up on what was discussed.

### 00:10:00

Sebastian Nagel: Will we be setting the schedule or kind of which day of the week or which time?

Kevin Hammond: I think the heart working group will have autonomy to do that.

Kevin Hammond: But if there are inputs that people want to make probably the initial meeting will be fixed …

Sebastian Nagel: So we will start a synchronous communication channel which will bootstrap into kind of synchronous meetings on whatever they find as a suitable date and time. of course.

Kevin Hammond: but then the timing might evolve. Sebastian, if you try to punch time that suits too many people, it never works.

Sebastian Nagel: Yeah. No,…

Kevin Hammond: Did you have particular constraints or is it something you want specific just a general

Sebastian Nagel: The afternoons for me are always full, and I'm really keen in chatting kind of getting involved there. but yeah, that's just obviously for example I wouldn't propose a conflict with the TSC otherwise I think these subset of people want to be that's fine by me.

Kevin Hammond: Yeah. Yeah. we need to try to do that. the reality is that if you want to include people in US time zones later in the day Later in the European day is better.

Sebastian Nagel: Maybe we need to have two even eastern one for western. no that's good. I just wanted to know maybe we had a time already in mind or there was a legacy time when it were last held right so we could just maybe reinstate that one as seemingly it worked out in the past of similar or a subset of the people who should be involved. just wondered whether there is starting

Kevin Hammond: No, nothing was discussed yet as taxex or Christian can probably coordinate that. We'll need to work around the intersect staff availability as well of course.

Terence McCutcheon: I believe the previous this is about hard fork,…

Terence McCutcheon: I believe the previous meetings were scheduled roughly 1 hour before the release meeting.

Sebastian Nagel: That is…

Terence McCutcheon: Believe that was the cadence.

Sebastian Nagel: how much is that end right?

Terence McCutcheon: I would say there might be room for discussion there…

Kevin Hammond: Yeah, I think that was probably mostly for convenience of the people concerned.  I mean in some ways it makes sense to have the release meeting first and then the hard fork meeting even to possibly cast part of the release meeting as a hard fork working group  Sust.

Terence McCutcheon: where if there should be a wider release meeting at any point like the other technical

Terence McCutcheon: working groups that are hosted via Intersect that every third or fourth week weekly that's something that's hosted by Intersect and can also be utilized for the hard fork purposes. So,

Sebastian Nagel: I saw a recent request by somebody whether there is kind of one intersect calendar having all these working groups on a time schedule throughout the week or maybe every other week. I think you responded tax maybe you want to also kind of share anything here as we're talking about scheduling yet another working group or committee. just getting to know a few of…

Sebastian Nagel: what things are at present, the schedules are at present.

Terence McCutcheon: So I've got a written reference that is on right now the open source committee getbook page.

Terence McCutcheon: But I also have basically direct control to the various calendars. So, if it's not on the intersect events calendar and thereby transferring to the event dashboard that some of you may have seen, then for whatever reason, I'm not aware of and the intersect events calendar is what populates Discord. and then there's a certain script that populates that to the events dashboard.

Terence McCutcheon: So B basically I mean not to be a bottleneck or a stopgate but that all comes through me. So if you're not seeing something it just means that I have not been approached or given the correct information.

### 00:15:00

Sebastian Nagel: That sounds wonderful. can you provide a link to that events calendar you mentioned?

Terence McCutcheon: It's an internal only access to update that. and I don't believe that last I knew is that they didn't want the public link to that being shared. because again that calendar is accessible in Discord, which I understand only shows two weeks at a time.

Sebastian Nagel: …

Terence McCutcheon: What's upcoming in the next 14 days?

Sebastian Nagel: so if somebody wants to know what's the schedule, Discord is the ground proof for kind of public reference.

Kevin Hammond: Yeah, the fact it only covers two weeks is a bit of a problem for irregular meetings text, right?

Terence McCutcheon: Yes. Yes.

Sebastian Nagel: So the events summary and the intersect discord server.

Terence McCutcheon: And that's why we've started putting some of those on the events dashboard to see that a little bit further. But I'm very well aware of the severity of the calendar issue and so it's been something I've been working on basically the last 18 months in addition to everything else that I'm doing. So as things change I'll work in flex to make sure that those are more widely known and…

Terence McCutcheon: we're still just trying to figure out the best tool. So that is the goal as well. So,

Kevin Hammond: Yeah, the more automated you can make it,…

Sebastian Nagel: That does it for my question.

Kevin Hammond: the better. Great. should we move on to the agenda? yeah. So, conscious of the time, Alex, do you want to skip ahead to the prow changes? I think we need some vote on that here. Is that okay? This is the max TX unit. We need confirmation from the TSC.

Alexander Moser: Sure provided you yesterday or two days ago, no it was yesterday with the rationale that we would like to post with the governance action to change the max transaction unit cost. I hereby ask the TC…

Alexander Moser: if we can move forward with the actual governance action. Is any vetos bring forth

Neil Davies: second that I mean…

Neil Davies: if people want more questions basically we could say the text that was written several months ago in that action will be the final text apart from a reference to the minutes of this very meeting about it actually being approved by this meeting.

Alexander Moser: Therefore, there is no way to get hold of them anytime

Neil Davies: Right? So this is a formal report from the parameter subcommittee to the TSC saying we oppose this parameter change. Please can you say

Neil Davies: Listen.

Kevin Hammond: So let's do this formally, Alex. So you are formally proposing that this group confirm the recommendation to update the Pluto proto parameter for max TX units. and that we then issue that as a form of governance action via intersect. is that correct?

Alexander Moser: Y do proposers have votes too.

Kevin Hammond: So, someone want to second that? I'll that. Neil seconded that. So, could we take a vote on that then please? Yes.

Kevin Hammond: proposals have votes too. can we take this in a way which we can record the votes? So, I suggest raise your hand…

Kevin Hammond: if you're in favor. So, I'm seeing is it eight in favor? I'm assuming there please lower your hand. So all that's every voting member in favor as I understand it. carried unanimously. Are there any abstensions or no votes? just a matter of procedure.

Neil Davies: eight. D.

### 00:20:00

Neil Davies: Could you still have your hand raised?

Kevin Hammond: We assume you're voting in favor. Great.

Neil Davies: Okay, gone down. Good. So intersect who's going to take Kevin you going to approach intersect right so debit I will…

Kevin Hammond: Perfect. Great.

Kevin Hammond: So we can consider that proposal carried Alex which is great and we'll need to progress the onchain governance action. I will approach intersect about it. It may be that someone else has to carry it forward because I'm going to be away for a couple of weeks. Yeah. What…

Neil Davies: if you tell me what needs to be done I will Okay. Yeah.

Kevin Hammond: what needs to done in the short term is I need to be put in touch with Ryan Williams and we need to agree on how to do it. But Ryan's the guy.

Jonathan Kelly: Ryan's the

Kevin Hammond: But I'll coordinate behind the scenes to get that Brilliant. other items we've got 10 minutes.

Kevin Hammond: Duncan, you previously raised discussion about the stock battle discussion with the SPAS. Is that a short agenda item?

Duncan Coutts: Yes I think it is. Yeah sure.

Kevin Hammond: Do you want to raise it now?

Duncan Coutts: So I think it was really just reporting back from a conversation that so okay just stepping back we had had a conversation in this committee few weeks ago about some SPOS's particularly people who run small SPOS's being unhappy about the lot in general the lot of small SPOS's they have a difficult time and they had a specific  proposal which was to reverse a change that was introduced prior to governance coming in to do with how the VRFs are used for chain ordering in the case of slot battles.

Duncan Coutts: and the proposal specifically was to reintroduce an asymmetry in the situation that there were slot battles that would be in favor of the smaller SPOs. and so we discussed that in this subsequent to that, I offered to go and talk to the folks who were bringing this up. and we had a longer discussion about it and we talked over the history and I think we sort of cleared the air a little bit about why was this done and, a few mere culpas and that sort of thing on my part.

Duncan Coutts: so the end of the conversation was basically what advice was I giving and obviously I wasn't trying to talk for the whole committee but I did say that I don't think the committee is interested in I don't think the committee wants to take an opinion on whether there should  or shouldn't be a bias for or against small SPOS that we would be happy to go with whatever the community consensus on that is. but we do have an interest in making sure that whatever mechanism is proposed of makes sense coherent if it involves incentives which it will do that those incentives make sense in the round etc.

Duncan Coutts: and so my advice was that they should go ahead with writing the CPS. they were a bit concerned that this was just unnecessary bureaucracy and they've got limited time being small SPOS's. I made also the point that we also have limited time as volunteer members of the TSC. so there's a limited extent to which we can do some of this stuff for them because we're also working on volunteer time. so I said they should go ahead with writing a CPS. Don't try and make that too big. It doesn't need to be a big writing the problem statement. they can to some degree use the fact that there was already a budget proposal from IOG which got approved by DREPs.

Duncan Coutts: that is some indirect evidence that the community via DREPs are interested in skewing things towards smaller SPOS's because part of the question was how do you establish that there's consensus and then the other part the advice was go and talk to those people who are doing that because they obviously have paid time to work on this issue and so get in touch with the  people who are actually working the people at IoG who are working on the incentives stuff and make sure that they understand your opinion.

### 00:25:00

Duncan Coutts: So that was where we left it. And I wouldn't say that all grumpiness has been resolved. Certainly but hopefully that there's a path they can see forward.

Kevin Hammond: Yes, it seemed to me Duncan that the issue for the state operators worked around the incentives and any concerns worked around the block production.  So the month two are tied together the SP issue and obviously for block production any bias is potentially problematic.

Kevin Hammond: But the incentive scheme is less of an issue should we say and…

Kevin Hammond: so I think the SPO issue is really about the incentives rather than the block production

Duncan Coutts: Yeah. Yeah.

Duncan Coutts: And we made the point and we went over this issue again and again about the thing that they were looking at how much was that actually going to change.  The point I kept making was that, it's very little and that they probably want something that is tunable and something that's much more substantial than something that only makes a difference, 2% of the time thereabouts. That's not enough to make a small SPO profitable.  So yes absolutely it should be part of the incentive stuff and as you say although we didn't actually make this point clearly in the meeting just saying that they need to come up the point is they need to say the problem clearly and then the people who are working on a potential solution can think about potential solutions and those aren't the same groups of people and that's another reason why writing a problem statement is actually really useful here because it's not unreasonable to expect them to work out a mechanism

Duncan Coutts: and do all the incentives analysis. but if they can clearly state the problem and they can get community consensus that people agree that there is a problem, that we want to support, skew things towards small SPOS's so long as it doesn't create systemic problems and then go and talk to the people who are working on that to see if, they can put some paid hours into figuring that out. And as you say, Kevin, that could be on the reward side.  not necessarily on the block production side. So I think that's maybe a rather longwinded summary

Kevin Hammond: Great. Nicholas is calling

Jonathan Kelly: I'll just add that the IOE budget line I think Carlos Lopez Delara is currently taking active feedback on this. so if there's anybody watching this meeting that would be a point of contact to continue discussion.

Duncan Coutts: Yeah, thank you.

Kevin Hammond: Great. So,…

Duncan Coutts: Yeah, I wasn't quite sure who they were supposed to contact. So, thanks

Kevin Hammond: thank thanks so two minutes before the layoffs call. so we could either cover TSC committee budget briefly or perhaps mentioning the security council bug bounty nomination for Mike Horn might be interesting. this question with us. No question.

Christian Taylor: Yeah, I'm here. sorry. Yeah. Can you repeat that?

Kevin Hammond: Do you want to quickly cover the bug bounty issue?

Christian Taylor: So, what we're doing is the OSC a while back as we were still drafting the budget wanted to, compensate Mike Hornin for his vulnerability, disclosure before plumbing, and make that the first payment of the bug bounty program. we just want to make sure everyone's in line with that and is good with it. and we can do some fanf fair around it if everyone's okay. and the disclosure we had it down I think the budget allocation is somewhere between 5 to 10,000 for the vulnerability.

Christian Taylor: that's up to the security council right now to make a recommendation and then we'll bring it to the TSC and OSC for their thoughts and comments as well related to this. So

### 00:30:00

Kevin Hammond: Always nice to see the efforts of community members recognized in this way.

Jonathan Kelly: I'm sure Neil is intimately familiar with the vulnerability raised around

Kevin Hammond: Christian, no comment.

Neil Davies: You could say that. I wouldn't possibly comment.

Kevin Hammond: So conscious of the last meeting is about to start. I'll just quickly mention the TSC budget issues. so at the ISC meeting on Monday, it became clear and it wasn't clear to me before that it would be possible for the PSC to apply to put forward its own budget proposal for operational cost that we didn't get in the earlier round with the agreement of the board.

Jonathan Kelly: Pull out.

Kevin Hammond: what I had thought is that this was in the control of the budget committee. Apparently it isn't. but apparently what we would be able to do would be to put board a proposal to board request support for putting an operational funding request that could cover things that we discussed support for the hard working group perhaps support for technical town halls and other things.

Kevin Hammond: So I'm just raising it here as a possibility and we can carry on discussion of that in the Slack channel or in future meetings. But it did seem like an interesting change in perspective and something that would help us progress the goals of this group. Great.  For those who want to go to the layoff meeting, shall we call the meeting to a close now? Thank you everyone for attending the meeting and I will see you all in at the next meeting in two or three weeks time. Bye. Thank you.

Alexander Moser: Happy vacation.

Jonathan Kelly: about pregnant.

### Meeting ended after 00:32:40 👋

This editable transcript was computer generated and might contain errors. People can also change the text after it was created.

  
**