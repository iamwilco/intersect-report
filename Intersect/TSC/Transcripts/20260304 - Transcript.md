**

## Technical Steering Committee - 2026/03/04 15:58 CET - Transcript

# Attendees

Alexander Moser, Benjamin Hart, Bosko Majdanac, Kevin Hammond, leandros bsp, Mark Bùi, Neil Davies, Nicolas Biri, Ryan (Cerkoryn), Sebastian Nagel, Terence McCutcheon

# Transcript

Bosko Majdanac: Hello Kevin will join too. We were just on another call.

Ryan (Cerkoryn): Are we pushing these meetings back an hour starting next week? I noticed that on my calendar. I forgot about that.

Neil Davies: I think this one's trying to be except in British Columbia anymore,…

Benjamin Hart: Yeah, I think you're going to have with daylight savings time,…

Benjamin Hart: it's going to get pushed back and then pushed forward for you. So Europe goes to daylight savings a little earlier and…

Ryan (Cerkoryn): That explains it.

Benjamin Hart: I believe that this is on a European time zone meeting and…

Ryan (Cerkoryn): That makes sense.

Benjamin Hart: then yeah it's going to be about a two or three week interruption for

Ryan (Cerkoryn): Yeah, that sounds fine. I totally forgot about daylight savings. Forgot that's a thing here. Yeah. Yeah.

Neil Davies: isn't it? I like it.

Ryan (Cerkoryn): I'm not a fan of daylight savings.

Benjamin Hart: Yeah, they've just done their last transition. Oddly enough, they've decided to lump themselves in with mountain time effectively.

Ryan (Cerkoryn): It just screws up everybody's sleep schedule.

Benjamin Hart: Yeah, I don't know anyone…

Ryan (Cerkoryn): Especially…

Benjamin Hart: who actually likes daylight savings.

Ryan (Cerkoryn): if you have kids. It just messes everything up.

Neil Davies: But the funny thing is my wife insists she doesn't like it not being daylight saving.

Neil Davies: She doesn't like the other way around. I always have pity for the poor Chinese. They've only got one time zone across the whole country, right? And basically they should have six or something or something like that. Basically, some people are always waking up in the dark. Yeah. Hey, when civilization collapses, we can go back to sundials.

Benjamin Hart: Yeah.

Alexander Moser: In comparison to China, Russia has 12 zones something like that.

Neil Davies: Yep. Yeah.

Alexander Moser: The complete opposite. It's ridiculous.

Neil Davies: China's got I think it depends how you think bodies work. I'm 12 minutes behind the sun here. it's this nice orange globe in the light…

Kevin Hammond: What's a thumb Neil?

Neil Davies: which is lighting up all the surroundings. I've actually moved into a darker corner of the room. I've got out of my office and it's getting too hot because of the solar gain.

Kevin Hammond: So, apologies for joining site late. We're in a call which was running a bit late and that I got the wrong meeting for some reason. so, I suggest we start the meeting So welcome to the technical steering committee meeting of the 4th of March 2026. we have one, two, five tax steering committee members present as I understand so we are not quarant at this point in time unless someone else joins. As usual, I've pasted the agenda into the chat.

Kevin Hammond: So, are there any other items that people would like to be, added to the agenda? And I know that Ryan, you need to leave in 20 minutes.

Ryan (Cerkoryn): Yeah,…

Kevin Hammond: So maybe what we should do is to cover your item first.

Ryan (Cerkoryn): You want me to talk about the paper I put together?

Kevin Hammond: 

Kevin Hammond: That would be great. Are there any other items you need to add to the agenda?

Ryan (Cerkoryn): …

Kevin Hammond: Mark and Ben, you're joining us as guests. Any issues you want to raise with us?

Benjamin Hart: I'm just here to keep up on gossip.

Kevin Hammond: 

Kevin Hammond: It's nice to have you go ahead rhyme and then we'll come back to the actions.

### 00:05:00

Ryan (Cerkoryn): So I was just reading probably a couple months ago now at no April 2025 there was an IG paper reward schemes and committee sizes and proof of state governance that I read through because I was interested in the DR compensation thing. I think the methodology is good but there was some premise that didn't sit right with me.

Ryan (Cerkoryn): Basically what they did was boil it down to every outcome on a governance action is either good or bad, which I don't think is something that is realistic or measurable, right? Because I think everything's going to be shades of gray. So, I wanted to try and, I don't have a PhD of my own, so take everything my criticisms with a giant spoonful of salt. But I wanted to see if I could do it better, not assuming that you could start from a binary outcome of either good or bad and then try to quality control because I don't think we can quality control. if we can't measure good and bad. so I decided to try and optimize for different things. so one of them is decentralization which is a commonly cited concern about voting power right now that is too concentrated and then the other one is participation trying to get more people participating in governance. so those two axes are what I optimize for trying to make my own method. and I came up with this idea exclude K pay and it's very simple.

Ryan (Cerkoryn): you just take the top krep. So I as an example use 10 and you exclude them and then you pay the next n. So we'll say n is 100. and then I wanted to see how that would help because intuitively it would make sense to reward decentralization by incentivizing the next up in terms of dreps in terms of voting power. so I ran a couple of simulations and they're there at the bottom and I'll get you in one second, Mark. U and kind of came to the conclusion that it could be more beneficial with smaller budget amounts. it even extremely small budget amounts. So one of them has a budget of 100 ADA and if you have an N of 100, we're rewarding 100 DRPs. That's one ADA per DREP per proposal. So that's just enough to cover the transaction fees of voting.

Ryan (Cerkoryn): And that seemed to have had a positive effect on both decentralization and participation. And as you scale up the budget size, the rewarding proportional to voting power starts to overtake in participation, right? The more voting power you have, the more rewards you get. but decentralization seems to be to always favor the middle out method. and…

Kevin Hammond: Could you share the link to that paper in the chat,…

Ryan (Cerkoryn): that was basically my conclusions I came to there. what was your Yes,…

Kevin Hammond: please? Right.

Ryan (Cerkoryn): I shared both of them. they should be there. The original paper and my own. Yes.

Kevin Hammond: Thank you, Mark, you had a question.

Mark Bùi: I'm sorry to roll in late. So you guys were talking about the rep conversations like work scheme stuff, right? Yeah. Yeah. There has been a while, and they don't get to certain level.

Ryan (Cerkoryn): Mhm.

Mark Bùi: I mean there have been some source of GI which talks about the rep tipping span and stuff but I think that's quite unstable for a long term because in some sort of sense I think you have to move the ref some sort of a market first because there will come like people who reveals the GA and stuff and we delegate our votes to them. So it's better to create some sense of the market themsel and based on the delegation power we can calculate some sorts of parameters on the reward schemes…

Mark Bùi: but I just don't know what is the allocations if in case we want to run that reward scheme what is the allocation size of the budget that we would spend for draps

Ryan (Cerkoryn): Right. I think you made a good point there.

Ryan (Cerkoryn): I think basically the market by delegators choosing which dup they want to delegate to is the best quality control we have. Right. So those deer reps that are higher in quality will get more delegations. but you can't measure quality as did you vote yes or no on this governance action because nobody knows what the correct answer is. So I think using that for quality control is ideal. And then the other methods we have for incentivization is decentralization and participation. which is why I split it up that way.

Ryan (Cerkoryn): And I think that on one end of the spectrum you have the problem of rewarding plutoaucracy. If you reward the highest voting power, you're just creating a centralizing force. And on the other end, if you make it too easy for the I guess low end of the dreps to make good income on voting, then you have civil risks, Because nobody can just split into a bunch of DRPs and collect a paycheck from each of them. So I kind of like this idea for one because it's very low budget, I don't think's anybody's going to split for one eight per proposal or 10 ADA per proposal and two you still have to maintain yourself in that topish N range right so if there's a thousand D reps the first 890 don't get anything then the next 100 get a small incentive and then the top 10 also get nothing so I think it's resistant on both ends but that was just kind of what I put together in the paper so quick summary of

### 00:10:00

Kevin Hammond: Was the 10 based on the current situation in Cardano or…

Kevin Hammond: or is there some rational basis for that? Right. So n is the total number of draps or…

Ryan (Cerkoryn): I'm just throwing out easy numbers.

Ryan (Cerkoryn): So, I created heat maps of the different numbers of K 0 through 60 and then N 30 through 200. And the heat map kind of shows how they score. It seems to be consistently that a K of 10 does well. And then N anywhere between 100 and 200 seems to do well.

Kevin Hammond: the total number of draps that are rewarded.

Ryan (Cerkoryn): That get

Ryan (Cerkoryn): Thank And it's also worth noting that it has a fall through mechanism. So if a DREP chooses not to vote on a proposal, the next DRREP will get the reward. So if you're outside of that top 100,…

Kevin Hammond: And the top K get no rewards in your skin. No.

Ryan (Cerkoryn): anybody that doesn't vote, you could still get an incentivized for it. That's correct. In my mind, if you're a top DRUP, you have the power of influence is your reward and you can vote on your own treasure withdrawals. you have enough voting power basically to have that as your reward so to speak or your incentive and it pushes us away from having a centralizing effect right it encourages the next ISD repres to grow in size I

Kevin Hammond: Any comments from anyone else on the committee?

Mark Bùi: I have this opinion. so if we raise the rep some source of the right reveals and stuff AI agents they can do it with the prefix rule as really quick and really fast. So I mean the ref should be someone that is beyond the quality of just reviewing the gas. it's like the one who can raise the problems put our problems so for people to submit gas to the platform well because if we were about to drive the refs as someone…

Ryan (Cerkoryn): Mhm. For sure.

Mark Bùi: who can re proposal someone who can reveal G we basically just roll in the wrong the old path of the project capitalist and…

Mark Bùi: you know what happened to project capitalist lately. Yeah.

Kevin Hammond: Yes, I think we've had discussion before Mark about whether DRAs are the right people to review view proposals and…

Kevin Hammond: I think it's clear that they are supposed to be generalists rather than specialists. so if there is a very detailed technical proposal I wouldn't expect most ds to be able to do the review themselves without assistance except in a few cases there are some dups I know who are very technical but they are in a distinct minority I'm not sure I agree with using AI to do reviews of course in fact in other settings I'm

Kevin Hammond: involved in I'm explicitly required not to use AI to do a review. I'm required to use my human judgment.

Mark Bùi: Yeah. I mean at the end of the day AI is just like a tool and just it's up to you to decide because whether we vote or not is still upon us. but I mean for general stuff like summarize main key points and resources. I think we all need some source of AI agent to do that because nobody gonna read every line of the proposal anyways. Yeah.

Kevin Hammond: the problem is it can influence your judgment and if everyone is relying on the same everyone's judgment is influenced in the same way so it's certainly very easy to construct bias in a voting process that

Kevin Hammond: Okay.

Mark Bùi: Yeah. Yeah. I quite agree on that. if we were to put out a set of rules that is a two stereotype for the LM. So basically for every GA they can just rely on that stereotype rules and they're making out reviews which maybe sounds very logical but it's based on that stereotype preferences. So I mean the rep it's someone who must build their own set of rules so that they may have some different economical perspective and I think that is a good way to build that. It's not to put everyone into a certain set of rules and make them reveal B and reveal C like that. it's going to be very concentrated,

### 00:15:00

Kevin Hammond: So you've presented your proposal to us Ryan.

Kevin Hammond: I've not had time to look through it in depth. I'd like to go in and have a read through. what's your ask from us? would you like those who are interested to provide you with comments?

Ryan (Cerkoryn): Yeah, just generally feedback.

Kevin Hammond: Yeah.

Ryan (Cerkoryn): I mean, I'm on the fence about the compensation idea myself. So, this is just I challenge myself to come up with something that's less bad than existing proposals. And so, this is what I come up with. So, feedback is the general thing. It is true.

Kevin Hammond: And out of transparency, you're a DREP yourself, so you might be in position to benefit from this compensation scheme.

Ryan (Cerkoryn): And I would abstain if a vote came up for that reason. So it depends on…

Kevin Hammond: And you'd be looking to put this forward as a CPS or a SIP or something of that kind

Ryan (Cerkoryn): if the community is really still pushing for compensation, if they have better ideas.

Ryan (Cerkoryn): I think this could actually run as an experiment first before being as a SIP. I mean, ultimately it could be incorporated into the ledger and automatically paid out to people's Europe stake accounts. that could be a thing in the future if it has success. I think a better trial would be maybe a future budget proposal. We set aside x amount of ADA and we just pay it manually and…

Ryan (Cerkoryn): say, "Hey, we're going to, maybe Intersect manages it and say, "Hey, we're going to pay reimburse DREPs, one ADA per proposal." See if this changes and has the effects we want. And if it doesn't, then we don't renew it. So yeah.

Kevin Hammond: Yes, I suspect Intersect wouldn't want to do that.

Kevin Hammond: They've already complained to me about micro payments of a hundred $100 or…

Ryan (Cerkoryn): Yeah. Yeah.

Kevin Hammond: so at a time. It's Okay,…

Ryan (Cerkoryn): There'd have to be stipulations of maybe we pay it out only once every couple months something. I don't know. But yeah, just throwing out an idea there. So it doesn't have to be Intersect either. It could be Whoever wants to take it up.

Kevin Hammond: So then let's table this. We'll come back to it. and those who are interest so we'll put it on the agenda for next time and we'll solicit feedback from the committee in the background and those who would like to provide comments please do so and we'll just come back to this because it's an interesting idea.

Kevin Hammond: I was involved in the original discussion with the researchers on DREAP compensation. It's one of the things that we decided was just too much to put into set 1694. And we also thought there would need to be some experimentation with different schemes before we could decide…

Ryan (Cerkoryn): for sure.

Kevin Hammond: what was sensible to include in ledger rules. So I think your approach of testing it out is a sensible one if we can work out the mechanism to do.

Ryan (Cerkoryn): Mhm. For sure.

Kevin Hammond: Thank you very much. moving First item on the agenda actions from the previous meeting. Boston.

Bosko Majdanac: So for Alex Moser to publish the community post regarding the staple operator and that was shared and we have reposted it from the DSC account, for Leandros, it was to incorporate feedback from the product committee into the KPA document by next week's meeting, meaning this week, I suppose. And that meeting is after this one, something like that. So, was that done based on a thumbs up? It was from Andrews.

leandros bsp: Everything was okay with that.

Bosko Majdanac: Kevin and Neil to convene a dedicated session to draw the formal technical concern statement regarding constitution 2.4 for the civics committee. So did that happen or not? Okay.

Kevin Hammond: Not yet. boss, we've both been too busy with other things.

Neil Davies: Yep.

Bosko Majdanac: So should that stay on the action items list for the next call?

Kevin Hammond: Yes. keep it as an action item and I'll aim to sync up with Neil.

Bosko Majdanac: Okay. So that will stay on the list. Okay.

Bosko Majdanac: for Borcoin for myself and Ryan Williams to update the hardwork timeline diagram but s also we also had another meeting yesterday for the hard fork so we will give an update later that's on the agenda Ryan I mean dup compensation paper and then Sebastian who is not here so organized a dedicated tech session for TSC to dive deeper into linear layouts risk management

Kevin Hammond: I

Sebastian Nagel: I am here. I joined late.

Bosko Majdanac: you're here. I didn't. Okay. Okay.

Sebastian Nagel: I'm also a bit on the go,…

### 00:20:00

Bosko Majdanac: Okay.

Sebastian Nagel: but I can hear you.

Bosko Majdanac: So, is DSC court right now? Maybe it is since Sebastian joined. So, if it's six of you guys, then linear layers risk management. that was the action item to organize a technical session.

Bosko Majdanac: So I suppose that didn't happen yet.

Sebastian Nagel: Not that I I think it was a follow-up of last week's conversation we had following the monthly and it's happy to get any insights or feedback. I mean the people on the TC if you want to share any insights with me let's have a conversation as synchronously on the Slack or maybe organize a inerson chat there independently I'm all for it but I'm not prepared for today or anything if you want to have it on the agenda.

Kevin Hammond: Yeah. …

Kevin Hammond: why don't we maybe set up a doodle poll and then we can organize a session. You can Yeah.

Bosko Majdanac: So that's the action.

Bosko Majdanac: So to set up a loop to actually schedule this one. Okay. Yeah.

Kevin Hammond: And then not if people don't sign up, Sebastian, there's no point having the meeting. Right.

Sebastian Nagel: Yeah, I'm game. If you want to share any insights with me or just have me I mean technical discussions around the matter are always appreciated.

Bosko Majdanac: That concludes the list of the action items. So I suppose we can go to the next thing on the agenda and that is the composition. Okay. Van Rosen Harox status.

Bosko Majdanac: So either whoever wants to jump in and…

Bosko Majdanac: give the status Kevin, maybe you shared it in the heartful correcting group channel if you want.

Kevin Hammond: Yeah. …

Kevin Hammond: so the half working group is convening every week now. based on the state of progress no node version 10.7.0 is in preparation it is very close being complete. that won't be the version we go to the hard fork with, but it will enable testing on preview possibly pre-pro. So, we'll be able to go to a situation where we're testing, but there are still some things some changes in the works that the team has to do prior to having a candidate for node version 11.

Kevin Hammond: So the meeting discussed likely dates for the halfhour you're currently projecting roughly May Bosco based on current status…

Bosko Majdanac: late May. This is what I'm there just a forecast.

Kevin Hammond: but it's hard to predict because we're essentially waiting to get a final version of note and as I was pointing out in the meeting we're exactly the stage where you don't know what might crop up yet. So once we've got the version of the node, all the issues have been fixed, we've done all the regression tests, we don't have any performance issues, then we'll know that we're in a good state to go. But at this point, we can't quite predict when the final version of the node will land.

Bosko Majdanac: So we don't have a crystal ball.

Bosko Majdanac: So yeah, this is just the forecast is based on the sequence of things that needs to happen and assumption that the node will become available in 7 to 10 days whatever and…

Bosko Majdanac: then there is no significant setback. So of course we don't know yet.

Kevin Hammond: Great. So,…

Kevin Hammond: we've got a rough idea about when the half will happen.

Kevin Hammond: There's going to be an X space tomorrow. understand…

Bosko Majdanac: Yes. Yes.

Kevin Hammond: what time is.

Bosko Majdanac: 3 p.m. UTC

Kevin Hammond: So I will send my apologies for that because I have a conflicting event. It's getting very busy at the moment. But it'd be great to have representation from the TSC there, people who can answer any questions. So please do go to that meeting if you can.

Kevin Hammond: We discussed So there's also the monthly SPO call immediately after that.

Bosko Majdanac: after that one.

Bosko Majdanac: Yeah. Yep.

Kevin Hammond: So there'll be an opportunity to update the state pool operators with the current state and we are starting to track who else needs to be informed as I understand at BOS. So this will be DAP developers it will be exchanges and very importantly it's also going to include no developers. I noticed in the Amaru proposal they have an ambition to participate in the vamrosum hard fork. So they will need to be kept in informed about the status.

### 00:25:00

Bosko Majdanac: Yeah. I think diversity group is on the readiness list.

Bosko Majdanac: However, I wasn't aware of the thing that you said about tomorrow. So, Okay. Makes sense. Thank you.

Kevin Hammond: We keep them involved. they need to be kept informed.

Bosko Majdanac: Yep. Yeah. Okay. Okay.

Kevin Hammond: They participated in previous meetings.

Bosko Majdanac: Mark there is no telegram channel to the best of my knowledge…

Mark Bùi: I'm sorry. does Intersect have a telegram announcement channels, for the meeting and stuff? Because I only open Discord when I actually works and usually there's a lots of notifications.

Bosko Majdanac: but I can tell you for the hard fork related

Bosko Majdanac: ated meetings and events. I just pasted the calendar that anybody can subscribe to and you will get all the meetings related to hard forks there. If you want to have any other intersect related meetings where intersect is involved, I can share other calendars as well. But the one that I shared is specifically for halfwork either half fork working group meetings or X spaces all of these will be there with the respective dates and times. Kevin you are asking me or…

Mark Bùi: Thank

Kevin Hammond: Yes. Yes, please. can you point us out that's the link you've posted above?

Bosko Majdanac: yeah that's the hard fork related events in Luma.

Bosko Majdanac: So you can subscribe to the calendar and you will be informed of any event be it the hardworking group or DXACE or whatever else we introduced there.

Kevin Hammond: Brilliant. Thanks a lot,…

Kevin Hammond: Again, if we can…

Bosko Majdanac: Yeah. it is going in a tweet.

Kevin Hammond: 

Kevin Hammond: if we can tweet that out. as long as we're doing our part to promote it,…

Bosko Majdanac: It is going in the weekly hardwork bulletins. it's being updated but still sometimes people just don't read don't notice that it. okay. What's Yeah.

Kevin Hammond: So, you can't force people to read things, but you can make sure that it's available for people to read.

Bosko Majdanac: And of course it's not a wall of text, so anybody misses what else? Parameter update status. That's sorry.

Kevin Hammond: So, one last so we also discussed at the hard fork working group the process for defining scope for future hard forks.

Bosko Majdanac: Yep.

Kevin Hammond: So Ryan who has just left us unfortunately he presented a voting tool which will allow multiplechoice poll so it allow voters to decide between different sets they would included in the scope of a hard for example. it will allow discussion of different parameter settings for example. So, it's a very opened polling setup. Sebastian

Sebastian Nagel: I also just saw that the builder fest which is in Argentina later this month that there will be a session by Ryan Williams about no diverse hard forks or a session like that and I expect that we get further kind of details on that process and…

Sebastian Nagel: and also advertise that a bit through the community. So that's going to be an interesting session too.

Kevin Hammond: That's great.

Kevin Hammond: So Ryan Ryan Wy, I know he's presented his proposal to the SIP editors meeting yesterday. I can't remember the SIP number. we can locate it. So, this is going out to the community. it looks like an interesting way to conduct polls. And these oll they're done via metadata. So they could be tied to an info action or they could be open, I believe. And having them open is interesting because it allows time limits which aren't restricted to the expiry date of an info action, for example.

Kevin Hammond: So I think it looks like an interesting way to get more community information targeting initially hard fork content but it can also be opened up to other purposes as well. So the proposal which Ryan's putting forward is essent which we were discussed is essentially that the CPS and SIP process should be the point of entry to the work that's being proposed the things that are being put in for choice in the hard fork.

### 00:30:00

Kevin Hammond: the community then gets an opportunity to discuss their preferences and probably there needs to be some refinement later because it's quite possible that the community might for example say we want absolutely everything and then we may not be able to build integrate all of the things that people want. So this is a good way to poll for sentiment, but there still going to need to be some discussion about the actual content for the hard fork and the half working group will need to be involved in that moving on to the next gender item parameter update status. So Alex, do you want to take that?

Alexander Moser: Yes, but I can't say much more than last week. We're looking at it in the parameter committee meeting tomorrow. So far, everything looks good. I think more than I do.

Kevin Hammond: I was deferring to you Alex. so what I can say is so we've been provided with a slight modification of the parameters. This was these reflective changes to value data and nonvalue data. the polit team discovered a small mistake in the figures they'd put forward to us. so we've got a correction for those to consider at the next parameter committee meeting. assuming there's no issue with that. What we'll need to do is we need to put together with intersect a proposal for the parameter update and that could be enacted before the hard fork. There's no need to keep that back Alex. So as soon as the parameter committee is ready to make a recommendation it could be progressed.

Alexander Moser: Great.

Kevin Hammond: Okay, good. We're cracking through Anything else from the premise committee, Alex? I think that's the main item There was a proposal that I think we might also need to consider from Mike Horn. So Mike Hornan was proposing a reduction in the deposit data ader to 5 ader and this would be to promote inclusion. So this would be something that might be being brought up to the next parameter committee meeting. I don't think there's a PCP for that yet.

Kevin Hammond: But Mike has started the discussion…

Kevin Hammond: because this is considered to be a parameter which is critical to the governance of Cardano. So a three month lead time for discussion on changes to that parameter.

Alexander Moser: Yep. Agreed.

Kevin Hammond: Does we're in an open meeting. Does anyone have any feelings as to whether this would be a good or bad change? Happy to or take any technical considerations.

Alexander Moser: I would have a question to the really Adam Rush at the time and…

Alexander Moser: the teams who defined that threshold that parameter. when it initially come up, what was their reasoning for 500 data?

Kevin Hammond: Yeah, let's pass that on to Adam. and the governance team. I think it was partly a concern to avoid flooding the system with too much voting, Alex. So there was concern that we might have many vote transactions and that could dominate the mainet traffic. It might also caused some performance issues. but Mike

Kevin Hammond: seems to have done some tests on Sanchonet and he's confident that the load is minimal. That might have been part of the rationale. It might also have been that 500 ADA seemed to be a small enough value not to be exclusive but large enough that to require some skin in the game. But that was from the perspective of a rich country. And it does seem to be exclusive to participants in lower income countries and it may also discourage self-representation. Hello Nicholas.

### 00:35:00

Kevin Hammond: So essentially it means that you need to have a reasonable amount of ADA to be able to vote on to be able to vote yourself. Otherwise you're forced to use DREP and…

Kevin Hammond: and lowering the value would make it easier for participants to self-delegate to self vote.

Alexander Moser: But apart from social or…

Alexander Moser: voting governance aspects, was there a technical reason such as spam protection because certificates are too large? is there an attack vector…

Alexander Moser: if we lower that amount to be too low that comes up when it's five or less?

Kevin Hammond: There's so the cost of consolidating the votes is basically the product of the number of voters and…

Kevin Hammond: the number of governance actions that are being voted on. So if there are a lot of governance actions and a lot of voters then you're certainly increasing load on the system and there are points at which that could show up particularly the ratification Alex.

Alexander Moser: That's cool.

Kevin Hammond: So because we allow votes to accumulate up to the point at which the vote is ratified you need to postpone the voting calculation some extent. Okay. So I so with the numbers we've got I'm not sure that's really an attack. but if we had a very large number of DRAPs and we had a very large number of governance actions in play then there could be some load and that could manifest at the epoch boundary.

Kevin Hammond: So it could create some delays at the epoch boundary.

Alexander Moser: Do you remember…

Alexander Moser: what very large meant back at the time when we define 58 as deposit? What is very large in terms of DREP quantities?

Kevin Hammond: We stress tested it with the benchmarking team. I can't remember the exact numbers, but I think we've tried something like 10,000 GRPs.

Alexander Moser: Could we pull that benchmarking result up…

Kevin Hammond: So I can't remember how many governance actions.

Alexander Moser: until tomorrow for the parameter committee team…

Kevin Hammond: I can ask for it. Yes, absolutely.

Alexander Moser: because that would be super helpful in some putting that number in context now that we have a value or…

Neil Davies: Okay. …

Alexander Moser: some history of maximum governance actions life that budget cycle

Alexander Moser: 30 which was really socially already at the limit of Anything more than that is extremely unreasonable and also attacking wise unlikely as every one costs 100,000 deposit. We could easily handle that 10,000 drips which is at the moment also unlikely to happen anyway. But that information would make deciding whether five is a good idea quite helpful.

Neil Davies: the stress test from memory was done with I think the stress test concluded that the number of dreps didn't make any difference in terms of the calculation cuz it was all done incrementally as the transactions were processed and it basically tested I think 30 or 40 transactions happening at the same time. So I don't think we can go back to the details…

Neil Davies: but I don't think this is a major problem.

Kevin Hammond: No, but it was a concern I think when the original number was being considered…

Kevin Hammond: because we didn't have benchmarking results. they were done as we were rolling out the version of the node that took us into either Chang or…

Neil Davies: But those benchmark marking results were done before they must be a 18 months old now. Yeah. Yeah.

Kevin Hammond: Plman might have been Plyman rather than Chang. Yes. So we do have the results.

### 00:40:00

Kevin Hammond: Alex, I can ask for those. I know exist.

Neil Davies: That should be I don't think that code we could ask…

Kevin Hammond: They might be for an old node version.

Neil Davies: if that code has been dramatically changed. I think the basic thing was the chain would run out of capacity before you could make it a big problem…

Alexander Moser: Yeah. Yeah,…

Neil Davies: but the chain would be full of votes be way before you got to the point where and not doing any useful work before you caused a problem. it's a different problem right?

Kevin Hammond: That I would see as a problem.

Alexander Moser: I would.

Kevin Hammond: Yes, it's problem of capacity.

Neil Davies: It's not a problem of performance.

Alexander Moser: Cool. Thank you. Good.

Alexander Moser: Then let's put that on next week's agenda to check in on that topic.

Alexander Moser: Maybe we could also ask Mike to write the PCP for it.

Kevin Hammond: I've pointed him at the PCP process.

Kevin Hammond: I will ask him…

Alexander Moser: Amazing.

Kevin Hammond: if he's willing to attend tomorrow's meeting. I'm not sure how busy he is at the moment. just making a note of those actions. so nothing else to be said. so everything is in hand for the police update.

Kevin Hammond: we have this other thing issue the DRAP deposit to consider but everything is taking over nicely there TSC budget update so Bosa you've put together a mirror board I would ask people to check my comments on Bosow's so check my feedback.

Bosko Majdanac: I actually just shared the mirror board that was put up by IC or somebody else. So there is a section for DSC there with the word packages and small descriptions. So I did something you gave update to it given so I'm not sure what is the next step. So should I update the mirror according to your feedback or what should happen next?

Kevin Hammond: And…

Bosko Majdanac: Just give me a sec to find the threads then. Yes.

Kevin Hammond: yes, we can paste that into the chat.

Bosko Majdanac: Yes, that's what I'm trying to do.

Kevin Hammond: But what I propose to would be to update the mirror board with my version and unless anyone objects strongly and then we can proceed to refine the text. So if anyone has any feedback, it's not yet critical as I understand at Bosco, but it will become critical fairly soon. So what Bosco has done is to take the budget proposal that we had put forward and to aggregate the items into a number of different work packages and that's what's being provided in the mirror board. the process I standard is we put those items in and then there's going to be some discussion consolidation.

Kevin Hammond: So some items might be transferred over to the OSC. So they might be overlap with the OSC. For example, some things might be picked up by the budget committee and there might be some intersect central items that have to be merged in.

Kevin Hammond: So we just need to consolidate the budget. Do you know anything about that process, Bosia? I was asking…

Bosko Majdanac: I was looking for a thread.

Bosko Majdanac: Can you repeat the question? but the only thing I know for this week is to iterate in a feedback loop.

Kevin Hammond: if you had any details about the process that we have to follow.

Bosko Majdanac: So to update, but nothing on how it should end up being. I'll try to figure out after the call.

Kevin Hammond: Yeah, it's key. It keeps informed. so we're aware there's supposed to be a feedback loop. We don't know what the feedback loop is. so it just keep us informed as to I can't find it either.

### 00:45:00

Kevin Hammond: I was looking for that.

Bosko Majdanac: I shared the thread for…

Bosko Majdanac: what we were discussing for work packages for mero I shared it in the chat but if you're looking for something else then actual text for But your message.

Kevin Hammond: I can't. Could you paste the actual text, Boss? The text my changes to your work packages.

Bosko Majdanac: Yes, I can Just give me a sec. I'll paste it in chat here. I don't know.

Kevin Hammond: Right. Right.

Bosko Majdanac: I don't know. Yeah, it's a bit Not so well formatted in this chat. But I pasted the link to the thread. It should be visible there.

Kevin Hammond: I can't connect that link unfortunately.

Bosko Majdanac: That's strange…

Kevin Hammond: I ask I know Google and…

Bosko Majdanac: because you're there. It's your M. It begins with your Okay.

Kevin Hammond: Slack are messed up. Okay. is that all of the work packages bos

Bosko Majdanac: Okay these three are just my suggestions so I don't know…

Bosko Majdanac: what others can do or cannot do but it's in the technical steering committee channel so I don't know what do they do let me trying to find a meaningful way for everybody else to see it. Let me open the mirror board and share it. But I need to update it with what you're saying. We have some comments. No, this is Lorenzo overlap security overlap. What is the scope? Okay, it's Lorenzo asking some questions.

Bosko Majdanac: but these are the things that are being put there. and the next step for me would be to update it based on your feedback then to ask TSC members to give feedback on it plus to understand the questions being asked from Lawrence as well or you can I don't know what's actually in them didn't put too much attention to it this will need to be covered by internal badge

Bosko Majdanac: …

Bosko Majdanac: core operations planning seems that it would be covered with internal budget.

Kevin Hammond: …

Kevin Hammond: that's good information. So, we'd put this into our proposal because we didn't know Bosco Thanks.

Bosko Majdanac: But that would only help to finalize the version of the TSC operational budget. So we would exclude these for example but I would like to confirm with Lorenzo on these things So we avoid some back and forth communication. So I can switch back to sorry where is in this tab.

Bosko Majdanac: So yes true I know what the action item is for TSC budget update. So one thing is to clarify…

Bosko Majdanac: how the feedback loop works in this context and just to make sure that the comments being written in mirror are relevant so we can consider them. Jine should be open to everybody but I don't know.

Kevin Hammond: Does everyone in the TSC have access to the mirror board?

Kevin Hammond: So, everyone can comment on that. Great. Okay.

Bosko Majdanac: Yeah, but I would like to update it based on your feedback on Slack first.

Kevin Hammond: So let's try and have the internal discussion via Slack consolidate any discussion there that reflect that into the mirror board.

Bosko Majdanac: I will put the message in the thread and also we'll send it to the main channel so you can find it quick.

Bosko Majdanac: DSSE budget items. I did it in the DSC channel. So the next agenda item if you want to take it over Kevin constitution are you speaking about the budgets I

Kevin Hammond: Yeah, before we do that,…

Kevin Hammond: Bos, I would just ask the TSC members if they are broadly in agreement with the discussion with the items that have been put in, have they had the opportunity to look at those? Do they have any feedback that we should incorporate budget item?

### 00:50:00

Kevin Hammond: Yes. Yes.

Bosko Majdanac: Uh-huh. Okay.

Bosko Majdanac: Are you asking for their feedback now or general? Uh-huh. Okay.

Kevin Hammond: Giving people the opportunity to voice feedback at this point in time. Obviously we can so if anyone has any points to raise now now it's a good point to raise them for discussion. Sebastian, you've visualized yourself.

Sebastian Nagel: No, I have to admit I haven't looked at this myro version now of it and I would need to look there again because it's the latest point where we consolidate it, right?

Kevin Hammond: Look in Slack. so Bosco prop made some suggestions. He put those into the mirror board.

Kevin Hammond: And…

Kevin Hammond: I commented on Bos's version, but I don't think you've included my comments, Bos. Not yet.

Bosko Majdanac: Not yet.

Bosko Majdanac: Not yet. I can do it after the meeting while I'm preparing the meeting notes and everything. I can clean this thing up. But for the latest on some of those working packages, you should look at Slack at the time being.

Kevin Hammond: So look at the site version and comment on the version and…

Bosko Majdanac: Yep.

Kevin Hammond: then comment on the mirror once it's been updated.

Bosko Majdanac: Yeah, I will let you know guys in on Slack when the mirror is updated so you can easily switch back there. Yeah.

Kevin Hammond: Could I So you've taken what we broken down into two streams Bosco and you have consolidated into five or six work packages. one of which it may be picked up centrally by intersect…

Kevin Hammond: which is fine.

Bosko Majdanac: And there might be some overlap with the open source,…

Bosko Majdanac: right? Yeah.

Kevin Hammond: There might be some overlap the open source so we need to double check for example there might be overlap but there might be gaps. So one of the concerns is we don't want to put in any double spend but equally we want to make sure that everything is properly covered. So if we have concerns about something it should be included and then we can agree with the OC for example whether it's in their budget whether it's joint budget whatever the appropriate approach is tax

Terence McCutcheon: Hey, so there are going to be some changes to the open source committee budget, but I was looking at that item in particular. as far as I understand, there's no overlap because the TSC line item is specifically vi funding to the security council. we had things that were pro provisions for an incident manager, but nothing for the council specifically.

Terence McCutcheon: So, I don't know…

Terence McCutcheon: if that's just not a request that got made to the open source committee or whichever, but as of now there was not any overlap in what was being asked.

Kevin Hammond: What I propose is we consolidate the budget requests there.

Kevin Hammond: So we're asking for something coherent tax and then we can determine which committee has ownership of the budget.

Terence McCutcheon: Yeah, I think Bosco and…

Terence McCutcheon: I can look at that offline because there may be some other changes to that as well. not yet confirmed, but we'll try to bring that back if not next week, then the week after, but that's also factored in the same conversation.

Kevin Hammond: And we were assuming that the OSC would apply for a renewal of the bug bounty for example.

Terence McCutcheon: …

Terence McCutcheon: the exact placement of that has not yet been determined. there's a scenario where it could fall under the OC budget or it may fall elsewhere.

Kevin Hammond: As long as it's included in the support for the security council,…

Kevin Hammond: I think that's the important thing. So the ownership is less important than the fact that the budget is Great. So actions on everyone.

Terence McCutcheon: Got it.

Kevin Hammond: First of all, comment in the slack on the work packages which are simply summarizing the items we had discussed in the budget proposal that we put together.

Kevin Hammond: Once we've got consolidated versions, Bosa will update the Muro board with those and we can track the discussion in the Muro board and we will monitor the situation with any intercept requirements on the budget.

### 00:55:00

Bosko Majdanac: Sounds fine.

Kevin Hammond: My understanding from previous discussions was the plan was to submit a proposal roughly at the end of this month. So I'm suspecting the clock will ing. fin item on the agenda, constitutional review. This was basically held over so Neil and as I said at the start of the meeting, we've not had the chance to sync up yet. So we'll hold that forward to the next meeting.

Kevin Hammond: For the benefit of anyone who wasn't here last time, it seems that the civics committee will be looking into a revision of the current constitution to correct some of the issues that have been found both by us by other parties. And we have also passed on I said last time the discussion of the min size parameter how to deal with that to the civics Any other items that anyone would like to raise in this meeting? Great.

Bosko Majdanac: End of the day.

Kevin Hammond: Thank you everyone for a great meeting, good discussion, a lot of fun as always and I'll catch you all again very soon. Bye everyone.

Alexander Moser: I don't

Kevin Hammond: Brought you.

Sebastian Nagel: Is it good timing?

Kevin Hammond: You're making us all jealous Sebastian.

Sebastian Nagel: No, it's just I was a bit confused whether I should pay attention still. she just brought me a beer here but now I think it's good that we're done.

Kevin Hammond: Unfortunately, I still have another two or three meetings to go to.

Sebastian Nagel: Yeah. Yeah. No, I started early today.

Bosko Majdanac: See you.

Kevin Hammond: See you then.

Sebastian Nagel: See you.

### Meeting ended after 00:58:35 👋

This editable transcript was computer generated and might contain errors. People can also change the text after it was created.

  
**