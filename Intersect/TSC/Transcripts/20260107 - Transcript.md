**

## Technical Steering Committee - 2026/01/07 08:29 CST - Transcript

# Attendees

Duncan Coutts, Kevin Hammond, leandros bsp, Neil Davies, Nicolas Biri, read.ai meeting notes, Ryan (Cerkoryn), Ryan Williams, Sebastian Nagel, Terence McCutcheon, Udai Solanki

# Transcript

Nicolas Biri: Can you hear Kevin?

Kevin Hammond: Happy new year everyone.

Ryan (Cerkoryn): Happy new year.

Kevin Hammond: 26 will be just like 25 but one better.

Ryan (Cerkoryn): least one better.

Kevin Hammond: So I'd put together a outline agenda which I pasted into the Slack channel. I just copied it into the chat here.  Were there other items that we should be discussing today? I'm conscious we've all been away for a few weeks. Okay. Bosco is away today. it's a holiday for him.

Kevin Hammond: Hi Ram. so the agenda basically is picked up from the last agenda. I think it should be a fairly quick meeting. I'll just wait a minute or two for anyone else to join us. Hope everyone had a good break.

Kevin Hammond: Nice lasting.

Sebastian Nagel: I

Kevin Hammond: Do you have access to the action items text?

Terence McCutcheon: Yes, I do.

Kevin Hammond: So, we'll be able to run through this.

Terence McCutcheon: So, from the last meeting here was an outline for the operational budget. Sorry.

Kevin Hammond: Just wait a second. I'll start the meeting properly. Just give people a second.  Okay, I think we can probably start now.

Kevin Hammond: So, welcome to the meeting of the technical steering committee, the first meeting of 2026. today's date is Wednesday the 7th of January 2026. And as I was saying before, we started the meeting properly. We've got a relatively short agenda because we're just catching up after the break. so we'll be re refreshing items that we covered in previous calls and then looking forward to what it is we do in 2026. So thanks you presenting to us the actions from the last meeting.

Terence McCutcheon: So first one up was for Kevin to draft an outline of the 2026 TSC operational budget and share it with the group. Here it says by the end of the week. I believe that a copy of that was shared again. within the channel today short blog post or ex thread about the impact of the constitution committee size if I remember correctly there was a draft for that I don't know that actually went out formal invitation to the product I do know the product committee did not meet this week so I don't know if many would be in attendance here today but this is on the agenda here at least for us to discuss for Ryan

Terence McCutcheon: Kevin and Ryan finalized the train partition incident report. TSC members to review the vision document specifically the strategy and KPI sections. and then for all members again consider and submit nominations for the vice chair position.

### 00:05:00

Kevin Hammond: Great. So, we need to check with Alex about the blog post. I think he did post something. but we can confirm that. but I spoke to Bosco about the invitation to the product commit a number of people are apparently still away today. So he hadn't done that. I asked him to extend the invitation to them and then we'll wait for them to respond to it. So they might be joining us next week or we might set up a session with our representatives of the product committee to discuss that. chain partition report.

Kevin Hammond: we've got that as an item on the agenda, but TRDR a version was finalized before the break, but it's not been distributed to the community. 2030 vision we can come back to in the agenda. and nominations vice chair I think we'll have to wait for Bosco to tell us what the state of play is unless anyone wants to out themselves and say they've applied for a vice chair position.

Terence McCutcheon: I would add a note here. sooner the better for us to get this established there. We're quickly running out of time before what would be the next slated election regardless of any change in term period. so as that stands basically the elections although they take place in April that tends to start around the March time frame or even late delaying that decision further means we're operating with just one single chair with no backup to a point where we got other confusion going on. So just information

Kevin Hammond: Or technically next we've got one chair and…

Terence McCutcheon: Sure.

Kevin Hammond: we've got eight backups.  So maybe I would say it's not as bad as is being implied, but it would be great to have a vice chair in post. and as I've said before, it shouldn't be a huge amount of work to do that. So please do consider Great. So moving on to the agenda chain instant partition working group.  I see we've got Ryan Williams here also got Ryan Kakorin. Would one of you like to present the current state? I think you're both at the last meeting. Ryan's Ryan Kakorin.

Ryan (Cerkoryn): So let me pull up the transcript for that meeting. I believe so I'm looking at the report right now. I've left a couple of comments on it. there was some discussion about what terminology we want to use when it terms to desired undesired minority majority chain, pick and chicken pig chain. I think that there's still some debate happening on what we want to call it. and then I left another comment on there just about key follow-up actions about just enhancing testing to cover cases like these. I don't think that the transcript for that meeting is here. but I can summarize some of the other stuff. draft report is nearing completion.

Ryan (Cerkoryn): key findings included that the blockchain ledger remained consistent, preventing double spends on the chain itself, and that approximately 500 transactions only appeared on the non-preferred chain with 20 previously unaccounted for.

Kevin Hammond: So Neil's was it not delayed due to asking for early view? the insect board and executives asked for sight of this before it's published. we gave them a view of this and…

Kevin Hammond: my belief is that we're basically waiting for feedback Ryan Ryan W on that. Is that correct?

Ryan Williams: Yeah. Yeah.

Ryan Williams: So we shared it in executives and board just before Christmas holidays as the working group had committed to deliver by then. over the holidays, yeah, we've been just waiting on feedback essentially before publishing publicly. as of yesterday, we did have some feedback from executives and I've just been updating the report with those suggested edits. Is all quite minor stuff. and we'll go over that with the working group this afternoon just to merge those suggested changes in,…

### 00:10:00

Ryan Williams: but I believe we're still waiting on specific board feedback. and that would be a blocker for publishing unfortunately. I don't want to speak for the board maybe…

Kevin Hammond: So that's the current status.

Kevin Hammond: So my impression is the report. So why Ryan, do you want to answer that

Ryan Williams: but I can have a guess. I think they feel the board feel this is part of their remit and part of their responsibility due to I don't know perhaps the importance of this report to review it.

Neil Davies: Okay.

Kevin Hammond: I'm sure we welcome any feedback on the report the board provides to us.

Kevin Hammond: Obviously what we don't want to do is trying to delay the report necessarily. but taking on board feedback is always important. my impression from the report was as you're saying Ryan that It's complete. I don't think there's anything that we would want to add to it. There's some details that we're discussing. So one of the things that Marcus Goofller raised was whether we knew precisely what the percentage of nodes was on each of the two chains.

Kevin Hammond: So looking at it I think we had some indication of what the relative weight was on the two sh we don't have direct evidence so we might need to slacken the statement that we'd made there remove numbers we seem to have suggested about 6% on the preferred chain and…

Ryan Williams: Yeah,

Kevin Hammond: 94% on the non-preferred chain. But we were making some assumptions there, I think. So, we either need to back that up with evidence or else soften the statement.

Ryan Williams: I have that as an agenda item for the call this afternoon as well, So, we can discuss with the group there.

Kevin Hammond: So, the call will happen immediately after this on the timing is not perfect from that perspective.

Kevin Hammond: So we'll provide an update from that meeting and hopefully it's just a matter of making editorial changes and then the report can be published. I one really want to put this to beds.

Ryan Williams: I agree with that too. Same sentiment from my side on that as A bit frustrating being blocked as we are with it to be frank.

Kevin Hammond: M anything you want to ask that or I know you've been involved in the working group.

Neil Davies: We pick it up this afternoon. I mean I mean I think we just have to make it clear by put saying the timeline of how the document was constructed that basically we are now waiting on the board has had several working days to look at it.

Neil Davies: If it's really that important, then they should pull their bloody finger out and do something about it to be very Welsh about it. Yeah.

Kevin Hammond: And…

Kevin Hammond: and to make sure we don't get the wrong impression, it wasn't delivered to the board the day before the Christmas break. It was delivered a week before in a close to final draft forms. we've had at least a working week to look at this

Neil Davies: So I mean we just have to make that clear I know this is being recorded but there was a pressure to be quickened and get it delivered before Christmas all of which has the pro that promise has been broken not by the people doing the work right that's…

Neil Davies: what I say I think it's just clear that it should be pointed out that's all you

Kevin Hammond: We'll discuss it in the working group later.

Kevin Hammond: But Thank you Neil and everyone else who's participated in that working group. it's the report I think is it's quite interesting. We managed to get to the truth of what happened as best we could in the time available. And there are obviously further details that we don't…

### 00:15:00

Kevin Hammond: where we don't have the full facts at this point in time that we investigate.

Neil Davies: and…

Neil Davies: and als I would also like from for this it's been recorded etc. The fact is that but the thing that strikes me is no one's screaming like hell that they got badly done by as far as I can tell. and that's important to know. I mean, we can't know. There's 20 transactions we can't quite work out. but no one is screaming,…

Neil Davies: look my children are starving because you did this type thing. So, I think that's really important that the system as a system maintained even across this event maintain consistency.

Neil Davies: I think that's the strength.

Kevin Hammond: Yeah, absolutely.

Kevin Hammond: It basically snapped back to the preferred chain.  there was full consistency maintained across that period and the only issue was the transactions that appeared on the non-preferred chain during that period which obviously didn't which as far as possible were replayed onto the preferred chain

Neil Davies: And that speaks to because when people look at risks and DeFi risks and chain bridging risks it's always about a hypothetical condition which may or may not occur and we have a practical problem that happened and that the actual risks that the hazards that matured that does I mean I'm not saying there isn't any but we don't know of any and no one's screaming at us and all the rest of it.

Neil Davies: So it wasn't perfect but it didn't seem to have any operational effect on people which is actually I'm finding surprising. I would expect at least somebody out there to have in some ways lost something right apart from a bit of inconvenience…

Neil Davies: which it doesn't seem to have been the case which is good. I think that's a strength that should be played up in an appropriate setting later on.

Kevin Hammond: Let's discuss…

Kevin Hammond: how the best way to present that. I think we already did in the working group, but this may be something for the comm's team. we want to stay factual in the working group. but there are positive messages indeed coming out of the handling of the incident and the resolution of the incident. it could have been worse. It could definitely have been worse.

Neil Davies: The point is, it's always been my adage. you can't and organizations can't avoid problems. And I know people say, " they've had a problem. They shouldn't have had it." But it's actually how they handle them is the strength is the real value when they occur.

Neil Davies: And I think this is being handled very well by the community.

Kevin Hammond: That's great.

Kevin Hammond: And kudos to the community for coming together and executing such a rapid response to the problem with that. Without that it would have been a much worse situation. Great. So we should move on to the next item on the agenda.  So the next item I put forward was the hard fork update. So this is basically slight new news item. the development status is that we have a almost complete version of the node.

Kevin Hammond: it's expected to be finalized and put out for testing within the next week or two. so this would be what we're expecting is that we will put 10.6.2 out for testing on some testn net. it will have all of the capabilities that needed for the hard fork.  We're just waiting for final integration of the A few last minute changes. and we would expect that to then probably become the release candidate for version 11 of the node the version that go through the pro protocol version 11 the van rosenom hard fork.

Kevin Hammond: due course there's another version of the node in preparation 10.7 which includes support for LSM. this is the log merge tree implementation off out of memory storage solution. So that's in preparation. it doesn't have any features that are essential for the hard fork. So it may well be that that then becomes a version 11.1 or something in due course and doesn't get released before the hard fork or it becomes an alternative to a 10.6 for the hard fork. But we'll need to see how the timing works out.

### 00:20:00

Kevin Hammond: What we don't want to be doing, I think, is to delay the hard fork for the sake of features that are not absolutely essential. So that's the current state of play. So based on what we know at the moment, it's likely to be a 10.6based release, which is the release candidate, but it might be 10.7 depending on timing and any bugs or issues that are spotted. So we're getting close. we will need to review the There's some new cost model settings for plutous primitives. We'll need to do that next week.

Kevin Hammond: Ryan, and I know Ryan Williams, we're going to have a meeting to discuss all of the different parameter updates and the timing because this is now getting potentially a bit confusing in terms of what has to be done over the next month or two.  So, we've got some postponed updates because of the constitution committee elections and we've got some other things which coming through the pipeline as well as these changes that are needed for the hard forks and we'll need to put together a schedule that will allow for all of those to happen in a reasoned fashion. So, that's the state play. any questions on that?

Kevin Hammond: So there's no date being predicted for the hard block at this point in time. all we can do is look at development status. I said expecting a preview version of 10.6 within a week or two is probably the best guess from where we are at the moment. that then needs to go through thorough testing.  Once it's been tested and people have updated their tooling, we'll then be in a position to put forward a hard fork event hard for governance action onto mainnet having done that previously on preview and prepro. So looking good timing not completely certain at this point in time.

Kevin Hammond: We don't have a tight agenda. Ryan, do you want to just speak to the thing you've put in the chat?

Ryan (Cerkoryn): So, the incentives working group has two parameters they're wanting to, present as well. And of, I'm sure you guys are familiar with the efforts to increase K to a,000 and also, we recently discussed, switching min cost to 75. and I can make the case for that one as well if that's a newer thing that people haven't, heard about. I can present those next week. but the big thing that we're trying to not do is we don't want to step on the toes of the parameters committee because I think that there's a requirement to set the hash of the previous successful parameter change for every parameter change governance action. So those will have to be coordinated so that they don't cause each other to fail. so we want to make sure that we have that in a row and then of course of that group are still prepared to put up the deposit funds on their own but are still seeking the blessing of the parameters committee. Oops.

Kevin Hammond: So, the next meeting of the parameter committee is on Thursday the 15th. Ryan, that'll be after the next meeting of this group next week.

Kevin Hammond: So, I next Thursday.

Ryan (Cerkoryn): Right. Next Thursday.

Ryan (Cerkoryn): Yeah. Sounds good.

Kevin Hammond: So, it'll be good to if you're present and we can have be an interesting discussion about reducing pool cost. Great. Thank you very much.

Ryan (Cerkoryn): Push it.

Kevin Hammond: Did you want to present that again next week or have we basically covered what you wanted to say?

Kevin Hammond: Do you want to have more time next week to go through your proposals in this group? Right.  Hat.

Ryan (Cerkoryn): I am happy to present either of them.

Ryan (Cerkoryn): We have the draft already for the governance action for state pool target numbers. So we could share that and you guys can just leave async comments if want. but I don't know if the case for lowering min cost at 75 has been made yet besides when we discussed it before the break you and me Kevin why that would be helpful. and we have some data to support why lowering it to 75 is helpful due to the decreases in block reward size. but I can make that case as well if that's something that the parameter committee would be interested in sponsoring that governance action as well.

Ryan (Cerkoryn): …

Kevin Hammond: Great. So,…

### 00:25:00

Kevin Hammond: I think it' be good to have at least an outline discussion in this group as as well as a fuller discussion with the parameter committee.

Ryan (Cerkoryn): sounds good to me.

Kevin Hammond: So, let's give you a bit of time on the agenda next week to do that.

Ryan (Cerkoryn): Appreciate it. Thank you.

Kevin Hammond: Next item I had on the agenda was TSC operational budget.  I circulated a draft of an operational budget based on the one that was put forward in April last year. seems like a long time ago. so I've circulated that happy to discuss that now or happy to give you a bit bit of time just to look through it and then we can go through it in detail next time.

Kevin Hammond: I think there definitely seems we had some support from James joined us last time and James was definitely in favor of providing support to community members for example and we need to do more in the way of technical outreach. So I think there's definitely a case to make for some form of operational budget.  We probably need to do this fairly quickly if we're going to do it. Otherwise, we'll be running into the 26 budget cycle and we'll have lost a year of budget. So, happy to go through the budget with you now have to give you a bit of time to think about it and then we can discuss it fully next time.

Kevin Hammond: Nicholas. Okay.

Nicolas Biri: I prepare to have a week to review the budget and then we can have a discussion. I guess at least on my side it will be easier to do it this way.

Kevin Hammond: Great. Yeah, I was expecting that given the timing and…

Nicolas Biri: Okay,…

Kevin Hammond: my memory has also lost a bit of effect. too many mints pies and Christmas pudding.

Nicolas Biri: perfect. it give you all week to look at…

Nicolas Biri: what the figure you put in and to w through next week. Perfect.

Kevin Hammond: Okay.

Kevin Hammond: What I haven't done in the operation budget, all I've done is to identify headings. so we had a discussion I think of the outline headings last time. I haven't put any numbers in terms of either ADA or dollars.  One things we'd have to do would be to determine what reasonable amounts were. But I find it's always better to discuss what before you start to argue about the cost of So that way you get your priorities right and you don't say we're not going to do X because it's too expensive for example.

Kevin Hammond: so once we've decided what it is that we would feel was sensible we can then start to put numbers to this but it wouldn't be a large budget proposal. It will be quite a small budget proposal compared with other ones that have been put in. So we're not talking about millions or tens of millions of Asia. we all take an action to read through the current budget proposal and u please make asynchronous comments on the draft there and then we'll have a full discussion next week. modul the meeting with parameter updates.

Kevin Hammond: we've touched on this. Ryan W. Anything else you want to say on that?

Ryan Williams: Probably not. We have a call tomorrow I think to go through that and try to work on that and we can present back to this group the outcomes of that.  The only other action that's worth mentioning is as per this group's recommendation inceptive moving forward with submitting a hard fork naming governance action for max van van rosen in hard fork so we're aiming to get that on the network this week so we'll be in this current epoch

Kevin Hammond: So you've got a draft set of metadata.

Ryan Williams: Yeah. Yeah.

Kevin Hammond: I took a look at it yesterday, looked like a good summary to me. you waiting for a bit more feedback on that, but it' be good to circulate that metadatative to this group so they can provide any input to it.

Ryan Williams: I do that right now.

Kevin Hammond: There's nothing secret in it I think. So it could even be public at this point in time.

Ryan Williams: No, that's yeah yeah yeah it's been shared around with quite a few contributors anyone who may know Max or wanted to add something definitely nothing secret I'll share with the group now it is share commenters okay yeah…

### 00:30:00

Ryan Williams: if you do have proposed edits please yeah if you get them in today tomorrow so we can make sure we get this on chain on Friday. Thank you.

Kevin Hammond: Great. Thank you.

Kevin Hammond: So, we'll take an action to look at this by tomorrow.

Ryan Williams: Yeah, it's pretty straightforward small metadata based on the previous one we had done when we renamed Chang 2 to plate. so yeah should be quite straight forward.

Kevin Hammond: So, final item on the agenda unless there's any other business is the 2030 vision. as I said, I've asked Bosco to approach the product committee with you to organizing a joint meeting.

Kevin Hammond: We had an action from the last meeting to look at the KPIs. Has anyone done that or were you otherwise occupied? Neil, I know you had some thoughts on the KPIs.

Neil Davies: Sorry, one moment. Yeah. I think my confusion having read the report is…

Neil Davies: what I'm seeing numbers but I'm not seeing how the KPIs feed into resolving a problem statement. Are you with me?

Kevin Hammond: Right. Yeah.

Neil Davies: The KPI should lead into a supporting person.

Neil Davies: we have this issue right and we with sub issue ABCD right and that you should be able to say this KPI meeting this KPI addresses this issue it's that sort of logic that's missing that appears to be missing to me…

Kevin Hammond: So you're saying the KPI is not tied to the

Neil Davies: because it should stand out when you read the darn thing first thing I'm through okay the point is the objective it's just that

Neil Davies: flow that it's the standard flow I'd expect to see in a call to action statement, for any document, right, which is just not there. okay, I'm just trying to be, I'm sorry to be cor if people who know me, I'm the least corporate person, but I understand how to interact with corporates. and I know it's a pain in the ass and people don't like it, but there is a logic there that needs to because What everything that I'm hearing of everybody else is about people wanting to spend money using ADA and…

Neil Davies: the people who have that money in their pockets are typically people who speak corporate in general. Right? Just saying.

Kevin Hammond: Right. Right.

Kevin Hammond: So you're saying to summarize we need to increase usage of the chain. Is that right? Is that  Yeah.

Neil Davies: no, the point is that I'm not trying to say what the product committee should say, Right. Because that's the product committee's role. But what I am saying is if it's increase the usage of the chain, right? Then you should be saying or if A is increase, objective B is make it vi etc. You should be able to tie the KPIs to why succeeding those KPIs would succeed with those objectives, in a direct way, right?

Neil Davies: because it turns out that you may not be able to fulfill all the KPIs and some will be less critical than others so that the point is the formation of this document should basically end up with the mission statement that everybody sort of gets behind in that way right and…

Kevin Hammond: we need concrete examples to discuss with the product.

Neil Davies: I mean I'm doing this at the highest yeah just saying yeah when we come talk to the product committee then we'll put some concrete examples together but I think it's just the general thing is that flow of motherhood and apple pie making better pastry crust and…

Kevin Hammond: What's  That's good.

Neil Davies: better apples getting rid of the apple blight type sort of levels of abstraction

Sebastian Nagel: I do recall that last discussion it was mostly about these objectives of reliability right which the KPIs are a bit off or basically not we don't see the connection there the adoption bits maybe is more okay these are product criteria metrics they can track it this way this makes sense or that we don't have any objections on that or we didn't discuss any so far and it's was mostly about the reliability for example being measured in clockless intervals that was I think a thing…

### 00:35:00

Neil Davies: No, no. So there are technical measures…

Sebastian Nagel: which was technically unound to kind of use that thing as a measure for reliability for example not in general are not filter

Kevin Hammond: Okay.

Neil Davies: but the other thing I did I remember stating last time is this notion of threshold target and stretch there were numbers put in there right and the consequence of not meeting those numbers wasn't discussed

Neil Davies: And I think that the point is it felt more like a top down management statement of this is what we want and you couldn't because you couldn't relate it back to…

Kevin Hammond: right? hey,

Neil Davies: what the consequences of not succeeding were in any shape in any way then it really just feels like yeah it doesn't hold water from that's my problem.

Sebastian Nagel: Okay. Okay. Good. My problem is not that.

Sebastian Nagel: For example, I just want to say I don't care whether these are aspirational numbers or not. I couldn't care less or I think I like that there is aspiration and that this is fine because the consequence doesn't impact it's a product strategy and…

Neil Davies: So Sebastian,…

Neil Davies: if they have no meaning, why are they there?

Sebastian Nagel: I think it's a product committee's remage to define…

Neil Davies: …

Neil Davies: Sebastian,…

Sebastian Nagel: what is a good strategy or…

Neil Davies: but yeah,…

Sebastian Nagel: what not.

Neil Davies: but actually, as a technical committee, shouldn't we the very thing they're asking us for is that their product strategy is one that is coherent and consistent? And that's why we're going to be awkward here.

Sebastian Nagel: Why I think yes the coherence and consistency of these metrics is important to us.

Sebastian Nagel: Whether they are realistic and achievable or attainable I think is maybe not so much my concern.

Neil Davies: That is an amazing statement to make,…

Sebastian Nagel: for example.

Neil Davies: That is an amazing statement to say. if the technical committee isn't there to try and object an potential objective reality, then that I must admit I completely disagree with you on that point.

Sebastian Nagel: So I think one thing which stands out by just looking it again was for example the reliability metric is something I think we discussed last time which we're not so happy with right for example this one about the kind of that much percentage of uptime being blockless intervals or

Neil Davies: Yeah. Yeah. I agree. you read it through. All right. And that was a technical metric which was just badly formulated.

Neil Davies: But if we're asking but to make the statement I'm sorry I'm going to come back is to make the statement that it doesn't matter what numbers they put in there is right because you're almost saying they'll get what they get and

Kevin Hammond: Yeah. Yeah.

Kevin Hammond: Let's take a concrete example here, mean, there's an aspiration, I know it isn't in there,…

Kevin Hammond: but say there's an aspiration to have 1 second finality for all transactions. we know that's not going to be technically Well,…

Sebastian Nagel: Yeah, we would be pushing back on that…

Sebastian Nagel: because it is not consistent with what we believe is technically easible. Yes. But whether it is the total value locked variable $200 million or $400 million or $50 million, I think there is no objection there. For example, right?

Kevin Hammond: it might be depending what the implications are, Sebastian. I don't suppose the product committee has looked at the implications. So, if you have a high total value locked, that might have some implication on how the total stake is distributed amongst state pools for example. Right?

Kevin Hammond: It might have an impact on liquidity. So there might be other things which there might be side effects of some aspiration.

Kevin Hammond: So you do need to think about those in terms of the total system operation.

Sebastian Nagel: So do I understand correctly that basically all KPIs should be scrutinized and…

Neil Davies: and I'd like to know…

Sebastian Nagel: rewritten with your advice or is it just a few things which are to be discussed and

Neil Davies: how meets the aspirations in all cases. because otherwise there's no consequence to failing to meet them and…

### 00:40:00

Neil Davies: therefore they have no meaning. So that would be my starting point, right? …

Sebastian Nagel: which is a process question not about the actual metrics themselves.

Sebastian Nagel: So maybe first about the role of the KPIs and…

Neil Davies: then whether they're realistic.

Sebastian Nagel: then about which KPIs make most sense technically.

Neil Davies: No, no, no.

Neil Davies: Then what happens is right so then you look at in that light having looked at them in that way right you'll then be able to say wait a minute let's just pick this finalization if your stretch is 1 second but your threshold is 15 then that's okay right we can see that's a technical achievement we don't see how you can get to one but as long as you haven't made you've made that a stretch I'm just trying to give  a stretch goal, then that's perfectly okay, so we're not saying you we're not trying to dictate things, but we are trying to dictate. There should be a reason about when you put all of these things together, there should be a point inside there which is actually achievable, right?

Neil Davies: If you've got aspirations basically that you can't meet both of them at the same time, you need to identify those as a product problem,…

Neil Davies: not as a because otherwise it becomes an implementation problem.

Kevin Hammond: Yeah. …

Kevin Hammond: I think the argument, Sebastian, is we should scrutinize all of the KPIs. We're not necessarily going to push back on all the KPIs. we need to determine whether they make sense and

Sebastian Nagel: Yeah, And I think most are fine and a few just require further specification or discussion. Right. For example, the reliability one which I recall as being one we discussed. But for example, a total value locked sounds completely fine.

Neil Davies: That was the obvious bad case, right? That was the obvious bad case. That's why we just

Sebastian Nagel: 

Sebastian Nagel: Yeah, exactly.

Kevin Hammond: Ryan, you've been waiting patiently.

Sebastian Nagel: The obvious good case is for example a TVL goal, and maybe being a goal is not that bad or is it a KPI but a consequence of the process there? It doesn't really matter much. No

Ryan (Cerkoryn): No worries. I have to drop for another meeting in two minutes, so I dropped everything in chat. But in general, I kind of agree with Neil's concern I think that the strategy as it is now is too broad and it kind of seems a lot like we're going to throw everything at the wall and see what sticks. so the way I approach it is we need to identify those things that are most impactful. what do we think is what changes can we make that are going to affect the KPIs the most. So we determine that first and then second we actually deliver on those things and measure how well we delivered them maybe leis is what it is and maybe it took an extra year, maybe we delivered six months early. and then third we measure how that thing that we delivered actually affected the KPI.

Ryan (Cerkoryn): So maybe we expect there to be more users,…

Ryan (Cerkoryn): maybe we expect more TVL, maybe that didn't happen. So we need to actually measure those things. We can't just throw everything at the wall and see what sticks and hope that our KPIs go up because we really don't have any ability to just magically make more users on the chain or magically make more TVL. we have to have second or third order effects that lead to those things.

Kevin Hammond: Yeah. Who's responsible…

Kevin Hammond: if the KPI is not met?

Ryan (Cerkoryn): Yeah, that's the other thing.

Ryan (Cerkoryn): There's no way to hold anyone accountable for these. They just seem too much.

Kevin Hammond: Okay, sorry making some notes now. Nicholas

Nicolas Biri: U I'm just wondering if what is requested from us from the product committee is a critique of which KPIs they have chosen and why they have chosen it and whether they make sense or not or whether it's a technical feasibility and  valid technical definition of this KPI. To my understanding, it should probably more the second than the first. I sympathize with everybody who have feeling about the write up of the product committee and I think we can all have a personal opinion about the write up.

Nicolas Biri: It's just that as a committee we should probably just focus on the technical feasibility of what has been written rather than giving our opinion about the KPIs that were chosen and the value of this KPI. and again it doesn't prevent any of us to give our opinion to the product committee and to interact with them and change their mind about their work. It's just that it's a different committee and I don't see…

Nicolas Biri: why we should interfere with what they are doing aside the technical feibility which they request if I understood correctly your opinion on Yes.

Kevin Hammond: I think it's probably deeper than that,…

Kevin Hammond: Nicola, Nicholas, because it could be that you've got conflicting KPIs, right? So there it's our duty to say

### 00:45:00

Nicolas Biri: But again it's Yeah. But Yeah.

Nicolas Biri: But we're down to an assessment of the technical feasibility of these KPIs for example. In that case it makes sense for us to tell if you want to reach this and that it can't be done it can't be done at the same time because of that reason if there's a technical reason behind it. my problem is that it looks like we are judgmental about the approach of the product committee and…

Kevin Hammond: Yeah. Heat.

Nicolas Biri: I don't think it's something that we should do as a technical committee.

Neil Davies: This is a standard consulting problem.

Neil Davies: people come and give you all their things and they ask you for is this feasible right and then you have to go back and say to them but actually you haven't asked the really important questions because there are these technical interactions you failed to capture that I think is beholden on us to give them to them give us to give the feedback to them and that's basically where we're coming from here the key thing the reason we will have difficulty and ongoing  difficultly this is unless we understand which ones are the most key KPIs to make if that makes sense. we will not be in a position to turn as a community to start doing the value judgments the trades will come up over the next couple of years.

Neil Davies: I'm saying do this badly I'm looking for a nice polite word, but you can think of the right word ourselves over in the future.

Neil Davies: Okay, that's 40 years of experience speaking. I'm just being going to be agist about this at this point. it's a really bad way.

Kevin Hammond: Yeah, I've always found that being crit critical early on saves an awful lot of time later in the process and…

Kevin Hammond: a lot of money.

Neil Davies: commercially it hasn't done me very well because basically it stops you wasting money and lots of organizations are actually there not to deliver product but to waste money right and I can name you dozens that I've interacted with but I don't think that taking the community's money and not delivering should be the primary goal of the activity here it should be to try and…

Neil Davies: deliver that's all I'm saying okay thank

Kevin Hammond: I imagine we're all delivery focused here,…

Kevin Hammond: Neil, but it's what we try to do, and I'm sure the product committee wants its aspirations and goals to be delivered. So, we can work together.  What one of the things we do have to as I've said before is to then refine from this 2030 vision towards some achievable 2026 set of goals. So that's something we'll have to filter through. Okay. does anyone want to say any more on that or shall we close that issue down? We can come back to that next week. Great.

Kevin Hammond: any other items up for the agenda that we haven't covered?

Kevin Hammond: Tax mentioned vice chair nominations. So do consider that. anything else we should discuss in this meeting?

Sebastian Nagel: We don't have a date yet for this discussion with the product committee,…

Sebastian Nagel: It's January. It was mentioned, but probably not yet scheduled.

Kevin Hammond: No, it's not yet scheduled.

Kevin Hammond: I asked Bosow to contact them again yesterday. I know that Sam Leathers is away because it's Orthodox Christmas today, I think. So, it's about time to contact him. but he'll hopefully be back and in operation by next week. And I'm doing this I'm pushing this early.

Sebastian Nagel: Get back.

Kevin Hammond: So because the earlier we have the discussion the better but obviously there's no immediate rush to do this but getting the discussion going earlier I think is better than postponing it.

Kevin Hammond: They may not be able to make this time in which case we'll need to schedule some other meeting with them. I think'll be a series of we should be working together.

Sebastian Nagel: Yeah, it just feels like there's maybe not one…

Sebastian Nagel: but two or three discussions needed. Just speaking from this.

### 00:50:00

Kevin Hammond: Sebastian. Exactly.

Sebastian Nagel: Yeah, exactly.

Kevin Hammond: Thank you very much for everyone. as I said at the start, I hope everyone has a happy and prosperous 2026 and look forward to continuing to work with you all going forwards.

leandros bsp: Happy New Year.

Kevin Hammond: You. Bye.

Nicolas Biri: It's there.

### Meeting ended after 00:50:32 👋

This editable transcript was computer generated and might contain errors. People can also change the text after it was created.

  
**