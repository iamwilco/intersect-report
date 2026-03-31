**

## Technical Steering Committee - 2025/10/22 08:22 CDT - Transcript

# Attendees

Adam Dean, Alexander Moser, Arnaud Bailly, Benjamin Hart, Christian Taylor, Jessica Gilbert, Jonathan Kelly, Kevin Hammond, Markus Gufler, Neil Davies, Nicolas Biri, Sebastian Nagel, Terence McCutcheon

# Transcript

Nicolas Biri: Hi everyone.

Kevin Hammond: Nicola. Hi Johnny.

Nicolas Biri: Okay.

Kevin Hammond: Hi T. How you doing?

Jonathan Kelly: Hello, welcome back.

Kevin Hammond: Thank you. How's it been?

Jonathan Kelly: Some interesting sort of light on agenda meetings recently and I think we don't even have an agenda today. Absurably.

Kevin Hammond: There is because I've just put one together.  John, I'll paste it into the chat and we can decide what to prioritize. I haven't managed to go through the actions text. I'll just take a quick look at those.,

Terence McCutcheon: So if we see here 10:15 publicize  STO participation in governance action.

Kevin Hammond: So, I'm not seeing anything in the active notes here. Wait a minute. Is it further down? ober 29th to October 22nd.  Okay.

Terence McCutcheon: Looks like raising awareness about parameter changes which is still being done. That technical or we can fix and the actions from the previous meeting on the 8th were just related to the linear layout conversation…

Terence McCutcheon: which is already on the agenda. It's okay.

Kevin Hammond: So, I'll just pop into the chat the actions from last week and Neil Neil and Nicholas you have to leave at…

Kevin Hammond: what 1500. are there items you want to prioritize? Okay.

Nicolas Biri: one that might miss me is…

Nicolas Biri: because I saw Arno it's I think Sebastian mentioned yesterday in the TSC channel that it will be nice to have a chat about antithesis. So we probably need to add this to the agenda probably especially as Arno is here.

Nicolas Biri: he's nearby at least because based on his scam he's is not exactly here but he's connected at least otherwise regarding the prioritization I don't have any concern I guess on the layer statuses Sebastian can give an update so you don't need me on the other side I don't need to lead anything so I'm good with  Whatever we want to come first. Yep.

Kevin Hammond: So, as a guest. we could start with Arno and then allow Arno to leave us whilst we continue with the rest of the agenda. does that work? And the linear layoffs I basically put as a placeholder so we could have a catch up and…

Nicolas Biri: Okay, good.

Kevin Hammond: further discussion but we could also I imagine postpone it until next week if you and Neil are not here Nicola. Does that sound sensible? Yeah. Brilliant. So, I know why don't we let you kick us off with a discussion. first of all I'll formally convene the meeting. So, by my calculation we are quarre this is the technical steering committee meeting of the 22nd of October 2025.

### 00:05:00

Kevin Hammond: And we have one, two, three, four, five, six, 7. I make it Four, five, six, seven, e Nine voting members present. So, almost complete Great. So, first item on the agenda. I know you've very kindly offered to present the status of the antithesis work to us to explain…

Kevin Hammond: what it's all about and to give us an overview. have you prepared any slides for that or

Arnaud Bailly: Yeah. …

Arnaud Bailly: not really. Thank you for having me first. I haven't fully prepared slide, but I have a couple of things that I can show you and I can share the links for further investigation. just to set the stage or to manage expectations. my goal here is to seek guidance from the technical steering committee regarding this project and whether or not it would make sense to keep pursuing this project and to keep working on it and if the answer is yes how this would be done and how this could be done should it

Arnaud Bailly: and especially when it comes to the question of first of all funding the project both for the license fees and for the work around the project to make it usable and to become cardo community asset. so maybe just I'm going to share my screen I think that so yeah maybe let's start with the beginning.

Arnaud Bailly: I'm not sure who is familiar with antithesis but antithesis is it's distributed systems simulation testing tool that is built by a company of the same name which offers the ability to test a complete system. and I will come to that Neil if you don't mind. I'm trying to make sure unless everybody is familiar with which mean that I can completely skip the introduction but maybe it might be useful to remind us everyone what's what it is. Yeah.

Alexander Moser: I think it may be useful for the recording and…

Alexander Moser: honestly I also don't mind to hear it

Arnaud Bailly: But I will go quickly over it just like I won't spend 10 minutes explaining just to give a quick recap of…

Arnaud Bailly: where we are at. so it's a distributed test testing system that we have been experimenting with in March or February we got in touch with the team and we started prototyping and proof of concept within the card foundation. more precisely with the HAL team and part of the frastructure Nibson and Leio cup from the CF trying to understand whether it could be useful and if it could be useful and what problem exactly it solves.

Arnaud Bailly: So the problem it solves seems to me for the current ecosystem is the ability to be able to run complex test for a scaled down network to run complex tests in an environment which is first of all deterministic.  So this mean that we can reproduce all the test and we get the benefits from typical property testing that we are used for we are used to and it also provide the ability to explore and to fuzz the environments and to fuzz the various execution paths and to inject faults and faults which are network faults which can be memory

### 00:10:00

Arnaud Bailly: memory consumption or memory CPU throttling chaos monkey by killing various nodes So that's what it does. we have been working on this for a few months now in two directions. trying to understand if it could find issues.  So we had a first phase back in April May where the team has been working on testing the calendar itself and we found a couple of issues. So some of them were expected and we found a couple of unknown bugs actually one of them I think led to the need for a patch because it was considered a security bug.

Arnaud Bailly: since then we haven't done a lot of efforts on the testing side because we have been trying to work on making the tool more usable for the community at large.  not only the calendar team but more in the spirit of the non- diversity efforts and to make it possible to run test or to make it easier to run tests for any team that would be interested in using the infrastructure because so far until this point it was mostly something that was reserved for I mean it's a SAS system so it has authorizations and it can  only be used by some people from within some organization and so on.

Arnaud Bailly: So what we did was building some tooling to make that easier. And this culminated in the node diversity workshop that we had in September where we had a first workshop with the entities team trying to understand how the tool could be useful for various node implementers. And by node implementers mean we mean not only full node or full consensus node implementers but also maybe data client nodes, all kind of people implementing stuff around the network. Johnny Yes,…

Jonathan Kelly: do you mind showing the GitHub repository specific to Cardano on the meeting and also for the minutes just a link to that repository would be useful for people to go very further.

Arnaud Bailly: I will share the link in the chat. far okay you have them so right now the repository is in the foundation so we are revamping the documentation…

Jonathan Kelly: I already have. story.

Arnaud Bailly: but most of the work and the action happens there so that's where we have the various assets to be able to run this we have been working on one of the things that we have been working on within my team  was what we call NTCLI which is not very good name but it is what it is. The idea being that we are building a tool and a common line interface that will make to make it easy to trigger test run for anyone who is in control of a GitHub repository which can control and build the assets needed to run anis. with the goal of tracking and tracing those usage on the Cardano blockchain itself.

Arnaud Bailly: So basically what NTCLI does that it records a test request using some onchain and onchain smart contracts and an on offchain oracle and agent to read transactions and trigger yes thank you Sebastian that's a very good one and the reason why is because first of all I personally think that we should duck food our development  for and second it seems like because we have this shared resource which is the antides infrastructure which we are paying for it seems that it would be quite useful to be able to trace to track the usage of this resource and to understand whether it is used and by whom it is used and why it is used for.

Arnaud Bailly: this has some side effect around the fact that if you trigger a request for some tests then you will get some results and we have some kind of mechanism to encrypt the results so that we don't leak test results which might potentially have a security implication and it's only in the second stage where we can really interpret and understand the results that we can start to work with the teams or the team involved to do something. so that's where we are at.  So we have this store and what I've started working on and the reason why I requested to maybe present something with it with the technical steering committee is we have something that works. We have I think some convincing evidence that the tool is useful.

### 00:15:00

Arnaud Bailly: It's useful both for testing the car node itself but also it's useful for testing more widely the ecosystem by mixing and matching different kind of nodes. So we were able to run test mixing the Amaru node and the K node. but obviously given the fact that the environment is a bit adversarial the software needs also to be prepared for this kind of adversial behavior.  So this mean that some other nodes or tools that have been built. So I mentioned some of them here might not be at the stage where they can survive long in this environment. but yeah and so I've started writing this document with the idea of proposing that this effort be supported and funded by the Kalano treasury itself as a community asset.

Arnaud Bailly: so far it's been funded by the CO foundation and we have the funding until the end of this year. and now the question is what's next? Do we care? is this something that we want to build and to turn into a community owned and community-led assets and something that would be useful for all kind of implementers that are working with the maybe core network components.  It could be and obviously that encompasses the core team but the core team having been working on this for several years they already have some internal tools but there might be end to end test that would be interesting to be able to run there.

Arnaud Bailly: it will also be interesting potentially as a one gauge or one data point when it comes to deciding about confirance of various implementations, confirmance of protocol changes that would impact potentially several clients and so on. And yeah, so that's where we are at. I would be very happy to share all this stuff with you. So I'm going to share the documents that you have it and you will be able to understand what's inside it. and yeah I guess I don't want to spend too much time of your time but that's where we are at.

Arnaud Bailly: So my ask is to get some feedback potentially asynchronously or offline obviously but yeah

Kevin Hammond: Johnny.

Jonathan Kelly: So there's three potential funding paths for this. Would you view this as something that would come under something like the open source office tooling sustainability or would that not be enough of funding towards the idea of what you think it would cost? Could it go through the intersect budget process for 2026 or is it something that could be proposed directly on chain outside of intersects budgetary process?  Which do you feel is the most viable path?

Arnaud Bailly: I think the optional one is so I think I will answer Adam question and it will answer a question. The license cost for anthesis is $400,000 a year. That's license cost.

Jonathan Kelly: which I think takes it outside of the maximum funding available for tooling sustainability from open source.

Arnaud Bailly: 

Arnaud Bailly: Yeah, So that's…

Jonathan Kelly: So it would become either part of the budget for 2026 through intersect process or a direct onchain proposal.

Arnaud Bailly: that's why I didn't pursue the avenue of the open source funding tool because it seems like it's a larger share given the cost of the license. and…

Kevin Hammond: That's just sorry.

Arnaud Bailly: so yes so you have everything documents that I will share with you…

Kevin Hammond: Sorry to clarify. I'll know that's just the license cost. Are there operational costs as well? Eg cost

Arnaud Bailly: but all in all I think that from our experience so there is a license cost there is some maintenance cost if we agree that having this kind of tooling around makes sense and I would estimate something like around one FTE to keep the thing working on to keep the thing working and maintain the tool maybe not one FTE for years but at least to put the tooling at the level where it's basically self-sustaining and all in all including a bit of hosting for some offchain services and…

### 00:20:00

Arnaud Bailly: whatnot. and then there is the cost for each team to bake and define their own systems. yeah so that's…

Kevin Hammond: So to answer Adam's question about funding cost,…

Kevin Hammond: ad Adam, we're talking something in the order of half a million dollars to $600,000, something like that. plus the cost for the teams of complying with the antithesis requirements.

Arnaud Bailly: 

Arnaud Bailly: that's roughly the idea something like that.

Kevin Hammond: But direct cost of half million dollars or more. Neil

Neil Davies: No. I stuck some questions in the chat because I know Right.

Arnaud Bailly: Yeah. I don't know…

Neil Davies: So I was just going to say so to me right yes there's the get out of bed cost…

Arnaud Bailly: if you want to answer me.  Yeah. Yeah.

Neil Davies: which we've just discussed half a million right the thing given I had interaction with the people doing this and I got feedback from them. the key question is is it if you put a human being's effort into this and a human's e effort into some other stuff what's the relative return on investment mod forget about the get out of bed cost take it from that's really important here because it was my impression which I'd like to get that this was although it did find one or it was my impression that it wasn't cost effective in that area right number one but I'd like to

Neil Davies: have that impression done. Part of that was because there was a non-trivial rate of false positives as far as I understood. when they ran the darn thing, they got back antithesis failures which turned out to be impossible to happen in real life due to various things. So I mean I don't know the false positive rate is important because that eats up a lot of human effort. I think this issue it would be a Cardano based resource which brings it for those who've had any academic background national labs or European style lab type thing where now you're into who's going to that one person to run it is probably an underestimate because you've now got an administration to turn around to construct to who gets funding who makes the decision who gets access who handles the contention for access to that resource.

Neil Davies: It's like you got a big bloody telescope and you got lots of astronomer teams competing to use it. Who's going to make the decision of who gets to use it next? Right? These are the questions I think that have to home viewing cost. is it robust in a regression environment? If I can I reproduce the faults regularly if I rerun it,  because basically I want to be able to go back having fixed the fault and know it that if I use it 10 times the fault turns up twice right and I rerun it I still can't and I always get the fault reproduces a question it's really important and then you mentioned conformance testing is this genuinely something that could scale to act as a conformance testing requirement it can act I don't think it can because you're talking

Neil Davies: about one piece I mean does it multiply the human beings effort being put into it right to me that's the question does it give that multiplier so that we're getting more for the developers because in some sense the developer time is our most restricted resource that now they don't need to be answered now…

Neil Davies: but you were looking for input those are the inputs

Arnaud Bailly: Thank you for that.

Arnaud Bailly: Yeah, I'm probably won't have the time to answer now, but I'm definitely taking notes and we provide sor answers. yeah. thank you for that. Yeah. I will write down try to provide the answers to those questions. probably not I mean to give a short answer I think so yes regarding I think the false positives that's true that was true at the onset and the initial phase that's definitely the case especially because anything it needs a bit of tuning to the particular thing we are trying to test we spend some effort reducing that so right now we basically have zero

### 00:25:00

Arnaud Bailly: possibilities. On the other hand, doesn't really have the skill set or the incentive to do the work that a normal or an actual QA team should do which is actively trying to change bugs and bank configuration. we are more working around the tooling and making the thing more useful and more accessible than really working on trying to find bugs in the cloud node or any other nodes for that matter. But so far yeah we have removed this noise that we had initially which was a bit annoying.

Arnaud Bailly: and to the question about the conference testing system I mean it's a bit hard to answer but as a multiplier we clearly have a multiplying effect because we know that for I mean the equip we have something like a 50 100 ratio between the actual execution time and I would say the amount of testing that is really run against the system because of the fact that the system runs at a much faster pace.

Arnaud Bailly: Basically if I may this to me entis it's something like IOS sim but scaled up to be able to support any kind of software not only has code that's basically…

Arnaud Bailly: what it is with a bit more stuff and around analysis about the bugs and the various paths they provide stuff that might be sense.

Sebastian Nagel: plus fault injection…

Sebastian Nagel: which is nothing which does right so it's detministic simulation and reproduction

Arnaud Bailly: Yeah. But at least for this part.

Sebastian Nagel: but then also fault injection and all of this on a kind of operating system level …

Arnaud Bailly: Yeah. and…

Sebastian Nagel: which is independent of technology s***.

Arnaud Bailly: and also with time travel debugging ability.

Arnaud Bailly: So this mean that when you find a fault you can basically travel around your system in time and in space of course depending on…

Arnaud Bailly: how much tooling you have in your images and it's still not trivial obviously but you can really do a lot so I was thinking about the comparison in terms of the ability to play with the

Sebastian Nagel: So I was not saying that doesn't support fault injection.

Sebastian Nagel: I want to say this is kind of having fault injection batteries included which IOM for example is But of course things on top can do fault injection tests using iOS which we are to comment on this response on the chat. is this technically interesting?

Sebastian Nagel: As we're a technical steering committee, is this something which Kadano could benefit from or is it worthless because everybody has better tools already? what is our stance or maybe what is the ask? Yeah. Mhm.

Arnaud Bailly: Yeah, I think that's my ask ultimately do you think it makes sense to pursue this effort?

Arnaud Bailly: If you don't think it makes sense then basically that's at least one data point and one answer from technical experts. So we need to take action after this segment.

Kevin Hammond: Neil, Neil,…

Kevin Hammond: Nicola, I consciously need to go. So, do you want to make

Neil Davies: Yeah. Yeah.

Neil Davies: My point is I'm sure if you with unbounded effort and unbounded time is a useful tool, My problem is costbenefit analysis. And my main value for this is not actually the dollars, it's the humans, it's the human cost because the humans are the things we don't have enough of. That's sort of my point. If you want to technically I'm sure it can explore parts of the space. but it's the whole problem with any form of walk around a random space. whether they will occur in practice, are they reasonable? there's always you're reducing a risk. Is it worth that investment?

Kevin Hammond: Nine, do you want to quickly

Neil Davies: Always the question. And now I got to go. Bye-bye.

Nicolas Biri: Yeah. yeah,…

Nicolas Biri: I guess the major question definitely will be as the cost benefit ratio. I spoke with Brian who have tried the tool during the diversity workshop and he was quite pleased actually to see how fast he was able to spot a bug into the simulator using antithesis. So it's one evidence that we can get value out of it. Is it enough value to cover the cost of the effort? I guess it's definitely an unknown.

### 00:30:00

Nicolas Biri: It also depends on how much traction we could put into it. I guess again it comes down to does the community want to fund this effort and how much traction can we get out of it and what will be the benefits of this traction afterwards. from my perspective if we have enough money to spend this effort for one or two years gather some evidence of the use of the use of the tool or the lack of use of the tool. It will be quite interesting. but it's just one view among the whole community. So yeah that was my two cents on this.

Markus Gufler: My additional scent would be that this is also a question now to know or…

Kevin Hammond: Thank you. Marcus

Markus Gufler: 

Markus Gufler: to all of us here. so Sebastian mentioned that everyone or the different node teams with their architecture and coding environment have already some system in place but that's specifically for them and may and this now is the question will this antithesis or could this become let's say the agnostic the neutral place where all the nodes can appear

Markus Gufler: here on a comparable place that is not very specific or let's say focused more on the Heskell side or on the RA side or some other language side but it is just more the neutral place where every note with his team and when they come out of their individual environment and then go to a public place where they also show that they work or they are buck free or they can perform  from specific tests in a comparable way.

Kevin Hammond: So I'd say that some general testing framework that allows comparable testing between alternative node implementations is very viable.

Markus Gufler: Mhm.

Kevin Hammond: Marcus, the question is whether antithesis is that testing framework. it may be that it's part of a bigger test framework.

Sebastian Nagel: What we've seen in the node diversity workshop is I think everyone has been appreciating or not being upset about the level of interface or level of substraction they have been picked right so antithe thesis says everything needs to be a docker container for that matter it can be virtualized and run in this way some teams were picking up quite quick on this I must say we had the go people very much having a dingo node running in like a kadano

Sebastian Nagel: node cluster which had been prepared by our knowances team beforehand but having this not only consensus node but also data nodes in such a small scale but very adversarial or hazardous environment as I think it's very much actively fault tested having that up to speed quite quickly was good to see I think the biggest question for my end is not so much about the cost benefit it will be

Sebastian Nagel: costing a lot in the beginning but I think if we can make it useful it will pay off as it is going to be very much a system everyone can use of course it should be considered but I'm more worried about can this be productively fault testing right so is it not too harsh and…

Terence McCutcheon: Okay. Thank you.

Sebastian Nagel: can we make it more useful in terms of exploring the kinds of systematic faults we  care about maybe also what you mentioned Kevin what is the right level of operational behavior we want to see from a healthy block producing node in such an environment what kind of scenarios needed doesn't need to pass but I think this is also to be explored and should be maybe just in scope of the next phase of this I think a small team I heard one or two people only working on the CF kind of to make this work and getting it up and running is maybe too little to kind of

Sebastian Nagel: really explore that fully whether this can be done. so maybe some kind of benefit and must be given to we don't have it like there may be still a lot of false positives or kind of lots of unrealistic or too harsh environments and scenarios in the beginning but this must improve in the next phase to see it kind of for continued mid and long-term use.

### 00:35:00

Kevin Hammond: Great. Thanks, Sebastian. thank you very much, Arno. …

Terence McCutcheon: Perfect.

Kevin Hammond: does anyone have any final comments on that? Because I'm conscious there are other things we should be discussing in this meeting.

Arnaud Bailly: Thanks a lot.

Arnaud Bailly: Thanks a lot for having me and…

Kevin Hammond: Yeah. Thank you, Great.

Arnaud Bailly: happy to answer any questions online offline or asynchronously I mean where to find me so whenever and wherever you want I'm going to so we have some also planning next week within the scalation so I'm also going to ask what the coloration wants to do with that because we initially thought that this would be useful as a tool and it should be but yeah I agree that the human factor is important here because it's not magical. You still need to put the effort and the smarts and to put some thinking into what you are going to test and how you are going to testing and what you are really looking for and this is not trivial and the expertise to do that is not that common anyway.

Arnaud Bailly: The thanks for listening and…

Arnaud Bailly: having me.

Kevin Hammond: And we may call you back or…

Kevin Hammond: or otherwise engage with you maybe set working group to per Thank you very much.

Arnaud Bailly: Yeah, I'm in the Discord and everywhere. So, don't no problem to have more discussions around this.

Sebastian Nagel: Thanks.

Kevin Hammond: So I'm also conscious that Jess is here from IO so we had an item on the agenda which was reforming the hard fork working group. I penciled tax by that and basically as tax raised it within the TSC channel but we can also take it there.

Kevin Hammond: J Jess would you like to introduce yourself to the group and…

Kevin Hammond: then we can progress discussion on the reforming of the half working group.

Jessica Gilbert: Yeah, I can do that.

Jessica Gilbert: Say, hi, I'm working at IO and I guess taking on the role internally within IO to coordinate the hard fork release. I guess we've been talking at a high level about an upandcoming intra era hard fork and I think we're now at a point where we're ready to sort of propose the expected features and I guess I wanted to bring it to the group today to get some feedback on.

Jessica Gilbert: So it was my intention to share the document ahead of time. sorry that hasn't been possible but yeah I guess that's who I am and why I'm here.

Kevin Hammond: Great. Thanks,…

Kevin Hammond: Jess. So, I've shared a link to the document in the channel. what I would say is for formally what we should be doing here is to get input from the community on the proposed scope of the hard port. we shouldn't just be presenting it as a fate comply to the community of course and that what we should probably be doing is to delegate to the hardworking group to help us define that scope and to engage with the community to ensure that the scope is accepted. does everyone agree with that?

Kevin Hammond: We can look at this scope now if we want and provide some feedback on that if we wish. Tech text, what's the schedule that we were talking about for restarting the hard working group?

Terence McCutcheon: I was still waiting on some additional feedback internally. basically there was some of the IO team or rebuilt IO team was being brought up to speed. but my understanding is working on getting something set up before the end of the year.

Terence McCutcheon: That way we're kind of into a cadence. So, probably weekly or fortnightly starting soon and then ramping up to weekly kind of December, January as needed.

Kevin Hammond: So when are we expecting the hard fork to take place now?

Kevin Hammond: Jess I've been away for a couple of weeks so I've missed the release meetings.

Jessica Gilbert: Obviously that's down to the community to decide.

### 00:40:00

Jessica Gilbert: But I was hoping that we would be in a position to pull it to an onchain vote middle of January.

Jessica Gilbert: But obviously all of that is down to when the features are ready when we're in a position to push it onto test nets for people to be able to and hit readiness. But the the goal was that we would be pushing it to an onchain boat middle of January and the goal would be to start obviously socializing it now getting feedback and ensuring that we haven't missed anything that is important to include in it.

Kevin Hammond: Great. So,…

Kevin Hammond: so what I'm saying, Jess, is obviously the timing depends on the status of the delivery. but if we're looking for an early 26 potential hard fork date, I think Jan January is possibly on unrealistic.

Jessica Gilbert: Sure.

Kevin Hammond: Okay, just to set the expectations but it seems that what we should be doing is to convene the hard working group as quickly as possible because we've only got one to two months left in 2025 and there's going to be a lot of work to get things prepared for a hard fork. so we shouldn't be delaying any longer and…

Jessica Gilbert: Sound it.

Kevin Hammond: we should be co-opting members from this group to join that. So I know originally he'd spoken about expanding the half scope of the half working group to be basically release management. and I think that kind of makes sense.

Kevin Hammond: We should be thinking not just about the next hard fork, Jess. We should be thinking about the whole cadence of releases, about the hard hawk, the Dystra hard fork that's coming up after this. And this should be a standing group. So it's got a cadence where we look at we first of all identify the scope scope we agree the scope with the community and…

Kevin Hammond: we then ensure the development gets done that will lead to the hardcore or other relief taking place.

Jessica Gilbert: Okay. Yeah,…

Jessica Gilbert: I mean that sounds sensible.

Kevin Hammond: So I know we had a few volunteers to join that group before.

Kevin Hammond: Adam, you were one of Johnny, I think you were one of them. Is that correct?

Sebastian Nagel: Me too. I just had raised my hand also. I would like to be part of that group when it starts again. I think we speculate even to use the release time slot the other discussion time. But yeah my hand raised is also I was brought to my attention that some people in IO believe I mean we name hard forks and there has been a proposal for naming the next upcoming hard fork in respect or…

Sebastian Nagel: kind of in response to Maxon Rothsam's passing recently. there was one consideration we could bring to the hard committee or working group right away besides talking about the scope as proposed of course I hope I don't mistype now maybe there's a space between his lost and…

Kevin Hammond: Drew would like to type his name into the chat for his record.

Kevin Hammond: Yeah.

Sebastian Nagel: his touch yeah was Dutch no it was more cons.

Alexander Moser: Sebastian, was that discussed with his family?  Initializer.

Sebastian Nagel: So it was somebody said initial idea level I think Alexi from the ledger team brought it up. I had it in my mind too. Probably others thought about it. We had left diploma on the last hard fork unfortunately too. we should try to make more hard forks than people dying. That would be maybe a goal.

Sebastian Nagel: I think we should discuss with his family. that's a good point. Thanks for raising it.

Kevin Hammond: Okay, great.

Kevin Hammond: So, I think again we can delegate this to the hardworking group to progress. we've established principle I think of putting the name to the community prior to the hard walk as an info action.

Kevin Hammond: So, that's one thing that we would want to put to the hardworking group. So rather than taking a decision on behalf of the community, we're presenting it to the community to allow them to comment on that and to agree with that or not. Yeah. So Adam, you're saying we need to give community enough time to support the police primitives. Stu, would you want to speak to

Sebastian Nagel: And this is also me presenting that somebody suggested it in initial thought only.

### 00:45:00

Adam Dean: Yeah, I mean it's what we hear every single time now that there's a hard fork. this kind of ivory tower concept from IO of we pushed a release. All you have to do is upgrade to it and it's good to go. We can hard fork. which doesn't work when there's new Plutous primitives that might break downstream explorers and downstream transaction building libraries and everything else because every time the Plutous cost models change, which is what happens every time there's new Plutous primitives, it breaks all the downstream tooling. So again, if we aren't release ready today,…

Jessica Gilbert: Absolutely. And the intention is absolutely there's no need to rush this hard pork.

Adam Dean: there's almost snowballs chance outside of an utter dire emergency that we're hard forking in January. so we definitely need to be working on longer time horizons now that we're community governed.

Jessica Gilbert: I know people are keen to have it out but there's no reason like you said for it to not follow proper process. and whilst January was a goal like you said the only way we would be hitting it in January is if we were sort of code complete within the next week or two.  So whilst that was almost an aspiration ultimately the timeline for the hard will be governed by the community and the steering group

Sebastian Nagel: Yeah, we had discussions even on the node diversity workshop also in this group and other groups I think between the kadano nodes that's at the epicenter of the whole downstream and everything right so having a release candidate for that version upcoming version whatever what the whole version includes between that and the hard fork three months would be a good time frame we believe between this very first tier one infrastructure then we have downstream tooling  infrastructure sometime needs to change and now deps in this case maybe with the Plutus primitives. I think yeah so I just want to voice that this has been roughly what people felt reasonable in the past in conversations I was involved in and yeah that is definitely a topic for the group too the art frog

Kevin Hammond: So in Texas is raising a point. Alex may want to comment on that about the parameter changes. So absolutely any parameter changes need to go to the parameter committee for this particular  It's an intra era hard talk and we're not expecting it to be especially complicated but there is still a process that has to go through discussion process and recommendation process.

Kevin Hammond: Alex. Yeah.

Alexander Moser: Agreed.

Kevin Hammond: And Adam, you're pointing out that we need to allow for the holiday period in this for the developers for the downstream tooling developers …

Kevin Hammond: but also for the GREs and SPOS's who would need to vote on the hard fork itself. So we need to factor that That's why I was saying January is unlikely Jess just from where we are already.

Jessica Gilbert: And like I said,…

Jessica Gilbert: I mean ultimately that's an aspiration, but we need to form the hard working group and obviously get feedback. I mean the purpose for today really was to take the proposed expected features and to start getting feedback on that and give people the opportunity to flag if there's anything obviously missing because I guess until we've kind of fixed the scope it's really hard to fix the date but January was just an aspiration but obviously it's subject to following all of the proper processes and…

Jessica Gilbert: that isn't a deadline  line. It's an aspiration. Go text.

Terence McCutcheon: So just some basic tracking at the very least from here maybe Jess I can get a list from you of…

Terence McCutcheon: who all needs to be initially invited. My other assumptions understanding as of now would be Kevin, Adam, Johnny and Alex as optional. Sebastian you said you yourself as well or

Sebastian Nagel: Yeah, I'm definitely interested. I'm not sure what required and optional means. I think hard for coordination group is probably open,…

Terence McCutcheon: Were there any issues with that list that I had would be the important question I was asking.  Hey,

Sebastian Nagel: So, anyone who wants to learn about the next hard fork and wants to chime in should be welcome or have at least a chance to get into it.

Kevin Hammond: We'll need to keep it fairly focused initially, ian. but expand it out as we go. let's take this so I don't think we'll get a complete list in this meeting text. what I propose to do is we take this offline and u and we make sure that we invite all of those who are essential to the initial meeting and any member of the technical steering committee who should be able to be involved in that meeting either the initial one subsequent ones.  Great. Yeah. So, Alex, do you want to speak to PCP4?  This is the premise change proposal.

### 00:50:00

Alexander Moser: Yes I can briefly mention it. PCP00004 was initially planned to go out together with the governance action we have currently planned which is on prep already that was spun up through PCP00003.

Terence McCutcheon: What the f***?

Alexander Moser: PCP stands for parameter change proposal. This is the formal way to talk to the parameter committee or make proposals for these parameter changes. And the Bluetooth cost model team reached out and said that they would like to adjust certain V2 values to match them closer to V3 ones. As with the hard fork, new ones are duced. So the V2 cost models need to somewhat reflect also those new ones that are being introduced in the hard. That was probably not the best explanation, but I think you got the gist.

Kevin Hammond: Great. Thanks,…

Alexander Moser: I was put on the spot too quickly.

Kevin Hammond: Alex. Sorry about that. So, again, conscious of the time, a few things to Be good to get an update from you. you've just started to mention the current parameter update proposal,…

Alexander Moser: Yep. It's fine.

Kevin Hammond: which is being prepared for onchain. Also, Johnny, a report on the disaster recovery fire drill will be great.

Jonathan Kelly: Yep. which

Kevin Hammond: Alex, are you still feeling on the spot? Go ahead.

Alexander Moser: The current parameter change governance action is going really well. Ryan from Intersect helped us get it out on preview and on preprint and the rationale is now final. All the signatures match and the hashes and we're basically ready for go live. Ryan is the guy indeed.

Alexander Moser: And I believe now we are waiting for ratification on the test nets to see the actual result of enactment and then we hit the button on mainet.

Kevin Hammond: And for the person anyone watching the recording, this has changed to the max transaction execution units for the memory units for Pluto's right.

Kevin Hammond: So it's an increase to the execution units that available for Pluto scripts. So it will be interesting to see the effect of that on mainet.

Alexander Moser: Timeline wise,…

Alexander Moser: we're looking at second week of November as a possible date to submit on mainet. That depends a bit on  Test that.

Kevin Hammond: So again, you need to watch the dates because you'll be certainly getting into the Christmas break period for that to be enacted with potentially a six week time voting time. Brilliant. Thank you very much, Alex. Johnny, do you want to update us on the fire trail?

Jonathan Kelly: So, we killed Sanset last week. We did scenario two as a test. So, we stopped all block production. So, the way it works was because Mike has control of over delegation, he delegated 1/5 of all stake producing delegations to each of the six SPOS's participating. So, I had 1/5 of all stake as did each of the other people.  So we stopped all block production for over 24 hours which is over the equivalent 36 hours on mainet. if you convert it with one epoch it's like 7.2 hours before you hit that not able to add a block to the chain issue. We verified that it wasn't possible after 24 hours and you weren't able to get the ledger information at all and couldn't build upon the chain so it was just locked in place.

### 00:55:00

Jonathan Kelly: So then we took our little group of six people and the scenario to recovery method mentioned resetting the wall clocks going back in time and running them at 10x speed, but practically there wasn't actually a method that we could find to do this. is anybody aware of a tool that does exist that allows people to reset their wall clock back in time and run it at 10x speed across a small group of SPOS's because this didn't seem to be an available tool.

Kevin Hammond: There was two that Nick Clark mentioned, Johnny. …

Jonathan Kelly: The tooling that we used was DB synthesizer, but that is not the equivalent of running a wall clock at 10 times speed. And we weren't able to source something. And we had been asking up until the test scenario for a number of weeks, Mike and myself, what tool do we use for

Kevin Hammond: so I said my memory is that Nick Clark mentioned such a tool or library that you could use. I can't remember what it's called,… but he certainly  Yeah.

Kevin Hammond: 

Jonathan Kelly: unfortunate unfortunately people not remembering…

Jonathan Kelly: what it's called and not being able to point us to using it meant that we couldn't use it. So what we did instead to recover is an alternative method which is to use DB synth And DB synthesizer allows you to take a VRF key and a KZ key and append to the chain up until the expected tip with a less dense chain of empty blocks.

Kevin Hammond: Yeah. Yeah.  Okay.

Jonathan Kelly: So you could rebuild the chain back up to the expected tip. and as long as the level of stake distribution in the Kzen VRF keys using DB synthesizer is enough to not have that large gap of over 7.2

Jonathan Kelly: two hours or 36 hours in the case of mainetap then you can recover and we were able to recover using DB synthesizer but it led to a large discussion about because DB synthesizer is something you run locally and you requires you to attach KZ and VRF keys to it would you be able to convince a series of SPOS's with enough stake weight to give up their VRF key and KZ key to get to that limping along  long density of blocks to be able to continue from where we are. So it would become a more centralized recovery method if you did that. Now it may be that practically that's the right way to go because the idea of synchronizing 10 times speed across the world wall clocks with block production happening without hitting a number of battles.

Jonathan Kelly: It seems very optimistic, but maybe I'm wrong, maybe it would work.

Kevin Hammond: The expectation Johnny was that nodes would be producing empty blocks.

Kevin Hammond: So if you don't need too many blocks to be produced.

Jonathan Kelly: Yeah. Yes. Yes, indeed. But if they're producing empty blocks at a 10 times rate versus real time going back in time to start doing that and you're trying to synchronize them across the world with a small group of participants is it likely that at a 10 times speed versus real time you're going to be able to synchronize those clocks so that there isn't going to be battles between the empty blocks.

Jonathan Kelly: No, I know. You just need enough density so that it meets the minimum requirement of time between each block.

Kevin Hammond: Yeah. Yeah.

Jonathan Kelly: And it's a 36-hour requirement, so it's not so bad. You're not going to have that many clashes. But the way we were able to recover was because I had 1/5if of the stake, I was able to do it just with my own KZ key and VRF key alone and build a limping along block production. Even if you did centralize this recovery method, the good thing is it is verifiable that all those blocks in the less dense chain that get you back to recovery are all empty.

Jonathan Kelly: So if people argue that this is a centralized recovery method, you can verify that nothing nefarious was done in the rebuilding.

Kevin Hammond: Yeah. …

Kevin Hammond: what I would worry about would be SBO's handing over VRF and KZ keys.

Jonathan Kelly: So, that was my concern in the meeting that it's on the recording.

Jonathan Kelly: Mike's going to put up an edited version of the multi-day meetings that we did about trying to get this recovery and that topic came up. People wouldn't be willing to give away their VRF key. Maybe you could convince them to do a KZ key and then rotate it, but it's quite unlikely even then. People are quite security conscious. the thing is it possible to run DB synthesizer in such a way that people could be pulled for their VRF key and KZ key information without having to actually give it up to a centralized actor if there's a way to do that where it could just get the required details without having the private key. That would be one way to solve for this.

### 01:00:00

Jonathan Kelly: But yeah, the thing is we couldn't find a tool that was explicitly able to 10x the speed of Cardano node production across a small group. It just wasn't available. We'd asked multiple times before running the test and nobody gave us an answer as how to do it.

Jonathan Kelly: And we're not done with testing. We'll do different scenarios. And if people do provide us with the tooling, then we'll test the 10x

Kevin Hammond: Anna, do you want to comment He's gone.

Sebastian Nagel: You're muted or your audio doesn't work. probably reconnecting.

Kevin Hammond: Wait for him to come back and he can then fill us in.

Sebastian Nagel: Yeah, here it is.  Yeah.

Kevin Hammond: He is Hello

Arnaud Bailly: Hello. Yeah, I just wanted to you can you hear me?

Jonathan Kelly: Yes.

Arnaud Bailly: Just wanted to say that I've been using DB synthesizer for testing purpose inside in Amaru and building test net and it's really not too complicated to turn to make sure that if you have trusted parts that can communicate with each others they can basically use this tool to share the empty blocks they are producing so that the keys don't leave the various parties.

Jonathan Kelly: Yeah, it wasn't clear from the help that was available in the tooling itself,…

Arnaud Bailly: 

Arnaud Bailly: I mean that's No, no, you can't do it right now…

Jonathan Kelly: but aha.

Arnaud Bailly: because but what I'm saying that it's not a far stretch to turn to Okay.  Yeah.

Jonathan Kelly: Yeah, I didn't think it would be a far stretch and…

Terence McCutcheon: Pretty

Jonathan Kelly: it was definitely a topic that came up it's in the governance chat ironically for some reason. so if you go to the Able Pool Discord, you can see that being proposed by myself. Is it possible to have people hold their own KZ and VRF keys and still contribute to DB synthesizer block rebuilding? Because that would be the most efficient method because you wouldn't have to run a 10 times speed node version or any of that.

Jonathan Kelly: you just build the density required chain of empty blocks in a distributed way that could then be slowly released to the people that are part as it goes into the relays across the network people then would be able to build upon that chain so yeah if that becomes something that the DB synthesizer can do then that might be a better method and…

Kevin Hammond: Yeah.  So they

Jonathan Kelly: if so then the SIP might better be updated to reflect that and actually mention DB synthesizer tool as a tool and reflect the fact that it can be done in a distributed way. And the next one we're going to test is scenario one where there's two different forks because of a bifurcated network. so there'll be two versions of Cardano node chain and then how to recover from that. So, we're still doing

Kevin Hammond: So to ask Adam's question, it sounds as if the actions are to write a report to highlight lessons learned from fire drill to carry out additional test scenarios.  So this scenario one in particular Johnny and to determine he whether additional tooling either DV synthesizer or fast forwarding clock is necessary to carry out a

Jonathan Kelly: It was just that we didn't even have any tool available to fast forward the clock and it became a big discussion do you get a specific Cardano node that's built that allows for this because it becomes a huge coordination effort if you do it that way and different SPOS's have to work in that exact synchronized tandem way. It's very much like a big ask I would say but if you can do db synth and have people build it outside of having to run 10 times speed…

Jonathan Kelly: then it becomes easier to manage there was a utility that came up that allowed you to spoof the time to a specific service on your Linux environment so you

### 01:05:00

Kevin Hammond: Yeah. …

Kevin Hammond: as I said, Nick Clark did mention a library to Mike that might be used and a wrapper tool might be used. Yes. Yeah.

Jonathan Kelly: didn't actually actually change the clock on your Linux environment, just the service itself. But again, that's a lot to ask people to do and set and configure and get right and get the timing exactly right,  So yeah, zip might need to be rewritten to use DB synthesizer is the consensus so

Kevin Hammond: Yeah, that's fine. So, if you could maybe make a note of the action points, Johnny, do you want to put those together and then we can record those?

Jonathan Kelly: Yeah, I'll put it in a technical staring chart.

Kevin Hammond: Great. Anything to add on the conscious of that we're over time by five minutes.

Jonathan Kelly: just that the SIP method did work and we got set back up and running and then did the workshop the next day.

Kevin Hammond: So that's a positive outcome, Johnny. we were able to successfully recover the sound chain.

Jonathan Kelly: A chain that had no blocks for over 24 hours.

Kevin Hammond: Able so we had for an extended period of time relative to the normal rate of production. So 24 hours on Sanchet it was something like a week I think it would be the equivalent of about a week on mainet.

Jonathan Kelly: would be the equivalent of much more than that over the 36R requirement for it to fall apart.

Kevin Hammond: So the fact that we were able to recover Cardano from a network that hadn't produced blocks for an extended period of time is extremely positive and shows the robustness in the network. And having done this of course we hope that we never need to use it in practice but at least we know that we have a methodology that will work if in the worst case situation. sounds very very successful, good outcome and some excellent lessons learned and some improvements to be Great. I'm going to call the meeting to a close once I've mentioned the item that Sam Levers raised with us.

Kevin Hammond: So Sam is asking for input from this group to the Cardono strategy document. he's up Cardano vision. he's asking for input on the enabling technology pillar. I will share the link to that in the chat.  So if everyone could take a look at that and provide input. He's asking to raise PRs. I'm not sure whether we can coordinate quickly enough to do that since he's planning to present this at the Cardano summit in about two to three weeks time.

Kevin Hammond: But if we can't coordinate a single PR, perhaps you can individually contribute PRs. Yeah, I found his link which I will paste into the chat there. do we want to try to coordinate single PR or is time scale too short to do that or individual responses better? feed that Sounds like you need to feed that back directly, Adam. Right.

Adam Dean: I hosted a workshop in Barcelona on Saturday where I said exactly that. So, it's on the record.

Kevin Hammond: But it probably needs to be on the PR as well.

Kevin Hammond: So I raised it with this group. I'll push it in the Slack channel. and then I will take an action to look at myself to start to put together a document that others can contribute to they wish. otherwise individuals can provide responses directly. So is that okay?

Kevin Hammond: But I think if we try to coordinate 10 responses, discuss them in detail and provide the feedback to Sam before the Cardano summit. There probably isn't enough time to do that. Great. I'll put something together and start to make my own comments in it and allow other people to update that.

### 01:10:00

Kevin Hammond: and then pass it on to Thank you very much everyone. for the record, the Cardano summit is going to be happening in Berlin on the 12th to 13th of November. So for anyone watching this, please go along. you be very welcome are there. And Marcus, anything you want to say about it from a CF perspective?  Yes.

Markus Gufler: on the summit. yeah, I'm not prepared for it now, but there are still some places or for tickets. So, if you can suggest some friends to look into, attending it then it will be helpful. Other than that the main agenda may looks like a lot of enterprise and adoption activities but a little bit hidden you see also there are three master classrooms with governance also with technical SPO networking topics so everyone can find something there even…

Markus Gufler: if the main agenda and the main stage doesn't look like there's the not the workshop the hackathon that's on day zero so before the actual two summit days and…

Kevin Hammond: So there are events happening on the day before the summit proper on November.

Kevin Hammond: Am Great.

Markus Gufler: it is on a other venue so it's not the summit venue itself but what I mean is actually on the summit venue there are also three master classrooms with let's say more technical or more specific speific topics where everyone can find something interesting for him.

Kevin Hammond: Thank you very much, Marcus.

Kevin Hammond: I hope to go myself. I haven't sorted out the travel yet. So I look forward to seeing some of you in Berlin in two three weeks time. Thank you very much.

Markus Gufler: So every committee member or someone with active roles and with voluntary contributions when he wants to get a ticket please reach out to me.

Arnaud Bailly: Thank you.

Markus Gufler: I can help to get a good deal on it.

Kevin Hammond: Thank you very much.

Kevin Hammond: So, call the meeting to a close here. any items we've not covered, we'll either cover out or we'll leave to the next agenda to the next meeting. Thank you very much everyone.

Sebastian Nagel: Thank you. Right.

Kevin Hammond: Thank you an talk to you all again soon.

### Meeting ended after 01:20:27 👋

This editable transcript was computer generated and might contain errors. People can also change the text after it was created.

  
**