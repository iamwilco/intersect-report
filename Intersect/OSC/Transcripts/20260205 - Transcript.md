**

## Open Source Committee (Intersect) - 2026/02/05 07:41 CST - Transcript

# Attendees

Bernard Sibanda, Christian Taylor, Darlisa Consoni, EMMANUEL TITI, Harun Mwangi, Jordan Hill, Otter.ai Notetaker, read.ai meeting notes, Reshma, Robert Hever, Sebastian Pabon, Terence McCutcheon, Uche Obasi, Udai Solanki

# Transcript

Christian Taylor: Hello. All going.

Reshma: Hi Christian. Yeah. am I audible?

Christian Taylor: What's up?

Reshma: Am I audible?

Christian Taylor: Yeah, I can hear you.

Reshma: Okay. I'm going to

Christian Taylor: Which otter are we going with? Looking at that.

Christian Taylor: Not one of them was stands.

Christian Taylor: How you doing?

Terence McCutcheon: What was that again?

Jordan Hill: Hey, Christian. Hey, guys.

Christian Taylor: Hey, we are lots of friendly AIs. Rush was just there.

Christian Taylor: We go.

Reshma: Yeah, I came back.

Reshma: There was a problem with my headphone. So, I was fixing that. question before we head into the main sections. I attended a meeting that was in my calendar OC agenda meeting. Is it still there or I attend that meeting there was no one?

Terence McCutcheon: I'm sorry.

Reshma: Yesterday there's a meeting in my calendar OC agenda set.

Udai Solanki: Yes. Amen.

Reshma: So I attended the meeting. There was no one in that meeting.

Terence McCutcheon: Yeah, that one's on pause right now. I'll if that comes back. I've pulled away the main invites.

Terence McCutcheon: So the only way you might have that is if you have the open source committee calendar. I left it on there for my recordkeeping, but yeah, right now that's on pause.

Udai Solanki: Yeah, I also briefly logged in there Rashma and I thought we are going to set the agenda for today.  So yes. Yeah. Yeah. Yeah.

Reshma: Yeah, that was the first meeting I saw in the calendar.

Reshma: So I miss couple of meeting. So I thought I would come in that meeting and know what is happening. So there was nobody. Yeah. Yeah.

Terence McCutcheon: We'll work on that.

Terence McCutcheon: But the best place to catch up is definitely going to be Discord. That's where I've been pushing a lot of updates for everybody. So,

Reshma: Yeah. I've seen

Christian Taylor: which is a question for y'all too. is Discord a good medium or would y'all prefer a Slack thread or we migrated Discord with the previous committee members,…

Christian Taylor: but we can always change medium if it's easier to coordinate.

Udai Solanki: I think yeah one thing…

Udai Solanki: which that's what I see in happening in intersect using slack clickup this and there's so many channels so you need to be all around I'm okay with the discord I do miss time to time some alert but Still I think that will not get solved by moving to another media. tools too possibly it is about being attentive right in India most common for us we use you hardly missed the WhatsApp…

### 00:05:00

Udai Solanki: but I don't recommend WhatsApp  Yeah.

Christian Taylor: We can also just book tickets to your house to that.

Christian Taylor: Yeah, a lot of my channels on WhatsApp are on ignore right now. So, hey Robert, thanks for doing it.

Robert Hever: Hey everyone, I share your pain. I set a culture very early when I was with my company that I only answered emails and Slack and everything else I deliberately took my time on. So everyone just went to that channel to find me. It was very helpful, but I also missed a lot of messages.

Udai Solanki: And here it's not about company,…

Terence McCutcheon: Fair enough.

Udai Solanki: It's about the community. So different choices, different committees. So yeah. Okay. Tax over to you.

Udai Solanki: Please guide us.

Terence McCutcheon: Yeah, I was looking I was giving another minute or…

Terence McCutcheon: two here. U I know we don't always have the time,…

Christian Taylor: Yeah, Gayorg will be out I think this week.

Terence McCutcheon: but I was getting another minute or two because we are not yet for so it's just trying to get to that place here. most likely.

Udai Solanki: Okay.

Terence McCutcheon: So, not court can't make decisions, but let's at least get through some of the review and we'll circle back as we need to. so, here is the agenda that's been prepared. we actually are now court. We have Sebastian. So, perfect.

Terence McCutcheon: so for anybody who's wanting to know, welcome to the open source committee meeting February 5th and we are court here with UD Rashma, Jordan and Sebastian. it's four out of seven which we're down to at the current time. So just for reference. agenda here today developer advocate Charlie 3 tooling milestone stuff events there's a whole bunch of stuff so we're just going to kind of jump right in is the only developer advocate here so let me just give him a quick space to provide any update he might have for us

Uche Obasi: Yeah. hi everyone. so so far the developer advocates has been working really hard on going about the activities like the developer working groups sessions and then the onboarding sessions as well. but most importantly what we've been super focused on for the past week and into the next week is the Cardano Africa Tech Summit. So hopefully we all should be there next week.

Uche Obasi: So it's like this huge event that kind of like gathers every card enthusiast within the continent as far as I'm concerned. yeah. So, we've just been trying to see how we can…

Terence McCutcheon: Awesome. Thank you so much,…

Uche Obasi: how we can participate and get more people on board and also talk to the community members during the conference. So yeah yeah that's pretty much about it for now.

Terence McCutcheon: All we'll keep moving right along here.

Terence McCutcheon: So some of you may have seen the document that's been shared in the discord channel there that is regarding Charlie 3 if I'm not mistaken for project incubation specifically on the basis of assisting and moving along with the open source strategy for the Charlie 3 Oracle at least some of those repositories but as I'm not the professional we do have one here I will pass this over to Robert and I'll also kind of give you about that five  minute timer like you had yesterday so we can keep on with other things.

### 00:10:00

Robert Hever: Sounds good. Thank Appreciate the time today, everyone. and I'm apologize. It's, 6:00 in the morning for me. I think the steering call yesterday was 7. So, I normally don't expose myself to people this early. it's not but, I'd like to submit Charlie 3.  Moving on to the incubation and for open sourcing why now is maybe the question. If Charlie 3 is one of the oldest companies in Cardano we started in 2021. We launched one of the first contracts after the hard fork. we have four solutions across 117 repositories. obviously not all 117 are going open.

Robert Hever: but we have two native oracles, a partner chain that's built on the partner chain tooling for Midnight that we're open sourcing and we currently have a DEX aggregator. And so the question why now is we've had conflicts at a board level for quite some time about this decision. but now I'm in sole control of Charlie 3. I'm the only board member and it's a decision that I've been trying to make for years. and I think that it aligns with what's missing or a gap in one of the kind of dirty secrets of Cardano is the infrastructure that people are doing is bootstrapped, fragmented, ad hoc. this leads to users being liquidated in the background due to bad data u and other events that get kind of brushed under the rug.

Robert Hever: and these users get paid off and you never hear about it. And so one of the big problems is a standard or for using an accurate and secure data network to bring data on chain. and Charlie 3 has that and we're trying to drive adoption and distribution. and that's our vision or mission is for the adoption of smart contract technology in Cardano. one of the most telling signs for us was our biggest customers have come to us because large whales have wanted to use our Cardano ecosystem and said we're not moving funds on until you use secure infrastructure. And they delivered our sales and so what we're trying to do is maximize distribution and maximize access.

Robert Hever: And so we're willing to give over the IP to Intersect have a support with governance on how we're going to maintain this and build this out so that it's supported for the builders. and I think it's a long time overdue. I think with the incubation that's our first step. We're primarily looking for advisory on how to make this transition. It's complicated.  We've already open sourced most of our solutions choosing licenses and putting contributions standards on it but we're not experts in this field and I'm alone as an executive member. So our team needs support as we move through this transition. I want to keep some of it private.

Robert Hever: so this one enterprise fork of one of the open- source repos we're going to keep for web two clients. and then the second one is going to be a marketplace that we're already developing. similar Red Hat, we want to sell certification for a marketplace where people can build and sell or offer free adapters. so we've given some examples that we're going to put out of adapter to about 30,000 tokens on other chains. and so yes, I think that's pretty much in a nutshell what we're trying to do thank you very much for your time. Appreciate it.

Christian Taylor: 

Terence McCutcheon: I don't want to be too fly by night.

Terence McCutcheon: Are there any questions from committee members?

Terence McCutcheon: Hey there.

Udai Solanki: Yeah. …

Udai Solanki: thank you Robert for the proposal and first of all, I totally agree with the kind of requirement or problem statement here. if I go back about an year ago, I saw this as a potential need or problem.  I proposed one the building opensource Oracle of course was not approved that point of time and we are heard of Charlie 3 definitely before and you being open to make it open source is great news for Cardano network I think so thank you for that initiative so that's the first part the second is I'm trying to understand what mechanism you would like to work

### 00:15:00

Udai Solanki: you said just now I'm just trying to grasp that but one question is are you looking for any financial aspect in immediate term or you just handing over this to intersect and at least in near term any financial assistance is expected not expected I could not see in the proposal very clearly so if anything there if you can be explicit about  It heat.

Robert Hever: So we do have some catalyst support for this transition. So immed we have a small team and we don't make as much money as people think.  And so we're probably applying for the maintainer retainer for our team members to help with that. and then probably I put one more submission for the tooling in March. and that's just to make sure that the team in the spring has some support in the transition for extra work to shift it over to the repos to you to support people coming to them asking for questions, creating documentation, creating additional guides and then promotion, but very little financial. the main thing I'm scared of and the worry I have is doing this properly.

Robert Hever: I'm more concerned with the governance aspect of our north star is adoption. so it's not so much I'm looking for funding. I'm looking for we've already open sourced MIT our current push Oracle and pull Oracle. This is already available. we've AGpl part of it which we're going to probably move back to MIT. I don't know what license to choose. And so this transition right now is already happening. we just need support first because it's happened very quickly. and then funding requests I would put in probably one for the tooling I think sustainability aspect.  Christian.

Christian Taylor: Yeah. UDay to clarify, what I've consulted him with is the maintainer retainer to compensate the devs as we open source There's a project support request to do this right for our open source lawyer just for a few hours to make sure we've done this legally and structurally sound and then tooling sustainability after the transition's already taken place as Robert was mentioning. But all around it's very less the financial ones.

Christian Taylor: It's more about just giving this back to the community in the right

Udai Solanki: Okay.

Udai Solanki: That's good. Thank you. I mean, Robert, I can give the feedback that in the last two years, I would say I had to have kind of two custom le And in other words, implemented two different Oracle for different needs. And that's where my point was like there's no need to build Oracle for every need, right? There should be a common infrastructure and I should be able to use that same Oracle infrastructure for different needs. So that's where my thought were coming and…

Robert Hever: Yes. Amazing.

Udai Solanki: you making it open source definitely make a lot of sense. So pull in support for that.

Robert Hever: And I went down to Raro in Vegas and we're working very closely with Palm Economy. I know Phil at Anastasia has an open source Oracle. I've talked to so many people and I'm like, why didn't we have a conversation? Why did we waste development time? we could have reused what we already have. And so this really was pushing me to go everyone has these fragmented solutions and…

Robert Hever: 

Udai Solanki: Yeah. Yeah,…

Robert Hever: some of them we've spent probably two $3 million on our solutions. We've been up since October 22 with not a single downtime. So there's a base here an infrastructure that the community can take and it's open. They can trust it apart from the Twitter FUD and the politics they can see the code and they can start working on it and it's governed by Intersect.  I think that's for our team that we've worked so hard. That would be a big win for us.

Udai Solanki: all for it. having said that, maybe you did say something about that some part will be private. Can you clarify that maybe once again?

Udai Solanki: I'm not sure that full project is outsour I mean open source or is it that some part is not so we shouldn't be tying in the user for some part that they need to go to you and pay for it how is it can you just explain a little bit

Robert Hever: So we have one solution is just a DEX aggregator that's already open source. It's already MIT and we're just maintaining it. And that one we're going to continue to scale and probably release some other adapters like that.  We have the current push oracle which other users like Moneta is using a version of it. Fluid that's going to be fully MIT. we have a pull oracle which that's someone requests data at the time and then we send it there's only one on Cardano right now. It's native. That's full MIT. So those three already are going to be full MIT.

### 00:20:00

Robert Hever: We have a partner chain solution which is based on the partner chain tooling for midnight which is basically a side chain designed for oracles and we have a bridge that posts data onto Cardano. Right now that is BSL because we didn't really know what we're doing. and that's part of the transition is what licenses are we choosing. we will likely go full MIT there as well. we might put an AGPL on the bridge. I'm not sure. I want to push more towards Apache or MIT. but that version we're going to customize the side chain for our customers. So we're going to release the code as MIT most likely and then fork it and create a custom version. And this is solely because the enterprise customers that we have don't want their version open. And if they do, great. Yeah, we just wanted that option.

Udai Solanki: Okay, just checking that is if this part of description is there in the report maybe I'll look into that but that's good. Thank you. the one question to you back that you just mentioned and what I heard I'm trying to understand right that the proposal right now is for incubation side right but then we are talking about maintainer retainer then we are also talking about tooling so it look like all the kind of the initiative we have in open source we are covering through this one so maybe for my understanding maybe Christian you can explain or… maybe Robert you  Focus.

Udai Solanki: 

Terence McCutcheon: I can take this on directly here.

Terence McCutcheon: So, the way that the programs they were designed to work together. and at this point, especially considering kind of the length of the process of different projects not applying, wherever we're at, there's a point where within our current budget, we need to show that the process does work. and in this particular case, we get an opportunity to work with a founding project in Cardano or close to it anyway.

Terence McCutcheon: so it's not necessarily the worst example to allow participation in every program but every program has its own constraints and every application will be validated as such. So if there's u by incubating it incubation and the maintainer retainer program are kind of linked. We already have an example of that with evolution SDK. so that one's not as crazy to pick up on. the next piece is going to be the tooling piece.  And so if there are tools required now that this project is becoming open source, right, that's a different tool and is supposed to have a specific functionality to the Cardana ecosystem and it'll be based on those merits alone. So go ahead, Christian.

Christian Taylor: Yeah, the whole focus of the paid open source model is to sustain all the critical functions and so it presents a menu of options. Now, incubation is not directly tied to that. It's meant that Intersect can serve as a mentor for open source best practice and it does not guarantee funding inherently. That's where the committee has to decide what can be approved.

Christian Taylor: So yeah they all work together but we can use case as to what's needed. Now if one project was incubated and they wanted 500k for development costs I don't think they need maintainer retainer inherently.

Udai Solanki: Yeah. Yeah.

Udai Solanki: So that's kind of my point was I want to ensure and as I started with I fully support the initiative and really appreciate Robert but just I want to make sure that it's not the multiple funding is kind of applied or even if it is applied we want to be aware properly so I understand now that it is coming through the initiative of incubation right so that some of the supporting services we're providing can be provided but no direct fund there and

Udai Solanki: Then eventually it will be put in mainer retainer program.

Terence McCutcheon: Yes.

Udai Solanki: So there's ongoing maintenance is happening. That's the main kind of the funding for Robert's team. And then when the specific tooling time to time when is required there could be some funding from Is that correct interpretation? Okay.

Robert Hever: Yeah, it is that we have some support right now but I suspect once we make the move we're as a business owner I'm nervous but I want to make sure the team it can obviously continue working on the solution that we  don't run out of funds and it's abandoned mid transition. And so that's kind of my intent is transition, get the dust settled, get the retainers in for the guys that are there that are maintaining and then put in the reasonable tooling requests that come up over the next 60 days. Yeah.

### 00:25:00

Udai Solanki: Yeah.

Terence McCutcheon: All right.

Terence McCutcheon: Any other pressing questions on this? Spent a little bit more time than desired, but that is There is a poll live, so voting members, please make sure that you attend to that. again, that is the nine dots in the bottom and then you should see polls as an option. So, please make sure you submit your vote on approving Charlie 3 for project incubation. I'm going to hop over to the selection criteria. So, this is for the tooling sustainability program. you guys may have seen me talk about this in the Discord a couple of different times. We're going to go ahead and just take a look at it right now.

Terence McCutcheon: Christian and I went through and made some other changes here, but I've got kind of a final markup that I'm just looking to make sure that we can get published. So, I can go through this slowly, but I didn't want to take the whole meeting time here. there's also something I'm checking on with Andamio after this. So, let me actually take a moment here.  Is there anybody that has time about 30 minutes after the meeting and wants to sync on how funds are dispersed for the tooling program? If there's no comment on that, then I've already included the relevant committee members. in this particular case here, we should also ask or look at we don't need to make a change immediately at this time.

Terence McCutcheon: But paying through the Andomio platform, we would typically stay paying in the ADA token. we can still pay up to these thresholds or we can look at changing these bands to be in an ADA value. Does anybody have a particular preference on that or should the payments kind of stay in that US value but we pay the ADA accordingly to the cost?

Jordan Hill: I think at this point we have to switch it to ADA …

Terence McCutcheon: Anybody else?

Jordan Hill: because we can't control the price of the funds we have for this program.

Udai Solanki: Yeah, I guess maybe it's difficult to change as well. But yeah, this ADA versus USD has been a constant discussion, when it's high, then it look like my god, too much ADA going or too much going. But when it is not then so yeah I think it's tricky one particularly I'm comfortable so far there's a range right mentioned there so accordingly I think in situation it can be approved so mostly I'm fine either way…

Udai Solanki: but yeah other members also can mention

Christian Taylor: Yeah. …

Christian Taylor: and the price bands just serve as guidance. you can always allocate more or less than what's in a area. It just provides projects expectations kind

Terence McCutcheon: So, is there any specific call for a decision on what we do as far as do we leave it Do we change that to A? I would note that USDM factors are still a consideration, but we are not in a position to do a transfer at this time. So,  Can I get some feedback? So, we're saying change to ADA or leave it in US dollars. I'm missing the point here, sir.

Udai Solanki: to me as I said doesn't make much difference eventually we are paying in ADA anyway the program got approved equivalent USD getting ADA now I know it's very difficult for you as intersect also to manage the fund right so we are already in difficult situation anyway. I'm rather preferring little bit that this can be kept it right now and…

Udai Solanki: we see the situation as it comes. I'm comfortable because the range is there. So that's what I'm saying.

Terence McCutcheon: …

Terence McCutcheon: go ahead, Bernard.

Bernard Sibanda: Yes, I go for supporting Katano projects, stable coins like USDM. if it can be in USDM is a stable coin native to Cardano supporting also our communities. I think that is my opinion. Thank you.

### 00:30:00

Udai Solanki: But not eventually it's going to be paid in EDA.

Udai Solanki: This is in the pro program point of view. What do we put it? Eventually it's going to be paid in EDA. So that's the supporting card.

Bernard Sibanda: So I don't know…

Bernard Sibanda: what is the cost but I believe there is a cost of transferring money from US dollars to ADA when you need it maybe I don't know…

Bernard Sibanda: how big that cost is but if it is on the Cardano native token USDM I may be wrong. I believe we should have very small transactions there. Thank you.

Udai Solanki: I don't think there's any difference at least in the two situation there is no

Udai Solanki: difference in There is a cost but that doesn't change if you put here USD or USDM or ADA doesn't change anything. I think it's a matter of due to the exchange prices fluctuating so rapidly that's…

Udai Solanki: why this discussion is coming. I understand

Terence McCutcheon: I'll let Christian go,…

Terence McCutcheon: but I put up a poll, by the way, just so you guys see for leaving the tooling sustainability program as marketed in US dollars, but when I'm going to get the details on Andamio, we would pay that out through the Andamio platform in A. If we get an opportunity, we would convert the remaining ADA funds for in the tooling sustainability program to USDM and then work with the Ando team to transition the payout from ADA to USDM accordingly. so yeah, leave your thoughts there. Christian

Christian Taylor: Yeah, to clarify too for those who may not have been there when the original decision was to go to ADA, we have to me some of the USDM before we can convert it for liquidity or…

Christian Taylor: something like that. so, Intersect has to partner with MBX and Manetta to get that done. And it's like a 30-day process and conversion just for the FYI.

Terence McCutcheon: Okay. …

Terence McCutcheon: I'm going to keep moving forward here. As far as the tooling program selection criteria, that's going to go for an async vote. I was going to put that here. but please make sure that you go and look at that document, add to comments or add new comments if just reply to a comment and signify your approval of that change. and we'll get that finished up, but that'll go to async vote. and that needs to be addressed right away because we do need to send off the milestone form on that.

Terence McCutcheon: the next piece here is the main retainer program interview report and I have that here as well. This was also shared in discord. This reviews the first round the 15 applicants that we had where we've selected eight individuals from that group. there's a brief overview of each candidate. Nothing that goes too far in depth. as I mentioned there was some assistance in creating this document.  So, just wanted to make sure that I didn't miss anything. I'd already made quite a few edits, but at the end of the day, you guys need to sign off on it because it's getting published on your behalf. so, if you have not looked at this, please do. but I am going to put up a poll signifying approval for this document. again, with the assumption that hopefully you guys have had a chance to review this ahead of time.

Terence McCutcheon: questions come with concerns, but

Udai Solanki: So I gone through the report. Looks all good. I mean question is first my understanding is that it been interviewed by previous committee member and some members right from our community and it looks very detailed nicely described what was found right as a current committee members what we are proving I'm not able to verify all the content but assuming these contents are correct these contents details the rational and everything looks okay. So we can definitely approve the report that this report is acceptable. but I'm not going putting any effort to verify any of the content.

Udai Solanki: 

Udai Solanki: Is that okay or your expectation is different?

Terence McCutcheon: All we need is a signatory.

Terence McCutcheon: If you approve of it, that's great. if there's concerns, then comments need to be left so that we can address that accordingly. but other than that, a period for review has been given. just need you guys to be familiar with this stuff because again, it's as the body in this point of time, you're the ones being signed off as having approved this document. So, you just need to be comfortable that that's what's out there. I'll tell you, it's on blue in the face that I've done this as factually as I possibly can. right. But the entire purpose of this here is that we have the OS the committee, right?

### 00:35:00

Terence McCutcheon: The OSC is the check and balance of the work produced by the open source office in a support capacity.

Christian Taylor: I'll give a read through the report too just to make sure it aligns with what I saw during interviews.

Udai Solanki: Yeah and understand tax is a good point. I mean I've not been part of the interviews but I seen the notes of interviewers and I trust believe those are correct and then based on that looks like this report is prepared and report format and…

Udai Solanki: 

Udai Solanki: otherwise expectation point of view it meets the expectation right so that way I'm quite comfortable and I will be able to sign it off

Terence McCutcheon: Wonderful. All right.

Terence McCutcheon: Before we get into the next topic here, just a reminder, last I checked, we had at least five So, we do need to see at least those five votes coming on the polls. again, if you're just attending the meeting or here for other reasons, you do not need to contribute to the here. but voting members, please do make sure that you have responded to the regarding Open Source Summit Minneapolis, so the total cost of the sponsorship is $38,000. that's US dollars. I've spoken with them via email and in a meeting. Linux Foundation is also a nonprofit organization.

Terence McCutcheon: So they do not allow any other further reduction in the cost of the sponsorship. so the 38,000 is where we sit. If we sponsor more than one event at any level, the discount that we would receive changes from 5% to 7%. that brings the cost of the North America summit to 7,200 and I also shared in the discord the India summit would be around some oddund 4400 or something like that.

Terence McCutcheon: have to double check those numbers so there's an opportunity where potentially with today and Rashma we could get them access to the India summit if we wanted to try to further reduce the cost of the Minneapolis summit. It is not at all required. I also put something in there A back wall would cost somewhere in the neighborhood of $3,000. that's additional funds.  Right now we're a bit on hold because basically paying for the summit right now would expune the rest of our tangible funds that we have and that is purely based on the ADA value at this time. so if it's me I still think the summit's very important. I don't know that there's a way that we can reduce to a silver because of the attendee capacity there.

Terence McCutcheon: I think if we're going and we're going to do it, it needs to be at that gold level. but we have time to kind of hold on these things.

Terence McCutcheon: So I'll take some open thoughts and discussion here as to what you guys want to do. At the end of the day, it is your decision.

Udai Solanki: Yeah, I'm quite in favor of it.

Udai Solanki: But yeah, the ADA price is now dipping even last 24 hours going bad to worse,  But there I wanted to add here I maybe need to check but I'm thinking or considering to attend the Paris blockchain summit or the Paris blockchain week its so is that edited tax already there or I need to add

Terence McCutcheon: So that event I was actually just looking at that today. I was just marking that as an event that we might need to pull back from.

Terence McCutcheon: that particular event had not been officially approved but individual attendance is approved. Again, it's really just where do we stand with the ADA value and what we can pay for and…

Terence McCutcheon: which events are priority. so I'm not going to explicitly say no to that. but right now if the priority is the summit then we may not be able to cover that one. Does anybody wish to add the open source summit India assuming costs allow to further reduce the cost of Minneapolis the North America Summit or…

Udai Solanki: So I'm talking mostly from the attending point of view…

Udai Solanki: but Just mentioning and I will write it down and we'll see how Edi kind of play in the next few weeks.  how much was the cost again for India.

### 00:40:00

Terence McCutcheon: do we just stay focused on Minneapolis at 38,000?

Terence McCutcheon: Let me check the Discord channel here. Apologies. Sebastian,…

Udai Solanki: Good.

Terence McCutcheon: I just saw your comment. you can add additional people to that meeting. apologies, guys. I was not necessarily spamming but I had a lot to share with you guys this week. if we did both events the open source summit India is a cost of $4,650 and provides us three passes. So that would be one for day one for Rashma and one for the two of you to decide…

Udai Solanki: And we will have the booth as well.

Terence McCutcheon: who else might join or potentially Christian if he's able to make it.

Terence McCutcheon: The no actually let me double check that.

Terence McCutcheon: I have it right here.

Reshma: Actually that summit is happening in Bombay right?

Reshma: OSS India 26.

Terence McCutcheon: Mumbai Okay.

Reshma: 

Reshma: Yes, Mumbai. as a mother of a young child I cannot leave my hometown so it's far away from the place so I'm not able to participate in that  Yes.

Terence McCutcheon: So, you're saying you have personal reasons that prevent you from traveling? Okay, no problem.

Terence McCutcheon: the sponsorship at India does give a top two chairs and a tabletop sign with logo. It also provides power.

Udai Solanki: I mean I'm not given third on this one.

Christian Taylor: When did that happen?

Udai Solanki: We'll let you know my feedback but Christian possibly can guide on if he's coming will be perfect then to I think do that.

Terence McCutcheon: Yeah. at this point, I mean there's quite a large cost, right? we're talking 5,000 plus in additional cost for another summit just to save $800 on the one. So I'm not saying for us not to consider the summit in India. but we can kind of look at that if there are funds remaining in the ADA value returns. whereas we can just focus on the mainline numbers of what the cost of the North America summit is.

Terence McCutcheon: I can put that up as a poll if there's general agreement, it would be that we just pursue the North America Summit at its regular cost of 38,000 with our already included discount.

Udai Solanki: Yeah, I mean I would say the India one maybe we can make the decision at later stage that's…

Udai Solanki: what I will push the decision for India but I mean do we need to make the Minneapolis submit decision  Isn't today

Terence McCutcheon: Yeah, I'd like to have the decision today. That way I can sign the contract whenever ADA value is appropriate and so it's a good stewardship of funds. you guys will of course be notified about that. but if we get back to the original agreed contract value then we have already understood what that's going to cost us. So, …

Terence McCutcheon: the 38,000 equaling 72,000 ADA, right? Or 76,000 ADA,…

Christian Taylor: adversely. If it goes up to a dollar,…

Terence McCutcheon: excuse me.

Christian Taylor: we can do a lot of things to you. So, I also won't know if I'm able to go that way or not. Just depends on baby and his passport status. But, yeah.

Udai Solanki: Yes, understand.

Udai Solanki: Even going back to the Minneapolis summit, I mean it's not only the sponsorship thing, The travel and all those things will be also there tax, right?

Terence McCutcheon: that is so that's one of the big things that's tearing apart that event. this is also something where if the value returns there's a significant portion of funds that would be converted into fiat so that we can pay for them accordingly. So basically if we assume for just a moment right let's say that we have a random number if it hits the right value all of that 150,000 ADA would be converted into fiat so that we have the right amounts to pay for different things but the difference is that right now instead of the 76,000 which we'd be budgeting for Minneapolis the actual event sponsorship cost right now is coming and…

### 00:45:00

Udai Solanki: Yeah.

Terence McCutcheon: at 130 to 150,000 with fees. So it's almost 200%.

Terence McCutcheon: What's up?

Jordan Hill: I'm all for approving the Minneapolis summit today just so that we have flexibility to act on that if the price of ADA improves and then for the India summit it makes the most sense if we have at least two attendees with that booth attendance.

Jordan Hill: But I'm okay to wait on that. depended on if the price of ADA approves and people decide to go

Terence McCutcheon: Okay, Bernard.

Bernard Sibanda: I want to check again on the North America summit. It is a Linux Foundation event. Am I right?

Terence McCutcheon: Got it.

Bernard Sibanda: Yeah. I think the Cardano Linux partnership on open source is very important and attending as a gold member I think is very valuable. In that sense I go for it.

Terence McCutcheon: All righty then.

Terence McCutcheon: so what I'm gleaning from this here is for North America, yes, we're kind of putting all our eggs in one basket for right now. basic not that's the wrong way to say it, but we're going to pursue that to the best way possible here, hoping that we get a valuation return. the back wall will leave for a later decision. or we can decide that asynchronously. And then as far as India, that's on hold until we confirm if we have attendance or not. now, there are going to need to be some planning meetings for this. I am trying to get things done as quickly as possible, but with us not being able to garner the sponsorship right away, I don't want to set up meetings that are not having purpose. so I'll circle back on that, but please let me know if you're interested in being part of the planning meetings. If you are attending, I actually do expect you to contribute if you can, please.

Terence McCutcheon: So let me know what times you would have available for a 30 minute or one hour meeting on a weekly basis weekly every other week as time goes on. think about kind of throughout the month of March and April what we could get together because we're going to have to finalize things in those two months and hopefully by the end of March again that's all value dependent. Okay, I'm moving fast. please check the minutes. Harun. …

Harun Mwangi: Are the meetingings open to everyone here?

Terence McCutcheon: the meetings would probably be just for the committee for planning. but I'll take any feedback that you guys have based on where the plan stands. I'll be able to share that with you guys once the committee has something together. the next thing on the agenda, we're going to keep moving because we are running out of time here.

Terence McCutcheon: So, the maintainer retainer program, we do have a number of new applicants. Stuff kind of flooded in over the last number of days. I think we're up to eight or nine applicants for what'll be round two. This is really good for us fulfilling the program. but I do need people to be able to attend an interview. we do need committee member feedback and scoring on both the applicant data and the interviews themselves. And we're now going to be tracking this in ClickUp.  So right now I'm going to be duplicating some of the information into ClickUp so that we have it tracked for what stage each person is in. but again we will still use the Google Sheets documents for scoring and data tracking. so please I would say reach out to me or drop your times in the channel when you're available for interviews. I can put something out like a let us meet but honestly what's going to be best is individual times.

Terence McCutcheon: Okay, I can attend interviews in these window blocks.

Terence McCutcheon: And then I can just send out the invites accordingly. questions on that.

Sebastian Pabon: No questions.

Sebastian Pabon: I was involved in the interviews of the first cohort. I can help with that if I can help with this one. Yeah. Thanks.

Terence McCutcheon: Wonderful. Yeah.

Udai Solanki: Yeah, I will provide availability tax.

Udai Solanki: Next 3 4 days I'm not available but I think next week Thursday for Friday onward I'm available. So I will provide you my availability.

### 00:50:00

Terence McCutcheon: And also something to consider is more than just this next coming week. it's kind of through the end of February what you might have available for that.

Terence McCutcheon: So, look at the upcoming weeks plural, please, when you're sending those times. and again, if you got a standard set of times, a standard two or three hour block that's available weekly, that's really helpful. It's not how long The interviews are usually 15 to 30 minutes. So, it's super quick. I just need to know when you might have some free time. We can throw that keep it moving here.  Once again, we've got whiskey, vodka, and dandelion light. These were all decided asynchronously. I'm just calling for it officially here in the meeting. these projects have been onboarded to the maintainer retainer program. That leaves us with three project spaces left for us to onboard. if we get into a situation, again, as we may be extending some of the maintainer retainer program, you guys may have approval of additions there for Charlie 3.

Terence McCutcheon: We can discuss whether or not we reduce maintainership on some of these other projects to just one so that we can add additional projects but the primary goal is to get our 25 which again we're three away from and to get up to two maintainers per repository there. So to package the filler again whiskey vodka and dandelion light have been added to the retainer program. I expect that we may already have some applications for them, but if not, please do be sharing those in addition to the other repositories. Sebastian, they do.

Sebastian Pabon: Yeah, whiskey and vodka come from the sing the same projects built in fine scales.

Terence McCutcheon: Yes. Mhm. Yeah.

Sebastian Pabon: So we have to consider

Terence McCutcheon: My understanding is that that's already been considered and that would be very similar to how we have SDK and mesh multisync. So not necessarily a problem for us to have two projects from the same group. Again the core projects are all from intersect but I understand that's not the same comparison. So okay run through this here just real quick.

Terence McCutcheon: because that'll lead into question. So, first, the committee elections are coming up here in April. We've already been made aware of these. as it stands currently, we have seven members on the open source committee and of these members, two are departing in April. So, that would mean that we' be electing five. if I can just get that confirmation here that everyone agrees we' be looking for five people to join the open source committee then I will move that along.

Udai Solanki: So the two who are kind of terms completing in April, who are the two Okay.

Terence McCutcheon: one is a member who's actually not been attending and…

Terence McCutcheon: may be dismissed by the time we reach that period. kind of interesting it's working out that way timelinewise. but actually the dismissal would come by the end of February. the other one is Gayorg is our current chair. Okay, with no other qualms,…

Udai Solanki: Good to know.

Terence McCutcheon: I'm going to see that as a passing motion, if you will. So, five committee members to be elected in April 2026. please do note that would be for a two-year term as well. So, u I understand our expiring members not here, but when you are marketing to others, please do advise that a two-year term has been approved.

Terence McCutcheon: and so that would be the expectation when they sign on. More details will come out with the election data. So, I'm going to let Christian give the updates on the accelerator program specifically, but it does involve budget to an extent. so keep in mind that the OSC would need to decide whether or not we wish to write a contract that promises funding from a future Treasury withdrawal or whether or not we just want to pay out what we have.

Terence McCutcheon: in that bucket. Additionally, we also need to confirm if the committee is willing to divert all funds to one supplier to manage the delivery of the accelerator program or if you'd prefer that be milestone based, meaning that they would only be able to pull certain amounts of the funding at a time and we can decide how many milestones that is because that's still under contract. But let me hopefully pass this to Christian to give the rest of the updates.

### 00:55:00

Christian Taylor: So to make this kind of have impact we've been able to consolidate a partnership with both Chinstrap and Storm for what we have allocated in the budget to do all three programs and include a demo day at the end with mentorship available. that'll run the full cost of the budget and it's only going to be one workshop not a series done. It's the most realistic thing.  commercialization working group already gave their thumbs up for the scope. and Storm has agreed to ride the worry of the ADA price fluctuation and take what's there. I'm encouraging for them to take administration of the program.

Christian Taylor: and my current thoughts on they did put in a request that if ADA drops even further. either we have some mitigation strategy where we include in a future treasury budget pending that gets approved or we could pull from the project support bucket since this program does support projects. There is that delineation we could try to explain. or we delay the launch of the accelerator till the price is more reflective is kind of where I'm going with it rather than doing another promise. but I rather pull from project support rather than promise on a future withdrawal we have no control over if we were to do anything like that. So that's just the update. I also sent the proposal over to Chinstrap to make sure they're okay with it since they're being included and wrapped in this.

Christian Taylor: But we also are open to do the milestone program if y'all want to do it that way. It's just more admin on our side to facilitate that. and I will link that proposal in the Discord shortly.

Terence McCutcheon: All right. Questions, comments, concerns, anything on the accelerator program updates?

Christian Taylor: To clarify too, Storm would be taking ownership to get these projects prepared and in front of investors on their demo day.

Christian Taylor: That's the key thing there. So,

Udai Solanki: So just trying to understand in isolator program one is that incelator they have the admin fee.

Udai Solanki: So of course that's one part but the people who participate in this program do they al get the kind of advisory and kind of support or are we talking about funding as well  There.

Christian Taylor: So the basically people…

Christian Taylor: who come through the program will get a three workshop series to help them figure out how they commercialize open source software, how they get ined

Christian Taylor: business model strategy and pitch texts together and then product market fit and technical validation. then at the end of that they get put in front of investors for the demo day and do mock pitch and then they have onetoone mentor options available. Now the program we've already slotted 5,000 goes to chinstrap for the option one. The other 45k will be split from storm to all their mentors in the education program as well as the investors that come on board. anything additional from this is where we potentially do odd hawk project support requests from the projects themselves if they need additional support because that's kind of what that program is meant for anyway. But the reason I'm doing this is because with the way ADA getting any kind of workshop series quality like this with also getting in front of investors for the budget we have is almost near impossible.

Christian Taylor: So, I had to pull some strings to get them to agree to this. so I think the idea of this is to pilot if this accelerator is going to be even workable and something to potentially help build a more native Silicon Valley in the future. because I think the only other options right now is like the Tech Stars or…

Christian Taylor: Draper U. and those are big budget funds right now. So this is just to see if there's interest in this kind of thing for project but yeah

Udai Solanki: Yeah. Yeah.

Udai Solanki: Ultimately, yeah the help I think could be appreciated but I think ultimately these player will come that if they can get funding either from here or through some investors kind of the thing right so that if we can be successful in that level I think this program can attract lot of  Trust. Yeah.

### 01:00:00

Christian Taylor: Everything else we have in the possum is towards open- source projects. This is the only one that comforts those postc catalyst business products and trying to help build more mature projects that way.  So, yep.

Bernard Sibanda: Yes, I am aware of an accelerator program shared with the ambassadors. I think it's run by Kadano Foundation.  I want to find out how will this one be different to that one.

Christian Taylor: So, the venture hub, we've already been in contact with them with the commercialization working group. Their, programs, I think Storm ran the first one if I'm not mistaken. that's why we were put in contact with them. this one's different in the sense that it is more general projects and focused towards post catalyst projects in particular. I mean anyone can still apply but you're going to get an exclusive commercial open source software course and then the other two are the more generic things. and the venture hub on their next cohort specifically focusing on RWAs and DeFi I think.

Christian Taylor: So they actually have topics that they're choosing for their program. But what we're trying to do is if this program is successful is to partner with the venture hub and create something that's more not entitydriven…

Christian Taylor: but have a CDC equivalent that helps commercialization activity that brings everyone together because what we want to do is provide multiple pathways and multiple options to everyone. and the other differentiator is our program is a virtual. we won't have a on site that I'm aware of. So, that's the other piece.

Terence McCutcheon: All right.

Terence McCutcheon: Quick note here that everything that was pulled for appears to have passed. I will obviously confirm that with the meeting minutes as well. I know we're down to basically one minute, but does anybody have any questions on anything that we discussed today? Anything that you need to note? I'm going to give another ploy that says if please can we update the activity level in Discord? obviously I understand everyone is busy. but I'm kind of a chatter box to myself at the moment. minus Sebastian coming in at some times. So, if we can get a lot more active there, just kind of keep an eye on that. Let's increase our async communication here. That way when we get to these meetings, we are all more well informed.

Terence McCutcheon: And again you can DM me on certain stuff, but there's not much that we can't talk about as a group. so please just put it in the channel and any questions that you have in depth and let's get into it. thank you everyone. See you in a couple weeks.

Christian Taylor: Thank y'all.

Sebastian Pabon: All right.

Udai Solanki: Thank you.

Jordan Hill: Hey  Yes.

Udai Solanki: Thanks everyone. Bye-bye.

Bernard Sibanda: Thank you.

Reshma: Thank you.

Bernard Sibanda: Hi everyone.

Reshma: Byebye. Please hold up.

### Meeting ended after 01:03:54 👋

This editable transcript was computer generated and might contain errors. People can also change the text after it was created.

  
**