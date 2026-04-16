**

## Technical Steering Committee - 2026/04/01 - Transcript

# Attendees

Adam Rusch, Alexander Moser, Bosko Majdanac, Ian Hartwell, Kevin Hammond, leandros bsp, Neil Davies, Ryan (Cerkoryn), Ryan Williams, Terence McCutcheon, Thomas Lindseth

# Transcript

Ryan (Cerkoryn): How's it going?

Terence McCutcheon: Hello.

Terence McCutcheon: Busy day.

Ryan (Cerkoryn): For sure.

leandros bsp: Hello. Pretty well.

Ryan (Cerkoryn): How's it going?

leandros bsp: I can't complain. How are you?

Ryan (Cerkoryn): Doing Finally finished up the end of quarter stuff yesterday. So, getting ready for vacation this weekend. It'll be nice.

leandros bsp: All right. Sweet.

Bosko Majdanac: Hello guys.

Neil Davies: All I

Ryan (Cerkoryn): Hurry, hurry.

Bosko Majdanac: I was wondering whether it was bad connectivity at my place, but that's not usually the case. So I just saw just a few of you and no cameras on and no Kevin and nobody really let me see whether Kevin will join. He I didn't see him saying anything about missing. Mhm.

Neil Davies: No, he's around. let's put away. I've been talking to him, this morning. Okay.

Bosko Majdanac: I really give him I wonder whether Google changes sometimes when you change the time zone whether Google changes the link

Bosko Majdanac: Just give me a second. I will post the link to the call just in case in the chat. I realized The one in the intersect calendar is different. exact. Hi Adam. Hi Thomas. Hi Kevin.

Kevin Hammond: Hi Bos,…

Bosko Majdanac: Text. Yeah.

Kevin Hammond: we were following the link from that was within the insect calendar. Oscar.

Bosko Majdanac: Yeah. I suppose that was something to be checked for.

### 00:05:00

Bosko Majdanac: I thought I saw that Google changed when we change time zone or something like that. It is strange but we should check text. Let's check this offline after the call or anything. So just to make sure that the intersect calendar and TSC are in sync or links. the stage is yours, chair.

Kevin Hammond: Just give me a second to copy the minutes and The agenda and actions has rejoined us as well.

Bosko Majdanac: Sure.

Kevin Hammond: So I'll just pin those for the benefit of anyone So welcome to the technical steering committee meeting of the 1st of April 2026. no April Fool's jokes today I'm pleased to say at least none that I've noticed which is probably a problem. So, we've got a fairly packed agenda. Welcome to guests, Thomas, Adam, and we have four TSC members present, myself, Ryan, Leandro, and Neil. So, any decisions that are taken will have to be ratified outside this meeting. so conventionally what we do is we start with the actions of the previous meeting.

Kevin Hammond: Thomas, you're only here for the first item. Do you want us to take that out of order and then you can leave and then we can go back to the actions from the previous meeting or are you happy with us getting through the agenda items in order?

Thomas Lindseth: I'll hang around the full meeting. So, you do it how however you want.

Kevin Hammond: Then we will go through the actions from previous meeting as usual just to check where we are. And as usual, if anyone has any items to add to the agenda, please raise them in the chat now and we'll attempt to include them in actions from the previous meeting. Bossing.

Bosko Majdanac: Okay, so it was Kevin and Udai to meet with intersection representatives to clarify the division of security budget between security council OC and DSC. So up to you came in and…

Bosko Majdanac: you Did that happen? What's the outcome? So this thing stays on the list,…

Kevin Hammond: That hasn't happened.

Kevin Hammond: Boss, I've not had enough time, I'm afraid. But I was hoping you would be on the call so I could sync up with him, but I will take an action to sync up with him out of the call. Yeah, is going to be a major problem.

Bosko Majdanac: right?

Kevin Hammond: The issue, just for Adam's benefit, there are some items that we're proposing in our budget that relate to the security council. There are items that the OC is proposing and items that Intersect is proposing.

Bosko Majdanac: Excellent.

Kevin Hammond: We just need to make sure that we're covering everything coherently that things go into the right place. So, we might update the TSC budget with additional items, for example, if they're more appropriately covered by ours. but we're not trying to steal anything that the is doing.

Terence McCutcheon: Just for clarity, there is alignment internally with the Cardano tech team that the OSC would not be requesting the bug bounty or the security incident officer since that would be included in the intersect proposal. So I just want to clear that conflict.

Kevin Hammond: But what I'm assuming tax as we continue with the TSC and OC members of the security council jointly overseeing the dispersement of the bug bouting.

Terence McCutcheon: There's supposed to be specific language that the OC and…

Terence McCutcheon: TSC are still involved in the review process and any program changes. It's just intersect as the budget holder.

Kevin Hammond: Great. Thank you.

Bosko Majdanac: Next one. Kevin and Neil to collaborate on the revised proposal for professional technical reviews that includes risk registers and higher due diligence standards.

Kevin Hammond: H hasn't happened yet. Bosco, I would say that's probably unless there's something which needs to be reflected in the budget proposal which we can discuss,…

Kevin Hammond: I think we can probably say that's less urgent.

Bosko Majdanac: Okay, agreed.

Bosko Majdanac: The next one on the Android update the 2030 KPI document with the latest feedback from the product committee and…

Bosko Majdanac: shared the communitydriven initiatives memo. So that's on there.

leandros bsp: Yes. not too much to say about it.

### 00:10:00

leandros bsp: I had a call this week with the researchers on IoG about getting a better measurement of the chain quality. Basically, we landed back on the chain density, but they helped me break down the chain density into the three components that would dictate it. And they had one interesting note, that would be to change the measurement window instead of a per epoch to a genesis range window. So, that would give us a better indicator of security against long range attacks. it's a nitpick.

leandros bsp: It's not really that critical but I'm bringing it forward for discussion if this makes sense The problem with the genesis window is that we don't have a precise start point and end point to take the measurement in a consistent so we'd have to redesign a bit the way we measure it.

Kevin Hammond: Do you want to discuss that later in this meeting Leandroth offline which is Okay.

leandros bsp: Yes, definitely. after the call I meeting with the product committee again about this thing. So at any point we have time to talk about it I'll be here and grateful. Thank you.

Kevin Hammond: So, let's try to include some time in the agenda for that.

Bosko Majdanac: Okay, thanks. next one. Text to share the confirmed time slots for the upcoming election X spaces and virtual hub events in the chat and Slack. So, did that happen? Text. I suppose it did. I wasn't here last week, so You feel thanks.

Kevin Hammond: Let's assume that tax has either done that or…

Bosko Majdanac: Okay. okay.

Kevin Hammond: will do that. but Okay.

Bosko Majdanac: I can ask in a different way. Are you all aware of the times and…

Neil Davies: Yes, it was posted in the Slack channel.

Bosko Majdanac: time slots when the XACE and virtual hub will happen? Neil one Perfect. Done. Kevin reviewed the notes 10.7 pre-release note and provide final TSC approval for the release. So there are other news after that. So yeah.

Kevin Hammond: Immediately after the last week's meeting,

Bosko Majdanac: Okay, and the last two are on me and I didn't do a thing on them due to other stuff traveling and to Argentina and then these other picking up more priority items this week. So I will handle this.

Bosko Majdanac: So it was investigate the physibility of an RSS feed for TSC updates for better communication and then again to coordinate dual pool to schedule the private linear layers risk management the drive with Sebastian if there is still an interest for that. so those two keep lingering in the background but they will be handled.

Kevin Hammond: So I think we definitely want to progress both those bosses.

Bosko Majdanac: That's for Yep.

Kevin Hammond: The technical communication for Adam's benefit is something that we have been looking to improve conscious of the gap there. and we need to try to improve it. We had asked in the budget for a communications officer the …

Kevin Hammond: but that has been lifted to an intersect level and…

Bosko Majdanac: Shut up.

Kevin Hammond: the doodle poll I think we want to discuss the risk of layoffs. The layoffs meeting is actually happening right now. So it conflicts with this meeting. So unfortunately Sebastian can't attend but we absolutely ought to schedule a session.

Bosko Majdanac: Feel free of course maybe it's about the approach to this.

Kevin Hammond: If you don't have time I will just kick off some doodle polling myself. Bos I can do it.

Bosko Majdanac: So if you are the familiar enough with it by all means jump in.

Kevin Hammond: We've probably spent more time discussing it than it will take. Great. So,…

Bosko Majdanac: Yeah I agree. I agree.

Bosko Majdanac: Okay, that's the full list of the action items. there's nothing more on it. So I suppose we can go with the agenda.

Kevin Hammond: first item on the agenda, CC Mensai's timing. So, Thomas Lindsef is here. I think Adam's probably going to be interested in this discussion. so to Thomas given that we're not expecting to produce the Pluto's cost model update on mainnet in the near term there might be an opening to progress the CC minize reduction please go ahead.

### 00:15:00

Thomas Lindseth: So, following the ISC call on Monday, myself, Bosco, Kevin, Ian, and Larissa was in a quick call to discuss exactly that. whether or not it's a sensible time to submit the min size parameter change. I have been talking with civics members and they have already voted that they would like to see this governance action. they did not vote on timing. So the feedback from civics is that if there's time they are supportive of it.

Thomas Lindseth: So the question remains is it so by submitting CC MS size governance action tomorrow which means in this epoch will that delay the Bluetooth cost model anything at all? If not, the recommendation from Civics is to go ahead with CC Min size tomorrow.

Kevin Hammond: Neil, so when we discussed the Plutous cost model update before you were proposing to give the community time to provide us with feedback on any impact. So we've had a bit of feedback from gathered by Alex. I've raised the issue with PI learning and…

Kevin Hammond: not had any response. Community has been very quiet about this.

Neil Davies: I have a concern…

Neil Davies: because of the change of the nature of the parameters because they've gone up for pre-existing activities there is this technical feas possibility that transactions will not have the appropriate ader paying for them as they cross they won't declare themselves correctly when they create new transactions. So my concern as to say is crossing the actual epoch boundary when this is actually done transactions might fail because they're badly costed and people who have been lazy in doing their pricing and don't do their pricing each time but take some optimization may get caught out.

Neil Davies: I just want to make sure that were they to get caught out, we have done our darn best to tell them they should have looked. Okay, that's my problem. how on earth this is again down to the communication. Adam There were two.

Adam Rusch: Yeah, thank you. So that's in regards to the Plutous cost model. so' I guess what would be the scenario where they would not be paying enough ADA for the transaction to go through? would it be because they have not updated their tools to take it into account or because they aren't

Neil Davies: So the transition across the boundary right is one of timing. You create it in one and you use it in another.

Neil Davies: The tools problem is that we know there are people who are lazy who pick numbers and they don't change those numbers they don't actually go and evaluate the cost of processing the transaction they create a number and then they just reuse that number when they build the transaction. So and some people are very lazy and just set the numbers at full anyway. including various people inside Iowa it turns out once so it turns out that basic so I'm just saying it's that and that's the circumstance that make sense basically they're using old information they don't notice the information's changed normally normally…

Adam Rusch: Mhm. …

Neil Davies: if the costs were being reduced right for these and they have to use this particular there's two or three operations whose cost has gone up right

Neil Davies: Normally up to this point actually either they're new parameters or the costs have gone down. So this is the first time you've ever had costs going up. That's my problem.

Adam Rusch: yeah, I guess how much do we think that communicating with people will change this? I mean, if they aren't listening to us now, will additional time talking get it until they actually hit reality.

### 00:20:00

Neil Davies: The suggestion was one month we blitz them, told them it was Took their opportunity for them to object for some to raise objections, right?

Neil Davies: The assumption would be that having told everybody there would be no objections or…

Neil Davies: there'd be spirious ones and then we engage in it. Then when those people get caught out, we can say, "Not us we did our best." You know, you weren't listening, right? Yeah.

Adam Rusch: But yeah,…

Adam Rusch: but we already publish this and start the socialization process?

Kevin Hammond: We've not had a lot of response back on this.

Neil Davies: But only by a couple of weeks that as far as I'm concerned,…

Neil Davies: we're two weeks into that month, right? Yeah.

Kevin Hammond: Yeah. what…

Adam Rusch: Okay. I …

Kevin Hammond: what could happen here, is we could allow the CC miniz reduction to overtake the Pluto's parameter upgrade that will give a bit more time for the socialization. and…

Kevin Hammond: then depending on the outcome of the CCM size

Neil Davies: I would suggest once the CC bin size is either locked in or…

Neil Davies: completed depending on how depends on you can tell when it's about to happen if it's going to happen right we can then assume it's happening and then start the second one off we don't need to wait for it to finish entirely

Adam Rusch: maybe I think that the Plutous cost model is probably more likely to pass than the CC minize because the CC minize has a higher threshold, so, I guess my fear would be the danger of if it does fail, you're going to have to build it as a dependency on the previous one, whichever one you put first. do these I know that CC minize is not necessary before the hard fork,…

Adam Rusch: but I was under the impression that L cost model is preferred to have passed before the hard fork. Is it preferred or a necessity before the hard fork?

Kevin Hammond: It's preferred Adam.

Kevin Hammond: It's not a necessity. But if it's not passed before the hard fork, the new perimeters won't be available.

Adam Rusch: Right. Yeah. Yeah. Yeah.

Adam Rusch: That was I guess my understanding.

Kevin Hammond: We'll come back to the timing of the hard fork later,…

Kevin Hammond: but based on what Bosow was estimating yesterday, it could be late June to July before the hard fork is enacted.

Adam Rusch: I guess one question would be…

Adam Rusch: what Neil I guess I see what you're saying about giving everybody a month. If we waited for another couple weeks, do you think that would be sufficient to then put out the So yeah. Yes.

Neil Davies: We're already,…

Neil Davies: as far as I'm concerned, we're already two weeks into the months. So the whole point was the idea was give them a finite but non-trivial a period of time to complain advertise it as best as we can right and then when the in because somebody's going to be upset by it right it's almost certain that somebody will be upset by it and we have at least said we did our best right and…

Adam Rusch: Mhm. Yeah.

Neil Davies: this is and then they'll argue you don't communicate with us to the RSS feed which says here's where everything we say you got to

Neil Davies: that type of simple thing would have been our in the long term would be our on shield for the brown stuff on the fan.

Kevin Hammond: But I think we're done. So the question is simply do we allow the CCM size to overtake given that we've got at least another

Neil Davies: I see no problem in this because the in size I mean if you work out if we actually sequentialize these if we did the CC bin size tomorrow I can never do the arithmetic in my head when would we be able to submit with absolute certainty the next one…

Adam Rusch: I mean,…

Neil Davies: because we got to be

Adam Rusch: honestly, I think you would have to count on 60 bucks because I think that the CC min size may become contentious. there are a number of community members…

Neil Davies: What about so I'm just trying to work out six weeks from now is when right so…

Adam Rusch: who when UT submitted this they started talking about the possibility of this will lead inevitably to the CC collapsing down to five members instead of seven because some of them had the feeling that and so these are all not technical factors right? Yeah. Yeah.

Kevin Hammond: MidMay, June,…

Neil Davies: if we enacted so that basically miday right six weeks from midmay is end of June Bosow's telling me the hard fork would

Neil Davies: 

Kevin Hammond: end of June, beginning of July.

Bosko Majdanac: You can see yeah Ryan is sharing the pentat.

Adam Rusch: And I guess I could kind of feel more so here's my thinking. one is I understand what you're saying about the sequentialization, I will give you from a socialization perspective why I think it's better to do the mincc size the CC men size second instead of first. I think the Plutous cost model if appropriately handled will be much less controversial with the community. I think you're right. I think there's going to be some people…

### 00:25:00

Adam Rusch: who complain about it when few people have some stuff break because people won't be paying attention. They won't do it right and then we'll just tell them we told you so. Right. Yeah.

Neil Davies: Okay,…

Neil Davies: Adam, I'm happy with either way round,…

Adam Rusch: 

Adam Rusch: Yeah. Yeah.

Neil Davies: right? Okay.

Adam Rusch: 

Adam Rusch: Yeah. Yeah. arms. Okay,…

Neil Davies: So, the key point was we were all ready to do this about four or five weeks ago. and then the cost model got changed on us by the polluters team and the numbers right it's not so basically we prepped it all right everything was simple and…

Adam Rusch: I see. Mhm. Thank you.

Neil Davies: safe and then along came this s*** they've up the numbers we can't just do it like we'd normally do right we have to be a bit more right so I'm more than happy…

Adam Rusch: Yeah. Yeah, That's helpful context.

Neil Davies: if we shout about it that in two weeks time and we can send one out there we

Neil Davies: I would be very happy that we put the Plutous one on thing on chain, right? And…

Adam Rusch: Mhm. Yep.

Neil Davies: basically because they still have to be linked, right? …

Adam Rusch: Yep.

Neil Davies: then you put the min size you could start you could make the assumption that it was going to succeed…

Neil Davies: then put the size on min size a couple of weeks later and then the debacle of whatever happens with msize will happen…

Adam Rusch: And then length in size after that.

Adam Rusch: Yeah. Yeah.

Neil Davies: because that's going to be the gating item before you can put the hard fork in. That's fine.

Adam Rusch: I'm good with that. Yeah. And I think I'm comfortable with this sort of saying let's give this two more weeks of socialization. I think that makes a lot of sense. I appreciate the context you guys are giving me. yeah, this is, I don't know, promise you, tell me what you think about the CC men size. I think I mean, I've been frustrated because I've been wanting to get that updated, but I also have been mindful of of the fact that you guys are all working on these processes that are all interlin in many ways.

Adam Rusch: And so that's why I kind of wanted to come here to get the context of this and make sure I knew what was going on. So, yeah. Thomas, what…

Thomas Lindseth: Yeah. Yeah.

Adam Rusch: what do you think?

Thomas Lindseth: from my perspective. I mean,…

Thomas Lindseth: I think I already said it, as long as we don't interfere with the Pluto cost model in any way, I'll endorse submitting the committee min size right away. if it affects Pluto's cost model in any way, shape, or form, I would always put Pluto's cost model ahead of it.

Adam Rusch: Yeah. Hey.

Kevin Hammond: So let's continue as we were…

Kevin Hammond: we're aiming we've started the countdown for submitting the police cost model update Neil we've got another two weeks to run try and…

Adam Rusch: Yeah. Mhm. Okay.

Kevin Hammond: do a bit more communication on that and trying to make sure people aren't surprised. so Adam just so you're aware so the rest of the TSC is aware the changes that Neil's describing to the primitives they would take effect before the hard fork so they would take effect immediately the changes to enable the new primitives would then take effect at the hard fork okay so we don't want people to be caught out by there's this cross mod update going in

Kevin Hammond: It's not going to have any effect until the hard fork. We need to make it very clear. Look guys, it's going to have an effect on there will be even having submitted the update,…

Adam Rusch: Right. Yep. Absolutely. Yeah.

Kevin Hammond: there's still a chance for people to do testing because until the proposal is ratified, we'll still be working with the old cost model. So we will be giving people a lot of time to be aware of the change and…

Adam Rusch: Mhm. Yeah.

Kevin Hammond: to make any changes to their DAPs.

Adam Rusch: And if we're giving this two more weeks, that means we can submit it during epoch 625.

Neil Davies: …

Neil Davies: so the main purpose for not doing it immediately after that number change is we've never had a figure go up before, So this is a risk that we knew it was a hazard but it became a risk to people that we wanted to literally make sure they had every possible notice to object

Neil Davies: if we don't get any objections then I'm sorry you should have looked inside the filing cabinet when we did it's really about not we have been shouted at so many times that we don't communicate with a

### 00:30:00

Neil Davies: We're just trying to make sure they get a chance. Okay. I'm happy with that. I'm more than happy. I mean, I mean, I am completely frustrated how slowly these parameter changes we can make, and I was miffed when, we'd spent something like 3 months getting ready for this parameter change and then at the last minute parameters went up which was not what we expected. Okay. which is…

Adam Rusch: Sounds good to me.

Kevin Hammond: Yeah. No. Yeah. Okay. So, I think we probably spent enough time discussing that item. Should we move on?

Bosko Majdanac: Can you just for the record for the notes what is the decision? So which one goes first?

Kevin Hammond: There's no change to the previous decision box here.

Bosko Majdanac: So cost model size.

Neil Davies: which is that the Pluto's cost model goes first and the committee means size we could suggest because we're not making follows two epochs later.

Neil Davies: Okay. Yeah.

Kevin Hammond: Yeah, we can ratify that at the next meeting or…

Bosko Majdanac: Okay. Yeah.

Kevin Hammond: out of that. Okay, so moving ahead. TSC budget proposal. I've shared a link in the chat. guests may not have access to that. I'm not sure. there's restricted access. Hi. Hi, Alex. you've joined us. Boss, could you maybe open and share that?

Bosko Majdanac: to share the document.

Kevin Hammond: Yeah. no, just share it with me so people can see.

Bosko Majdanac: Just give me a sec. on a Google doc, I think it's here in this one.

Kevin Hammond: Yes, you have a screen moment. Could you Yes.

Bosko Majdanac: Do you want me to open it or…

Kevin Hammond: 

Kevin Hammond: Just So we can just show people…

Bosko Majdanac: or just schedule? Okay. Okay.

Kevin Hammond: where we are in the proposal so state players we've pres presented this to the ISC. and to intersect staff. we included the comments we took out of the comments that were made last time about the value of various items. the intersect has changed the template. so I spent a fun morning this week taking all the stuff that we had previously written and trimming it down to fit the new size limits which has hopefully been done effectively.

Kevin Hammond: So if you'd like to just scroll through it Bosco just scroll down. Yeah. So this is essentially just keep scrolling. So So thing I want to highlight is we have restructured as I said last week to four work packages from five. the budget I've included the feedback from UDI about the technical work packages about the need for technical review in that but when I was doing revising the proposal this week I took the liberty of increasing the support for security council members so I took the liberty of aligning it with the

Kevin Hammond: support for the ZIP editors and that increases the total budget slightly. It increases it by about $20,000 over the course of the year. so the total budget we will be requesting comes in at slightly less than $400,000 to support all the activities that we were discussing. and WQ1 as before includes a program of 10 technical workshops where the majority are online based on feedback from this group. WP2 is the technical engagement in the security council. This is support for community members if they need to be involved in security council.

Kevin Hammond: WP3 is funding the parameter committee sit editors and hard fork working group similarly. So again we're not necessarily expecting all of that support to be taken up but the funding is available there to help increase the engagement to reward people for the time they're spending on those activities. And the final finally workb is funding the establishment of a pilot independent technical review program. So the goal would be to set up the program to obtain sufficient technical experts to put together the pool of technical experts in 2026 and to pilot the provision of technical reviews in the 2027 budget u proposal.

### 00:35:00

Kevin Hammond: sorry, the 2077 budget round and that is a fairly minimal spend. We had a discussion last week about whether the spend was enough, Neil. I haven't made any changes to the cost per review. now would be the time to make a proposal to do that. So, I'm assuming that we're awarding at $150 per review, which is aligned with the funding that you would receive from research councils. but is not a significant return for the effort that people might need to put in.

Bosko Majdanac: Kevin, do you want me to scroll down more on other aspects or…

Kevin Hammond: only if people want to. so everyone in the tax steering committee has had the chance to look at this hopefully.

Bosko Majdanac: I just share the link again in the chat just in case.

Kevin Hammond: So, happy to take any further comments or feedback on that. but otherwise I would think we're reaching a point where we are fairly comfortable with the proposal. you've seen it we've taken feedback from Intersect staff. we've adjusted the proposal in line back we've received.

Adam Rusch: really happy with the proposal. I'm really pleased with what you guys are doing and the way that you're approaching working with Intersect the community to make this happen and with our vendors and so yeah I said I'm just really happy with the proposal and definitely something that u we're going to talk about more I know with the board as we move forward.

Adam Rusch: So, I think that we're supposed to talk about it next week to formally improve everything.

Kevin Hammond: Great. Thanks.

Kevin Hammond: So, we'll have a discussion about whether we're correctly rewarding the support for the technical reviews, Adam. So, that might go up slightly. We're obviously cognizant of the community's concern about funding, but this is a relatively small level of funding and it will help keep people technically involved in the ecosystem. So, it will help continue to provide the technical knowledge and expertise that we need to properly function within Cardano. So, we think it's a good expenditure of funds

Adam Rusch: Yeah, I agree. It's always great to get more collaborators in there. So that's fantastic.

Kevin Hammond: Thank you. Any comments from anyone else? Leandros, Alex, Neil, Ryan.

Neil Davies: I just saying thank you Kevin for putting the evidence. Yeah.

Ryan (Cerkoryn): I'm just recreating my diagram because I used the wrong document. So, ignore the one I posted.

Kevin Hammond: And thank you, Claude, for helping.

Bosko Majdanac: You follow us?

Kevin Hammond: So, let's move on to the next item. Van Ross and Hard Fork. so, there was a meeting of the hardworking group yesterday followed by the regular release meeting which we've determined is definitely the wrong way so state state play is bossio base what we're expecting so we've released node 10.7.0 we released that late last week based on the benchmarking review the team has discovered that there are some serious performance issues with node version 10.7.0.

Kevin Hammond: So the bad news are that 10.7.0 is not mainet ready and we are not going to recommend that it become mainet ready. there also are one or two issues within the consensus side that to they detected some rare conditions in which the consensus could fail. there could be a failure within the consensus not a security issue but a node failure an exception could be triggered which is undesirable. So the proposal is to put together a version 10.7.1 to fix the attention from moving 10.7.0 to mainet to creating a 10.7.1 version that fixes these issues.

### 00:40:00

Kevin Hammond: and the team believes that it has found the smoking gun for the performance issues, but the person who's respons would be responsible for fixing those was away yesterday. So, that needs to be confirmed and checked. So, all going the issue has been found will be fixed and we will be moving to a 10.7.1. Neil

Neil Davies: Is this bug in the consensus that causes the node to fail? Is it a random failure due to environmental conditions or could it be triggered by the blockchain?

Neil Davies: I.e. Are we looking at a potential cascading failure where everything all the nodes fail at the same time or not? Okay, fine. Thank you.

Kevin Hammond: No, my understanding from the team it's more of an environmental thing.

Kevin Hammond: So if it's certain conditions that specific nodes could Yeah,…

Neil Davies: Okay. I mean I was just correlated failures just that I just heard my alarm bell went off. That's Fun.

Kevin Hammond: we'll obviously check that Neil, but it's not been flagged as an issue, but it's something that the team wants to so then focus shifting to 107.1.1 again what we would expect is to have a release within our one to two weeks. we are still expecting there to be further changes before we get a hard fork ready version of the node and node version 11.

Kevin Hammond: So we would still from where we are be expecting a 1072 and we'd be expecting 1072 to become the node that became 11 x. So we're still some way out of having that version of the node. So that's the development status. Bosco, we've put together a risk register.

Kevin Hammond: Again, I've linked that from the chat. Maybe you'd like to sell us more AI stuff,…

Bosko Majdanac: Yes,…

Bosko Majdanac: just give me a sec. It's here. sharing. they want to give me some more AI stuff. Okay, here it is.

Kevin Hammond: not give it to us.

Bosko Majdanac: Yeah.

Bosko Majdanac: Okay, it's kind of premium.

Kevin Hammond: Bosco has kindly put together a risk register for the hard fork based on the one we produced for Plymouth.

Kevin Hammond: And what we've done is I went through this yesterday. I've added in some additional risks and I've classified the risks based on the current status as of yesterday. So what we're planning to do is to use this as a readiness tracking tool and obviously given the state we're in there are some clear risks at the moment the things colored red in particular community not being ready for the hard fork clearly it's not ready at this point in time but it's highlighting things we have to do to mitigate the risk multiple iterations needed to get to node

Kevin Hammond: version 11.x from node 10.7.0 where we're seeing that happening that obviously is a risk to the timing of the hard fork. So these are the critical issues. we've included some mitigations and notes there and we've started to identify which teams are responsible and Bosa you want to identify the individuals who would be the contact points for that. so the other risks unacceptable issues found during testing and require remediation. we have possibly found that in the form of the consensus issue but it is being It might still be a risk in future. So that's a risk which could rise or fall in the table. the performance issues need extensive remediation.

Kevin Hammond: We've had performance issues. so that has been an issue. We were rating this risk higher before the release meeting, having been to the release meeting and discovered that there may be remediations. We've lowered the current threat level of this particular risk, but it's one we have to track. There could still be worse performance issues. And then there are other things that we need to address to do with technical support around the hard fork that needs to be raised with the developer team. We need to make sure we've got people on call text. We need the security council to be aware of that. we need the instant manager to be available around failure to hard fork in a timely manner. This is just a general risk.

### 00:45:00

Kevin Hammond: So not really within control. If the community decides not to hard fork so that it's not enacted by July then that's what they choose but then we might have to resubmit the proposal. And the final risk is a generic one we've carried over. it's not a particularly serious risk but it's a possible risk which is the node fails to enact the hard fork. and the way we are mitigating that risk is of course to try and test the node on multiple test nets to go through the usual process of forking preview prepro etc ahead of time and to go through extensive testing within the team.

Kevin Hammond: So that's just summary of the risk register as we have it at the moment. there may be additional risk that we need to include in that register.

Kevin Hammond: Thank you for putting that together, Bos. Does anyone have any questions about that or anything I've said I think these are the…

Bosko Majdanac: or in…

Bosko Majdanac: if I may ask do you see any other thing that is likely to go wrong with Harford that we didn't measure There.

Kevin Hammond: if you're asking me I thought about this yesterday and these were the main risks that I saw. but I'd appreciate feedback from the rest of the TSC, of course, because other people may be aware of other risks or they may have particular concerns that I haven't addressed in this To be fair,…

Bosko Majdanac: Yes. Exactly.

Bosko Majdanac: I suppose we can move on. there is 13 minutes left and we seems to skip Ryan's Ryan Wy consistently with a great start that he keeps being left for the second part of the call and we rarely have time. I'm just saying.

Kevin Hammond: he wasn't here last week. Bos Right,…

Bosko Majdanac: Okay, I wasn't as up. So, yeah, good point. I suppose we can switch to the agenda again.

Kevin Hammond: Ryan, hand the floor over to you.

Bosko Majdanac: I think yeah, so we did discuss cost model, right? So, we covered that one specifically already.

Bosko Majdanac: So from sip farm to hard for this that's what

Kevin Hammond: Unless there's something else you want to raise, Alex, but I think we've covered everything. Ryan, over to see

Ryan (Cerkoryn): Gosh, I was talking on mute this whole time. yeah, I could talk about SIP 179, but since Thomas is here and this is his SIP, if he wants to give it a quick summary, that's cool, too, since he happens to be here. or if not, I could go. It's fine by me since it's a surprised face.

Kevin Hammond: When you

Thomas Lindseth: No, I can talk a little bit about it. So, yeah, I don't know if anything at all SIP 179 has been brought up in TSC.

Ryan (Cerkoryn): I think the primary thing that the TSC is interested in is using it to select zip short list for the Dixra hard fork.

Thomas Lindseth: Let me share my screen then and I can show you exactly what to expect. let's see. So Cites is right now the only platform that covers CI 179. it lives here under surveys and polls and fairly easy. You connect your wallet and sorry I'm on the wrong user. Okay, I'll just tell You connect your wallet. You can then create something that looks like this. oops, that was the wrong one. need to click here. So then you can add questions as many as you want.

Thomas Lindseth: There's multiple types of questions from single multi-choice, numeric range, and open text fields. yeah, and then you submit a transaction containing the metadata for that survey. you send that to yourself. once the tool registers it which takes about a minute you can then start voting and answering those questions by submitting a transaction from yourself to yourself containing the response metadata. as I said there is one live currently on mainet.

### 00:50:00

Thomas Lindseth: this one it's created by me and I'm the only one who's answered it so yeah, you can see the responses. You can see what wallet it had, the stake, the date, and the transaction. And yeah, you can fill in Ryan. I wasn't prepared for this, so you can Yeah,…

Ryan (Cerkoryn): Yeah, no worries at all.

Ryan (Cerkoryn): Sorry to call you out but yeah so I have been working simultaneously on implementing it some of the governance tools.

Thomas Lindseth: no worries.

Ryan (Cerkoryn): So the SIP does not require being embedded in a governance action but it can be optionally linked to one through an anchored. So I was tweaking with the source governance tools which is tools cggov and the cf voting tool and I have opened a poll request on each of them to integrate recognizing when one of these surveys is linked inside a governance action.

Ryan (Cerkoryn): So way that would look is you could submit a governance action probably an info action but doesn't necessarily have to be and it would populate the survey based off that the anchor to the survey and when a DREP or a CC member or SPO goes to vote on the governance action it will give them the survey options as well and the response is recorded in the voting response to that governance action. so in theory, what that could look like for the Dixra short lists list is we could have an info action that says some generic statement of this is the Dixra short list and then you'd vote yes, no, or abstain on it, but then it have a survey of all the different SIPs we'd like to select. and then you could survey people on which SIPs they would like to have included that way. So the poll requests for those three tools I mentioned are submitted is actually merged into CGV.

Ryan (Cerkoryn): So I think you could technically view if there were governance actions with surveys on them on mainet you could view it on CGV right now. ideally there will be some of these on preview so that we can kind of battle test them against each other because we want to make sure that the tools read and write the metadata the same way. Otherwise you're going to get disagreement between tools and that would not be a good thing. but it should be mostly other than being battle tested, I think the SIP is pretty close to being merged and ready for stuff. So, we start thinking about how we want to include SIPs to be voted on. so one of the ideas I'd floated if we want to do a waiting mechanism, they're like this zip will take a ton of work, so it needs to be weighted heavier. This SIP is, less work, so it could be weighted less. And then we could select a total amount of weight that we can include in in one hard fork.

Ryan (Cerkoryn): So we're going to do all the SIPS, it would be awesome, but realistically we can't do that. so we have to pick and choose. And this way it gives us a way to pull the DREPs and…

Ryan (Cerkoryn): the community at large on which ships they would want to see in a hard fork.

Kevin Hammond: Yeah. …

Kevin Hammond: so the goal here is to start to get community input into the, development program and into the hard fork, Adam. And obviously for that to have maximum value, it really needs to be kicked off pretty soon, Ryan. So, we really ought to start polling the community as people are starting to think about preparing budget proposals…

Kevin Hammond: because this will then be information that could be used to support specific budget proposals.

Ryan (Cerkoryn): Agreed. That's an excellent question.

Kevin Hammond: What would be the process for determining the sets? who gatekeeps the sets? Right.

Ryan (Cerkoryn): I think somehow we'd have to determine which SIPs could be in scope and then get a big list of them. all the ones that could be and that's I guess gatekeeping as you would say it but has to be done at some level I guess. So putting together that list I think myself and I think probably a couple other people have been talking about it so I could probably spearhead that I do have actually a link to some of them. I'll have to find that link later but trying to just collect community input.

Ryan (Cerkoryn): I don't know if there's a better way to just be like, "Hey, are we forgetting any SIPs?" Or if we just go through the SIP process and look at all the ones that have been done in the past year or two. I'm not really sure on that. I'm open to ideas,…

Kevin Hammond: So once it's on chain,…

### 00:55:00

Kevin Hammond: you can't change it. You can't change,…

Ryan (Cerkoryn): right? For sure.

Kevin Hammond: So it's important to get the list right or maximal, not to accidentally exclude something from that list. Yeah. Yes.

Ryan (Cerkoryn): Yeah. Yeah, I'll have to brainstorm that when I come up with the solution of how we can build out the initial list to begin with because now that's becoming the bottleneck, right?

Kevin Hammond: So what I probably suggest is syncing up with Ryan Williams who's one of the SIP editors and Ryan will probably have a good idea about which things are forkable or require a hard fork which don't and then I said I would be maximal so don't try to filter the list let people select all of the possibilities Please.

Ryan (Cerkoryn): access. Sounds good.

Kevin Hammond: So, I'm happy to commit a bit of time to looking through the list with you. just ping me and…

Bosko Majdanac: Another ship again. Ryan.

Kevin Hammond: we'll sort out some time. Great. got a couple of other items.

Ryan (Cerkoryn): Was this me again?

Kevin Hammond: Yeah, governance actions. Do you want So you can either cover that or we can get the Andros to tell us about the KPI changes.

Ryan (Cerkoryn): I'm fine either way.

leandros bsp: Yeah. Hello.

leandros bsp: It's nothing major. I haven't gotten any feedback from the product committee about members. I assume that they are going to give me some feedback at the call later in five minutes the only real change that the researchers of IOG flag and it makes sense is measuring the chain density during genesis windows and not during epochs. And as far as the implementation for that goes, it becomes a bit tricky for the business logic behind this because then it would have to be a rolling window and then we aggravate the lowest peak during any time frames quarter or a year. but it has the advantage that gives us a more accurate measurement of the chain security to long range attacks.

leandros bsp: That's the only concrete Yeah. Sorry for jumping in. I only have about 3 minutes.

leandros bsp: I want to hear everyone's opinion about this. Makes sense. It's overkill. No. Mhm.

Kevin Hammond: I think in increasing security against long range attacks is a good thing to do.

Kevin Hammond: The Android so that I would be in favor of very happy to come in on your call with product committee…

Kevin Hammond: if you pass on the details.

leandros bsp: Yes, I'll send it right over.

Kevin Hammond: And if you can then share the final document with us so we can look at the KPIs they're being proposed. Just do that in the Slack channel. That will be great. So to finish off, Ryan, so we reviewed your proposal on the NCL budget action some time ago that you gave us some feedback on that. events in the community indicate that this is a good thing to progress.

Kevin Hammond: Why don't we have a proper discussion about it next week rather than trying to discuss it in a minute or two this week? But were there any particular questions that you had about that?

Ryan (Cerkoryn): No, that sounds good.

Ryan (Cerkoryn): There's actually just technical feasibility of how to do the state tracking is the only complicated part and we actually just had some movement on the GitHub page this morning. So giving it a week to work on that I think is probably good idea.

Kevin Hammond: So, we've got a point of the sip here. if you can any ask from our perspective then TSC members hopefully will get a chance during the Easter break if people have an Easter break to look at it. Yes.

Ryan (Cerkoryn): Yeah, I can quickly summarize the issue.

Ryan (Cerkoryn): So the idea is to do a net change limit as a protocol parameter that's enforced by the ledger which on its surface sounds really simple. The complicated part is the ledger has to keep track of a history of two things. It has to keep the track of because it's a percentage of revenue.

Ryan (Cerkoryn): So, it has to keep track of revenue and it has to keep track of how much has already with been withdrawn. And so, the way I have it written now is to keep state for a whole 73 epics which is one year of revenue and amount withdrawn for every epic in that point. which is a lot of state for a supposedly stateless ledger to have to track. so the feasibility of right

### 01:00:00

Kevin Hammond: Yes. …

Kevin Hammond: it's not a huge amount of state potentially, because you only have to record the totals. You don't have to record all the individual entries that give rise totals. So you should only be recording something like 2 * 73 times whatever the size is of the values that are representing that information. So that should be something like a kilobyte of data.

Ryan (Cerkoryn): Yeah, I think it should be a very small amount of data. It's just that that's been the primary push back in the SIP discussion page. And then also the other big one is how to enforce it, whether it should be ledger enforced or guardrail script enforced which has gone back a couple different times on which the better way to enforce it is. Also, should it be enforced at proposal enactment or…

Ryan (Cerkoryn): at proposal submission is another question because I don't think a guardrail script can do it at enactment. It can only do it at submission,…

Kevin Hammond: If you want it to be effective,…

Kevin Hammond: it has to be at enactment, doesn't it? Right. Yeah,…

Ryan (Cerkoryn): right? Which as of this morning, I think now we're leaning away from using the guardrail script and towards the ledger and enactment as the enforcement mechanism.

Kevin Hammond: because otherwise what can happen is so you can get five or 10 proposals submitted at the same time none of which breaches individually the net change limit…

Kevin Hammond: but when collectively would breach the limit. So I think you have to enforce it at enactment time. That means it would have to be done in the ledger rather than in the guardrail script.

Ryan (Cerkoryn): Yep. Yeah,…

Ryan (Cerkoryn): I would agree with that.

Kevin Hammond: I mean you could put a looser condition in the guardrail script which was this action by itself would not breach the current NCL. But then you'd have to extract information and expose information from the ledger to the guardrail script and that is not being exposed. So the ledger is not passing on information about the last 73 epochs.

Ryan (Cerkoryn): Yeah, there was also discussion about whether epoch is the correct mechanism to have it, right? Because in theory, you could just have it do one for the whole year, but then you'd be locked into a yearly cycle by the ledger. Or you could do quarters or…

Ryan (Cerkoryn): you could do months.

Ryan (Cerkoryn): 73 is just because we use epics anyways and that's how many epics are in a year. It's seemingly arbitrary, but it could be less state to track in theory if you use a bigger chunks. It would just be a less resolution on your window.

Kevin Hammond: It would be more complicated for the ledger I think to deal with an annual change than with a number of epochs.

Kevin Hammond: the number of epox could be counted automatically.

Ryan (Cerkoryn): I'm also inclined towards epochs.

Kevin Hammond: And then what you're assuming is some rolling window,…

Ryan (Cerkoryn): I think epox good.

Kevin Hammond: Ryan. It's certainly different.

Ryan (Cerkoryn): Yeah. Yeah. That allows us to I think having a rolling window is a good thing because they're not like I have to wait till next year to submit my NCL. it's just constantly refreshing which I think is a good thing.

Ryan (Cerkoryn): So yeah, on its surface this SIP is quite simple, but the details get a bit more complicated the deeper you go into.

Kevin Hammond: They do. Yeah. so you'd be changing the rush to rush to spend treasury funds as soon as the NCL is announced to change to make treasury proposals as soon as the last big pig spend has reached at 73 or…

Ryan (Cerkoryn): Yep. Mhm.

Kevin Hammond: whatever the number is epoch difference,…

Kevin Hammond: So I should probably go and join Neandros Bosco.

Bosko Majdanac: Just wanted to say that applications have been started for all committees and…

Bosko Majdanac: currently TSC is the only one without that. It's too early, but I'm just stating the obvious. Seems that nobody wants to join you guys. Just kidding. It's too early.

Bosko Majdanac: It's too early to say. Generally, it has just started. But I'm just saying the only one without any application so far.

Kevin Hammond: So, let's again push that.

Kevin Hammond: So, I think you pushed that in the Slack channel, Bos. …

Bosko Majdanac: I will for whatever we didn't discuss and…

Kevin Hammond: but let's also promote it via the T TSC X account.

### 01:05:00

Bosko Majdanac: I think could be important and also I will start the thread and select no worries.

Kevin Hammond: So, let's post that out and encourage any TSC members whose term is coming to an end to consider applying. So please do reapplying.

Bosko Majdanac: Yeah, absolutely. I'm just saying. Okay. that's it from my side. Anyways, I'm stopping sharing. We'll share the notes as usual if possible even today as soon as they're available.

Bosko Majdanac: I agree. But

Ryan (Cerkoryn): Take care everyone.

Kevin Hammond: It is indeed scary but you have to overcome your fears and it's incredibly important. Okay, thanks everyone. Catch you again next week.

### Meeting ended after 01:05:57 👋

This editable transcript was computer generated and might contain errors. People can also change the text after it was created.

  
**