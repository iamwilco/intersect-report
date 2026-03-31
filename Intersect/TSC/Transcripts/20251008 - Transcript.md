**

## Technical Steering Committee - 2025/10/08 08:28 CDT - Transcript

# Attendees

Alexander Moser, Christian Taylor, Duncan Coutts, Jonathan Kelly, Neil Davies, Pi Lanningham, Sebastian Nagel, Terence McCutcheon, Thomas Vellekoop

# Transcript

Sebastian Nagel: Now it's starting with Christian starting the recording.

Duncan Coutts: Yes, recording is started.

Neil Davies: We need a question.

Neil Davies: So, do you want to roll back? So, because we're not Yeah.

Sebastian Nagel: So yeah, let's set the stage briefly. So we used the time because today we don't have any agenda set or no chairs around. We use the time to have a discussion on layers.

Neil Davies: And we're not actually call it. So, that would be Yes. There's only six of us.

Sebastian Nagel: So it's more of a technical conversation on Laos with you having had time to kind of look at the SIP Neil knots too maybe Duncan not too so he also had a time to look at it I think I'm going to be a proxy for the R&D team as I was involved and…

Sebastian Nagel: my co-author there I can comment on things on some things but sometimes we might need to kind of say I need to gather more Thank you.

Neil Davies: …

Neil Davies: post the conversation last week and of other conversations with people started looking at the likely detailed behavior of the proposed less linear layoffs.  And as Johnny has just put in the commentary, I mean I talked to my colleague Peter because I'm Welsh. I do much better sort of in a BIC setting, than actually sitting down writing paper. I'm not very good at doing that.

Neil Davies: We discussed the fact that it is not it the way in which the thing is currently formulated is it's doing lots of work that is going to throw away and this is not a good thing for red large system it's not good systems engineering and this is likely to cause issues right so how do we quantify that some of these issues and one of the issues I believe that's going to happen is that for a large portion of the behavioral it's all that…

Neil Davies: if you were to compare a poss lineoff with the same basic parameters the linear layos will have possibly I mean longer delays and spend a lot more efforts doing that than if you just had preus by itself. Yes. Yeah.

Sebastian Nagel: Okay.

Sebastian Nagel: Let's maybe be a bit more precise on some of the things. So you mentioned wasting work. What kind of work you're saying there? And you're saying longer delays. The delay between what? so that means the B…

Duncan Coutts: So the wasted work is the EVs being thrown away, right? Because they're produced, and…

Neil Davies: And all the voting there boy at four. Yes. Yeah,…

Duncan Coutts: the stuff that goes Yeah.

Sebastian Nagel: which is basically disseminated which is an endorsed sequence of transaction references.

Sebastian Nagel: that cannot be used as It needs to be re reannounced and any voting which happened will need to kind of redone.

Neil Davies: it's more than that, But yes, basically that's what I'm saying.

Sebastian Nagel: No, it's not more than that.

Neil Davies: It's a lot more.

Sebastian Nagel: What would be more All right.

Neil Davies: Yes. it's actually worse than that. That's part of the problem. I'm going to do the initial case first of all before I start talking about how to attack it, Because I can see a whole bunch of attacks as well.  But let's do the initial one first of all, so it goes like at the point at which you have a memple and basically if everything fits inside an RBWorth i.e a poss block then basically the system behaves just like it's like paus it never issues an AB. Tony do you want to jump in here?

Jonathan Kelly: I was going to do the summary myself…

Neil Davies: Right. Right.

Jonathan Kelly: but that you're doing it.

Neil Davies: So now that's a meta argument.

Sebastian Nagel: which is a desirable property,…

Sebastian Nagel: So whatever we have it should just behave the same way as today.  Okay.

Neil Davies: I'm not going to make a value judgment on that decision, Because that what I'm saying this is its behavior, right? let's start with the behaviors, I'm not trying to justify any of the behaviors. I'm just to describe them. this is really important because otherwise you need to get to that end point where you understand the beat. So if the amount in the mele right now is more than that then you basically turn round and you construct an EB.

Neil Davies: Let's consider the first cases that there's an RB's worth plus half an EB's worth half another basic block size just to put some numbers on it right not an arbitrary number…

Neil Davies: but a fixed number which is 50% extra okay 50% of…

Sebastian Nagel: 50% of the…

Sebastian Nagel: what could go into a plus block or…

Duncan Coutts: Okay.

Sebastian Nagel: 50% what could go into an EB block.

Neil Davies: what could go into a pis block right so this …

### 00:05:00

Sebastian Nagel: So, it's barely more than what would basically be processed with browse today we're talking 50% more than the limit today,…

Neil Davies: that's no, that's okay. No, no, barely more is not actually the right way to talk about. I'm just talking.

Sebastian Nagel: right? Mhm. Yeah.

Neil Davies: Yeah, but what I'm trying to say here is I'm going to consider various cases, right? I'm breaking it down. This is one case right now.

Sebastian Nagel: And just to be clear, I want to summarize, The proposed parameterization of the SIP is the capacity which can go into prow and the capacity which can go into such an EB,…

Sebastian Nagel: So we're talking a kind of It's more like 5,000% more. So we're like 50x or so which can go into an EB more than what can go into a browse.

Neil Davies: Sebastian,…

Neil Davies: I got to hold you there because actually were you to do that,…

Neil Davies: I believe the system would collapse, I am point is…

Sebastian Nagel: No, so no you're judging now,…

Sebastian Nagel: So basically you're talking like I'm just saying the capacity which can go into EB is Mhm.

Neil Davies: what I'm trying to do here is slowly build up an argument which every basically makes sense right I'm trying to avoid the sort of grandstanding statements about what he could do what all I'm trying to do here is to say this is the way it would behave from the way you've done the protocol permit next Yep.

Sebastian Nagel: Thanks. Yeah.

Terence McCutcheon: Hey sorry at the risk of becoming PE number one just wanted to suggest to some improvement as far as the overt talking. I know you guys are excited and I don't want to change who you are but let's use the hands and demonstrate the right things for committees especially since these recordings do get published.  So,

Neil Davies: So as you can see I will yield when requested. Here we go. So let's go. We know we now got an RB poss block size and a half. therefore an EB will be generated and that EB will start to be propagated. Right now the system can evolve at that point in two ways. there's two broad categories of system evolution at that point. The first one is in the time permitted for and required for the EB to be sorted disseminated voted upon the votes cast and…

Neil Davies: settled right which according to the SIP is 15 seconds we'll take that right That's the minimum time.

Sebastian Nagel: 14 14 is the parameterization…

Sebastian Nagel: which is the minimum time between two RBs when to be using You will have the certificate way before but basically this is the minimum time you need to be able to use it.

Neil Davies: So 14 it turns out makes no difference.

Neil Davies: 14 or 15 seconds.

Sebastian Nagel: Yeah. Correct.

Neil Davies: Basically at 14 seconds the pass on arrival schedule says you will wait 14 seconds or less than 50% of the time. No, the median is something seconds.

Sebastian Nagel: 40% of the time it basically is only reaching to that

Neil Davies: So basically what I stated was so…

Sebastian Nagel: Yeah. Yeah.

Neil Davies: what I stated is you will take that path less than 50% of the time.

Sebastian Nagel: We will even more likely see blocks before 14 seconds most of the time.

Neil Davies: And actually the numbers the other part it's somewhere between it's somewhere between 50 and…

Neil Davies: 40%. But I'm just saying it's less than 50. Right. but we could pick for 40.

Duncan Coutts: And…

Duncan Coutts: that's just a property of the pass on distribution.

Neil Davies: That is a much positive distribution.

Sebastian Nagel: And it's a direct function of the time we used to kind of need to see a minimum between these two blocks. Right? This is directly the protocol parameters. Right? If it's 14, it's only 40% of time we can reach that. It's just always the same distribution.

Neil Davies: It is I think I come back to what Duncan said the statement. it is basically a first to finish synchronization between a fixed time and a passon distribution which is a passon parameter right and the parameter as chosen it means that more than 50% of the time another block will reappear right so point one at least half

Duncan Coutts: So half the time an RB will appear before the EB has a chance to be incorporated. that's the summary.

Neil Davies: Yes. Okay.

Duncan Coutts: For endorsement block.

Neil Davies: So, right now point is when that occurs the EB is waste. Yeah. Play text.

Terence McCutcheon: I apologize. This is actually a clarifying. Are we saying ED like echo delta endorsement block?

### 00:10:00

Jonathan Kelly: And take a small ring.

Duncan Coutts: The Leos terminology here is RB for ranking block,…

Terence McCutcheon: Okay.

Duncan Coutts: EB for endorsement block and linear EOS does not use input blocks anymore which are IBS.

Terence McCutcheon: Yeah. Don't want to go overly crazy, but some things used to be described, so no worries.

Neil Davies: Yes, no problem. so we accept that basically 50% of the time the work being done for all the diffusion will actually be wasted work right…

Sebastian Nagel: Yes.

Neil Davies: because any other RB generated during that time invalidates the previous EB yes okay right so now we'll get started on opportunity cost in a little while.

Duncan Coutts: and there's that opportunity cost as well. But yeah,

Neil Davies: Right? So the next step goes like this of the thinking. I'm going to keep my head clear here. the imagine okay so already we're in that position. imagine in this situation that you do get to the point where work has all this EB work has been done. Right?

Neil Davies: In the situation where the contents of the EB are this at this size, when you get to that point, what the protocol says is you do not generate an RB at that point. you generate a certificate for the EB that is generated,…

Neil Davies: And then gently any other stuff that you've got, right, you then put into an eBay.

Sebastian Nagel: You announce another one.

Sebastian Nagel: Yes. Yeah.

Duncan Coutts: Yeah. …

Duncan Coutts: so the new RB contains not transactions but certificate for the previous EB.

Neil Davies: It doesn't contain any and what's important is it doesn't contain any transactions.

Sebastian Nagel: So I want to add something at this particular thing. So there's been some uncleararity in the current write up of the SIP. it's not very explicit that there is no other transactions allowed in the EV when there is a certificate.

Sebastian Nagel: And it is a bit of a discussion still ongoing right where this is really mutually exclusive.

Sebastian Nagel: but I would tend so my current understanding is that it is mutually exclusive because that is more beneficial to reach protocol security because just we will have more room for the timing constraints to fall into place. if we would allow transactions next to the certificate, the timing constraints are much more stricter because we must have a ledger state ready with all the endorsement transactions already applied in order to validate the remainder of the block.

Duncan Coutts: Yeah, I understood there was some design decision about whether it should be or

Neil Davies: I'm slightly surprised that's the reasoning because my reasoning for this is if you did allow transactions in that RB you have just presented the ultimate front running opportunity for DAPs right that and…

Neil Davies: that but what I'm trying to say is there's basically a whole risk in there by just doing that and I'm sorry I really don't want to discuss design decisions here right I want to discuss the behavior of the system as documented and you agree that at present right there are no transactions being put in that in this situation there's a certificate and an IB right I'm discussing the right so we get there right now so…

Sebastian Nagel: Yeah. Yeah,…

Sebastian Nagel: I could comment on the front running opportunity there though if you want, but we can also just skip it for now.

Neil Davies: 

Neil Davies: because the point is I'm trying to avoid doing that…

Sebastian Nagel: Okay. Yeah.

Neil Davies: I'm trying to get through what I'm trying to because the whole point is going off sideways and appealing to emotionality is not the way I want to do this. I want to do right.  So let me ask you if that was imagine we've already agreed that more than 50% of the time this is now behaving just it's like poss. It's doing more work but it's behaving just like poss. right. Yes. So in the running just pay us in the situation where it was a block and a unit and a half 50% of the time right it would have followed that route and those transactions that would have actually ended up in an RB All right. Okay.

Neil Davies: Let's take the situation where both you compare I'm just setting up the comp so the point is the RB and…

Duncan Coutts: Sorry, Neil,…

Duncan Coutts: I haven't quite followed that. What's the comparison? this RB and a half versus versus what?

### 00:15:00

Neil Davies: the half both the leas and the poss behave the same.

Duncan Coutts: But are you imagining POS with a bigger block size or what? I've slightly lost track of…

Neil Davies: No, no, no. I'm just saying right.

Duncan Coutts: what your comparison is.

Neil Davies: I tell you what, I think you've become clear. Let me just do the next bit.

Duncan Coutts: All right.

Neil Davies: That half in imagine you've got the same timing behavior in both the preos and the linear layos approach. Okay.

Neil Davies: At the point where you come to do the voting and you voted on the EB, if that had been a PROOS implementation, all of those transactions that were in that EB would have actually been in what I forgot what they called in Preyos,…

Duncan Coutts: H.  So you mean this next half would be in the next block.

Neil Davies: but basically the block produced by Preyos. I mean that mean does that make sense? first of all does it make sense to you basically that stuff that was in EB over there right will basically pop up here right and all of that would have been in this block being produced by here right i.e.

Neil Davies: It is absolutely just the same timing as in that circumstance.

Neil Davies: And this is why I picked this half block whether you're doing chaos or linear layoffs. Yes. …

Sebastian Nagel: And in this scenario,…

Sebastian Nagel: you're assuming the man poolool didn't grow in the meantime.

Neil Davies: I'm about to deal with that point,…

Sebastian Nagel: …

Neil Davies: right? because I'm no paint the hole right first of all I'm making sure…

Sebastian Nagel: if it wouldn't grow, right, you would basically have the Yeah.

Neil Davies: because actually I'm using Duncan as my muse here because if Duncan Duncan looks like this then I'm not explaining things if he does that or…

Neil Davies: so what I'm saying is that imagine nothing arrives for a second then basically that second chos block would have contained the stuff that's in the Ebeam so the timing is identical in the sense the service time is identical yeah But right imagine more does arrive.

Duncan Coutts: Yeah, for that.

Duncan Coutts: For those two steps. Yeah.

Neil Davies: Okay, imagine now it starts to arrive such that it basically starts to have that more has been done in the mele in the pos the residual of the mempole or the residual of the block size would have been actually minted at that moment in time. Right?

Neil Davies: Whereas in the linear layos case, they can't be minted at the same time. Therefore, they are put into the EB. So that other section of that mele now is experiencing lower delay,…

Neil Davies: a longer delay, a higher latency.

Duncan Coutts: a higher latency.

Duncan Coutts: Yeah. Yeah.

Neil Davies: Okay, that's my next point. Right, Sebastian?

Sebastian Nagel: Yeah. Yeah.

Sebastian Nagel: So this is still this

Sebastian Nagel: at the initial announcement of the first block, let's call it RB1, we announce the on top 50% as an AB and…

Sebastian Nagel: we had it full with the transactions. I'm not sure in which scenario you're in. maybe we can't certify or we can certify, but I think it's rather cannot certify,…

Neil Davies: I'm assuming we can certify.

Sebastian Nagel: so if we can certify, we had all So then we had basically the 150% browse at the same timing as you said before certified in on the second block in this chain.

Neil Davies: No, no, no, no, no, no, no, no, no, no. It's only half of powers certified at RB2.

Sebastian Nagel: Yeah. Yeah. Yeah. Yeah. I agree.

Sebastian Nagel: So then in RB2 we would have basically the original 150 things.

Neil Davies: No, no, you keep saying it's 50%, because the original 100% was already certified in a sense it was okay.

Sebastian Nagel: Okay. Yeah.

Neil Davies: So, it's only 50% at this point, That's…

Sebastian Nagel: Okay. Yeah. Mhm. Yeah.

Neil Davies: 

Neil Davies: what I'm saying. It is 50%. And what I'm actually saying is all of the other transactions that arrived during that time are now some of them could have been included under poss.

Sebastian Nagel: Mhm. Okay.

Neil Davies: They could have been included at that point in time. They can't be included. They have to be put into an EB. So there at least an no no no it's…

Duncan Coutts: Yeah. And…

Duncan Coutts: then anything that goes in and anything that goes into the EB experiences basically an extra block of delay because at least if it gets incorporated in the next ranking block.

Neil Davies: what yes but actually more importantly right what will happen is that you're moving half I'm using half just as a number right you're moving half a poss blocks worth you're not servicing it and you're delaying it service. Now, it could be 50% of the time that the block would go you go another direction and therefore it would be incorporated But 40 or 40 the other it's going to be so am I saying that in this circumstance sorry Johnny let me just finish this and I will then yield to Right.

### 00:20:00

Neil Davies: In this circumstance, the people who arrived between those two blocks those transactions will experience a longer delay than…

Neil Davies: if they were in fa. Okay, Johnny.

Duncan Coutts: or…

Duncan Coutts: even simpler, anything that makes it into an EV will experience at least one more block worth of delay than anything that would normally make it into a ranking pot.

Neil Davies: The point is this is now I mean yeah because it turns out that there's a turning point right in this process.

Duncan Coutts: As it gets more overlaid, then that gets higher and…

Neil Davies: Yeah that so I'm trying to describe below that turning point Johnny. Yeah.

Duncan Coutts: higher. we should let Johnny go.

Jonathan Kelly: It sounds to me like what you're describing is this potential cascading knock-on effect of the ranking block being used only for certificates, limiting how much can go into your ranking block because it might be 50% of what it could have been under the old system…

Jonathan Kelly: because there's only 50% of a ranking block into the one that was certified and then they have to roll over into another EB. So, that could continue to happen and you could end up not having the ranking blocks actually be at capacity.

Neil Davies: saying I'm not willing to make that statement.

Neil Davies: I'm not saying that right…

Jonathan Kelly: Okay. …

Jonathan Kelly: I'm willing to make that interpretation of what you have said so

Neil Davies: because there is a point at which there should be a turning point here right at which linear layers may may deliver more throughput and then if you were to compare chaos with linear layos it would perform better right there should be one and…

Neil Davies: I'm trying to get to the point of when this will happen Sebastian Yeah.

Jonathan Kelly: It's a costbenefit analysis I think…

Jonathan Kelly: sometimes it works if there's because you're giving the very limited example of just half of an existing ranking block but there are as Sebastian said potential examples where it's way more than that and then the benefits are higher in those cases but most of the time it probably won't be like that. So because of that problem, there's an issue

Neil Davies: No, actually I'm actually trying to be more incisive than that, You need to realize I'm slowly letting the string out here to tie around and hook, right?  If this is not me I'm slowly making what I'm trying to say here is as we go through this analysis I will show right that what I think is going to happen is that only under extreme circumstances will actually linear layoffs give any benefit right so right that I'm trying to build this up constructively as opposed to right Sebastian

Jonathan Kelly: Yeah, I feel like that's what I said.

Neil Davies: No more notes.

Sebastian Nagel: Yeah, I think you mentioning that turning point is actually what I want to say, So I really appreciate this kind of analysis at this exact boundary of where load is at the limit of prayers, the servicing would be like that there would be no latency increase where with leos we would experience one additional kind of indirection and exactly in that kind of now maximum load browse you will have a kind of longer inclusion latency on layers but then as we kind of have more load further than this which is kind of not just 100% prowess right but a bit more because what we've been describing so far has been 100% browse load because we just happen to have it already a bit over and then we just add the same thing as…

Sebastian Nagel: what already was there, So we cannot just

Neil Davies: back Sebastian this is…

Neil Davies: why I'm doing it by cases right right you're trying to extrapolate from this point so now I'm going to start making the next point right so to the first point I want to make is that you accept that basically in this oper in if the mempool is at this position and it's a position between one and a half between one and two times the come block right if the mempool is at this situation knight Then basically chaos would have outperformed in this temple respect delay layoffs linear layoffs. that's what that's…

Neil Davies: what I'm saying. I can show that. That's what I'm saying.

Sebastian Nagel: I accept that and…

Sebastian Nagel: it actually is exactly the case for all kinds of layers we have analyzed, right? But…

### 00:25:00

Neil Davies: What? No,…

Sebastian Nagel: but as you're stressing linear layers,…

Neil Davies: I'm No,…

Sebastian Nagel: it kind of is

Neil Davies: I am stressing linear layoffs because again I am trying to do a egoless approach to analyzing this problem. I'm not trying to talk about alternatives. I'm taking the two things presented to me and saying this is the comparison of them, right?  because'm trying to can I ask this is to get some understanding of how people understand this if the system was at 10% load right would we ever generate an 10% pio

Sebastian Nagel: 10% layoffs or 10% browse load. So can we make this …

Sebastian Nagel: then in terms instead of percentages let's just call it one transaction kilobyte per second data throughput which is about 20% preos load Okay.

Neil Davies: No, no,…

Neil Davies: no. I want to percentages. What I want, let me explain this, What I'm saying is imagine we have a fundamental per we say 100% is a payoff always being is basically a load.  Okay, I am saying it's a 10% of that POS load, which is basically where the system is at the moment.  Thanks. I

Terence McCutcheon: So, I just wanted to clarify here and I'm putting things together when we're talking about Laos and Preos if I remember correctly and I was just double checking. Looks like Laos is the only thing on the chart for delivery and I thought Preyos was put to a back burner. So, am I missing something where they're going to be experiencing co-release?

Jonathan Kelly: I think you're mixing up POS and…

Jonathan Kelly: and Paras at this point. There's different names. Yeah, Paras is a

Terence McCutcheon: That might be it.

Duncan Coutts: Preyos is…

Duncan Coutts: what we run right now. Preos is the protocol that Kadano uses right now.

Terence McCutcheon: Okay, Roger.

Sebastian Nagel: And the current parameterization of the Kadano mainet given a average 202 block production schedule, right?  which is another long range average of course and the 90 kilobyte transaction or 90 kilobyte block bodies will give you an over long averaged arithmetic maximum of 4.5 transaction kilobytes like data throughput for example

Duncan Coutts: So go on, I'll ask you a question again because this sounds like one of these queuing pon questions and I think the answer will be that very rarely you will get a full buffer. Not sometimes but not often.

Neil Davies: This is one of those wait turn right.

Neil Davies: So the point is at 10% load right the line will the EBS ever be generated and Duncan because he's a SWAT basically he's doing it right it will occur right so what I'm saying and it will occur and it will occur because the pass on schedule means that in the way this system works and the amount of memory the amount of transactions in the me

Neil Davies: are basically the dominant factor of the exact number at the exact time is not the throughput.

Neil Davies: It's actually the delay since the previous one occurred.

Duncan Coutts: Right. Yes.

Duncan Coutts: Because it's this bulk service model where you've got on bus on arrival of transactions…

Neil Davies: Bulk Yeah.

Duncan Coutts: which is relatively fine grained but then from time to time a whole block goes out but the difference the variation in those big blocks is quite substantial.  So if you have a long period of time between two platon blocks being produced then you'll get a full mele from time to

Neil Davies: So what will happen is even at 10% load, right? I'm picking 10% because it's ridiculously To Right.

Neil Davies: even at 10% load you'll be doing this with the EBS and you would be paying these costs and then the question is going to be how often is there even a possibility of linear layoffs breaking even right in terms of timing is the next point I'm going to try and make Sebastian

Sebastian Nagel: That's a very good point. I think I would say that's true, I can see that myself too. maybe the magnitude of…

Sebastian Nagel: what kind of is this work about announcing an AB voting on it, And then not certifying it because it's not actually needed because you have space in browse, right?

Neil Davies: I think again Sebastian right the opportunity cost metric we will come to look at that…

Neil Davies: because we're going to analyze that what we want to do is make sure that the understanding is correct and the model's correct right right so the point is the choice right key  question is how full will mempools be at various loads given that they're being serviced in various ways. Right now it turns out that in the work that we did for Apex Fusion, we built these bulk surface model mathematics in order to analyze this problem. Okay.

### 00:30:00

Neil Davies: And therefore we can actually quantify how often based on that number at v we can put a finger in the air right and get some numbers together as to how often at various loading factors would linear layoffs no would linear no because I'm actually doing the negative here linear layoffs is just a cost right and an additional delay I'm looking  Because remember I'm looking cuz what I'm saying is I'm saying when will it actually has the capability of giving any benefit cuz what we have just described here is the set of circumstances under which work is done for no end benefit at the moment. Okay.

Sebastian Nagel: Is there another way to look at this for source schedule because it's not only does even with 10% load right you sometimes have this kind of bulkiness but it also means right that while 60% of the time we are not even certifying in through lays right there is also these times when there is no block produced for minutes right or one minute or so just

Sebastian Nagel: and in those times even the trickle of transactions at 10% load can already fill up a menful higher than…

Neil Davies: Hold on.

Duncan Coutts: that's the key intuition.

Sebastian Nagel: what could serve. Right. Exactly.

Duncan Coutts: Yeah, that's the intuition as to why you get full memples even at 10% load because the poss block doesn't arrive for ages.

Sebastian Nagel: But In this situations, the endorsement and…

Sebastian Nagel: the certification through it, right, would actually

Neil Davies: Do I It's

Sebastian Nagel: help kind of use the time better,…

Sebastian Nagel: Which you have sometimes.

Duncan Coutts: But it doesn't arrive at the right time…

Duncan Coutts: because if you've got a minute in which nothing happens. It's at that point at the end of that minute you've got a very full mele but that tells you nothing about what's going to happen afterwards. If you had another minute afterwards then everything would be great but it's independent and random. So you've built up a backlog that you could put into a big EB,…

Sebastian Nagel: I see that that is independent. But It's not only bad. That's what I want to say, right?

Duncan Coutts: but your chance of being able to get a big EB through are still the same as before. And in fact, the lower the chance you get it through because it increases the time to diffuse, which changes it from,…

Duncan Coutts: 15 seconds to 16 seconds and that's why Yeah. I don't want to take up more time.

Neil Davies: Yeah. Yes.

Neil Davies: Thank you, Duncan. So the point here is it's actually the fact that there was a large gap before you generated this has abs doesn't have any influence on how long the next gap will be. Okay, that's the point. And actually linear layers only gains in order for linear layers to gain benefit right that gap has to be more than 14 seconds right which will only happen less than 50% of the time so what we're saying is so what are you going to start now how often will that occur how big will that be this is exactly why I'm referring to this appendix of the linear layer of the apex fusion stuff because that's where we quantified

Neil Davies: that. What was really interesting in that is that even at 100 at offering high loads huge numbers of transactions the first were either in the lower or the upper half of the mempool right and this lower and upper half of the mempool is equivalent to what I've been saying of one to two blocks of crouse. So obviously I'm making a large amount of noise and needing something because my little elf has produced me some lemon tea. Excellent. Thank you,…

Duncan Coutts: Yes. Go on.

Neil Davies: Sally. So…

Sebastian Nagel: Johnny, maybe can we get the hands cleared while you drink?

Neil Davies: what sort saying

Jonathan Kelly: Just my quick check on something just a sense check. you're talking about the diffusion of the EB. my understanding is the way the diffusion works is to reduce the amount of load to fetch things. it's hashing of the transaction in the EB to then people look at their own mem pool and only take the gaps. Is that correct?

### 00:35:00

Sebastian Nagel: That's correct. It's an optimistic protocol, right? It's an overlay protocol.

Sebastian Nagel: So that's why we only would fetch what is still remaining of what was endorsed which is

Jonathan Kelly: So the difficulty in distributing an EB is in…

Jonathan Kelly: how many gaps might exist between different state pools and having to fetch the gaps rather than the entire EB. Is that right?

Sebastian Nagel: Yeah, that's correct. and there is always obviously an optimistic viewpoint on this,…

Jonathan Kelly: Okay. Yeah.

Jonathan Kelly: No, the mantles aren't always the same across.

Sebastian Nagel: Where most of the time the Yeah.

Jonathan Kelly: Yeah. Yeah.

Sebastian Nagel: But they are quite consistent obviously in happy case,…

Duncan Coutts: and then the higher the load,…

Duncan Coutts: the less they are like each other.

Sebastian Nagel: right? Yeah.

Jonathan Kelly: The last contestant will be I just wanted to make sure that diffusion thing …

Sebastian Nagel: And the more distributed system also the less they are and of course if it is under attack, it's unknown.

Neil Davies: I can give you boundary numbers, right?

Sebastian Nagel: Nobody knows how much of a meool kind of partitioning can actually be exerted by a network-based attacker. And maybe Neil if I would like to see that data. Okay.

Duncan Coutts: And you have to validate them all as well.

Jonathan Kelly: what didn't necessarily mean that every transaction had to be fetched across the whole network at all times just the gaps but the gaps are significant enough at the high enough load but then text has it hand up yes…

Sebastian Nagel: depends. The voters need to

Jonathan Kelly: but the specific concern that was raised earlier was the diffusion so I just focused on the diffusion but yes you're right you have to validate

Neil Davies: Can I just answer John Johnny? So I think the key technical point I actually begin the technical point here is that the cost of having a missed transaction in your mele when you come to validate an EP will have a particular cost. Right. Right.

Jonathan Kelly: Yes, and not a delay.

Neil Davies: Right. A roundtrip time network delay to suitable people. and that's eating into your town budget of doing validation. All right.

Jonathan Kelly: Get

Neil Davies: This is actually quantifiable in the sense I can't say it's 42 but you can probably put some bounds on it with some work and it's not really a guess my experience would tell me is that those numbers of roundtrip times compared to reach each one of those is an extremely expensive operation in terms of the linear progress right so s equivalent to the cash hit it's equivalent concept is a cash miss in a processor pipeline

Neil Davies: Those factors are factors of 300 400 in caches. we could sit down there. my starting point would be they're at least that order of gratitude in this process too, I'm just saying those costs are going to be high, right? They have to be worked out. Text I'm actually currently working along whether that…

Terence McCutcheon: Yeah, I'm sorry. Just clarifying today's conversation is just a discussion to better understand what we're looking at or is there a future state where there's an idea to suggest redevelopment prior to a release.

Neil Davies: what we're doing is a viable solution. Okay.

Terence McCutcheon: I'm going off of what I'm hearing and what I'm hearing if I dumb it down is that this would create an unnecessary slowdown in the network…

Terence McCutcheon: which would be deemed unconstitutional So I just want to make sure we're not discussing a moot point.

Neil Davies: No,…

Neil Davies: no, this is No, no. Yeah, you need these points. I mean, please constitutionality. I mean, you and me need to have a discussion about who triumphs science the universe over people.

Terence McCutcheon: Stop it.

Neil Davies: Universe tends to win. We're discussing how the universe is going to constrain this, right?

Neil Davies: Whether it's constitutional not but text I hadn't even thought of that as an argument against this right my point is I actually think that not there are a whole bunch of reasons you have to understand all of the ways it's good to interact…

Jonathan Kelly: I do like the angle that you're slowing down people's experience in there where that's quite a fancy angle but it's not the technical

Neil Davies: 

Neil Davies: but in order to have that conversation in a solid way. you actually have to have an agreed model of what's going to behave and what's in scope and out of scope of thinking about and what I'm trying to do here is define in this region of operation this is likely what to happen and so far right no one said no you're entirely wrong Neil okay right okay okay that's what I'm trying to say and we can then push it further…

### 00:40:00

Duncan Coutts: plays. Yeah.

Neil Davies: because the next question comes at how frequently will poss give benefit not preos linearly as for some sort of benefit. Now this then plays into the system has modal modes in its operation. Yes.

Neil Davies: And for it to be choosing different in order for it to be better, it has to be in it. All the preconditions have to be true and the c and the things have to be true and all the stars have to align in a particular way for there to be benefit, right? And the other point so my intention is to try and…

Terence McCutcheon: Thank you.  Okay.

Neil Davies: work this up into someical stuff, At some point. let me finish. So that's and I'm talking to Vashy about that already because I think that you've already got resources. the second key point I want to make from a systems engineering perspective is that the fact that you were choosing from a probability distribution and the fact that sometimes it would behave just as neatly as preos and sometimes it'll drop off into this behavioral pattern and actually it's now being randomly decided upon. Right?

Neil Davies: means that the predictability of interaction with this is going to get worse, It's not going to be as predictable as we currently have,…

Terence McCutcheon: Thank you.

Neil Davies: and yeah, there but sorry it got distracted. This is important, right? Because currently chaos for all its randomness is still very predictable. You can bound it and think about it. And basically how this will show up is in wider distributions of times.

Neil Davies: And it would also show up we can actually go to the existing history of the last couple of years and say how often in the past couple of years would linear layoffs completed in a particular way have have made a potential had had the potential to make improvement.  and that we can then work out, will to turn were it to be turned on and run for the would it make any difference and I'm trying to do so one of the things I'm trying to assess here is giving it I'm not saying I mean I'm given that because of the nature of the thing we know that there's a percentage over here when it has a chance to be better how often would we have ever achieved that okay

Neil Davies: and at this point that's where I want to stop. I don't want to talk about the attack factors because basically you have to actually believe and understand this first part before you begin to see how the front running and the attack vectors and I could and how basically there will be behaviors which will be acceptable inside the protocol but basically There was one of the rules we had is that the attacker should have to do at least as much work as you to attack the system. Right? I actually think that linear layoffs creates an approach where an attacker can do a very large amount of cause everybody else to do a large amount of work. Right. Yeah.

Neil Davies: And therefore disruption.  So I actually think that that's going to be an argument as to whether people accept that risk. I'm just saying that

Sebastian Nagel: Sh…

Sebastian Nagel: because you're opening up a new topic here right with this kind of asmmetric resource attacks and so on is a completely other topic we can also talk about. I wanted to actually comment on really when does some layoffs pay off. Right? We now analyze this kind of I think boundary load case which is very interesting to look at. Right?

Sebastian Nagel: So you said when the mele is one to two blocks full of what we could serve better with prow load right so 100 to 200% prowess load we might have a better it sounds likely and I think everyone agrees here now we've been discussing about this that the service level will be better with just browse because we don't do anything additionally and we don't even try to kind of get things certified  But when does it pay off?  Isn't it all the time when it's more than this load in a mele when you have 200 300 20,000 times more or 2,000% more even right it's just really complete saturation of the network just very high demand then it is always better than just not having this very small capacity

### 00:45:00

Neil Davies: That's also not true…

Sebastian Nagel: Let's go.

Neil Davies: because actually the point is this is the corollery of at 10% load right the system will produce blocks a small percentage that meu will fill up that much at high loads the bottom half of the meu will all get served anyway Right. So this is…

Sebastian Nagel: No, no,…

Neil Davies: what there is still a fraction.

Sebastian Nagel: What is High load means 20 times more than what the capacity is what is maybe today.

Neil Davies: Its not you haven't flipped completely into the other mode.

Neil Davies: You are changing probabilities. Right? That's the point.

Sebastian Nagel: Yeah, it's a continuous service I think turning point as you called it originally Yeah,…

Neil Davies: I wish it was continuous. It's actually nondeterministic. in the sense that when I put my transaction in I will not be able to know a priori whether I'm going to be putting what situ whether I'm going to be arbed ei or whatever at the point of false.

Sebastian Nagel: but even if a day before you put the transaction in, you don't know what the demand is going to be tomorrow, Of course it is. But at the closer we are at the moment you put it in a vampool and kind of you having a kind of a good view of the network, then what the demand is and then what you can expect.

Neil Davies: That is a false statement. Let me explain  Basically, if this was a situation that we had at the moment, we have had the Cardano Foundation has very kindly through the opaces of Carl been running canaries, a canary system for the last year, two years, right? and actually those canaries get delivered 99 plus% time in one to two blocks. Okay.

Neil Davies: There is about an four hours in the last two years all right of time in which basically the system has been that heavily loaded. Yeah. again look I'm trying to describe this as a set of facts and…

Sebastian Nagel: Yeah, you're saying there is no demand.

Sebastian Nagel: I'm not kind of Yeah,…

Neil Davies: information but the Sebastian the point…

Sebastian Nagel: but looking at the past demand is not a good prediction for the future too, right?

Neil Davies: what I'm trying to say here is I'm trying to construct a model of effectiveness right and you keep on saying but the past isn't the predictor of the future the past is a validator of the model that's the point the past is a way of taking the common blood the models we're talking about and validating them and making sure that they are sound right okay that's number one secondly what was I going to say The comparison here is right.

Neil Davies: 

Sebastian Nagel: I mean's maybe do you agree with the Kadana problem statement…

Sebastian Nagel: which we're trying to solve here? If not then we should talk about that. thing is what is the concrete suggestion you want to put forth on the SIP 164 maybe.

Neil Davies: You have got a system at the moment that chaos that system could be scaled by just changing parameters.

Sebastian Nagel: Not much but a bit. Yeah probably.

Neil Davies: Okay.

Sebastian Nagel: Yeah. Yeah.

Neil Davies: 

Neil Davies: Factor two, factor five.

Sebastian Nagel: We looked at this.

Sebastian Nagel: Yeah. Something like that probably.

Neil Davies: Okay. Right.

Neil Davies: I am saying if at a factor of five let's pick a number will deliver the sort of service that you could get out of poss.

Sebastian Nagel: So you're saying…

Neil Davies: That's Yep.

Sebastian Nagel: if you would scale the current system by a factor of five, that was still kind of doable given the current network topology and all the system behavior would there still be a benefit in having something like proposed protocol?

Neil Davies: That would be a nice highlevel question to have an answer to,…

Sebastian Nagel: Yeah. And the answer is at very high demands…

Neil Davies: right? Again,…

Sebastian Nagel: which is something the community wants to be able to deal with.

Neil Davies: you've turned this from I am not trying to have that discussion. And I'm trying to have a good model here because you see the next thing that's going to happen here, right, is you keep on talking about demand and throughput and it is again my experience of 40 bloody years that's not actually what the paying customer who has the real money actually needs or What they want is a given quality in a certain quantity. And in this system quality is the time knowing bounds of the timeliness of the transactions to settle. You make that unpredictable. You drive away those customers. That is my underly if you're talking about if you want to move this into an economics and usage concern that's where my I come.

### 00:50:00

Neil Davies: But I'm trying to get there by showing that I'm trying to stop. And that worseness is going to drive people away.

Sebastian Nagel: But the predictability will not be different,…

Neil Davies: right.

Sebastian Nagel: It will just be I mean you acknowledge that prowess is randomness…

Neil Davies: You just agreed it would be different. You just No,…

Sebastian Nagel: but it can be reasoned about right.

Neil Davies: what you've just agreed is what you just agreed to.

Neil Davies: This is the point This is why I'm taking it step by step. What you just agreed to is in a whole region of operation POS would deliver things at better delays.

Sebastian Nagel: Yeah, but it has no room to grow.

Sebastian Nagel: So, it is not as predictable, if your predictability So, no, Neil, let me finish for once.

Sebastian Nagel: So if you're a customer right and…

Sebastian Nagel: you say I can get this level of service but only if it's not overloaded and it can get overloaded quite easily because we saw it here here and here in the past.

Neil Davies: and…

Neil Davies: the past evidence for that over the last four years is zero.

Sebastian Nagel: Yeah, because there's also people not wanting to overload the system, And there has been demands…

Neil Davies: What I right you are the point is you turning I'm trying to keep this as I said at the very beginning right I'm trying to turn this into a model of basically trying to…

Sebastian Nagel: which would have been served quicker with layos. It's true. And maybe knows he is an app builder. Mhm.

Neil Davies: how it's going to work what's the delay going to be what's it going to compare with etc etc because the big people with big money I would say are rational actors and they will be looking to these numbers. If you give them a system which is more unpredictable than another system, they are not and when we start looking at the means of what that unpredictably means for them, they are going to basically think twice. So I act what so one of my next meta level concern right is linear layoffs because it will not have a p predictable region of operation and…

Sebastian Nagel: Cool.

Neil Davies: will bounce around between various modes of operation will actually be on from the point of view of predictability a lot worse for customers to work with Duncan I don't want to take this any further after

Duncan Coutts: So I mean is it a fair summary here that kind of reflects what both of you are saying that I mean from the simulations in the CIP it looks like there would be a region beyond the demand that even Pros with bigger blocks could sustain that linear would be able to cover. and let's assume for the moment that's the case although it can't be too high because as we see also in the simulations in the CIP things collapse latency goes to pop very quickly once you get above a certain threshold. So I think in the CI it's like once you go over about 0.15 transaction megawatts per second things go bad pretty quickly.

Neil Davies: Okay.

Duncan Coutts: But let's…

Sebastian Nagel: What? 50 50 is the kind of order of magnitude we're talking about here.

Duncan Coutts: but let's assume so there's a region in which it has a higher capacity than even big blocks but you can't go too high right and maybe that's 10 times bigger but anyway it doesn't matter you can't go to the size of you can't go to these 12 megaby blocks I mean I don't want to get sidetracked but the data the graphs in the CIP show you can't go that big When it shows the latency collapses,…

Sebastian Nagel: Yeah. Yeah.

Duncan Coutts: it goes really bad.

Sebastian Nagel: Yeah, but that latency is I mean if you would run it with browse, you would have hours to wait before you kind of get into the mele, So it's kind of the back pressure is the same.

Sebastian Nagel: It proves that it is kind of back pressure just the same way as prow would be in that load. But I agree you don't want to get that sidetracked. Sorry.

Neil Davies: I get a framework to have this conversation…

Neil Davies: because I mean I agree with Duncan clearly I clear that and…

Neil Davies: I also think that you are being way overly optimistic about how that's going to work but I want to get this nicely I want to get the methodology sorted so keep on going down possibly Yep.

Duncan Coutts: …

Duncan Coutts: where I was going with this, I was saying so there's a region in which linear layouts would be able to sustain a higher throughput although it would have a much more varied latency and the distribution latency would be much higher. And then in the region below that which is where historically K the latencies would be strictly worse. That is that a summary of the argument? and then the question is is that a tough cell to people…

### 00:55:00

Duncan Coutts: because it's like your current workload would get worse but we can support the system running at a higher capacity and of course a pre system running under that high capacity will have very high latency because your demand would be higher than in the sense of to ledger time time to Yeah.

Neil Davies: But the point is at the point…

Neil Davies: where demand is less than supply for the system, right? Pros bas I'm saying it is my estimation that POS will outperform linearos and actually yeah so what I'm saying is that there's this mistake that higher throughput will lead to lower latencies right it's not always a given and I think this is one of those examples because it's not a work conserving system where

Neil Davies: that's going to be the case. And I'm also look I mean and the other thing I want to say is this nonpredictability right represents a massive technical risk right because what will happen is as you push this system closer and closer to production and you push it towards load you will not be able to manage this risk manifesting itself.  And so yes, you're going to say it manifested itself and that means that the thing you cannot do in this system right is control off the individual offer at loads which is you're going to and I say the way you've designed the system that's the only way you're going to keep it stable and you can't do it but that's a future discussion once we've sorted out the fact that we believe each other right on how

Neil Davies: it's going to perform.

Neil Davies: Then we can have that next level discussion of how you manage and control this problem. And I'm basically from a systems engineering perspective, you have put yourself between a rock and a hard place. And I think you and…

Sebastian Nagel: So…

Neil Davies: I think you're going to get squashed. That's my problem. Right. What?

Sebastian Nagel: what Duncan said before, it's strictly having worse performance in prowess loads. I'm not sure if I can follow that or I don't agree there because this is only the case when the additional work…

Duncan Coutts: That was just…

Duncan Coutts: what we were saying.

Sebastian Nagel: which you claim to be like monumental actually prevents for browse to be otherwise functioning at that load. No.

Duncan Coutts: So where it's strictly worse I think we agreed earlier was where it could be serviced by poss where it's within the capacity that PROS could serve anything that ends up in an EV experiences one extra block block of delay…

Sebastian Nagel: and we need to go through a certification because of the person on schedule. Okay. Yeah.

Duncan Coutts: but yeah then you can go bigger obviously and then when your EVs are substantially larger than RBs then you have the potential for higher throughput and  In situations where the demand is higher than what Preyos could service, then the time from when you want to submit your transaction to when it gets in could be lower.

Sebastian Nagel: So I mean the summary would then be right. So that there is strictly a lower level of service transaction inclusion delays for example because of this it can happen even on small loads that something needs to go through the EB being certified and…

Sebastian Nagel: then it has a longer latency.

Sebastian Nagel: basically, but this is also going to be a percentage, right? It's not going to be the majority, right? So it's a slightly less good operating in there's an overhead, let's call it an overhead, In this level of operation, which buys us the potential to actually have much better service quality on very higher loads, right? Mhm.

Neil Davies: Where? Let's quantify all of this,…

Neil Davies: Because if we end up in the position, look, let me say now if the overhead pays benefit 50% of the time, there's no argument. If the overhead gives benefit 05% of the time, there is an argument, I was choosing those numbers because then you work it out.  And because of that argument and as soon as you start placing the argument out right then you'll be able to talk about it's going to cost more says the SPOS's when am I going to see a benefit I'm going to see this I right right right right right right right right right right you able to say will I ever see in the time scales of interest and you start having a model where you can start quantifying all of this stuff that people are just I totally agree it could be a million times more load

### 01:00:00

Neil Davies: Actually, I don't totally agree because if you look, you then can start doing comparators if you were able to process all of the faster all of the UK's financial transactions,…

Neil Davies: is that a reasonable scale, which I would say yes for a global system that could produce do something the size of the UK, and those numbers are quantifiable, right? so you talk about scaling a thousand,…

Sebastian Nagel: …

Neil Davies: I'm saying this is not something that I'm going to suggest.

Sebastian Nagel: but we will come around to whatever model we're talking about. we come around to it's probably always a bad idea to prepare for something which is not even needed because you will not have the potential to do more throughput with zero overhead right I mean that the system kind of adapts automatically to it right in a non steered

Neil Davies: No, but in…

Sebastian Nagel: Okay. Hey

Neil Davies: what I said in the V, you're now trying to do there's a word for this type of argument, but what I said in my little video previous in the system engineering, what you're trying to do is that the cost of processing a unit of work is the same at 10% as it is at 90%. Right? And what I'm saying is that's what you're trying to do. and what you've done what you're saying is this system doesn't behave that way and that was the big bloody alarm bell that went off in my head right as soon as you make a system in which it costs the more work you do the unit cost goes up by work you do not have an implicitly scalable system full

Neil Davies: up. He

Duncan Coutts: Yeah, I mean you can have it not be a flat function. I mean the full layoffs has a fixed overhead and…

Duncan Coutts: then that means that it gets more efficient as you increase the load and it's relatively inefficient at low load because the overhead is no because the bigger your EBS the more often you lose them that's…

Sebastian Nagel: But this is exactly the same relation we have here.

Sebastian Nagel: That's not true. It's the timing.

Duncan Coutts: that's what the charts show right I mean that's why the time for transactions to reach the ledger gets ridiculous this as you've got look at figure nine in this DIP.

Sebastian Nagel: I mean But every system has a limit which you can perform, right? And that graph just shows how does it behave with this kind of demand, right? it's having more demand than it can serve.

Duncan Coutts: No, no, no, no. Because this is not showing a system that is operating beyond its demand.

Neil Davies: No.

Sebastian Nagel: There's going to be back pressure there.

Neil Davies: This is all right. This is the funible system.

Duncan Coutts: 

Duncan Coutts: No, That's not what it's showing. that's showing the system performing within its demand but having very very high latency. Right? So if the behavior under Preyos if you had a system that can accept a certain number of transactions per second just a very very simple model not even up to block blockchain and you're producing them higher than that the time that you experience that the time get to get grows unboundedly over time. But in this plot, it is stabilizing. I mean, maybe it's not running for long enough to be able to see…

Sebastian Nagel: Yeah, the fidelity is probably lacking there too,…

Duncan Coutts: where it stabilizes.

Neil Davies: Yeah.

Sebastian Nagel: And that the parameters are not perfectly tuned, Could also be that the size of EV chosen, the maximum closure chosen is a bit too big for the timing constraints,…

Duncan Coutts: It does look too big.

Sebastian Nagel: right? Yeah. Yeah.

Duncan Coutts: 

Duncan Coutts: Yeah, exactly. that's my point. That was why I was saying it looks to me like you can't go above, 0.15 TX megabytes per second because and presumably the reason that it starts to fall apart when you get too big is because you get more and more you get bigger EVs taking longer to get across the network, longer to be validated and therefore the votes longer to make it and…

Neil Davies: I So,…

Duncan Coutts: and then whenever an EV gets missed, you have then more demand which means the next DB is also huge and so you get the same problem again the next time around and that has a knock-on effect and so you get very high then you get very high latencies only occasionally do you get an enormous EB manage to make it in time on those occasions when poss puts a large gap between your blocks.

Neil Davies: so the point is an ideal system has this nice 45°ree line and when you hit its capacity, it stays at that point,…

Duncan Coutts: It's flat. Yeah.

Neil Davies: right? that's the ideal, Okay. what we're saying is this is that,…

Sebastian Nagel: this. Yeah.

Neil Davies: Wonderful. That is doing, right? But you haven't actually restricted the demand now.

Sebastian Nagel: We did.

Neil Davies: It's turning over. That's the point.

### 01:05:00

Sebastian Nagel: This is still running, right? So, we're doing the long simulations now. And there's some noise here but sometimes it is kind of bit bad on us. Sometimes a bit better on us,…

Neil Davies: Yeah. And what's happening right the point is this is…

Sebastian Nagel: But this is just normal, right?

Neil Davies: what we have to turn around.

Sebastian Nagel: Yeah, this is…

Neil Davies: What I come back to the point I said in the beginning right we said earlier…

Sebastian Nagel: what we're doing now. Kind of I mean there's been re good feedback here too, right? Saying yeah, okay, we should really have a look in how the saturation happens because figure 9 is not that good of a model for it to kind of really get there.

Neil Davies: if the delay is not predictable I'm actually going to say that there is a non-trivial number percentage of applications for which this system is not fit for purpose.

Duncan Coutts: Sebastian, in that chart you just showed us, that's an aggregate over a long period. it doesn't show what figure 9 shows, which is the latency that individual transactions experience. So I don't disagree,…

Sebastian Nagel: which is also a histogram of transactions there too in figure 9.

Sebastian Nagel: Yeah, it's overall transactions.

Duncan Coutts: right? But it's…

Neil Davies: But it shows the timing.

Duncan Coutts: but it's showing the timing of individual transactions whereas you are showing us the throughput.

Neil Davies: I'm not showing the through.

Duncan Coutts: So my point was that that was a system that was running within its capacity in that it

Sebastian Nagel: It was the same system, Just what we just saw on the thing. It was exactly the same simulation.

Neil Davies: But our point is that the delays are unpredictable. that's my point at this point right this is the meta is that an UN system that delivers unpredictable delays is not a system that people use any transport think about it right and…

Sebastian Nagel: I do agree on this one. Right. And

Neil Davies: so if you are going to spend money you're going to spend…

Sebastian Nagel: So is maybe a concrete let's try to make the constructive feedback right you would like to see kind of the histogram figure 9…

Neil Davies: if you're going to do this and at the end of it you end up with something that people are going to walk away from then that's not a good use of time and me. I want a logical argument that says I'm wrong.

Sebastian Nagel: but on a high load which kind of doesn't leak No,…

Neil Davies: That's what I'm looking for.

Sebastian Nagel: we're looking for evidence, not for arguing who's wrong or what not.

Neil Davies: No, no,…

Sebastian Nagel: Right. Mhm.

Neil Davies: no, no. A logical argument based on that. no. I don't think you understand the word argument in this context. Right. I am proposing a set of properties that I believe the system will have. So far no one has told me that I am  I am and I am saying that when you extrapolate these for property you end up with basically this randomness in timing or this unpredictability in timing simulations do not disprove if you're going to disprove me I'm saying start I am placing a solid peg in the ground and you're saying we can get around it and I'm saying you can't right that's my point and

Neil Davies: In these battles,…

Neil Davies: I typically will offer crates of beer and crates of whiskey and all the rest of it. And in 40 years, I've not paid up. I'm just saying. And I'm trying to avoid that for the whole I don't understand it well enough yet.

Sebastian Nagel: Can you suggest something?

Sebastian Nagel: I mean, can you help us in making it better then? Yeah. Yeah.

Duncan Coutts: Can I say something before I have to go at top of the hour?

Neil Davies: I think about

Sebastian Nagel: We should wrap it up anyways.

Duncan Coutts: But maybe next time I mean something that I was thinking about which it's not the same issue that Neil's worrying about here, but it's more of a kind of big picture strategy question. and I don't think we'll have time to discuss it, but I thought it might be useful just to raise the thought. so I guess the worry is that we're building in the best case we're building a system that can do a kind of intermediate level of capacity, right? It's bigger than let's say big block POS where Neil and I reckon we could be able to increase five times the block size or something under Preyos.

Duncan Coutts: And so this linear layoffs would give us something bigger than that but not too big is that and that's the compromise it's making right thereby not having full scaling and concurrency and the rest of it and so that buys you an intermediate amount of time in the potential of Kadano to become big and successful and the rest of it. but it's not clear to me that we're getting any closer to the time when we could actually achieve scaling, right? Because as I understand it, the concern that people expressed to the layoffs development team, which I think actually is not very well reflected in the CIP something that had been brought to the TSC but it was just directly between, but put that one to a side.

### 01:10:00

Duncan Coutts: So there was a change of strategy from let's go for something big and scalable because there was a concern that people would not be ready in time and so we do this thing that's sort of intermediate right but doing that thing that's intermediate does not get us closer to those people…

Duncan Coutts: who are deploying apps and wallets and whatever being ready to do something scalable like if you're going to do an intermediate point. it increases the throughput but it I'm still assuming the CPS is…

Sebastian Nagel: Where do we need to go?

Duncan Coutts: what we want that we want to be able to get to a stage where we can have actual a scalable design where we can get to more than 100 TPS in some reliable way.

Sebastian Nagel: Yeah, basically one of the motivations is economic sustainability.

Duncan Coutts: Right right.

Sebastian Nagel: I know there's different ways to go about it, right? But just not changing the structure of the network and…

Duncan Coutts: But it's not at all obvious that this would get us there that this is an intermediate point,…

Sebastian Nagel: the incentives. Yeah.

Duncan Coutts: before getting to something that would be Yeah.

Sebastian Nagel: No, it is actually saying in order to have economic sustainability kind of has been now then looked at okay what does it mean have the same number of SPOS's roughly right with the similar or kind of slightly maybe if there is changed hardware kind of costs need to be covered and the same kind of profitability not coming from the reserves but coming from fees right that is the argument around it and…

Duncan Coutts: Yeah. Yeah.

Sebastian Nagel: that is achieved is it 80 transaction kilobytes per second or so mere data throughput with the current fee structure right excluding Pluto for example right so we're talking about a break even of 50 to 100 yeah

Duncan Coutts: All So you might be able to get to that point, but I think there was an ambition to be able to have something that could genuinely scale. And my concern is that by going to this intermediate point, we don't actually get any closer to that because we say, …

Duncan Coutts: we can't do that now because it'll take SPOS's and D apps and whatever more than two years to adapt. But if you don't start, it's two years down the line. it'll still take them two years to adapt or three years to adapt or more than we have so we're not actually making progress is my concern towards something that's genuinely scalable right I can see the argument for having an intermediate point and…

Sebastian Nagel: Yeah. I mean,…

Duncan Coutts: I can see that the argument that by building linear layoffs that has many of the pieces of full layoffs it gets you closer on the development to but that was not the thing that made us change strategy the thing that made you change strategy was users weren't ready. So where is the strategy to move towards something that could be scalable in the end that encourages users to make the changes that they would need to get us to a scalable end goal.

Sebastian Nagel: okay. Yeah.

Duncan Coutts: That's my worry and…

Duncan Coutts: I don't have time to but maybe that's something you can think you can think about and maybe that's something that we could discuss.

Sebastian Nagel: That's it really.

Duncan Coutts: It's a big picture strategy question.

Sebastian Nagel: So it would be very good to have that one vert reiterated on the rationale of the S…

Sebastian Nagel: because this is really saying why is this a good step to take right…

Duncan Coutts: Yeah. Why is an intermediate?

Duncan Coutts: Why is this a right intermediate point?

Sebastian Nagel: why is this even a good step to take for the Kadano community now right and…

Duncan Coutts: Yeah. …

Sebastian Nagel: this is basically exactly the argument which should be there if you're missing something really having a comment there and a threat and…

Duncan Coutts: I'll try and…

Sebastian Nagel: just really make it big…

Duncan Coutts: put this down as a comment on the poll request.

Sebastian Nagel: which is different to your previous input.

Sebastian Nagel: we also received right exactly so we don't need to discuss it now…

Duncan Coutts: Yeah. I was just sort of lowle stuff. So, I'll try and phrase that and put it on the Yeah.

Sebastian Nagel: but yeah okay let's have it Yeah.

Duncan Coutts: right.

Neil Davies: these no I need to go as well…

Duncan Coutts: I need to go because I got to go for pick up.

Neil Davies: because actually these things need to be said and thought about and then come back we can't resolve them now right we'd have to All right then great conversation really looking forward to the video recording please I'll advertise it as well cheers guys absolutely…

Duncan Coutts: Yeah. Thank you, Sebastian.

Sebastian Nagel: But maybe we can also do it written in the future at some point.

Neil Davies: but in the future right…

Sebastian Nagel: Yeah. All right.

Neil Davies: because'm here as usual I'm up to here right that's the

Sebastian Nagel: Yeah. See you.

### Meeting ended after 01:26:37 👋

This editable transcript was computer generated and might contain errors. People can also change the text after it was created.

  
**