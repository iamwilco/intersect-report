**

## Technical Steering Committee - 2026/02/18 15:58 CET - Transcript

# Attendees

Alexander Moser, Benjamin Hart, Bosko Majdanac, Design Thyme, Duncan Coutts, Kevin Hammond, leandros bsp, Nicolas Biri, read.ai meeting notes, Ryan (Cerkoryn), Sebastian Nagel, Terence McCutcheon, Wilco van de Burgwal

# Transcript

Ryan (Cerkoryn): Howdy.

Kevin Hammond: You're multitasking today. Hi Ben.

Ryan (Cerkoryn): Yeah, I have another meeting in 15 minutes and then a third meeting in 30 minutes. So, I'll let me look at the agenda again.

Kevin Hammond: Is there anything on the agenda you'd like us to prioritize? I'm open.

Ryan (Cerkoryn): I don't think necessarily if it's super relevant to me. I mean, unless you want to talk about that compensation paper I put together, but it's just a rough draft. But I'm also happy to take written feedback or however you guys want to give on that.

Kevin Hammond: Yeah, we can ask the others. So depending on the time that we have available,…

Kevin Hammond: we might want to put that off to next week, Ryan, so we can all read through it.

Ryan (Cerkoryn): Sounds good to me.

Kevin Hammond: Hi, Alex. Hi, Neandros.

Alexander Moser: Nope.

Kevin Hammond: I'll just paste the agenda into the chat as usual. And as usual, if you have any items that you would like to raise or…

Kevin Hammond: anything you want to prioritize, please let me know. Great.

Ryan (Cerkoryn): I can actually drop a link that might be relevant to that SIP short listing thing that the other Ryan's working on…

Ryan (Cerkoryn): because I was trying to build a SIP with Thomas from Intersect and a proof of concept to make that possible.

Kevin Hammond: So, we'll just wait a couple of minutes for any late comments to join us. Neil Davis sends his apologies. Ben Okay, you're joining us as observers. Was there anything you wished to raise with us?

Wilco van de Burgwal: No, no, no, not really, guys. Hello.

Kevin Hammond: Hi. Hi.

Wilco van de Burgwal: It's just I just want to see how other committees work and see some more productive spirits than elsewhere. That's cool. I have nothing to say. Just keep going, guys.

Kevin Hammond: And Ben, anything from your side?

Benjamin Hart: No, I'm just here seeing what's going on.

Kevin Hammond: Welcome. Hi, Sebastian.

### 00:05:00

Kevin Hammond: Sebastian, when is the next the monthly layoffs session?

Sebastian Nagel: next week.

Kevin Hammond: So that will be at 1400 UTC.

Sebastian Nagel: One hour exactly before the TSC meeting.

Kevin Hammond: Would you mind posting the link to that you posted in the chat or

Sebastian Nagel: A note.

Kevin Hammond: and there's nothing you wanted to raise for example from the L2 working group.

Sebastian Nagel: nothing really. No. we had a bit of a funky schedule there. I'm not a chair anymore, So we have basically two chairs now on the layer two. George is running the American instances and then we have earlier Asian instances every other two weeks which Shiran from the IOE hydra team is picked up last week and yeah the schedule is a bit funky but the luma calendar is up to date also will make it consistent with the intersect calendar lenders I heard was good participation maybe a bit very hydro focused last week.

Sebastian Nagel: Let's see what No, it's two weeks ago because today is the next one.  I think of it later.

Kevin Hammond: So I propose that we start this call formally.

Kevin Hammond: So welcome to the intersect technical steering committee meeting is the 18th of February 2026. we have one, two, three, four, five voting members present. So by my reckoning we are not corate. So any decisions only be provisional would need to be confirmed by an out ofband vote by a vote next week.

Kevin Hammond: So, I've posted the agenda today into the chat. we have no other items to add to it as far as I'm aware. So, first item on the agenda is actions from the last meeting. So, Boss,…

Kevin Hammond: what actions do we have?

Bosko Majdanac: Okay, I will share the screen quickly.

Bosko Majdanac: Hello everybody. I will share the screen of the notes and action items from the last meeting. This is the most readable form that I could get.  So for Alexander and TSC and NDX promote the out to obtain mechanism for SPS to reduce governance friction for nonparticipating pools but I don't see it as an immediate actually action. So is there anything that you want to share there Alex?

Alexander Moser: I think it's valuable for SPOS's to know that they can remove themselves from the voting equation. but I guess that an expost isn't really addressing the right group because those that are active on X are mostly also active SPO but for those where this is relevant, it is large pools and sexes and,  staking providers.

Alexander Moser: However, of course, we can still draft that post and in fact I'm writing it right now because I saw it in the agenda and can just post it as a call to all SPOS's…

Alexander Moser: who want to remove themselves from governance.

Bosko Majdanac: Feel free to share in any possible way and…

Bosko Majdanac: we will deal with it and post it on the TSC account. next one. Sorry, Land Ro. I think you're here, right? So,…

Bosko Majdanac: it was to share the comprehensive KPI targets document and quarterly breakdown with a committee for async review. So, is that progressed well enough to be reviewed or not yet?

leandros bsp: Yeah, I've sent it.

leandros bsp: I can share what we have if you like right now so we can go over it. I sent the link last week, but I will send again after the call. let's see with there so you should be able to see. so the metrics that I recommend that we recommend are annual protocol revenue. This is very important for the sustainability of the Pluto fees created. This encompasses both the CPU units as well as the main units.

### 00:10:00

leandros bsp: And it's a very good indicator of business activity on the chain. Chain density is an excellent indicator of the chain health and the total value log because it's almost forced upon us by what analysts are looking for in blockchains. as far as the values that are selected I have a breakdown right here. The conservative value for protocol revenue is a steady growth of 30% year-over-year.  target is getting to the level of rewards that we have today without having to rely on the treasury and the stretch is being able to double the rewards to 4.8%

leandros bsp: 100% without any help from the treasury the reserve sorry the Pluto fees are following the same guidelines as the conservative target and stretch as the protocol revenue I'm just using the calculating the same values chain density I set the target to 4.5% this is what we had during the chain fork so anything above that I imagine is good and of course stretch is the perfect that's 5% the theoretical maximum and…

Kevin Hammond: Yeah, we should have some discussion on that.

leandros bsp: definitely Mhm.

Kevin Hammond: Andros, so the chain density I think it dropped to some relatively low level. So I wouldn't regard that as a good target to hit.

Kevin Hammond: But We'll have a discussion about that.

leandros bsp: Yeah, definitely.

leandros bsp: I just put some initial values so we have somewhere to work from. Ryan, you wanted to try many.

Ryan (Cerkoryn): I was just going to chime in and say that might be related to the issue we found with Binance pools not making any blocks for 28 days. That surely would have affected chain density.

leandros bsp: Yeah, but I think the lowest chain density we had in a per epoch setting is during the fork…

leandros bsp: where we had half the nodes producing on the one chain and the other half on another.

Ryan (Cerkoryn): For sure.

Ryan (Cerkoryn): That would definitely do it.

leandros bsp: MTLV I set the target to being a mid-range blockchain.  about the levels of Solana and the stretch being a high competitive blockchain around the levels we have around here. the nine bill will put us near Solana and the three bill will put us near Ethereum and Tron. wait this can be wrong.

leandros bsp: and the conservative target is just an appreciation of I think about 20%. And here we have everything broken down into quarters and years. This is what we would expect the protocol revenue to be for the conservative target. This is the medium target year after quarter with the year over year rate and the quarter over quarter rate. then we have the stretch and we follow the same model for the plutous piece the TLV and the chain density is a static number so I didn't put anything

leandros bsp: Mhm.

Kevin Hammond: So, I've put an agenda item to go through that in detail. Leandros, and saying we're going to follow up with the product committee later today.

Kevin Hammond: Sebastian If you want,…

Sebastian Nagel: you wanted to discuss the chain density now Kevin…

Sebastian Nagel: because it's quite intriguing.

Kevin Hammond: if it motivates you, Sebastian. Yes, let's do

Sebastian Nagel: Yeah, so the stretch or the target being 5%, right? That is it matching the nominal block production rate, right? It's kind of a 0.05 is the active slot coffient. That means right every 20th slot, which means 5% of the slots would be active, which would be in production.  If we put that as a KPI, it wouldn't motivate a denser schedule by that's just Risky means okay we will keep that parameter the same way and we just want to have as much as possible of these targets or which it can't get better than 5% given this parameter. That's what I want to say.

### 00:15:00

Sebastian Nagel: And if you would for example find a reason maybe because of some analysis of smaller networks and other chains right what Kevin I think have been doing that hey we could actually be a bit more tight on that right or more legs we would kind of meet or…

Sebastian Nagel: kind of influence the product targets here which is a purely technical decision maybe All right.

Kevin Hammond: Yeah, you're right.

Kevin Hammond: There's a question about how you measure the chain density. Sebastian, and arguably the correct measure is against a nominal 100% of what is theoretically possible over some

Sebastian Nagel: So we should normalize it by the parameter, Which is the target. I think isn't there another metric which is chain quality. which kind of is I think the normalization against what is the expected number of blocks and to what's the actual number of blocks over time that would basically normalize it against any parameter we select because of maybe security or kind of just for other technical reasons.

Kevin Hammond: as long as we're clear what the metric means. Yes. But then we can start to set as you're saying sensible metrics.

Kevin Hammond: So if we're dropping below the theoretical maximum, then we can determine that it's possible we're actually exceeding the theoretical maximum. Very unlikely, but possible.

leandros bsp: That's So I will look into the chain quality and…

leandros bsp: 

leandros bsp: change it to a 100% base measure of chain density. So the 5% will be 90% etc.

Kevin Hammond: And …

Kevin Hammond: we can discuss this, but do we know how we're doing currently relative to that metric?

Kevin Hammond: The Android is

leandros bsp: Yes, the lowest we got during the hard work was 4.5%.

leandros bsp: I went back to find that I'm counting chain density in a per epoch setting. I think that's the most appropriate for long range protection and it's a good time scale to look at and…

leandros bsp: that was 4.5% so normalized 90% one yes as far as I know that Where's the book?

Kevin Hammond: O over…

Kevin Hammond: what time frame were you? What Yeah. and the target the KPI you're measuring then is the worst behavior for any epoch?

leandros bsp: And I set that as the middle target.

Kevin Hammond: Yeah. Yeah.

leandros bsp: We could safely set that as a conservative target and set the middle target to let's not do worse than we already did. So someone between the perfect and what we got as the worst.

Kevin Hammond: So the qualitative question is what is acceptable and we don't really know that.

leandros bsp: 

leandros bsp: Yeah. Yeah. I tried to figure out if there is a minimum safe value…

leandros bsp: but I did not find anything.

Kevin Hammond: There is a minimum safe value and…

Kevin Hammond: we'd need to consult the consensus team about that.

leandros bsp: Okay, I'll be very useful.  Yes.

Sebastian Nagel: I also just wondered I mean the researchers have been using chain quality in even their safety proofs of robber and…

Sebastian Nagel: so on right and I should connect you with Yorgos you're Greek right Leandros so you can probably speak in native tongue to him like Yorgosaki banakos is one of the I think robberous  researchers. it's a whole group. and I let me connect you to him and maybe you can find a good kind of research back technical measure which kind of is a good proxy also for product decisions and is the chain running smoothly. That's what we want to expect here I guess right I express here. Yeah.

leandros bsp: Yes. that's the main reason for the specific CIP PI. Any other feedback on what we have here? Anyone want to complain that we have selected the wrong KPI and we should be using something else.

### 00:20:00

leandros bsp: 

Kevin Hammond: Yes. Unfortunately,…

Kevin Hammond: I've been a bit too busy myself to read through it properly, Andros. U but I've got a copy of it here and I'll read it as soon as I get a chance and…

leandros bsp: Thank you.

Kevin Hammond: I would encourage everyone else to also read through it.

Kevin Hammond: Once we've done a read through is there any reason not to make this public? I can't see anything particularly confidential there.

leandros bsp: No it's and…

leandros bsp: I'm just editing the document we already had. So anywhere we shared it, they can see it already. Okay.

Kevin Hammond: Great. But I think it's good to get information like this out and to start the debate.

Kevin Hammond: And Moving on.

Bosko Majdanac: Neil is not here, of course. so you can skip that camera, right? But it's also, an agenda item if I'm not mistaken.

Kevin Hammond: Yeah, we

Bosko Majdanac: Yeah. Okay. Ryan refined the SIP short listing name and process to present and stand function of the hardworking group. any updates on that?

Kevin Hammond: Brian W.

Bosko Majdanac: Yeah. Yeah. Ryan might be juggling between the different meetings.  we can revisit that later. For me it was to finalize as we are having in April 2026 elections committee elections. we are to finalize three specific election questions on lack to meet the upcoming this Friday. so I shared that on Slack. I will share the link again here.  So given how much time we need for other agenda items, I would just like somebody to review this is the link to the conversation to review three specific TSC related questions.

Bosko Majdanac: the links are listed there and then to confirm I mean the links the questions are listed in the post and then to also review the pack itself. But go on Sebastian

Sebastian Nagel: Did anyone raise that they need amendment or I mean they are half a year old now? They seem to work We have wonderful new members who all meet the criteria I guess.  So maybe there is no not even a need for changing them and if nobody raises that I think we can just assume them confirmed.

Kevin Hammond: So let's give people when do we need to fight these to by the close of play on Friday.  So let's allow people the opportunity to raise any questions by the close of play today tomorrow and otherwise we'll just forward them. So

Bosko Majdanac: Mhm. Yes.

Bosko Majdanac: Yeah, that's the idea. So any of you who need more information reach out to me and that's it. We don't need to cover anything more on this bit. and then it was for Kevin and Neil. I mean there's a meeting after today.

Bosko Majdanac: Leandress is also there I think. So invited to the call this week. So that's the last meeting on the action items list. aha.

Kevin Hammond: And end of the product committee meeting yesterday.

Kevin Hammond: You have you a holiday boss,…

Bosko Majdanac: Yeah. So it was my bad. okay. Just give me a sec. Want to switch to another tab. So that's it. I think.

Kevin Hammond: you weren't paying attention.

Bosko Majdanac: Not enough obviously. okay. I'm switching to a tab with agenda improving technical coms for hardwork etc etc.

Kevin Hammond: So, let's move on to the next agenda item. Yandra, so there's discussion coming out of Twitter about improving technical communications for the hard fork, etc.

leandros bsp: Yes. the last update was hinted very strongly that SPOS's need to upgrade immediately because of a security concern but no extra information and I find that to be problematic for our security model because SPOS are supposed to know what they are deploying in order to do the job. most SPOS's are not highly technical so reading through the commits is not great and half communicating might be the worst of both worlds because you are letting attackers know that there's something to look for and you are not letting SPOS's know what's happening.

### 00:25:00

Kevin Hammond: So something so seeing this from both sides, Leandros, we're in a peculiar situation where everybody has to upgrade simultaneously and we're doing it in a public space. so that's a very unusual security situation other situation. so what we want to do is to encourage people to upgrade but we can't always give away the details the exact reasons of a specific upgrade is necessary or desirable. so I'm not quite sure how we can deal with that in a suitably open way. but certainly saying this vulnerability would be airless.

Kevin Hammond: I would say, there is this bug. So, it doesn't have to be a vulnerability. there could simply be a bug. you may not want to draw attention to the specific bug. I'm open to discussion on that with members of this group.

Kevin Hammond: Sebastian that was one of the issues that was being raised on Twitter.

Sebastian Nagel: So this is about software bugs or…

Sebastian Nagel: needs to upgrade of particularly the Kadano node software package right the Kadano node or Okay.

Kevin Hammond: The other one was that they needed to join Interex discord channel to find out information about the and we were hiding away the details of what the hard fork was.

Sebastian Nagel: That's two separate things.

Kevin Hammond: Cool. Thank you.

Sebastian Nagel: I'm also very much concerned about the letter would rather be coordination in the open is better. now the first one if it is about the software component Kadana node I would go by where this is kind of released and distributed. I think the to channel is GitHub releases today. If that is the case another GitHub based workflow would maybe be a good short-term solution for that. there is the opport I think it's possible not sure if you use it for the kano node right now to have security advisories. So something you can do I think responsible disclosure of even bugs or security issues through that channel and you can get people into that.

Sebastian Nagel: so it's private by default unless you are a maintainer of that software package or you pulled into that context through the GitHub platform. So that would be an option. So now people need to have GitHub handles or people they talk to need to have GitHub handles so it reaches them and you want to kind of increase the reach through that.  But that could be an option to kind of do announcements too or get them on board on there is a security issue coming from the security council for example and you should really upgrade to this version or stay tuned that and now we have to be update so we could even open that as a threat before the fix landed you're on mute  Okay.

Kevin Hammond: Yes, but the security council might not be able to say what the nature of the threat was. Of course,…

Sebastian Nagel: Yeah, I understood that we want to have a channel to reach SPOS's to reach not directly public by default channel…

Sebastian Nagel: but kind of gradually open up and getting more people to get more eyes on that right as you

Kevin Hammond: So I think inevitably there's going to need to be some level of trust.

Kevin Hammond: And there might be a way to reveal some information it's recommended to upgrade there is a level X issue.

Sebastian Nagel: Exactly. I mean I guess security advisories or…

Kevin Hammond: So maybe that will be some way of giving a bit more information alternatively just having the endorsement coming from the security council rather than from community members might be the way to do that.

### 00:30:00

Sebastian Nagel: vulnerabilities or these kinds of things right have always two sides of things. one is the responsible disclosure so it can get fixed if it is detected not by even the maintainers themselves or people who would be able to fix it and then the other side how to get it applied and into the field right so I think to get both sides connected somehow in a way…

Kevin Hammond: thousands. Sebastian. Yeah.

Sebastian Nagel: where it is not public by default but can still be made public to hundreds of people right because we want to target hundreds of people operating these nodes  Yeah, but the first couple hundred is good and you don't have 100% reach always and maybe they talk to each other also outside of that channel, Of course that is the trust you mention right once you involve somebody and there is something stay tuned or that is exactly the thing and that's how you need to fix it yourself.

Sebastian Nagel: know if you involve somebody there you rely on them to not kind of disclose it differently to somebody else which would have not been on the channel otherwise Yep.

Kevin Hammond: So the team is already using the GitHub security advisory mechanism.

Kevin Hammond: So this is being moni monitored by intersect staff. issues being raised are being passed on and responded to and the issues that are being raised may be rewarded by the bug bounty program. So that is happening. I'll take the other issue back to the security council and consider…

Sebastian Nagel: I mean,…

Kevin Hammond: how to address the issue of notification.

Sebastian Nagel: 

Sebastian Nagel: we could use the same mechanism for that. maybe by deliberately on a separate advisory which doesn't disclose the details, right? But rather security advisory of needing to upgrade,…

Sebastian Nagel: but it's not disclosed in this one and it will later be disclosed in the other one, but it could still kind of be the same channel if it is amendable to or…

Kevin Hammond: Yep. I can answer that…

Sebastian Nagel: it's works for the people running nodes. If they're not on GitHub and are oblivious of GitHub, then that doesn't work for them. But then the question is how do they get the releases today? Right? If that is the release channel.

Kevin Hammond: but that's a question for another that's a question.

Sebastian Nagel: 

Sebastian Nagel: Yeah. Yeah. Of course.

Kevin Hammond: So moving on art fork information. So it seems that that's not as widely disseminated as it should be.

Kevin Hammond: Bos, I think we've got some actions to do there to make things more open. I think the Discord channels are locked down through to avoid spam for example on the channel. so…

Kevin Hammond: but maybe it's possible for people to get a read only feed from the discord channels. Maybe there's some way to do that.

Bosko Majdanac: I was looking into the technical possibilities…

Bosko Majdanac: but I didn't find anything good yet. So we'll see how to expose and what would be sensible to be disclosed that way if there is anything that needs to be taken care of with still looking into it but it is a thing because even if you can intersect for free then it makes sense that then you still have a couple of steps to go through before you are able to understand and be an observer.

Bosko Majdanac: sorry Sebastian yeah yeah yeah we are keep saying this in upgrade bulletins or whatever we are using that this is the way to engage one of the ways to engage but still this operational things where we could have more people involved is yet to be both solved I don't heat.

Kevin Hammond: So, if anyone has any ideas for how to improve technical communication, please notify Bosco or myself and we'll try to progress That's one of the items we'd raised as part of the 2026 budget. so it's been something that's been longstanding but I wasn't aware that people didn't know what was going into the hard fork for example. Great. 2030 vision KPIs we've covered there'll be a meeting with the product committee later today. parameter update status. congratulations Alex on getting the parameter update through.

### 00:35:00

Kevin Hammond: Would you like to take the site?

Alexander Moser: It's a group effort. I didn't do much.  I've just loaded with multi-rep time.

Kevin Hammond: I was impressed by the GRE vote. It was something like 86%. I'm not sure if that's a record, but it's certainly a very high percentage. so the grats were clearly in favor of this but it has caused a problem with the committee min size parameter that you was proposing to reduce

Alexander Moser: Indeed, but I heard you were in contact with him about it and he handed over resubmitting it to us or…

Alexander Moser: in coordination with Intersect. Okay.

Kevin Hammond: My man saying has Ryan Williams been in contact with him…

Kevin Hammond: but I don't know what the outcome of the discussion was. Alex there does seem to be some push back from DRAPS on the reduction. so the nature of the push back appears to be rather than reducing this parameter increase the number of committee members.

Alexander Moser: Let's go. Yep.

Kevin Hammond: So some people feel that the reduction in the min committee size is reaction to that and the correct thing to do is to increase decentralization by having more rather than fewer CC members.

Kevin Hammond: So it's not clear to you that even…

Kevin Hammond: if the parameter update was resubmitted correctly that get enough positive vote.

Alexander Moser: I mean the parameter committee did their analysis on this as well and…

Alexander Moser: posted it on the forum. I think it's PCP 0000 4 or 5. and they said the same thing that it's ideally  more than five and seven. But I think the purpose of this is to avoid situations like in December when the whole governance system just broke down because of the dependency on one single institution committee member. And lowering that to five just means it's a minimum size and not a target.

Sebastian Nagel: How can the maximum be increased or…

Alexander Moser: Just adding more in the CC action.

Sebastian Nagel: can this be done in the same go?

Alexander Moser: Yeah. CC add member the governance action.

Sebastian Nagel: So maybe it would be better looks or better marketing to say we both do that the same thing kind of reduce the minimum but also add one more seat same time.

Sebastian Nagel: Question is that will be right or we will lower it by one or two. How much do we lower the minimum two?

Alexander Moser: two two five

Sebastian Nagel: So maybe we should add to kind of balance out the misunderstanding.

Kevin Hammond: If it's possible to find two volunteers to be CC members, it's a bit of a thankless job. I suspect Sebastian All right,…

Sebastian Nagel: Yeah, I speak to Matias Bankard regularly.

Alexander Moser: Did you know that his CC key was hardcoded into the new ledger rules?

Alexander Moser: He's CC now forever. that for the record and…

Sebastian Nagel: Better not lose the keys.

Kevin Hammond: I have

Alexander Moser: for the recording this was a joke which he always also complains to us about it…

Alexander Moser: which is why that came up today. Good.  I think next topic.

Kevin Hammond: So we'll need to consider…

Kevin Hammond: how to progress with that and with the other parameter upgrades that were in flight. But the parameter committee is meeting next week I believe so they can discuss that. So, moving forwards, Constitution V2.4 review. so I did a review. I've passed it on to everyone here. Neil has tried to validate the review that I did. And his response this morning was on the lines of, " heck, this is a real mess.

### 00:40:00

Kevin Hammond: I can't even figure out what the differences are and neither can AI tooling, so he's not completed his checking of my review, unfortunately. if I have to go back and look at all the sources, it's going to take me two or three days probably to go through it because one of the criticisms is the diffs that are provided.  There are 90 pages of diffs. It's literally almost impossible to go through and check what are the changes between v1.0 and v2.4 of the constitution. so when I did my review I did it on the basis of what v2.4 was not v1 and my memory of what v 1.0

Kevin Hammond: zero was but I couldn't refer to a clear set of differences between the two. So there were some people I think Nicholas particularly were saying we don't want to pass this on as a official TSC document. we don't have the people here to take a vote on that anyway.  But obviously what I'm not going to do is to pass on anything which claims to come from the TSC without it being official. So the question here is how to proceed.

Kevin Hammond: We wait for Neil to complete his review and he's given me maybe another three days of work which might take me another month or so to go through or do we simply pass it on to relevant parties with caveats or do we say we've the whole thing looks like a real mess. We're seeing some of the issues cropping up with onchain governance actions. I feel there's a responsibility to warn people but the question is simply whether to do that officially or unofficially.

Alexander Moser: I would say the more important sorry to jump you Nicholas by not raising my hand. I think the more important aspect of making this list is having a list of to-dos or constitutions 3.0  though and not to tell people hey there is loopholes left and right but that at some point there will be a next iteration which is good and intended it's iterative improvement and in those iterative improvements the errors introduced in this version or inconsistencies should be collected somewhere so I think the task is not timely

Alexander Moser: necessary to be completed in a month but It has long-term value.

Kevin Hammond: Yeah, one of the issues is the constitution prevents itself from being amended,…

Kevin Hammond: Alex, I believe.

Alexander Moser: I no I really don't think so. But Nicholas also vehemently shakes his head.

Nicolas Biri: No, I totally disagree with this…

Nicolas Biri: because there's still a path for it. you can't have a constitution that lock yourself into something. That's why the CC can still agree on the constitutionality of a governance action that will provide a new constitution. So I don't see we can lock our self in.

Nicolas Biri: If we thought that we will lock our self in because of inconsistencies being pointed this inconsistencies the CC will have to take a decision on this.  That's why we have a CC

Kevin Hammond: Yeah, I agree with you.

Kevin Hammond: Pragmatically, I think that's the case. from a formal perspective, the CC needs to uphold the constitution as written. there is a problem.

Alexander Moser: I'm getting a friend that's downloading

Kevin Hammond: their position is not to say we don't believe in the constitution.

Kevin Hammond: If you're a CC member, you're required to uphold the provisions of the constitution as

Nicolas Biri: I think it's also part of the challenge I have with this discussion within the TSC.

Nicolas Biri: It's far beyond or remit. I do sympathize with the idea of looking at the constitution from a technical perspective and see for example if there's issue with the guards.  I think you are noticed some and I'm totally fine with this and actually it's something that we need to raise and as Alex say with the idea that at some point there will be an upgrade of the constitution and it's good to gather this kind of feedback. I think that going beyond the idea of giving a feedback on the technical side of the constitution is definitely out of rammit.

### 00:45:00

Nicolas Biri: It's a problem that I've raised several time with the work of the TSC that has been raised by others outside the TSC and I'm really uncomfortable with it. We should just stick to…

Nicolas Biri: what our remedy is. Our goal is not to solve every problem within the card space.

Kevin Hammond: No, no,…

Kevin Hammond: I'd agree. But if we spot issues, we should raise them, Nicholas. So,…

Nicolas Biri: 

Nicolas Biri: Yeah. Yeah. Yeah. Yeah. And I mean that's also why I said that for example all the issues that we have with governance actions parameters all this kind of stuff that are technical stuff we can raise them as the TSC and I'm fine with that every other comments I would love actually because we talked about several time it won't be a Wii because I won't be part of it.

Kevin Hammond: that's fine. Wait.

Nicolas Biri: I mean it can be if the scum reveals the TSC and…

Nicolas Biri: I will definitely explain why I'm not part of this because it's by far not remit.

Kevin Hammond: What…

Kevin Hammond: what I would say is I believe that there should have been a technical and a legal constitutional review of the constitution before it was put on chain the final version. if that had been done I think we could have avoided a lot of the issues and inconsistencies. So I think feeding that back is incredibly important.

Kevin Hammond: And as I was speaking, Nicholas, I no…

Alexander Moser: Because Kevin,…

Alexander Moser: wait a second. To be fair, it was built out in the open and you made four attempts to upgrade it for maximum visibility. If any of us would have taken up that input proactively as it was built out in the open, we could have given that input much earlier than after the fact. Now that it was approved in the fourth iteration,…

Kevin Hammond: if …

Alexander Moser: now we're saying but nobody asked us. Come on,…

Kevin Hammond: I wouldn't give a technical review.

Alexander Moser: it is not really help.

Kevin Hammond: I wouldn't give a technical review of something which was not final. Alex, you really can't do that. And what I would expect is the community would reach out. so what was surprising was that we've apparently discovered that the civics committee wasn't aware either or some of the reviewers.

Kevin Hammond: So what I would have expected this being within the remitt of the civ as the civics committee would have said to us there is a constitution there's a change to the constitution coming up please undertake review or some community member would have done likewise and then it could have been scheduled so I think there is responsibility on those making a proposal to follow such a process otherwise you get inconsistencies Alex and you may get legal problems as

Kevin Hammond: 

Nicolas Biri: If I…

Nicolas Biri: if I strongly disagree with this. it's a permissionless system. Everybody can propose something as long as they verify, as long as they commit to the constitution. if they think that we are valuable enough, they will reach out to us.  if they're going to reach out to us, it may be a TSC problem, not the community problem. That's all I have to say on this.

Alexander Moser: I 100% agree. That's exactly what I want to say as well. We have to stop thinking in ivory towers. There is no obligation from anybody to come to us for anything that's permissionless for a reason. And the fourth iteration of UT trying to get this across could have sparked our interest proactively as it was obviously happening a fifth and…

Alexander Moser: a sixth time as well. Them asking us is not their obligation.

Kevin Hammond: Then…

Kevin Hammond: then we have to live with inconsistency and potentially failure, Alex, when we could have prevented it.

Alexander Moser: Hey, this

Sebastian Nagel: I don't think that we need to live with it. If we have a good proposal, we can bring it up, I guess. So, we can fix the things we want to fix. I'm personally not going to do that because I kept myself out of it. I don't have the full picture, but I'm fine with any. I think they capture the same belief. in my opinion. But if we want to fix it, we can propose a fixed constitution. Let's call it 2.5 or 3.0. It doesn't matter. But I think anyone can fix it and…

### 00:50:00

Sebastian Nagel: including anyone in this committee.

Kevin Hammond: Yeah, I've considered that Sebastian.

Kevin Hammond: I think you'd have to go back to version one and then roll things forward rather than starting with 2.4. So it would be quite a big exercise I suspect.

Alexander Moser: I'm not a constitution expert, but there has been improvements over one to two and rolling that back would not make sense.  But it's up to all the voters who voted on this and will vote on version three to decide that we can just make a list of all the things in the guard rails primarily because we're the TSC what we see wrong and that makes sense and I think that's within our limit and that's very purposeful.  something. So,

Sebastian Nagel: I mean maybe commenting on I think if somebody goes to create another fixed version in quotes right of the constitution I think it would be perfectly fine to just bring it to us and  then basically say yeah okay this do to be all agreed and we can maybe carry it as the TSC and give it some substance and also buy a check mark if we want right but nobody needs to listen for that and nobody needs to ask us for that but it would be quite natural that if somebody on this committee feels like we need to fix it comes up for fixed version I'm all for it in checking that one and just seeing how that is better and basically if this is good then we can endorse

Sebastian Nagel: that means I think it's okay to drag the TSC in it but I think maybe what I'm more not comfortable is in dragging in that we should go now criticizing something which is out there already which has been approved and saying but you did it all completely wrong because we didn't care earlier and honestly I didn't care earlier and again I think both are fine and there is again  with Alexander I guess on this I think it's your argument that there is a committee who actually makes the constitution into constitutional actions

Kevin Hammond: So what I'm really trying to do is to down. because so I've done what I was asked to do. I don't think we can get a conclusive answer.  I is saying the job is just too big to do sensibly. Neil's taken a look. He's trying to use AI. he's not succeeded. so what probably we can take let's take a vote out of band on how to proceed. But what I would probably say is I've reviewed it. ve requested I found some issues.

Kevin Hammond: I'm not confident that the issues are genuine. the issues as far as I can tell there's nothing which has broken anything technically there are not directly not directly.

Sebastian Nagel: That sounds good.

Alexander Moser: You're

Kevin Hammond: One of the issues There it is.

Sebastian Nagel: So in terms of closing it down, I think it makes sense, So we have this on our agenda, We basically started working on this. We didn't vote that we should take it up or at least I was present on that vote. I don't think we need to have a vote for kind of stopping that investigation. we would need to have a vote if any outcome of that investigation would have a consequence of publicizing or saying, " this is wrong and this is why we need to change it." I think that must have a vote on is this the message of the TSC. I think anyone is free to continue that investigation.

Sebastian Nagel: I don't think it makes sense personally. if I think we have a few others believing that but I think we shouldn't be forbidding each other to kind of not investigate, right?

Alexander Moser: No, I think raising the issue and…

Alexander Moser: listing them what N is doing now and what Kevin did is valuable as long as they are concerned as long as they are contained within the TSC room which is mainly the guardrails the legal text above that should be civics committee stuff and the constitution is unconstitutional and the change itself that's a legal question and out of our right but if somebody would look through the guard rails and say there's versioning incorrect and there are these inconsistencies that is extremely

### 00:55:00

Alexander Moser: valuable and I'm super thankful that Neil is looking into this. But we shouldn't criticize those that proposed in doing that. We should just say, "Look, we found these issues.

Alexander Moser: Let's not them down.

Kevin Hammond: So there are some issues in the earlier text.

Kevin Hammond: So one of the things that's happened is some things which should be guardrails have been raised to a higher level and that has changed the interpretation of one of the issues is this thing we've been discussing about when is what is immutability for example. so there are things that reflect on the guardrails. also implicitly some of the things that previously were not guardrails have been promoted I believe. So there have been some accidental changes like that through the construction of this version of constitution. So it's no longer clear exactly what is guardrail and what is preamble.

Kevin Hammond: That separation has been broken to some extent.  But the mostly changes to periods the expression of periods in terms of days rather than weeks. technically every guardrail has been broken by this change because the text has been changed in all the guardrails.

Sebastian Nagel: I don't want to directly respond on it. I hope this is okay. Another thing I happen to kind of learn about the constitution recently is that bigger changes introducing new protocol parameters will require a constitution update,…

Kevin Hammond: Yes.

Sebastian Nagel: introducing these things. So we're already seeing on the horizon that we kind of will have 25 26 or whatever especially in that area which we care about which is the guardrail area when for example we introduce layers parameters and so on and I think we should take the lessons learned from this one when these things are going to be proposed and maybe we hold anyone building these things accountable for doing these updates in the constitution properly …

Kevin Hammond: Absolutely. We can certainly drive that and…

Sebastian Nagel: 

Sebastian Nagel: which includes me For example, on one of the projects

Kevin Hammond: we absolutely need to make sure when we're putting the guardrails that they're properly debated. Sebastian, so we'll need to have discussion over the guard rails and of course within the premise committee over the initial parameter settings, the recommendations. Great. Okay. reminded of time.

Kevin Hammond: so Kanana node update still proceeding still waiting for a 10.7 which will have we hard fork capable when it's promoted for no version 11. Dadeless is likely not to upgrade to 10.6.2 but to wait for 10.7 or 11 or 11 something 10.6

Kevin Hammond: 6.2 is out there and is likely be to be promoted to mainet ready status but it's not going to be whole my final items on the PSC operational budget I think I updated you last week. It's been passed to the insect delivery team. I've had some feedback on that. shared it with the insect steering committee. ISC is going to organize a discussion session to discuss all of the budgets at some point and I'll notify you of when that happens in case you want to join to participate in that. main items that the delivery team had issues with were rewarding small sums of money.

### 01:00:00

Kevin Hammond: So one of the things we're proposing was to provide support for working group members for example and the issue there is not that anyone thinks it's a bad thing to do it's a practical one over the cost and effort involved in doing that. So there might need to be some additional costing put in. It might need to be outsourced for example.  So we'll continue to discuss that with the delivery team. and then we'll also need to look at the review issue. So I took on board Nicholas's comment about the cost. I've increased it in the current budget proposal.

Kevin Hammond: We'll see how that plays out because what we don't want to be doing is to do things back.

Sebastian Nagel: Did I understand this that the budget items which are about kind of offsetting cost of review and after these proposals have been in the budget process the technical reviews. Is this a contentious item? Okay. I mean I've been asking last time about the sequence of things in the budget,…

Kevin Hammond: not particularly contentious. I think we'll have to raise it via intersect. we've already done that. so the delivery team's aware of it. we just need to keep people informed.

Sebastian Nagel: And I think these have been more on the bottom. So I just want to say if there is any problem about these things I'm more than happy to drop them because I believe they're not in the permit and the involvement in the budget process as a TSC I think these things should be reviewed the proposals should be reviewed the delivery should be reviewed…

Sebastian Nagel: but it's not the steering committee which needs to be there we need to steer Cardano and not the development of that flows into Cardano but that yeah yeah…

Kevin Hammond: The reps they need technical advice and…

Kevin Hammond: support. Sebastian …

Sebastian Nagel: 

Sebastian Nagel: then they contract maybe some of these experts on this committee and not the committee it I mean being in our budget it is kind of like we are basically contracting these reviews out right for example Yeah.

Kevin Hammond: so I wasn't proposing that the committee itself should be doing the reviews, Absolutely It'd be like any other group, Sebastian. it could be contracted out.

Sebastian Nagel: And I think my opinion is more than whoever controls the budget process should be making sure that the quality is good on it. And it is not only technical quality but also maybe other feasibility and so on maybe ethical matters or whatever. these things should be tended to. Yes. And I think but our technical expertise is more within helping Kadano stay on the path on parameter security artwork coordination.

Sebastian Nagel: Improvement proposals for example the SIP process is I think much in our alley.

Kevin Hammond: I think it's also important that we use our technical expertise to guide the development of Cardano Sebastian.

Kevin Hammond: So that is the point we are a body of technical knowledge and…

Kevin Hammond: expertise. we are in a position to provide advice to the GREs. the grets are taking decisions, but they absolutely need good advice. Yeah.

Sebastian Nagel: If the other things are not compromised …

Sebastian Nagel: if we have time for that then basically capacity for that maybe yeah it's not the most important thing to me personally as speaking out here I'm not speaking for everyone on the TSC of

Kevin Hammond: I think it's important to the community, Sebastian, that information is given that a fair assessment is provided.

Kevin Hammond: The community it does not have the technical capability that members of this committee have to judge the relative quality of each of the proposals that are put forward.

Sebastian Nagel: Yeah, I agree.

Sebastian Nagel: I'm not saying it's unimportant. I'm saying that there is more important things we could do if the budget time is limited. Right. And I see more higher priorities for us rather in the steering of Cardano in terms of parameters security concerns, manage or kind of release coordination and hardwork coordination and governance proposals as we see the technical matters of those I think are higher on our priority list rather than looking at the work proposed by people in one or…

### 01:05:00

Sebastian Nagel: the other budget proposal because we're not looking at catalyst  proposals and too right so I mean we don't have influence there maybe we happen to have one because through ters steering the budget proposal process there not sure what it's called even but yeah I think it's not unimportant but there's more important things we could

Kevin Hammond: …

Kevin Hammond: what we had determined before was that was to do with the scope of the committee which was that it was focusing primarily on core development issues.

Kevin Hammond: Bastian. so absolutely I would not expect involvement in catalyst proposals and I wouldn't expect invol involvement in any intersect proposals that were not or as this group defines it. But I would expect this group to be capable of providing technical support and advice to the Draps in forming their decisions. Failure to do that is problematic from a governance and…

Kevin Hammond: general perspective.

Nicolas Biri: If I may I think the review process is important.

Nicolas Biri: The question is probably whether it's a TSC remmit or an intersect obligation. To me it sounds more like an obligation on the intersect side.  Basically, if somebody go through Intersect to do a treasury withdrawal, Intersect should do the review and be sure that the quality is here. And it's an intersect obligation in my view at least. The challenge I have with this being part of the TSC is that all of us has another job. we don't have that much bandwidth.  I don't think we can do equally a good job to assess all the proposal even if we have the support of contractors to review the work. So trying to review stuff is nice but we need to deal with the capacity that we have.

Nicolas Biri: I don't think we have the capacity to do this and because it's an intersect obligation I would love to see this budget for revenue being adopted but being adopted not at the TSC level but at the intersect level at least that's my view on this specific topic.

Kevin Hammond: Okay, I can see the point of that. I think the original intention was that insect would do that. but it didn't happen last year, Nicholas. That's

Nicolas Biri: But I mean it's not because that's the same problem then with the constitution in my view. It's just that because something didn't happen somewhere in the community. The TSC feels that they need to be the super arrows that will do this. none of us is a superhero if maybe I'm mistaken but I don't think so.  So I think we should just stick to our job and if we think that something is important and this thing is important we need to raise it to intersect and if the intersect board disagree with it that's okay we have done our job we have raised a concern that's the most we can do we can't do everything and we need to pick our battle and going for the review of every intersect proposal is not my battle I don't have the bandwidth for it we will do a poor job at it and

Nicolas Biri: It's worse than not doing the job.

Kevin Hammond: Yeah, absolutely.

Kevin Hammond: I wouldn't try to person review every intersect proposed. The DREPs had to or they're supposed to and the job was pretty horrible.

Nicolas Biri: the Dre has to vote. the more information we give to them, the easier their task will be, which is why probably Interex should support the re review process. I don't think the TSC should be involved in it or the board should ask us to do this but then we need to have the mean to do this.

Nicolas Biri: I't did the review request come in any case from the board itself.

### 01:10:00

Kevin Hammond: No, it came to us.

Kevin Hammond: So, it came to us via the community. It was something we were asked to do last year, but there is obviously some friction there.

Kevin Hammond: So, I'll happily let me take this. So, I'll take this up with the delivery team and I will put that question to them.

Nicolas Biri: Yeah. Yeah.

Kevin Hammond: But the intersect then needs to do a proper job I think of in terms of providing the support that the GREs need in making a good judgment of…

Kevin Hammond: what are often very technical proposals. Should we Yeah.

Nicolas Biri: And I think it Yeah.

Nicolas Biri: Sorry. No,…

Kevin Hammond: Anything else to say on that?

Nicolas Biri: no. I was actually thinking that if we are bringing it to the intersect board, I think on my view on my side at least  the TSC job is done in just that we think it should be great to have a thorough review process at the end of a project that is backed by intersect and once we do this for me that's enough

Sebastian Nagel: I've also written out my previous point as I in terms of it's more a priorization thing also in the chat now in written format only in  Signal.

Kevin Hammond: Yes, I absolutely absolutely agree that we should be so focusing on the workflow and on ensuring that the work that's being done is of high quality. And this surely is part of the rematch. Yeah, there one point I wanted to raise …

Sebastian Nagel: I think we are out of time for today, right?

Kevin Hammond: which was to say to you that Christian Taylor He stepped down at the end of last week. he was an integral member of the security council.

Kevin Hammond: he established the OSC he transferred all of the repositories IO to intersect several years ago and he's been very active in supporting this group. So I would like to propose that we thank him for his service u and…

Nicolas Biri: What do you think?

Kevin Hammond: acknowledge his contribution to the work that we've been doing. Hopefully he's watching it.

Sebastian Nagel: Thank you,…

Sebastian Nagel: Christian. If you watch this, he stays in open source I read on LinkedIn So, he's going to stick around even I think in the ecosystem just being open source advisor. I think not with intersect but otherwise decentralized governance and community right doesn't need to be this one or the other members based organization or institution and…

Bosko Majdanac: I can send him the link to the recording…

Bosko Majdanac: because it's going to be transparent anyway. Yep. Yeah.

Kevin Hammond: That's great.

Kevin Hammond: Round of applause.

Sebastian Nagel: and tell them it starts at minute two right you need to watch through it

Kevin Hammond: Round of applause for question. Thank you. so I propose to hold the other items back. we can continue to discuss some of them in particular I think will looking at the DREApp conversation paper that Ryan has been preparing will be an interesting topic for next week's discussion.

Bosko Majdanac: My bad.

Kevin Hammond: Thank you very much and talk to you all again very soon.

Alexander Moser: Thank you too.

Nicolas Biri: Thank you.  Bye.

Sebastian Nagel: that way.

leandros bsp: Thank you everyone. Bye.

### Meeting ended after 01:15:59 👋

This editable transcript was computer generated and might contain errors. People can also change the text after it was created.

  
**