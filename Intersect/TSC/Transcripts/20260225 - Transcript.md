**

## Technical Steering Committee - 2026/02/25 - Transcript

# Attendees

Alexander Moser, Benjamin Hart, Bosko Majdanac, Duncan Coutts, Gauthier Paluku, Ian Njuguna, Ken-Erik Ølmheim, Kevin Hammond, leandros bsp, Mike Hornan, Neil Davies, Nicolas Biri, Pedro Lucas, Ryan (Cerkoryn), Ryan Williams, Sebastian Nagel, Terence McCutcheon, Udai Solanki

# Transcript

Benjamin Hart: I

Bosko Majdanac: Hi

Kevin Hammond: Hi. Hi, Dan. Sorry, I lost the window.

Benjamin Hart: No worries, Happens to the best of us.

Kevin Hammond: Yeah, this is the frustration of having systems in the browser then, right? Yeah.

Benjamin Hart: Yeah, you're preaching to the choir. I'm sure I have more than 40 tabs open at the moment.

Kevin Hammond: So what I actually do is I practice a system of sacrificial browsers. So I have browsers that are used for dedicated purposes and when they fail they don't take down the real stuff.

Benjamin Hart: Yeah, I do something very similar. are you familiar with Rambox?

Kevin Hammond: No. No.

Benjamin Hart: So Rambox is essentially to house everything that you might normally run as a chat service or social media. So, it's like a dedicated browser just for those things that…

Benjamin Hart: 

Kevin Hammond: Right. Yeah.

Benjamin Hart: what I presume you mean are the real things. but yeah, it's handy for a few reasons.

Kevin Hammond: Absolutely. I mean, especially important if you're doing development at the same time as participating in meetings. You don't want the meeting crash to take out your compilation, for example. No, no,…

### 00:05:00

Benjamin Hart: You're doing development in the browser.

Kevin Hammond: I'm not doing development in the browser, but I've had very badly. So, taking out browser is annoying because you can lose, for example, I'm doing a piece of development. I'm looking up things. I've got various documentation I'm reading.

Benjamin Hart: Yeah. Yep. Yeah.

Kevin Hammond: Browser goes down. I lose all my context perhaps. that's frustrating.

Kevin Hammond: But I have actually in the worst case had a browser crash take out a complete machine and that's extremely annoying if you're doing development on that machine. So good hygiene. Hi Handras. Hi Ran.

Ryan (Cerkoryn): How's it going everyone?

Kevin Hammond: Hi. How you doing? Having fun?

Kevin Hammond: I've seen Bosco before this week.

Bosko Majdanac: Yeah,…

Kevin Hammond: I've seen you before this week, Bos. So,…

Bosko Majdanac: of course.

Kevin Hammond: has anyone got anything to add to the agenda today? There quite a few items on the agenda. Hi, Alex. So, before we start properly,…

Udai Solanki: Hi, Kevin. Hi, everyone.

Kevin Hammond: Hi, Udi. Anything you want to add to the agenda, Yudo? Or anything you want?

Udai Solanki: Not today.

Kevin Hammond: No, no. Any again, as always, if someone has something to prioritize, we can do it in that order. So, Sebast, I've just been listening to the layoffs u monthly update. I'm aware that Sebastian is traveling.

Kevin Hammond: So what we're proposing to do is as soon as he joins us, He can give a summary for anyone who's not been able to be in that Anything we need to add from an intersect perspective, boss, thanks.

Bosko Majdanac: I added a suggestion for the agenda on Slack. You added it.

Bosko Majdanac: So that's it.

Kevin Hammond: Yeah. So included that.

Alexander Moser: Given I'm in the car I can't look at the screen. Are we discussing hard fork quickly? Is that on the agenda?

Kevin Hammond: Yes. The halfhawk state is on the agenda.

Alexander Moser: Thank you.  No, I want to listen to it.

Bosko Majdanac: Mhm.

Kevin Hammond: Do you want to speak to that,…

Kevin Hammond: I'm not sure there's going to be any update compared with yesterday. Alex, I think you're on the call yesterday.

Alexander Moser: Yeah, it was true to maybe start with that topic.

Kevin Hammond: Yeah, I'm sorry. I'm just doing a Hi, Nicholas. I'm just doing a quick check for who is present.

Bosko Majdanac: I think seven.

Kevin Hammond: So, welcome, Neil.

Kevin Hammond: So myself, Alex, Neandros, Neil, Nicholas, Ryan, Sebastian has just joined us and you present. So, and…

Bosko Majdanac: eight.  So man.

Kevin Hammond: Duncan has just joined as well. Nine. So, we have a full house. So, welcome to the technical steering committee meeting of the 25th of February, 2026. we have a fairly full agenda. I have pasted the agenda into the chat as usual. and I've asked if anyone needs to prioritize specific items. or if there are any other items to add to the agenda, any that crop up during the meeting, we can add under any other business, of course. so Alex has asked us to prioritize the hard fork.

Kevin Hammond: I'm aware that Sebastian has some time constraints. So, Sebastian,…

Kevin Hammond: why don't we kick off with you?

Sebastian Nagel: Yeah, thank you.

Sebastian Nagel: Yeah, I need to leave in about 15 minutes. linear layers update. Kevin asked me to give a brief update. I think we talked about the SIP when it hit half a year ago or so. I just came from the monthly review meeting. so we just concluded that I don't have the recording yet at this very moment to point you but I need to find The detailed link on our website in this list once I upload it tomorrow. So recording notes, I think transcript or chat whatever everything it was on YouTube so it is actually very public call.

### 00:10:00

Sebastian Nagel: and open to anyone. And today we demonstrated just recent progress on our road map including the layos prototype progressing. So we have EBS relayed on a small network but still it's operadano nodes. They're kind of patched right now.  And the slides will also be in that link exactly In fact, they are already public and I can give you these links earlier because doesn't need to be processed by Google. These were the slides from today.

Sebastian Nagel: they were quite dense because we had the Krispy kind of talk a bit about the technical considerations we've been facing and looking at especially around how many of EBS you need to keep to stay safe right and it's really only about this I would say the tail end of the protocol really right so once an endorsement has been made and it has been kind of disseminated how long do you need to keep it how much of this

Sebastian Nagel: data needs to be stored right how many of such elections can occur some of it is linear layers specific right in this protocol variant because we don't have a separate leader schedule or anything for EVs for layers work it's actually the same as browse and all the potential browse VRFs can leech to EVs so this simplifies things a bit but this already kind of shows like the complexity which there is in making this proper

Sebastian Nagel: So, yeah, what else? We had several additional supporting progress on temporal logic properties which we check on these prototypes. This is emerging. We had past the formal spec derived also trace verifier tools so we can keep check on the correctness of these early prototypes.  They are early I would say but they help in making this first future implementations of other node developers even help support them in making it correct. what else? Yeah.

Sebastian Nagel: Are there any questions about the project? Maybe I can answer.

Kevin Hammond: I suspect people would need to either have been to the call or…

Neil Davies: I would ask,…

Kevin Hammond: read the sign.

Neil Davies: from literally no knowledge, I'd ask what are the best two things or what are the two things that going on or what are the worst two things that you're worried about?

Sebastian Nagel: The best two things and the worst two things. I think that one of the better Yeah.

Sebastian Nagel: 

Neil Davies: What I would say in terms of best is things that are going better than you expected or…

Neil Davies: things ahead of plan or…

Sebastian Nagel: Yeah. …

Neil Davies: whatever. Yeah.

Sebastian Nagel: yeah. it's always tricky, right? Rarely anything is ahead of plan. that to be said. I think the priorization between browse and layos like which is a key thing right we shouldn't impact browse you have been in the conversation with the network team even there I think it's not that dire as we have been seeing it at first prototypes but we're still not out of the beast there I would say right so I think the multiplexing between networks is actually not too bad or… they were suspected to not fair, but I think it is reasonably fair and it's good enough. so I think that is slightly better, but still not kind of fully confirmed good, I would say.

Sebastian Nagel: 

Neil Davies: I yeah,…

Sebastian Nagel: And yeah,…

Neil Davies: I would add that perhaps some of the expectations there were false, but that's okay. I helped the network team bring them down into a sort of they were beyond what reality could deliver to you is what I was trying to say by yeah

Sebastian Nagel: we have been quite exploring in directions which were also a bit uneasy to me. I'd rather not have it was for the benefit of everyone priorization or rate limiting for one or the other protocols,  to kind of not impact browse too much when there is lots of layers things to be transmitted. yeah, rather not need that, Would be better. And I think it's showing that this is good. and another I think we're getting on top of things of what the storage requirements are, the access times are kind of clearing up a bit on the architecture of the processing logic of EVs and transaction closures.

### 00:15:00

Sebastian Nagel: maybe something which I find interesting is all of the things we're tackling would have been the case in all varants ever discussed about layers. So it's really always about the fetching the right amount of data and EBS and getting it into the chain at the right time and so on. The variance were mostly about how is the beginning of the funnel, right?  how is transactions leaving getting into the layers pipeline and process and so on. the variance we discussed last year kind of why or how the proposal is different to what was for example researched and published in research is mostly on how things are funneled to the pipeline.

Sebastian Nagel: But all those considerations about how much things you need to keep track of the EBS themselves the data to be dealt with right the amount of chain growth to be expected and so on all of that is just I think would have needed to be solved anyways so I think there's u good surprises that it's really simpler than what was aimed at but it's by no means simple and

Sebastian Nagel: So I'm happy that we don't kind of have additional complexity for throughput which will probably never be turned on because even the parameters we have been looking at will and this is maybe probably an interesting number for you all can lead to chain growth of gigabytes in a week depending on exact parameters right but we're talking gigabytes of chain growth in a week even with the parameters we suggest or…

Sebastian Nagel: even lower than that. and I highly doubt that SPOS will right away be ready for that and we will not be turning it on and it will be a gradual roll out anyways. And the ceiling we will hit in terms of how much of the chain can grow for SPOS's is Yeah.

Neil Davies: This is hing the thing that we noted eight years ago that eventually the cost of the disc becomes the constraining factor.

Neil Davies: on these systems and their total costs. there has to be enough revenue to support the disc growth.

Sebastian Nagel: Yeah. I mean, there has been other discussions lately about how fast Kadano should be, How much the chain really grow and isn't it not maybe a feature rather than a bug that it's not so fast moving that it is more like something you can keep the history over 10 years of, right? And I think this tension exists independent of…

Sebastian Nagel: how you're going to get throughut addressed and sequenced right I think that is u yeah  Yeah.

Kevin Hammond: So your analysis was suggesting something in a limit Sebastian around 150 gigabytes in six days…

Kevin Hammond: if I remember the numbers correctly. and is that going to have to be SSD or can you use disk

Sebastian Nagel: So what you're referring to Kevin is basically right how much of the worst case closure you need to kind of keep around in order to kind of quickly switch to a pro chain including that and that is basically exactly how much of the volatile history of the chain all the lay traffic potentially endorsed in that time you need to keep quite close right so that will probably mean SSD in terms of latency although the fetching is it's not what we discussed in the presentation. not the serving we discussed more the fetching.

Sebastian Nagel: But yeah that's separation between volatile and immutable history will also exist for layer storage right and…

Kevin Hammond: Yeah, is getting more expensive,…

Kevin Hammond: Sebastian. So no AI is driving the demand.

Sebastian Nagel: everything is…

Neil Davies: It is…

Sebastian Nagel: but compared to five years ago for example.

Neil Davies: but everything but it's bound.

### 00:20:00

Kevin Hammond: So they'reing the market

Sebastian Nagel: Yeah. Yeah.

Neil Davies: But it is bounded and independent of the length of the chain. That's what I think…

Sebastian Nagel: Yes. Exactly.

Neil Davies: what I'm hearing. Yeah. Mhm.

Sebastian Nagel: And this is true. As it was and as it will be. Yeah. Yeah.

Neil Davies: So that's the good things. What are the things you're worried about? We've just one

Sebastian Nagel: 

Sebastian Nagel: Yeah. Yeah. what I'm worried about is for example that originally we've been setting out to what are the things we want to validate early and we didn't really get through and get by that yet in order to so benchmarking the Haskell ledger really whether it can really apply that many transactions or not exactly fully validate not even reapply…

Sebastian Nagel: but rather create the ledger state of a given transaction closure. The more load layers can create.

Neil Davies: You're saying that this was something so it's benchmarking and…

Neil Davies: that basically you're carrying forward risk that this will affect things and you don't know whether that risk will mature yet.

Sebastian Nagel: Yeah, we're trying to mitigate that risk by doing the benchmarking, but it hasn't progressed as much as I was hoping for originally,…

Neil Davies: Okay. Yeah.

Sebastian Nagel: So that's why I think it's a bad thing. I don't think that it's u infeasible in fact.

Neil Davies: But no, I get it.

Sebastian Nagel: Yeah. Yeah.

Neil Davies: It's a hazard you're trying to understand.

Sebastian Nagel: And let me maybe give you a link right so there is this document which we keep writing right which is maybe for your interest and this is particular section what I wrote about I guess also three four five months ago what are the key risks or the key threats which you want to use to motivate the design right and what are the main risks we need to mitigate early and then how to go about that  what kind of experiments and prototypes can help mitigate that.

Sebastian Nagel: I outlined there that one is the network stack really do this freshest first diffusion as the researchers anticipated it right or assumed it's possible and another one is can a real ledger even process that much real kadano transactions right also something which was abstracted in the original paper research because transactions first  just emerged there, right, from the ledger as being and applied there and everything's idealized. and then there's the most tricky thing is the combination of two if don't want to have it's missing some words right now.

Sebastian Nagel: so in the core of the protocol right is basically the security argument like why is layers as an overlay protocol.  It's basically also the argument which was there in the paper but it was said yeah okay it's an overlay and it doesn't change how prowess actually diffuses blocks and whatever and in this idealized model there's no cross talk right and everything is just neatly separated and out of context right and then that's why it is secure or safe in the real world there is shared resources disk network and so on and taking that security argument of

Sebastian Nagel: of course in the real world was a challenge last summer and what we proposed in the SIB and that now really needs to be we could validate it with the simulations. So in again a more detailed model of what a node does and the sequence and also in a concrete topology we could validate that it is feasible to go that path. the adversarial behavior of it was started to be analyzed. I think we could go more and better there on the simulation front to really say okay it's feasible to do. We know it's possible given the real network and…

Sebastian Nagel: and kind of the latencies. but either it works or it doesn't work. I think if

Neil Davies: …

Neil Davies: Yeah. that the point here I mean I am not a great believer in I believe simulations can be beguiling, right? You got to be careful about that. They can lead you into false cry.

Neil Davies: But if you can measure these things and just lay them out as a sequence of dependencies you can typically see whether there's a huge risk or not. if basically you measure all this stuff and say it's going to do this and this and you line them up and if it doesn't work then you got trouble. if it does work how much slack have you got is the question right?

### 00:25:00

Neil Davies: So you're basically saying you still don't know whether there's sufficient process in Slack to hit the rates that you want to hit.

Sebastian Nagel: Yeah. Yeah.

Neil Davies: And that's going to be in how fast fundamental functions can happen like updating the ledger, validating transactions and things like that. is that a sort of summary of what you said?

Sebastian Nagel: I wouldn't say we don't know it at all…

Sebastian Nagel: but it is kind of still a bit unsharp and fuzzy around some areas…

Neil Davies: Right. the composition of them you don't have belief in yet.

Sebastian Nagel: where Yeah. Yeah. Yeah.

Neil Davies: You may know some of the numbers at some of the points but how all those performances will compose.

Sebastian Nagel: Yeah. Yeah.

Neil Davies: Yeah. Yeah. Mhm.

Sebastian Nagel: I have confidence I think in the happy path of it, it can work out, right? And also that I would say on the optimistic path of protocol, I think this is also what we simulated and that's why I think it's well covered, right? I'm also not worried about the threat vectors the attack scenarios which kind of can just disable layers right because you can just given enough stake and so on right it's not a big deal about that because that's just inherent in the design I'm more worried and the thing which is I think most interesting looking ahead and forward is really this adaptive thing in between right

Sebastian Nagel: the adaptive boundary in between it's going to be very hard to say for example let's go a bit deeper …

Sebastian Nagel: how much on a stake is enough that to have a given EBS and transaction closure such that the majority of the remaining on a stake gets it by that in time,…

Neil Davies: Okay. Bye.

Sebastian Nagel: And this is exactly the delta Q modeling for example which could help there which we tried but I think Eve and some others and Vashi were running into computational numeric problems there because just the model is a bit more complicated,…

Neil Davies: Yeah. I mean I talked to Vashy Weekly.

Sebastian Nagel: right? Yeah. Yeah.

Neil Davies: I don't Yeah, you can do much better than you you are. But I would say anyway, so the key point you're saying is so you say the happy path is good.

Neil Davies: I think I would just suggest if you can work how much slack you've got on the happy path and also the thing that is when the things don't go how much effort are you actually wasting how much computation do you have to throw away right if you give up on something because those are the sort of boundaries I would suggest to if you have to throw away half a CPU second's worth of work for example when you change something that effectively consumes the CPU and you can't get it back. So you may find that there is a simple calculation in that area which tells you at what point certain types of failure would cause the system not to make progress again.

Kevin Hammond: So this is great technical discussion, but I'm consciously got other things that we should No,…

Neil Davies: Okay, that's fine. You can always tell me off. You know that.

Kevin Hammond: no, no, it's all right. so what I'm going to say suggest is if there's any more detailed discussion, we organized the session. to go into that unless it wants to continue the discussion.

Sebastian Nagel: Yeah, I think let me just provide a like I mean…

Neil Davies: What?

Sebastian Nagel: what would be a good channel to take for the discussions?  I would say we're lacking a layer specific thing in intersect discord channels or what not right but for example a consensus working group channel would just fit nicely I guess for these kinds of conversations if you want to carry

Neil Davies: My purpose in asking these very high level questions was basically to get a sense of the underlying risks and how they were being managed,  more than actually the technical discussion because I think that's more the role here is what risks are still extent to the systems

Kevin Hammond: I'm imagining that if we need to continue the discussion then a dedicated session would be the correct way to do that. I'll leave that to those who would be interested in joining. That sounds great.

Sebastian Nagel: Okay, let's align it.

Sebastian Nagel: U let's organize it as currency. Thanks.

Kevin Hammond: So shall we return to the agenda? first item as usual, actions from the last meeting. So I pasted those into the chat.

### 00:30:00

Bosko Majdanac: For Alex, it was to publish an X post regarding the SP out abstain mechanism to the community.

Alexander Moser: Yeah, I was just reminded that I had to do this.

Alexander Moser: I wrote it, but I didn't post it to not spam too much from my account. I just have to  I can do that in One hour. Two. I'll let you know to repost.

Bosko Majdanac: That's perfect.

Bosko Majdanac: Perfect. Leandros, connect with the consensus research team, Yorgos, or I suppose that's the name, to refine the train quality metric for 2030 vision.

leandros bsp: Yeah, still pending. I haven't had too much opportunity this week.

Bosko Majdanac: Okay. Any help needed?

leandros bsp: No, I just DM Sebastian, so I'm going to try to get that forward.

Bosko Majdanac: Okay. Sorry.

Kevin Hammond: Just a time machine, boss. We just need a time machine.

Bosko Majdanac: 

Bosko Majdanac: Yeah, of course. for me it was to share the link to three TSC specific questions regarding the April 2026 elections. I shared it there were two confirmations like two agreements that the questions are fine and I suppose that's okay. Can we do it like we can ask people whether everybody agrees or whether anybody objects.

Kevin Hammond: I think we'd agreed last week, Bosco, that if nobody objected by last Thursday,…

Bosko Majdanac: That's right.

Kevin Hammond: then we would

Bosko Majdanac: I'm still playing safe. that's one thing and we have elections also on the topic of the agenda. So we will cover something else there. and for Ryan Wy present the de compensation paper for a dedicated discussion. that's on the agenda somewhere down below. I suppose we can move on with the agenda. So I don't know whether Alex wants hard work first or…

Bosko Majdanac: you're the chair. So feel free.

Kevin Hammond: I was going to suggest maybe covering the hard first…

Kevin Hammond: since Alex raised it at the start of the meeting.

Alexander Moser: I'm being put on the spot here.  It was just freshly on my mind from yesterday and what somehat triggered me raising the point is that in the hard fork working group discussion two weeks ago or that last time the forking node version was called 1062 and then it was suddenly  freshly decided that it was 107 and I was very confused about that the hardworking group didn't name the hardwork properly.

Kevin Hammond: So let me try to clarify Alex, so the node version that will perform the hard fork is node version 11. 10.6.2  two was a step that in that direction. It includes the Plutous primitives that are needed as part of the hard fork but it's not capable of performing a hard fork on mainet itself. So it was deployed onto Sanchet the Sanchet is hard forked into protocol version a few glitches with that but that's all that 10.6.2

Kevin Hammond: two is it's to allow early testing of the Plutous Primitives. So what we're expecting is 10.7 will become the candidate for node version 11.

Alexander Moser: Okay, good.

Kevin Hammond: So otherwise Ryan you're at the meeting. Do you want to summarize the meeting? You're on mute.

Ryan (Cerkoryn): Yeah, so I think that part you mentioned about node 10.7. So I'll skip over that. looks like the recent candidates estimated in one to two weeks. which will be the intended container for protocol version 11. there's a sand sanset incident. they forked to protocol version 11 using node 10.6.  6.2. but there's a Pluto's cost model update was misconfigured that broke script execution. and recovery efforts are underway for that. A hard fork timeline is currently if a stable node is ready in early March, looks like mid to late May 2026 is roughly the hard fork date. there were some concerns about DAP compatibility with PView Hash mismatches.

### 00:35:00

Ryan (Cerkoryn): …

Alexander Moser: Brian, just quickly on the timeline,…

Alexander Moser: when you say May hard fork, do you mean governance action submission or enactment? So mid-March the node version is ready and…

Ryan (Cerkoryn): that's a great question.

Bosko Majdanac: When it happens it includes…

Ryan (Cerkoryn): Okay. Yep.

Bosko Majdanac: if you're reading from those notes ran I think you have also the tentative timeline or something so you have the diagram and…

Ryan (Cerkoryn): Yep. Yeah.

Bosko Majdanac: yeah preview prepresent…

Alexander Moser: then we have until mid midappril mpril Really?

Bosko Majdanac: then I can't share the screen I can't share the screen it's getting sick

Alexander Moser: No. if we want to go enactment in May. Good.

Ryan (Cerkoryn): Yeah. sounds like enactment in May, my understanding. while he's pulling.

Kevin Hammond: So, I think Ryan Williams has a chart where he's tracking possible enactment dates that we were proposing to share, boss, but Alex is in the car,…

Bosko Majdanac: Yeah. Yeah.

Bosko Majdanac: Just give me a sec.

Kevin Hammond: so we'll have to explain it for him or give him a link to it.

Bosko Majdanac: Okay.

Ryan (Cerkoryn): Never mind.

Alexander Moser: Thank you very much.

Bosko Majdanac: This is the thing. So does this.

Ryan (Cerkoryn): Poss possible ratification.

Bosko Majdanac: Yeah. and…

Bosko Majdanac: I think this sorry and it go to switch between the tabs and this was the diagram before we had a discussion yesterday. So if we have a node ready in two weeks from now that will push all of these two weeks right. so the diagram needs to be updated slide. Okay, I will also share this link and I don't know why it wasn't shared in that gbook page but I will make sure that it's added there.

Ryan (Cerkoryn): Okay, that makes sense.

Bosko Majdanac: So this is the tentative time that you can use to follow.

Bosko Majdanac: Sorry guys, I was on mute. So, anything else we need to add on for future half planning other than…

Bosko Majdanac: what you left as a comment in the chat, Kevin?

Kevin Hammond: No, I think we need to start to get back to it,…

Kevin Hammond: Bos, because questions are now starting to be raised about what will be in the Dystra hard fork or rather what's currently being called the Dystra hard fork. so we need to start to put together a process to collect the requirements so Sebastian earlier was saying that he was hoping that linear layoffs would be in the Dyster hard fork that all needs to be agreed there'll be priorities that the community has to agree in particular if one of the items is delayed do we then hold it back or is it so important that we have to include it in the next hard fold.

Kevin Hammond: So the sooner we start to get the discussion going on that the better.

Kevin Hammond: And my understanding is we've moved to a weekly cycle for the half working group now.

Bosko Majdanac: Yeah,…

Bosko Majdanac: also to what Sebastian is saying, I will let no Ryan Williams about again to pre the idea of collecting the scope for Dystra and…

Bosko Majdanac: yes we have moved from weekly to weekly cadence on the hard work working group starting next week every week once a week go Brian Ver

Ryan (Cerkoryn): I was just going to mention that I was also working on that short list for Dystra by trying to make a proof of concept so that we can vote on which SIPS we want to have included in it. and the easiest way to explain it basically is just to click the image I shared in chat. It's basically just you have an onchain survey that's in the metadata and you can embed it inside of an info action and you can embed the response inside of voting on that info action which allows us to use info actions for information which will be nice. so you could do things like query the dre …

Ryan (Cerkoryn): 

Alexander Moser: Yoohoo.

Ryan (Cerkoryn): what sips do you guys want, what do you not want and then you could also query thing.

Ryan (Cerkoryn): There's different question types. So you can query numerical responses where the maximum is this value, and you choose a value in between. And you could use that to set protocol parameters if there's new parameters. and there's even a custom field if you ever want to do rank choice stuff or anything else like that. So the image describes it best. There's a SIP that's still being drafted that u will define it, but that's the TLDDR basically.

### 00:40:00

Kevin Hammond: That's great. what I'm anticipating,…

Kevin Hammond: Ryan, is the demand for content is going to overwhelm the capability of the teams to include it, the developer teams to include it. So, there's a lot of things that people are storing up for this next hard fork and it's quite possible not all of them can be included. Yeah, that's right.

Ryan (Cerkoryn): Yeah, there will have to be some decisions made and…

Ryan (Cerkoryn): maybe some stipulations put in info action itself about things we can and cannot do. And maybe we'll have a thing such that we can only pick the top 10 sips or the top 20 sips or maybe some will be excluded and some can't.  And those decisions will have to come down the road, I think. But we'll have a mechanism for it, which will be nice.

Kevin Hammond: And also depending on the status of development at the time that we come to collect the actual content for the hard Anything else you wanted to raise about that, Alex, or shall we move

Alexander Moser: Good. Thank you. I just wanted to vouch support for loading reference data and…

Ryan (Cerkoryn): I'll drop a link to that.

Alexander Moser: I'm vouching support for layers.

Ryan (Cerkoryn): I'll drop a link to that step here in a

Alexander Moser: I think a hard without layers would not make any sense. we've discussing layers since years now and…

Alexander Moser: doing another big era changing art fork without it would be missed opportunity otherwise we're postponing layers another two years we can't hard fork every six months especially not the big era changanging one…

Kevin Hammond: Not another two years…

Kevin Hammond: but pos possibly six months or something depending on how things worked out. Yeah. that's one of the things.

Alexander Moser: which is introducing instability that we can't maintain. There should be some stable stability someday.

Kevin Hammond: Yeah, I'm very sympathetic to that. That's one of the things we should be discussing in the hard working group. keeping a good cadence and avoiding upgrade overload.

Kevin Hammond: the both FCOS and the community. Yeah, abs. Absolutely. I think I gave one of the very first presentations on layoffs, Alex, and I think that was in Edinburgh and I think it was either 2022 or 2023. So, it's been a while. Great. so moving on, update on the 2030 version KPIs. Leandro, do you want to take that?  We had a meeting with the product committee.

leandros bsp: Yes, I've gathered the feedback. I haven't been able to update the document. Again, it's a busy week. I'll try to get everything integrated by the next meeting, next week.  And anyone who has any further feedback that I can integrate is very open to hearing.

Kevin Hammond: So, we provided the feedback to the product committee. We had a discussion with them slightly disjointed because they were traveling back from the Africa summit, but what we've agreed is to continue discussion on a two- weekly basis.  So there'll be a meeting with them again next week and anyone who's interested in the discussion is very welcome to join. We'll post the details next week in the Slack channel. Great. Thanks for doing that, very positive. I thought the discussion we were having about the purpose was well received and raised some interesting questions. Where do we want Cardono to go?

Kevin Hammond: how do we want to position it against other blockchains? So, it's exactly the kind of discussion that we should be having as well as the detail as well as the specific technical KPIs. Great. Would you mind and do you mind sharing that document again in the chat just in case people don't have access to it?

leandros bsp: We'll do. Sure. …

Kevin Hammond: Thank are we happy for that to be public now? I think we probably are. And yeah,…

leandros bsp: I'll be using the main channel, not the

Kevin Hammond: no, put it in the chat and we'll attach it to the minutes and we'll publicize it and unless anyone objects, of course. Great. next item on the agenda, parameter update status.

### 00:45:00

Kevin Hammond: it's going to hand over to you for that.

Alexander Moser: Not too many updates since last week apart Gian from the benchmarking team or from the Bluetooth team provided us with an update and Kevin I think maybe you have posted them already in the chat. I don't know.  But the parameter committee will receive the new Pluto's values. and we were reviewing them as we speak. Next big committee meeting is on next Thursday. so in two weeks time at the technical steering committee meeting, you can report on that. But as far as I'm aware, everything looks good in regards to the Pluto cost models.

Kevin Hammond: Yes, the updates provide us with they were just to two of the new bu built-in values. They're correcting some issues with the updates that we have been provided. Alex

Alexander Moser: Yeah. in terms of the now failed CC min size parameter change governance action I am not aware of the latest state…

Alexander Moser: if it will be resubmitted by Utah or by intersect I don't know but I'm aware that there is at least some coordination going on that if there is resubmission if it's not interfering with  any hard fork related or other parameter com parameter updates.

Kevin Hammond: So I raised this on Monday at the ISC meeting, Alex, and the way we left it was that the civics committee debate would discuss it and they would agree with you and others the way forward. There are two resolutions to the situation.  One is to reduce the CC min size, the committee size and the other that we'd identified was to increase the number of committee members and part the feedback on the failed par parameter update was suggesting that a significant number of the community believe that the latter approach is preferable to changing the parameter.

Kevin Hammond: So it seems correct to leave it to the civics committee to consider that and then they can either propose a change to the minimum committee size or else they can propose that new committee members are elected.

Alexander Moser: And you means two more.

Alexander Moser: So that the difference is two to the min size.

Kevin Hammond: So the reduction in the min size.

Alexander Moser: The reduction in min size to five would result in a delta between actual CC size and mean size to be two.  If they are raising the CC size now instead of reducing the min size, would that mean that we will end up with nine elected members? Okay.

Kevin Hammond: it would be up to the service committee. It could be eight, Alex. it could be nine. one of the considerations is the difficulty of attracting committee members and…

Alexander Moser: Okay.

Kevin Hammond: the time involved in actually serving as a CC member. So that there is a balance to be struck there. But the way we'd leave it to the celics committee to have a discussion for them to work out the best solution and we can provide by the parameter committee advice on suitable numbers. I think our advice was that they should have had at least eight members.

Kevin Hammond: I think we advised that if you want to have a discussion and say actually min committee size plus two is a sensible number better number that would be reasonable to do…

Alexander Moser: Yeah. Yeah.

Kevin Hammond: but at least one more than committee CC min size is essential if you want to avoid the kind of government lockout we can otherwise

Alexander Moser: Maybe what's also valuable to publicize through this meeting is a good discussion we had in Slack regarding the constitution and how the constitution guard rails are affected when new parameters are  Now that we have two new parameters enabled in the hardwork, there needs to be a constitution update in some point as well that include guardrails for those. Is that constitution update planned or on some agenda as well? Yes.

### 00:50:00

Kevin Hammond: Sorry, are you talking about the van Rossom update? There can't be any new protocol parameters,…

Kevin Hammond: It's an intra era hard fork models.

Alexander Moser: What about the Bluetooth?

Alexander Moser: It's cost bottles. Sorry. Yes.

Kevin Hammond: Cosm models. There are modifications of existing parameters but absolutely for the Dystra hard fork there will need to be constitutional changes and a change to the guardrails script essentially what the constitution says is if new parameters are introduced then there need to be guardrails for them.

Kevin Hammond: the BR it will need to be updated to enforce that. and if the constitution doesn't define any new guard rails, there's a catch all that says you can't change the parameters.

Kevin Hammond: Okay, so not ideal, but there's still safety if parameters are included. No, all we're doing is changing we're introducing new primitives in the hard fork,…

Alexander Moser: Okay, I was for some reason under the impression that we are introducing new primitives in the fun awesome hardwork for protos.

Kevin Hammond: but they only require a change to an existing parameter to the police models.

Alexander Moser: That part I was missing.

Alexander Moser: Okay. Yes.

Kevin Hammond: That's great.

Kevin Hammond: Thanks, It would be a bit of fun otherwise We've got to change the constitution. But luckily we don't. Alex, great.

Bosko Majdanac: question from the products.

Kevin Hammond: So moving forward, go ahead. a so the question from the product committee, we've discussed it a bit in Slack. the discussion may have reached its conclusion. was about including deposits and I think it expanded to mino in the definition of total value locked.

Kevin Hammond: So the argument is that if you've got a deposit, it's a kind of locking thing and if we're defining total value locked, shouldn't we be including that? So it's essentially a marketing question, I think, more than a technical question. We had a bit of discussion about that.  So I'm happy to pass on the conclusions from the Slack to the product committee unless anyone wants to discuss it now. It does affect the KPIs slightly. So it makes it easier to meet the total value locked.

Kevin Hammond: But I'm not expecting substantial amounts of ADA to be tied in with deposits. Maybe with min UTXO. Okay, I'm detecting the resounding silence as endorsement for simply passing back our discussion to the product committee. So I will do that.  Great. Constitution V2.4 review. So, we had a interestingly heated discussion last week about this. Neil wasn't present. I only summarized Neil's perspective. my position is I think we should now close down the discussion.

Kevin Hammond: I don't know if Neil's got any further feedback to make on the constitution, but I would propose to close down the discussion and then we need to take a decision on do we collectively pass that review to the civics committee with carvats or…

Kevin Hammond: do we simply say it's done there are some issues we let things right Neil You year.

### 00:55:00

Neil Davies: I think my point here is I mean m I was on here last week and…

Neil Davies: I was traveling. did people accept it was a mess? That's the first question.

Kevin Hammond: I'll let other people react to that.

Neil Davies: The current situation is not at all what we should be.  spread that way cuz if you don't think either you okay let me place it this way either you think it's perfectly okay to be completely slip I mean either it's a mess right or it's actually being done proply but if you're saying we allow a mess to travel forwards then

Neil Davies: I'd like to know why you can justify that position. Sorry to be vicious, but say something to me. is this actually something that we care about? I mean, do we care about Cardano? Because if the Constitution is a mess, we got to do something to fix it, right? If you're saying, " it doesn't really matter cuz it'll all sort it way out in the end." Then Why are we here? I mean, I'm confused.  Please talk to me. if you had a long detailed conversation last week, you should be able to answer those questions.

Alexander Moser: in my opinion. Yes, the constitution has some issues, so will every other constitution as well. Now, we can call in Exodus and say toxically, this is all b**. Kadana will fail without a constitution.  That's not clean and proper. It is not functional. But that's not the What is the truth is that DREPs and SPOS's voted for a new constitution that passed after four attempts.

Alexander Moser: So now we are within a new constitution that has some loopholes in them which we are free to point out and suggest in an update to a new constitution version three or 2.5 if you will and I think strongly that as the TSC it is our remmit it is our mission  to point those arrows out and put them in a list where in the next iteration of the constitution those can be considered.

Neil Davies: That's a reasonable position. Fine. Good.

Kevin Hammond: So it sounds as…

Neil Davies: Don't necessarily disagree with it.

Kevin Hammond: if what you're proposing Alex is we should pass on the list that I had been collecting maybe also Ryan had been collecting the caveat I had was that I couldn't do a complete review because I was essentially unable to determine the exact differences from version one of the constitution. the version 2.4 is a brace change and the differences are not listed precisely. So it is to do that accurately is a huge amount of work and not one that I'd be willing to take on.

Kevin Hammond: So if…

Kevin Hammond: if I'm passing on my list, I will always caveat it with go and go and do your own go and do your own research, but this is a possible issue.

Alexander Moser: That is also totally fair.

Alexander Moser: If you look at the history of law and constitutions there's always been some loopholes and errors and things found years and decades afterwards. So we not needing to consider the first constitution as Bible and…

Alexander Moser: the next constitution not either.

Kevin Hammond: That's true.

Kevin Hammond: Some of the issues they're relating to the structure of the constitution, Alex. So I think any revision needs to be better structured and…

Neil Davies: I say that we could also add to a suggestion in that they should put some effort into formalizing the change control proc.

Kevin Hammond: it needs to be internally consistent.

Kevin Hammond: So it's partly to do with the format of theution that we have. No.

Alexander Moser: Yeah, I agree.

Alexander Moser: I agree.

Neil Davies: process, right? So that they can b so these questions so that at least the nature of the change, Is clear. And secondly that due deference is given to the nature of the language of writing constitutions and standards such that they understand that changing bolding and things like this can actually have changes to semantics. Right.  that it people changing things days to months and things like this.

### 01:00:00

Neil Davies: it may seem like a simple thing to a human being, but given that the final intention of this is that there could be some automated checking of this we really need to and we need to encourage them to move more towards an automated form of checking and I do realize the whole law is code and I have got a huge history in watching people fail at this but we can do a hell of a lot better than where we're standing.  So that we don't end up with because the thing that we're ending up with is that the constitutional committees can vote something to be everything is currently technically non-constitutional if they wish to take that viewpoint and they're not being and they wouldn't be doing the wrong thing by the constitution. That's not a position you want to be in. Okay.

Neil Davies: I would move that we basically put together a document which says this reduces the list and gives some indication as to how we think they could avoid these problems in the future.

Kevin Hammond: We have to vote on that motion now.

Alexander Moser: Yep, that sounds extremely reasonable.

Neil Davies: Can we have that minute please that Neil was seen deemed to be extremely reasonable which is always nice. Yeah. You see my point here is they've constructed doubt and…

Bosko Majdanac: I'll try to remember this.

Alexander Moser: I'll sign that any time of the day. No problem.

Neil Davies: uncertainty. I'm trying for the sake of the whole community. the less doubt and uncertainty the less attacks could occur from other activities, in that sense. I mean, and I've had several conversations this week about amateur hour related to stuff I'm seeing around Cardano.

Neil Davies: We need to look more professional posttop. And this was a bit amateur-ish in one sense.

Kevin Hammond: …

Kevin Hammond: what I propose then so I'd included some recommendation in the review what it's just is if you and I can convene we can put together a bit of text and then we can pass this on to the civics committee and engage with the civics committee when it starts to put together a revision of the constitution.

Kevin Hammond: ution whether that's version 2.5 or version three whatever the revision is and it sounds as if Ken Eric is saying is working on a constitutional amendment process so absolutely…

Neil Davies: and…

Neil Davies: we would be willing to advise on any such process. Yeah,…

Kevin Hammond: but we would strongly recommend that the final of any constitution is reviewed both technically legally and constitutionally before it's submitted on chain

Neil Davies: cuz Yeah, the aim should be to remove ambiguity, not increase it as the thing as the constitution matures.

Kevin Hammond: Does anyone object to that course of action? And we will make sure that the text is passed on for ratification before we do that,…

Kevin Hammond: of course.

Neil Davies: Can I just disagree slightly with that?

Neil Davies: Pointed I think we should be as definitive as possible. we can say this is different from this. right is one right the point is we can point out any ambiguity that occurs. I think we have to point out why we are concerned and why we were so ahead about it.

Neil Davies: Is what I'm saying. I want to be firm about this as opposed to a bit wishwashy. That's all.

### 01:05:00

Kevin Hammond: I mean I think so looking at the remit of the TSC…

Kevin Hammond: which is to provide technical advice to government for government's purposes then I think we're absolutely required to provide feedback if we identify issues that are problematic and I'm sure we've got Ken Eric in the audience I'm sure they would very much appreciate that. What I don't think we need to do is to go out and say start to tweet something like the constitution is broken, the skies are falling.

Neil Davies: I would agree we don't need to do that. But still it can't just I hate this I watch too many things…

Kevin Hammond: Abs. Absolutely.

Neil Davies: where organizations make bad mistakes and they never actually sort of face up with them. and I can tell you whole bunches of horror stories so they never learn. I think we should treat this as the best learning process it can get away with.

Kevin Hammond: One of my concerns is that we end up in a situation where people start to legally dispute some of the provisions of the constitution. you don't want that to be possible. Yeah. So the things need to be robust.

Neil Davies: That would really bring everything to sort of as soon as you get that level of uncertainty gr things start going people take one look at you and walk away. That's what  I'm trying to avoid that's the certainty that governance of other people need. Yeah.

Kevin Hammond: So we've got an action to carry forward.

Kevin Hammond: We'll keep the committee informed about what's happening with that action and we'll engage with the civics committee can to progress the revision of the constitution and make sure that in the future revisions are less problematic. Great. do you want to just quickly finish off  Two

Bosko Majdanac: Yes. if it's for me and not Ryan. Yeah. Yeah. But quickly we can take this essentially line. So first thing is operational budget.  There are three things that are going to happen in the next two weeks. So this week I can work with you Kevin just to pick up essentially the work packages from our operational budget proposal and to put it in one mirror boards and that is for this week. I will share the link to it and we can work together if you need my help at all.

Bosko Majdanac: then the next week we are going to be I mean everybody else to refine finally the proposal to see whether they're do engaged in a feedback loop and then the week after so two weeks from now we are going to u put whatever we have as a final version of our proposal into the template that was provided by the budget  committee. So this mirror, week after refinement plus telate. for April elections, number of seats for election is five yet we have six. If you want to elaborate on that, but I think everybody is pretty much clear. So for the committee elections, we can only have five for April.

Bosko Majdanac: The only thing is that we have one member that stepped down and there is a different process for replacing if decides that it needs to be replaced because we can go on with nine as well. 1 nil  Yes.

Neil Davies: My suggestion would be that we make it clear that we're having five the top five will get a one-year post. the one who's six will get a six-month one.

Kevin Hammond: Yeah, the No,…

Neil Davies: Would that work?

Kevin Hammond: the terms are changing to two-year terms from the April election.

Neil Davies: So I'll take it again then the top five get the full seats right the two years the sixth person gets the remainder of the previous seat it's back up to the numbers. That's my proposal. Sorry. So say this,…

Bosko Majdanac: I'm not sure I understand. Text, can you help if you're still here?

Neil Davies: you vote, right? We rank everybody.

### 01:10:00

Bosko Majdanac: Mhm. Yep.

Neil Davies: The top five people will get the seats for the next two years. And one person beneath that, the sixth person, we co-opt for the remainder of the six months of the seat that's currently idle.

Bosko Majdanac: I don't think it's the problem,…

Bosko Majdanac: but I would double check. That's an interesting idea, maybe.

Kevin Hammond: I think it would actually so my understanding is the existing terms are being normalized Neil.

Kevin Hammond: So the October elections are being eliminated and that those who are currently serving until October would have their term extended…

Kevin Hammond: Unless they step. Yeah. So that would be until April 27 and the other five would be until April 28. We might want to see how the votes come out before we take a decision on the co-opting.

Neil Davies: So what I'm saying is whatever's happening to that cohort of people that sixth person joins But we could Yeah.

Neil Davies: But we could say that is our intention to co-opt right that person on those because we should try we made the decision because the difference was dramatic between the people previously and last time we were left in the position and one of the people stepped down etc.

Neil Davies: So I just want to find out if I'm going to suggest that we take that approach which gives us the power of option but we are using community input in the voting process to help guide that

Kevin Hammond: …

Kevin Hammond: I'm not sure we need to take a vote on that right now. the conclusion seems to be that we hold elections for five people now and then the motion would be depending on the vote outcome that we could co-opt the sixth as an additional member to replace the person who stepped down in October.

Bosko Majdanac: True and one more thing for April elections I also shared last week the application pack and that's also to be confirmed by Friday so I will remind you so there was a comment from Sebastian I think on the remmits or how you contribute or what the TSC is doing and I have changed the paragraph And I think it was also agreed by somebody else. So I will also ask again in the slack. So if nobody complains until Friday, end of the day, then we can consider it accepted as there was no negative feedback so far on the suggestion. That's it from me. I don't have anything else. We are over time. I don't know if you want to cover anything else.

Bosko Majdanac: 

Kevin Hammond: We'll postpone the discussion of the direct compensation paper to next week.

Kevin Hammond: And Ryan, you had a question that you wanted to raise offchain process change requests. I think that needs a detailed discussion. So let's agree to discuss that next week. Great. I'm assuming there are no other items of business.

Ryan (Cerkoryn): Sounds

Bosko Majdanac: You. Bye-bye.

Kevin Hammond: Thank you very much everyone and I'll talk to you all again very shortly.

Ryan (Cerkoryn): Take

leandros bsp: Did  He was

Kevin Hammond: Bye everyone.

### Meeting ended after 01:14:46 👋

This editable transcript was computer generated and might contain errors. People can also change the text after it was created.

  
**