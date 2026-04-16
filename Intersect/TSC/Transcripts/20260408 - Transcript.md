**

## Technical Steering Committee - 2026/04/08 - Transcript

# Attendees

Abid, Alexander Moser, Bosko Majdanac, Duncan Coutts, Ken-Erik Ølmheim, Kevin Hammond, leandros bsp, Neil Davies, Nicolas Biri, Sebastian Nagel, Terence McCutcheon

# Transcript

### 00:05:00

Kevin Hammond: Hi Neil.

Neil Davies: Yep. yeah, I just get myself a coffee and then I'll be coming

Bosko Majdanac: Hello guys. Hello

leandros bsp: Hello.

Bosko Majdanac: Hello.

Kevin Hammond: Good answer everyone.

Nicolas Biri: Hello.

Kevin Hammond: We'll just wait a couple of minutes for anyone to join us. So, welcome to Caneric and Abid as guests.

Kevin Hammond: as usual. Do you have anything that you would like to raise with us Canary or rabbit? we will be keric.

### 00:10:00

Ken-Erik Ølmheim: H no I'm about to send Bosco a DM. He needs some help with some metadata and I've been busy last week and I forgot about it to be honest. But yeah, just hang in here.

Bosko Majdanac: Look.

Ken-Erik Ølmheim: What's going on? Are we getting a hard fork or what? Great.

Kevin Hammond: I can guarantee that.

Ken-Erik Ølmheim: Great. Love it.

Kevin Hammond: That was no information I think we need some information from you.

Kevin Hammond: Yes, you need to provide information from family for the metadata.

Ken-Erik Ølmheim: Yeah, that's…

Ken-Erik Ølmheim: what I'm and I'm going to meet them on Sunday actually because Yeah.

Kevin Hammond: That's great to hear. And as usual, does anyone else have any items that are not on the agenda they would like to include?

Kevin Hammond: I'm taking the deafening silence as a no, but you can always use the chat. Hopefully everybody had a great Easter break. If you celebrate Easter,…

Alexander Moser: I was setting up smart contracts. Don't know.

Kevin Hammond: I've been playing around with game theory, Alex.

Alexander Moser: Very good topic. Who have you tried to trick?

Kevin Hammond: Mercy myself so far.

Neil Davies: Games shouldn't be about tricking.

Kevin Hammond: Abs. Absolutely.

Alexander Moser: Yeah. Let's construct a game that's win for everybody and…

Alexander Moser: surely not tricking.

Kevin Hammond: Win is definitely better than lose. Alex, great. So, let's get meeting started.

Kevin Hammond: So welcome to the technical steering committee meeting of the 8th of April 2026. just do a quick check on the attendees if I can find the attendees. So we have one two three four five six voting members of the steering committee present. So I deem that we are corate in case we need to take any decisions. So I've pasted in the agenda into the chat. as usual if you'd like to start with the actions from the last meeting. Poster.

Bosko Majdanac: Let me share the screen. Essentially the same thing that you're using every time so we can all follow actions from the last meeting. Just pasted it So a bit of formatting needed but anyway it's the same thing. So Kevin, it was for you and you died to think and to clarify the final division of the security budget between TSC and OC. So did that happen as two chairs or…

Bosko Majdanac: not? Mhm.

Kevin Hammond: No, no,…

Kevin Hammond: no. But my understanding was that the OC had transferred the to ect generally boss. So long as we're aligned with the intersect budget, we don't need to form coordination between the ISC and…

Kevin Hammond: the TSC.

Bosko Majdanac: For two of us…

Bosko Majdanac: which I sadly didn't do anything about is coordinate a doodle poll because it's not at the moment in my focus. However, if you can spin it up I mean let's think up async in a way otherwise it's not going to happen.

Kevin Hammond: It will take only a few minutes to do it.

Kevin Hammond: Bosco, I was going to do it before this call, but I got called into something else.

Bosko Majdanac: Okay I will get in touch with you on that. for Ryan I suppose. Yeah, this is for Ryan's wy but he's not here right or is he to prepare maximalist of forkable sips in coordination with tri will for the upcoming commun…

Bosko Majdanac: but I suppose nothing has happened there nor is the time maybe.

Kevin Hammond: No, no.

Kevin Hammond: So Ryan sends his apologies for not being here today.

### 00:15:00

Bosko Majdanac: Agreed.

Kevin Hammond: Let's just follow up with him on that.

Kevin Hammond: I think it's becoming important to progress this to provide input to the DR represent community as we go in to the budget front and of course it's for us as we're coordinating the hard forks as well.

Bosko Majdanac: So this will stay on the list of the action items. So this list of for sips then for leandros update the 2030 KPI document with the range window implementation data shared in select. Mhm.

Kevin Hammond: So Leandros and I were just on a call with the product committee where we were discussing that document Bos. So the been up I think it's been updated.

Bosko Majdanac: Okay.

Kevin Hammond: Leandros can confirm that.

leandros bsp: I'veed it with the requests by the product committee. I haven't included the genesis window calculations but I have here a note that is an option of calculating chain density based on epox or…

Kevin Hammond: So I think we can take that action as complete right. Great.

leandros bsp: a genesis windows whichever is selected we will apply. Yes. Yes.

Bosko Majdanac: This didn't happen. TSC account saw promoting of the April election applications via X specifically targeting prospective technical candidates. And I saw that Nicholas Bir wanted to discuss this suspect on the call, but you're the chair, so I'm just stating.

Kevin Hammond: I'll add that to the agenda. Nicholas, unless you want to cover it now.

Nicolas Biri: That's okay.

Nicolas Biri: It can wait the agenda item. No problem.

Bosko Majdanac: Okay.

Kevin Hammond: So, we've got an agenda item where we're discussing the elections. says, "Let's

Bosko Majdanac: Yes. Yes. and the last one on me, investigate the feasibility of an RSS feed for technical parameter updates to improve developer communication. so currently I'm more looking to the opening of the respective discord channels for anybody to be able to read. So that could be a way even though you wouldn't need to be an intersect member to have an access to the specific designated channels.

Bosko Majdanac: However, I just need a confirmation. So, I intend to do the same thing with hard fork working group channel and also if there is a channel for the parameter updates is there or not on discord.

Neil Davies: I don't think there is.

Bosko Majdanac: Is there any? Mhm. There is.

Neil Davies: I don't think there is.

Bosko Majdanac: Okay.

Neil Davies: So I mean I think if given that the TSC is the authority that accepts them,…

Bosko Majdanac: Mhm.

Neil Davies: that channel should be sufficient. Don't create too many channels for them to follow. Right. that's it. Yeah. you managed to skip the item that mentioned me…

Bosko Majdanac: I agree. I just want to make sure we understand each other.

Neil Davies: which I was very pleased about by the way in the thing.

Neil Davies: Could you Bosco I haven't done that. could you send me the URL for the professional technical view document?

Neil Davies: I'm down to do something.

Bosko Majdanac: You are off.

Kevin Hammond: Yeah, I was reading that action,…

Kevin Hammond: Neil, and thinking it was possibly a little garbled. so I think it was actually two actions and one was to as you had a propo you were proposing to look at how to do professional technical review Neil and…

Neil Davies: Yes. Yeah,…

Bosko Majdanac: 

Bosko Majdanac: I Ah,

Neil Davies: that's it.

Kevin Hammond: separately we were looking at the budget proposal and I was going to determine whether to $150 per review was a sensible rate or not.

Kevin Hammond: And we'll come back to it later, what I did was to increase the amount asked for $250 per review,…

Kevin Hammond: which I is a hopefully reasonable rate.

Neil Davies: So given that that's split,…

Neil Davies: if boss go out of band, you could send me the URL for that document cuz I've lost I can't find it. I will engage in that short fourth wiz as they say.

Neil Davies: Okay. No,…

Bosko Majdanac: so TSC budget document that's the Okay,…

Neil Davies: it's the professional technical review proposal.

Kevin Hammond: Yeah, I don't think there is a document,…

Kevin Hammond: I think the idea. Okay.

Neil Davies: So I can't finalize something, it has to be created. if the action is on me is to create an outline, then I'm willing to take that on. But let's put that in the minutes for this meeting. I think the note the AI needs to apologize for garbling things in the first place.

### 00:20:00

Kevin Hammond: And that's a sensible action, Neil. Correct.

Bosko Majdanac: I apologize for skipping your I agree.

Kevin Hammond: Yeah. …

Bosko Majdanac: I agree. But some level of manual check is always the So yeah.

Kevin Hammond: so it might be that we should coordinate on some sort of outline of the review process. The officer are happy to provide input to that as Great. Should we move on? first item on the agenda. let's go back to the agenda.

Kevin Hammond: TSC budget proposal. so not a lot has changed from last week. As I said, all I've done is to go through and make a change to the review rate and I've increased to increase the review rate from $150 per review to $250. that seems to me to be a reasonable reward for conducting a review. And this is not a review of an ongoing project. This would be for a proposal review as part of the review process. independently understand that intersect is looking at its own internal project review process based on the light of experience with the 2025 budget and the work that's being carried out. But we will discover more about that in due course.

Kevin Hammond: Boston and…

Kevin Hammond: the deadline of April 13th is still fixed. Is that correct?

Bosko Majdanac: As far as I know,…

Bosko Majdanac: But what is it? So, it's used. No, it's Monday next week, right?

Kevin Hammond: So if anyone has any changes that they would like to make to the budget proposal, now is the time to raise them verbally and today or tomorrow is the time to raise them in the form of comments on the proposal and I will take an action to finalize the proposal by Monday and assume that if there are no comments that people are comfortable with the current state of

Kevin Hammond: The proposal again taking silence as appribation. Speak now or forever. Hold your peace.

Bosko Majdanac: I love the tone of that language.

Kevin Hammond: It is a commitment. Good.

Bosko Majdanac: I know.

Bosko Majdanac: But I love the tone.

Neil Davies: …

Neil Davies: where It comes from the standard marriage ceremony in the United Kingdom.

Bosko Majdanac: It sounded so noble in a way. So that's why good. Okay, Kevin, your time.

Kevin Hammond: If you don't say anything, we will be wedded to the proposal. Moving on.

Kevin Hammond: Vamrom hard fork. so the no node version 10.7.0 there's been some progress on that. the team believes it may have found the cause of the performance issue that we discussed last week. Unfortunately, AWS fell over during the evaluation of the fix. So, we don't have any definitive information yet. We're expecting that imminently. but what it does mean is there will need to be a node version 10.7.1 that includes that fix and…

Kevin Hammond: any other changes. Neil, it was a whole Wi-Fi.

Neil Davies: When you say it fell over,…

Neil Davies: did this mean that the instances had to be changed or was this just a …

Kevin Hammond: Yeah. No.

Neil Davies: So that means that they got to go through a recalibration cycle…

Neil Davies: which will take another few days a week.

Kevin Hammond: I would think so.

Kevin Hammond: I Good.

Neil Davies: Some sort of hard that means basically you got to start from scratch and do an old one to make sure you're still getting the same numbers which you won't. Right. This is the problem with the What I'm saying is don't expect it soon.

### 00:25:00

Kevin Hammond: We will monitor the situation. we could I was going to say one good thing is we can get some preliminary information on we can't get the final benchmarking until the Amazon instance is recovered but we can get preliminary information on the timings there.

Kevin Hammond: Bos these were gross measures the performance it was something like I think we're being reported a 50% increase in CPU usage when synchronizing mainet so these were very observable even without running the benchmarking faster Okay.

Neil Davies: Okay.

Bosko Majdanac: Just a question I'm interested to understand. You probably know Kevin from before. So I will be quick. so how was decision being made about the node readiness when it was all IO before voltera? So who was deciding on when the node is ready? How was that working? because I'm not judging I'm just saying so are you part of IO or…

Kevin Hammond: Thank you.

Bosko Majdanac: not part of IO who is deciding basically on that thing? Yes.

Kevin Hammond: you're asking several different questions conflated into one bos.

Kevin Hammond: So the process that was being followed was the engineering team was taking a collective decision on readiness. and the performance and tracing team will have had a power of veto on readiness. if the benchmarking information was unacceptable as this seems to be unacceptable then that would be a veto on mainet readiness.

Kevin Hammond: Likewise the test team had a veto if regression tests failed then the node was not ready was not mainet ready. So those were those two gating points. then assuming the engineering team as a whole was comfortable the decision was taken by the head of product and the head of engineering for IO.

Kevin Hammond: IOE case that was how it was done. I do not believe for its current process.

Bosko Majdanac: Okay.

Bosko Majdanac: So it's basically IO that is deciding on the readiness of the particular node version for the mainet and everything else. so I was just thinking whether TSC has any role in it just out of ignorance or not because TSC is just a recommendation or…

Bosko Majdanac: what is the role of TSC in the Hour itself. What's it?

Kevin Hammond: So it's formally signing off on the node versions.

Kevin Hammond: So, there's formal signoff process which I have been coordinating my role as chair. so about a year ago the process shifted from only ternal sign off to also needing external sign off. So the product committee and the technical steering committee are both signing off on the node readiness and…

Kevin Hammond: that's done at the point when the release notes are prepared.

Bosko Majdanac: Perfect. That's actually the understanding that I wanted from this.

Bosko Majdanac: So, we don't need to spend any more time on it. But thank you. That was it.

Kevin Hammond: …

Kevin Hammond: so 10.7.0 performance issues may well have been identified, but we won't know immediately. There is also one of the issues which has cropped up. is that there's apparently a space leak that is causing a growth in memory usage up to six gigabytes over a period of 1 to two weeks. So it's a relatively slow growth. the information seemed to be that it was hitting a limit at that point.

Kevin Hammond: the benchmarking team believes this is a blocker to a mainet release an increase of that magnitude is not acceptable. no known cause at this point in time but the team is trying various approaches to try to identify it and again you don't need the full benchmarking cluster to track that down. a single node a small cluster is sufficient to determine the memory leakage. So that may delay a 10.7.1 again information and when we have it.

### 00:30:00

Kevin Hammond: However, the over overall timeline for firm rosom is although we have to take into account that there could be some slippage as a result of the investigation the overall timeline should not be impacted because at this stage we've provided a pre-release version of the node that DAP developers and others can use to start their own testing. So we're in a period when people should be testing against 10.7.0 Z is adequate for that even if it's not yet mainnet ready. So progressing the risk register has been updated based on the information we had but changes from last week to this week. We're still essentially at the same level of risk that we were at before.

Bosko Majdanac: I didn't get if you said it.

Bosko Majdanac: Pointing out what Sam said yesterday. So integration is already happening with TRET. It's already underway right against 10.7.0.

Kevin Hammond: Yes. Yes.

Bosko Majdanac: So, timeline still sense might be even more squeezed. Currently, it sits at the end of June.

Kevin Hammond: But the integration is starting to happen then. there should be no real blockers to the integration efforts starting.

Bosko Majdanac: Yeah. Yes. Yes. Yes. Correct.

Kevin Hammond: So we will probably expect 10.7.1 based on where we are probably expect that to progress into a node version 11. But we will see how that develops. Great.

Kevin Hammond: Any other questions on the hard fork? So, 2030 KPI document, you gave us an update earlier. Was there anything you wanted to add to that?

leandros bsp: Not particularly. mittee or anyone on the committee has an opinion about using what we already have that is per epoch measurement or if it's best to go for a genesis window measurement the genesis window measurement will give us a better indicator of long range attack while the perop measurement makes measuring much more straightforward because we have clear start times and end times. so Neil has something to say I think about this.

Neil Davies: Sorry, I was trying to find the right button. I would suggest you need both, right? because the whole density and you probably need to have historical density maps to show when the density was low. because if during operation there was a low piece of density there was last November, that represents a point in time where the attacker could have a bit more of an advantage. But if they do not exploit that advantage within a certain period of time that long range attacks becomes harder and harder.

Neil Davies: So, I think you're probably going to go for long-term range and basically per a moving average on epochs, the last 10 epochs or…

Neil Davies: something like that would be the sort of graphing I would do.

leandros bsp: Okay. Yes,…

Neil Davies: Makes sense. Yeah. I mean I mean it is my understanding that basically a lot of these theoretical attacks require people to not participate in order to be able to and therefore if there is high participation then basically these attacks aren't possible but I will get corrected

Neil Davies: if I'm wrong.

leandros bsp: that is my understanding too.

Neil Davies: So the point is while why there's lots of November was a problem because there's low density but because I have no idea how quickly that opportunity degrades but I think it's probably disappeared by now because of the nature of how it all stacks up. Excuse I seem to be attacked by a neighborhood cat. Decided to come in and say hello. Right. Okay.

### 00:35:00

Kevin Hammond: So the consensus team they have concerns as you say Neil if chain density drops below some level might be good to get their input on that may maybe put you in touch with the relevant team members but something around the 85 90% level I don't think is going to be a problem this is what we were proposing so we had a discussion we presented the

Kevin Hammond: findings to the product committee earlier. There was a good discussion about that just before this meeting. this particular measure is something it probably can't be used as direct marketing metric. What we're doing here is to monitor the security of the system and the health of the SPO ecosystem because that also contributes to chain density. But this is about maintaining current standards rather than about any kind of improvement. So it's a baseline measurement. We need this to have sufficient security and to have a sufficiently healthy state poor community. other metrics that we looked at these are things which they drive particular lines of research.

Kevin Hammond: So one of the metrics one of the KPIs was the level of income leandras from fees or other sources and what that suggests to the product committee is they should be looking at ways to either increase not the fees level. the work that we're doing should be aimed at increasing the fees revenue we should be investigating alternative revenue sources. So some research might be needed to determine that and that could be via partner chain such as midlight etc or it could be from other sources.

leandros bsp: Yes. I'm not sure if research is needed per se,…

leandros bsp: but several avenues will probably need to be investigated and attacked in order to achieve the target results. Yep.

Kevin Hammond: Yeah, as research in a general term,…

Kevin Hammond: it's not quite market research, but it's some kind of investigation into what alternatives might possible and what would be the impact of each of the alternatives.

Kevin Hammond: what we were the point we were making to the primary committee is it's not just a case of setting the targets but you might also need to be active in directing u work that was carried out to progress the goals that were being set and also that will be necessary to provide dashboards and…

Kevin Hammond: other ways to monitor each of the KPIs so we can determine where the progress is being made and that might in some cases have marketable value which is what they were mostly interested in. Anything else to add Leandra on that? Great.

leandros bsp: Yes. No,…

leandros bsp: I don't have something else to add or comment.

Kevin Hammond: So, moving on to the next item. Sebastian, I put a couple of items on the agenda for you. I'm conscious we haven't had an update from you recently.

Kevin Hammond: I know you were at the layoffs monthly meeting last week which conflicted this meeting. Would be interesting to get an update on how things are progressing.

Sebastian Nagel: Yes, of course.

Sebastian Nagel: I can give a short summary. Neil, you want to go first? You have your hand still raised? Suppose Yeah. So that was just a reminder. All right. yeah, we had the last monthly review meeting was last week or April 1st. The full recording can be found as always on our list. Put this in the chat. so it was the updates for March. We moved it by one week because of the builder fest.

Sebastian Nagel: A few people from the team of contributors to layers have been in the builder fest. So that's why we moved it. And I will let me just give a five minute rundown maybe of what the progress was by just using the slides which we also showed and just briefly skim over them. very prepared here. yeah, latest progress we showed was of the prototype. So of a very small setup which is a three node setup instrumented through graphana and other systems a new generation a transaction generating binary is used.

### 00:40:00

Sebastian Nagel: So to load the network in a given shape we would want to see the mele be clear and quicker. we demonstrated that especially in the builder fest we kind of saw exactly that behavior. We could already produce this on a prototype. So that means not only about producing EBS, storing, offering and relaying them, but now also adopting blocks which contain a still mocked crypto certificate of it and there's no voting yet but by including that bigger or certificate about the mele gets cleared out and bigger spikes.

Sebastian Nagel: So here this is a very high demand on a mele and we see on browse elections when an EB was certified the mele be depleted more than what the smaller spikes the prayers u would be. we showed that. So a bit more info on this new generation tool like the transaction generating tool by the performance and tracing team. we also demonstrated or no we pointed at anti-thesis being used in the layers repository.

Sebastian Nagel: So it's run by the GitHub CI in fact that a similar setup as we just saw is tested in this simulation based old injection test using some standard properties there. we're working with blink labs on this one and they will be smoothing out some edges so that these reports can be used by any of the contributors to the repo. this is an example of such a report where basically these properties u are checked throughout multiple runs and multiple hour runs compressed in a smaller wall clock time of course because of everything simulated. we had a report on delta Q. so Eve concluded his work.

Sebastian Nagel: this was an R&D work stream about modeling the diffusion and the processes of getting EBS applied and included and to kind of support the security argument of the layers design which depends on the diffusion of the EBS being in a given form shape but then parameters. so it's basically an extension of the brass diffusion model which already existed and taking this into kind of multiple dimensions combining multiple smaller subm models into a form be somewhat representing this diffusion of an EB.

Sebastian Nagel: I have personally not really reviewed this much yet but it seems it was reviewed by a few others. So seems convincing so far and…

Sebastian Nagel: will be useful it's an analytical model. We can use a parameter setting.

Kevin Hammond: So sorry.

Kevin Hammond: So going back to what you were just showing with the model. So what you're saying is in the case where you're fetching an endorser block, there is a five out of six probability that the transaction is in the mele and a one in six in the TX cache. Is that correct?

Sebastian Nagel: This is I think the current model…

Kevin Hammond: Is that so the numbers?

Sebastian Nagel: which is visualized here. Yeah. but I'm not entirely sure how these values are found.

Kevin Hammond: So what I was wondering is are the numbers coming from simulation or are they just assumed? Sebastian, do you know

Sebastian Nagel: I don't know. I can't answer it right now. There is this technical report…

### 00:45:00

Kevin Hammond: Okay.

Sebastian Nagel: which I just let me just give you the link to the chat which has more info. I think that's one I still have it on my to-do list to read that one to myself. just wanted to show that there's some progress there. we had a bit feedback or kind of some progress on the actor proof still on a somewhat idealized network. So let's see how that so Andre was presenting this and I don't want to go into the details here but this is of course the most formal mechanized way to kind of reason about the protocol.

Sebastian Nagel: But it's always to see how much of the real world is abstracted into things here especially the network safety.

Kevin Hammond: What's the safety property mean? Sebastian just Okay.

Sebastian Nagel: I mean this one is the browse safety property which is the common prefix.

Kevin Hammond: So this is just spray. It's not specifically looking

Sebastian Nagel: This is PR safety in the top and layer safety is I can't really read this one that much. the layer safety basically means that if prowess is safe and is it still safe with layers enabled right and under which conditions this is the case. And if I recall correctly …

Kevin Hammond: Mhm.

Sebastian Nagel: if the Andre is kind of almost proving and realizing that any extension of a safe protocol which doesn't change which still is uniquely determining. so the sequence of blocks that then the extended is also safe. but this is only true for safety I believe and not for livveness. we need to go back to the details about this one.

Sebastian Nagel: So I see you're intrigued and…

Kevin Hammond: Yeah. Yes.

Sebastian Nagel: there's maybe a bit more detail to be found on the actual recording and further and past work in this area. yes.

Kevin Hammond: If you don't the previous slide, the one you were showing the one that was the one summarizing the proof. Yeah. …

Sebastian Nagel: Yeah. Yeah.

Kevin Hammond: so one interesting result is that you're generalizing to other layoffs variants. You haven't proved this specifically for linear layoffs. you've

Sebastian Nagel: This is I guess again right this is if you just look at the alternate sequence of blocks right then that's all cool but of course if it abstracts away how you can get to that one and do you get to it in time right which is the intricate details about I think these things being safe or…

Sebastian Nagel: it's not as easy as it appears I believe. but this is my opinion about this work.

Kevin Hammond: But that…

Kevin Hammond: but the fact that you have improved it just for a specific protocol is a nice result Sebastian that's great. the final point possibly worries me because it looks like you're proving something like an eventual consistency property. yes.

Sebastian Nagel: That's exactly what I mean. Right. So with assuming the network has That very much true.

Kevin Hammond: and possibly infinite time.

Sebastian Nagel: That the take everything here with a grain of salt. these formal models are often conveniently abstract and if it's so abstract that it doesn't really relate to the real world…

Sebastian Nagel: then they're not so useful. yeah yeah yeah yeah yeah I hope you can tell by my assessment that I'm quite conservative in that area let's see …

Kevin Hammond: Yeah. …

Kevin Hammond: so obviously that's a limitation on what's being done. we need to be cautious about that.

Sebastian Nagel: then we had a few more also I think closeout remarks from other R&D work streams about modeling the me pool especially in terms of ME and front running capabilities and how these men was basically they were simulated also by another group. so it was William and Ryan who worked on some general statements coming from that work but these are I think more of conclusion in the end but not real findings or not real news I would say.

### 00:50:00

Sebastian Nagel: And again also this constraint analysis also provides a bit of a baseline of the ideal yeah things happening that things should be fine given the parameters and basically confirming a bit the simulations that what we did that it's possible to kind of get this kind of sequencing what we're aiming at so that the amount of CPU to kind of do the ver verification of all of these blocks. all of course assuming or kind of taking some lower level measures of how long things typically take to validate but on an optimal schedule this all works out within the limits.

Sebastian Nagel: But of course this constraint based analysis is kind of looking back at an optimal schedule of verifying everything. and the protocol implementation will not have the benefit of backside in that sense. but there is I think the one month before was that more information about this resource modeling. We showed some updates on the Rust simulations, another network stack simulation. I'm speeding up here because I don't want to give the whole presentation and just a teaser, right? we've been looking at committee selection specifically about this weighted fat comply with local solution its strengths and its weaknesses.

Sebastian Nagel: specifically what we are now mostly concerned with is the certification time in layers. that is quite big given the split between persistent and non-persistent voters and the ser size itself is also big but not a big deal but annoying and we realized of course that it's only due to the non-persistent part which is the very strong minority of the stake involves here this weighted fader complete partitions the whole state distribution into persistent voters which is most of

Sebastian Nagel: the ST and also the big ST owning pools and non-persistent parts which are selected on a local sition which are about the remainder of the stake but most of the cost in terms of size and time is attributed to this non-persistent cheap layers here and simpler schemes basically eliminate these completely at the cost of

Sebastian Nagel: being more predictable of course need to be bounded separately or differently and even then another scheme which is this public lottery might be a sweet spot which we're currently looking at. so yeah checking back with the committee selection is what we're doing here and just putting that together with benchmarks on the crypto but also benchmarks on the networking or at the very least using the simulations to see their impact on the networking.

Sebastian Nagel: this is also to derisk some of the delivery and then we had another lecture by Nick about at least 22 details on more product tasing I think the layers fetch decision logic to make it in a resourcebound way going through some benchmarks on concrete latencies of some disk storage u we had implemented so far.

Sebastian Nagel: and how these specific storage solutions one or the other would behave in not the average but the worst case and what to be cautious of and then taking this not only further in terms of what to keep in memory where and what's the quantities involved but also how much of resource needs to be allocated for checking how many of these things can emerge at which time in the worst case.

### 00:55:00

Sebastian Nagel: using these models of how many potential EVs can arise and then we identified and closed out with kind of a new threat which is basically not really an attack vector but rather a threat of course everything which is based on a VF election can result in this very unfortunate we call them what we call storms because they can't be engineered or used as a burst where an adversary can reveal certain big data at the one point but rather it can be a very unfortunate timing and how the protocol can react to these things.

Sebastian Nagel: because if you would always need to take account all possible this is this analysis all possible elections at all times then we might be so conservative that it becomes quite annoying to implement or unfeasible to run for SPOS's and…

Neil Davies: Could I just ask before we go on?

Sebastian Nagel: avoiding some things by design that's what we're after there. yeah,…

Neil Davies: If you go back to the slide…

Sebastian Nagel: this is Yeah,…

Neil Davies: which had the numbers on it.

Sebastian Nagel: which number?

Neil Davies: The one that's 600 go back 625 megabytes.

Sebastian Nagel: This one?

Neil Davies: Yeah. …

Sebastian Nagel: Yep. No,…

Neil Davies: what time limit have you got? That's an infeasible thing to build in a distributed network of the size of Moving that amount of data In a voting cycle,

Sebastian Nagel: I don't think this is so whatever I say here doesn't basically pay tribute to basically the more clear presentation as Nick gave it. so this particular

Neil Davies: saying that's a lot if you're wanting small stake pools to support that amount of data exchange right then you are basically rapid you are dramatically you're making a non-trivial change to the economics is…

Neil Davies: what I'm saying okay that's…

Sebastian Nagel: So I'm not sure ex this the number you're looking at right now is 625 megabytes here.

Neil Davies: what I mean I'm just saying basically it's not going to be feasible to implement this for small staple operators because they can't afford those costs, right? Yeah. Yeah.

Sebastian Nagel: So this is 50 and this is all the current parameterizations from the simulations right the one which is in the SIP which is this I think currently 12 and a half megabyte of EB closure and…

Sebastian Nagel: then of course in adversarial setting but this is not purely controlled by an adversary this scenario here they would be all distinct right so we're talking about 625 unique data Yeah.

Neil Davies: Yeah. …

Neil Davies: yeah. my But what I'm trying to say is those numbers would worry me from a point of view of actually practically deploying layoffs. as always I mean I have this con I'm just saying economic feasibility is of the actual solution that's a wing number

Sebastian Nagel: Yeah. Did so. Yeah. Yeah. Yeah. the number here is also in particular we came to it also more from what kind of storage or kind of and in this case also we kind of keep these very urgently maybe to diffuse data in memory or…

Sebastian Nagel: on disk right that's how we came to this whole analysis and…

Neil Davies: Yeah. Yeah.

Sebastian Nagel: basically our conclusion here is that's not The biggest problem really right that having things in memory or on this that is feasible like this is a way that's okay but not okay for the network right so that doesn't say it here right basically we can't really demand that to be diffused correctly yeah yeah it

Neil Davies: You're talking the point is 12 and a half. I mean, the time taken to achieve that, right, is going to probably push you outside your time budgets. and not as well as the inherent cost of all of the participants having to have that amount of capacity to pay for,…

Neil Davies: right? And now the words reserve bandwidth panic me because actually you can't reserve bandwidth in the internet, right?

Sebastian Nagel: Yeah. Yeah.

Sebastian Nagel: And that's exactly why there should be a cross there or something that more severe, Because That's exactly the understanding I believe which we also have, and Yeah. maybe in summary that's correct of course right and the details here really lie in like that EBS can be like even if they are only allowed on whenever a prow election is running right this is basically this super stupid simple and everybody complain

### 01:00:00

Sebastian Nagel: two simple linear layers proposal which kind of makes things very very direct in that sense right already in that situation we can see the probabilities of things happening in the worst case right very rarely but still kind of within a non-neglectable likelihood that EVs can emerge still on these schedules And we must be ready to deal with them. We don't need to be ready to deal with them in a way that this succeeds in certification necessarily, right? This is all still an optimistic protocol.

Sebastian Nagel: And it's perfectly fine if you don't have it operating in situations which can happen in theory or in some probability as long as they cannot be engineered to be happening all the time. So kind of they cannot be exploited by an adversary. that's why it's called storm and the measure can't be controlled. Yeah. this will be part of our threat model too and we'll be tracking these things there as we go forward. That was basically everything of the and this was not 5 minutes so I'm sorry. but if you want more details the monthly is the place to be.

Kevin Hammond: Yeah, thank thanks for the summary, Some interesting details there. if you can share the information in the Slack channel as well, so we can follow up on it, that would be great. G given the time, I propose that we skip over an update on the layer 2 working group. Spend that till next time, Sebastian. Be good to catch up.

Kevin Hammond: But lay two is not interesting. I couldn't possibly comment.

Sebastian Nagel: No, nothing's interesting there anyways right now.

Sebastian Nagel: No, no, no. But I also haven't been much in that one. And I think the next one is scheduled for next week, I believe.

Kevin Hammond: Okay, it's good to hear this progressing. I'm sure interesting things are happening. Alex, I propose that we delay the parameter status update to next week.

Kevin Hammond: We'll have a call shortly anyway and there's a parameter committee meeting on Thursday so we can get an update after that meeting.

Kevin Hammond: Bosa, anything you wanted to say about the election process?

Bosko Majdanac: other than…

Bosko Majdanac: a few things so less than a minute so I've already shared on the TSA elected members channel that all those five of you whose term is expiring at the end of this month can consider reapplying of course because at the moment of writing that I don't have the latest number but there TSSE was the only committee without any applicants so just consider that thing as well there was an X space yesterday there is going to be a virtual town hall tomorrow as we agreed the dates so I will pass the link to that after

Bosko Majdanac: the calls and also Nicholas wanted to add something on whether it would make sense to share from the TSC account so Nicholas…

Bosko Majdanac: if you're still here

Nicolas Biri: Yeah, very absurd.

Nicolas Biri: It's not about sharing the fact that people can apply from the Twitter account of the TSC. I think there was some idea floating around about pinging potential candidate and it's more this that is concern to me. I'd like the TSC to stay neutral in this and pinging people from the TSC account breaks this centrality from my point of view. I would suggest if somebody thinks that somebody would be a good candidate for the TSC, people can personally ping them. But I would not do this from the TSC account.

### 01:05:00

Kevin Hammond: So, I definitely encourage all existing committee members whose terms are coming up for expiry to reapply of course for a second term. and I'd encourage everyone to approach technically aware or suitably qualified candidates to join the TSC and to encourage them to apply before the deadline. I don't think we need to use the TSC X account to do that. Yeah, great.

Bosko Majdanac: Okay, there's nothing else on the agenda and…

Kevin Hammond: Thank you.

Bosko Majdanac: we have minutes early.

Kevin Hammond: Thank you everyone for a great discussion. Thank you Sebastian for your extended update on os. Good to see that progress is being made there and looking forward to hearing more about it and I will try to get a minute or two to set up a doodle poll so we can discuss the risks with that. Great. Thank you very much.

Nicolas Biri: Thank you.

Kevin Hammond: Catch you all again very soon.

Sebastian Nagel: All right.

Kevin Hammond: Thanks. Bye.

### Meeting ended after 01:06:22 👋

This editable transcript was computer generated and might contain errors. People can also change the text after it was created.

  
**