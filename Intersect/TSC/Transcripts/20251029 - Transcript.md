**

## Technical Steering Committee - 2025/10/29 09:30 CDT - Transcript

# Attendees

Adam Dean, Benjamin Hart, Christian Taylor, Duncan Coutts, Jonathan Kelly, Nicolas Biri, Terence McCutcheon

# Transcript

Adam Dean: All right.

Adam Dean: Do we know who else is out at this UPLC workshop or whatever's going on in Edinburgh? Okay.

Nicolas Biri: My understanding is that given was the only one I mean within the TSC hopefully there's other people…

Nicolas Biri: but within the TSC I think is the only one who is attending. So I don't know why so many people are missing. yes, Sebastian there's a Laos monthly call at the moment. So he may likely join after that.

Nicolas Biri: So in half an hour for others I don't know.

Adam Dean: All right.

Adam Dean: Given the first one, I don't know that we can actually take concrete action on. Johnny, do you want to go ahead and introduce kind of this community reward sharing schema update to the members that are present?

Jonathan Kelly: So this came through from the body of people working to try and come up with good changes to parameters to better distribute rewards in their opinion or manage stake delegation or rewards in general and there is a document that they sent along which I'll throw into chat here if someone can share it. and then there are five points. What they want to happen is ecclesia to be leveraged to vote on these five points which I'm now putting in chat as well for quick reference.

Jonathan Kelly: and yeah these being adopting SIP 50 which has been discussed in previous meetings setting a initial parameter value for that parameter of SIP 50 which is called L if it's to be adopted and adopting SIP 163 which is a new one for discussion the idea of timebinding delegation and having a delegator inactivity setting so after a certain amount of epochs if they haven't proved that their wallets  active in any way dropping delegation from an SPO. yeah, that's an interesting one. And then if that's to be adopted, what should be the initial delegator inactivity period for the parameter if it's introduced? And then adopt SIP 23 is the last vote, which is to do with introducing a min margin instead of min pool cost or as well as.

Jonathan Kelly: But yeah, these are the topics that are up for discussion to see if they get moved on to an ecclesia vote.

Adam Dean: And I've spoken to Ryan Wy, who's one of the kind of the lead authors of this document. and obviously I'm going to recuse myself as they're planning on using a tool I created for the voting. and I will no longer be on this committee after the elections wrap-up, which we'll get an update about here in a little bit. but what they were asking for is essentially the TSC to assess this document and make sure that what they are proposing is actually technically viable I guess is probably the best way to do it so that they are not proposing something that is theoretically or practically impossible for the Cardano network or in some way dangerous.

Adam Dean: So, they are asking for the TSSE's opinion. and I mean, I guess I'm in favor of it. It does give us a work stream and an actual deliverable that we can do. but I would suggest that we couch it in such a way that it's not a recommendation for or against, but is it technically possible if the community should choose to adopt these things, yes or no.

Jonathan Kelly: I guess I'll be first to comment. I think they're technically able to be introduced as parameters, but I have some doubts as to the effectiveness of them, but that's more of a subjective reasoning for vote rather than a technical feasibility question, which hat do I wear in the feedback in this

Adam Dean: Go ahead, Duncan.

Duncan Coutts: So I have to say I have not sit 50. but the standard question that one would ask in this circumstance is right I mean I mean typically you can change the rules in a game theory sort of setting but the typ question is what's the result how does it change the equilibrium are there new weird outcomes that you don't want basically has anyone done any analysis that's the standard

### 00:05:00

Duncan Coutts: And if there is analysis then that makes it a lot easier to both for us or for the DRPs to make an assessment.

Jonathan Kelly: I'll give you a brief rundown of SIP 50.

Jonathan Kelly: So this is the idea of introducing a parameter named L and its purpose is the higher your saturation point can be and the lower your saturation point can be. so it's trying to make pledge mean something more than it currently does because higher pledge people will have more of a right to get delegation. I find it personally uncomfortable because some smaller pools have lower pledge for a reason beyond their lack of conviction. That seems to be the way it's read. If you don't have high pledge, you don't have conviction.

Jonathan Kelly: some parts of the world have lower amounts of ADA that they can bring to the table in order to run a pool. And I don't know if it's as cut as you don't have the conviction if you don't have the pledge.

Jonathan Kelly: But that again is not a technical analysis and it's still something that could come into effect and work.  But whether or not the outcome is desirable is a

Adam Dean: And…

Adam Dean: and back to Duncan's point, which is I think how we should assess all of these has proper game theory and technical analysis been performed on these what happens if there's not enough pledge in the ecosystem in order for all icipate in staking. all ADA can participate in staking regardless. this would actually put an upper bound on how much ADA can be staked because pools would become saturated.

Adam Dean: so there is an actual threat and danger to this that the authors probably are not considering because in my opinion is once again coming from we're small pools and we deserve to have rewards too. and big multi-pools are bad sort of camp of

Jonathan Kelly: And even if it does come from that camp, I think there's this disconnect between that position and the fact that some smaller pools have lower pledge and if they got popular, they wouldn't be able to get the same level of saturation as someone else with a higher pledge. So, it seems confusing to me, but maybe I'm wrong. but yes, you make a good point, that if they did do it that way, then there wouldn't be a straight cut represent all potential delegated ADA.

Nicolas Biri: I won't.

Jonathan Kelly: That's a good thought.

Adam Dean: All right. But yeah, so not to belabor the point because again we're not corate in this meeting at the moment. So what I guess we would ask is that all TSC members would review this document probably just raise any and all concerns you have internal in our Slack or Discord channels. and then we can probably vote on a coordinated response. maybe in a week or two to give feedback to these authors. And so let's take that as a takeaway, Johnny, if we can ask for all present and…

Jonathan Kelly: Yeah. Yes,…

Adam Dean: non-present members to at least read over the document real quick and provide at least their highle technical analysis. Right?

Adam Dean: We're not asking anybody to dive really far into the weeds, but just give it at least a surface read and provide feedback.

Jonathan Kelly: And interestingly enough, Ryan himself might end up on the committee in the next number of weeks. he's a candidate, so he might be able to talk directly about this, but we'll see.  Not trying to tip the scale, of

Adam Dean: All and yeah, so our next agenda item was to have the hard fork working group scope discussion from text, but unfortunately we're not coret to take a vote and I know you did want to raise a vote text, so we might have to do that async in the channel.

Jonathan Kelly: It's possible we could Yeah,…

### 00:10:00

Adam Dean: Can you introduce

Terence McCutcheon: We did have a yes in the chat from Kevin.

Terence McCutcheon: So if everybody here was unanimous essentially that could pass.

Jonathan Kelly: 

Jonathan Kelly: this is what I was going to say.

Jonathan Kelly: And my vote is a

Adam Dean: Okay. …

Adam Dean: why don't we let text then introduce the scope for the recording sake and then we can make a vote.

Terence McCutcheon: Yeah. I'm not sure if I'm fully qualified on this, but if I'm looking for the sheet itself. I've got it here somewhere. it is. that. So, this has been shared in the channel, but will share it again I'll share it here in the chat just to be sure.  This is the current draft version of what is expected to be in this hard fork proposal. so does include updates to Plutus and to Ledger. those are detailed here.

Terence McCutcheon: I believe the target for hard fork at this point is sometime Q2 of 2026. but in the interest of having the hardware working group in action for they handle basically everything within 6 months ahead of when the actual hard fork takes place that would be the reason to get this up and going as quickly as possible.  Yeah.

Adam Dean: And so is the request asking if this is an acceptable scope for the intraera hard fork because I mean I'm pretty sure we've already had committee support for re reforming the hard fork working group and that seems to kind of keep simmering on the burner but not really moving and progressing forward.

Terence McCutcheon: So I believe it's just as simple as yes, this has likely already been circulated and the official decision is just to call for the reformation of the group.

Adam Dean: Just to start with, I'm not loving that we're doing an intra era hard fork purely on the basis of meeting contractual commitments to intersect milestones.

Adam Dean: So, that first sentence is a little bit weird.

Duncan Coutts: Yeah, that is a bit weird,…

Duncan Coutts: isn't it?

Adam Dean: We're not doing this because it's good for Cardano. We're doing this to meet a contract milestone and get paid. What?

Nicolas Biri: At the same time we could advocate that the fact that it has been approved means that we need to deliver it some way in some way.

Nicolas Biri: But I agree that the wording is wrong because it shouldn't be stating that it's an agreement with the intersect milestone. it's probably more the fact that it has been approved by the community and that we need to deliver it. So, the intersect milestone is an issue here probably.

Adam Dean: Yeah, I could see that as IOG's incentive to call for the upgrade to happen, but not why we would present to the community that we are doing an intra era hard fork.

Nicolas Biri: Yep.

Adam Dean: We're doing it because we're getting these new Plutous primitives that are going to unlock cool new features and they're going to do it prior to the full Dystra era being ready to roll out. but I certainly don't have a contractual commitment to perform a hard fork. so yeah. It just reads really weird to have that in there as the first line.

Benjamin Hart: Is there any other onchain event that this intra era hard fork actually enables or…

Terence McCutcheon: the only things that I can say at this point is to my understanding this document would be something that is immediately reviewed when the working group spins up in order

Benjamin Hart: I know there's Pluto's primitives…

Duncan Coutts: What do you mean in the zent?

Benjamin Hart: but do we want to speak to anything to do with how well it aligns with vision 2030? Anything like that?

Terence McCutcheon: to start working on the comm's package. But this document is not at all entailed or designed to be in my understanding the base of the comms.

Benjamin Hart: This isn't public facing.

Benjamin Hart: Okay.

Terence McCutcheon: This is just a general understanding to start the working group is how this was drafted.

### 00:15:00

Benjamin Hart: I mean with that context where it's really just to start the working group, I think this is fine. Go ahead, Christian.

Jonathan Kelly: Preston.

Adam Dean: First, go ahead.

Christian Taylor: Yeah, sorry baby to manage. But I was going to say the working group you can that's where added scope could be plugged in if there's other community things tying into this from product and stuff. and at the end of the day this is just a proposal that goes through. It can be slammed by the community and doesn't go anywhere.  So, you do have the control gates.

Adam Dean: No, I mean I think everybody's on board for doing the intra era hard fork. U so yeah, I don't see a major issue there. Just again who's this we get rid of this first opening sentence and we're good to go because there are a few issues that are being addressed and resolved here that shouldn't need to wait all the way until Dystra is fully ready. and then obviously we get some probably relatively minor in terms of impact new Plutous primitives that might enable new contracts to come online or new design paradigms to be deployed. but again, it's a chicken and an egg. We need the primitives before we can build the contracts. So, it'll be however long before those contracts start leveraging those new primitives.  Yeah.

Adam Dean: Shall we do a show of thumbs I guess in the chat if everybody's okay with proposing this as the scope to reim reinstitute the hard fork working group with the intent to work towards this version 11 intra era hard fork and…

Adam Dean: it seems like we got a thumbs up from everybody and that's the five present members and then Kevin Hammond who's not present today due to a conference attendance did vote asynchronously inside of the TSSE internal chat. So we will consider the motion passed. So we can go ahead and move forward. Tex

Terence McCutcheon: Okay, not a problem.

Terence McCutcheon: So I will work with Jess Gilbert on this and then as I understand looks like also Bosco and Ryan from Intersect are going to be involved here as well. so I'll get pushing on that.

Adam Dean: All right, and jumping ahead a bit, seeing as how we do not have Alex present for protocol parameters update, and Kevin is not present for the Cardano vision, input from the TSC.

Adam Dean: Can you give us an update on where we stand with the committee elections? yeah, sorry back to you again, Tech.

Terence McCutcheon: Sorry, that's to me.

Terence McCutcheon: So with the committee elections, there are seven candidates for the technical steering committee. Voting opened up on Monday at noon UTC. little interesting that we're going through a week of time change, but I'm sure we're going to work through that. still using UTC as the primary communication. We should be okay. And that's all happening technically. but voting is open until next Friday, November the 7th. and again, closing at noon UTC.

Terence McCutcheon: I don't know that there's many more updates than that, but if there is anybody that would like to either take on or take leadership of adjusting an onboarding slide deck for TSC, I wouldn't mind having some help there. so we have a new process or not a new process, but something to actually onboard these people with. whoever it is that is selected that may not have already stood on the committee previously. additionally, this does cycle back the conversation that seems to be ever ongoing, which is, the chair/vicechair conversation.

Terence McCutcheon: I believe we may have reached consensus, but there was still some thoughts going each which way because there had not been anybody from the cohort elected in April that had wished to explicitly stand up based on attendance and other reasonings.  So, the desire if it can be adopted by TSC is essentially to have a new chair each election term. Right now, that's 6 months. Potentially, that might change in the future, but for now, you'd have a new chair every six months, which splits the responsibility of that chair role amongst different committee members, but also ensures that topics stay consistent.

### 00:20:00

Terence McCutcheon: So, again, I don't know that we need to take everybody's time to continue that discussion here, but if there are thoughts that are relevant, we can. that's just a brief explanation on kind of what's happened so far, and hopefully that's sufficient enough.

Adam Dean: Go ahead, Ben.

Benjamin Hart: Just a suggestion it might be worthwhile to make sure that the chair is always from the newly incoming batch for 6 months as opposed to the outgoing…

Benjamin Hart: because then you have a succession in theory a module of the democratic process but I think that's probably better for institutional memory.

Terence McCutcheon: that is the design of the program.

Terence McCutcheon: So essentially here's where TSC stands as right now, nobody from the April cohort has explicitly stepped up to say I want to be the chair.  Sebastian did that in a previous meeting on the basis of being able to have and hold a meeting. but that was not necessarily anything that was longstanding. So if there is anybody that was elected in April that does wish to essentially take that chair role that could be called as a court decision by TSC and that sets the next six months in motion. Kevin, who is a candidate for the committee and is most likely somebody who's going to be reelected, could again be elected into what would be that vice chair capacity and would then take over as chair in April once again. again, if that's the decision of the committee.

Terence McCutcheon: So that's kind of where we stand that the design is to pick up and go with that always electing out of the group of newly electeds. but when I initially revealed that suggested that or whatever the term we want to use is there was kind of some widespread feedback that said that that might not work for us and…

Terence McCutcheon: it's kind of confusing as to why.  So,

Benjamin Hart: Yeah, I think it's a guiding direction.

Benjamin Hart: I don't think it should override democratic choice. Just an ideal that might be nice it's a recommendation in the same way that some organizations have a gender parody recommendation, but ultimately democrat the democratic process still remain

Adam Dean: Yeah, I'm not sure that I would agree, that we must have a chair that must come from these newly elected people. if the reason we're in the situation we are for those that are new to the committee or whatever is Kevin was the only one originally that stood up to be the chair of this committee. and I ran against him only so he wouldn't be running unopposed and that's how we ended up in the chair and vice chair positions of the committee u so it was more taking whichever volunteers you can get versus having so many candidates that we had to whittle them down so I think Ben said it's good practice that we should encourage somebody from the new co cohort to become the chair and be ready to take over that leadership role in six months

Adam Dean: the incumbent chair is gone because they don't stand for election or don't become reelected. so that's a good practice. It's a good best practice, but not necessarily a requirement.

Benjamin Hart: Yeah, I'd say it's my hope that such a guidance would as I've seen it in other organizations serve as an inducement to the kind of people like if someone who's just been elected on wasn't going to take up that role, it might induce them to run for a position. that's the goal.

Adam Dean: All there you go. 30 minutes and we got through the current agenda. Christian, go ahead.

Christian Taylor: Not an agenda item, just an FYI, is there are three more project requests coming in. not I guess for incubation, but it's from the Orborce network team projects that complement what they're doing. So I'll be passing that over to y'all's review, but it's for type protocols, IOSIM, and SERO and SERO may be a point of conversation because it's a complement to K agent, which is still TDD.  So, just prepping you all for that dialogue on

### 00:25:00

Duncan Coutts: I will need to recuse myself on those ones because colleagues of mine will be applying for the retainer role on those or some of those projects.

Christian Taylor: Okay,

Adam Dean: And so I guess the request is to submit these new packages for Intersect to own and…

Adam Dean: to have responsibility to maintain and manage going forward.

Christian Taylor: Yeah, essentially it's going to be part of…

Christian Taylor: what I guess we're calling core hasll node because it complements that. I know cast agents already covered under the contract and there's renegotiation going on with their contract or something. if we do have these in there, I'm going to confirm with IE that they are going to be the maintainers of these projects. and we're not just bringing it over willy-nilly.

Adam Dean: Yeah, I guess that's always the concern is that we end up the dumping ground and then we have to go and find the budget to maintain and support and take care of these repos…

Adam Dean: because we've taken on the onus versus leaving them with their original founders or creators and letting those creators make the argument to the community that they should be maintained and funded.

Christian Taylor: Yeah, the case in point for…

Christian Taylor: why this derived is Cardominals a CLI wallet that was given over to Intersect. The maintenance contract TX pipe did not go through for it. So the project is basically in a stagnation right now.  no active teams working on it and TXpipe forked it and created their own version. So I'm actually putting a proposal to sunset our version since there's no active person working on that unless another case can be made.  But that's the reason for this process.

Adam Dean: Go ahead, Duncan.

Duncan Coutts: Obviously I'm not going to vote on anything related to this because I need to recuse myself from it, but I should point out that technically two of those packages are existing dependencies of the Haskell node. So they're not random things that we have to maintain. They have to be maintained because they are dependencies of the existing node. It's just that for whatever reason they didn't get transferred the first time around. I'm not sure Maybe oversight. Maybe there's a reason. but they're in that sort of category.

Christian Taylor: It should have all three proposals shared to both OSC and TSC by the end of the

Adam Dean: All does anybody have any other business? Because otherwise we can give everybody back at a half hour of their day.

Benjamin Hart: Thank you for the half hour. May I have another?

Adam Dean: Yeah, You get a half hour. Everybody gets a half hour. All right.

Benjamin Hart: Have a great day, everyone.

Adam Dean: so yeah,…

Duncan Coutts: Cheers everybody.

Adam Dean: we'll adjourn this meeting. Have a great day, everybody. and we'll see you next week and…

Jonathan Kelly: J about to

Adam Dean: go from there.

### Meeting ended after 00:28:59 👋

This editable transcript was computer generated and might contain errors. People can also change the text after it was created.

  
**