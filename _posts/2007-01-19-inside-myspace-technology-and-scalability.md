---
id: 494
title: 'Inside MySpace &#8211; technology and scalability'
author: Marcus Kazmierczak
layout: post
permalink: /2007/01/19/inside-myspace-technology-and-scalability/
categories:
  - classics
---
Baseline magazine has [a good article on Inside MySpace][1]. The article discusses the technical issues MySpace has had to deal with growing to 140 million users. If you are interested in technology, scalability and large site architecture, definitely check it out.

It is interesting to read about all of the account milestones they reached and the architecture in place and changes they made to handle it. I was a little surprised that it started out on Cold Fusion, which I was programming with 10 years ago (which really makes me feel old). Now converted over to C# and .NET.

I was shocked to see that it took them until 17 million accounts before implementing cache servers, that would've been a more efficient use of resources, though it wouldn't magically solve the problem, exponential growth to 140 million users in two years is a scenario real difficult to digest using any technology.

I worked on scalability and system performance at ETRADE so definitely have interest and experience in this area. ETRADE issues of growth were a bit different since we didn't have the luxury of being able to lose data and 100% reliability was required, down time during market hours was money lost. The type of load is also completely different, ETRADE has a massive amount of transactions occuring during a short period of time. The transactions and data flowing is relatively small and controlled, just lots of them to process. MySpace has a massive amount of users at all times contributing random amounts of data, making for a different problem.

I have a little insight into Facebook's architecture and some choices they made in design. They made some earlier decisions which I think helped them avoid some of the major growth problems MySpace saw. Facebook also has grown at a slower more controlled rate. But some of their segmentation decisions are now becoming issues though as they try to expand further and integrate their many networks. It would be great to see a similar full in depth article about Facebok and see how they compare.

I do look forward to having some of these problems at [Maya's Mom][2], scalability issues to that degree means you are doing something right.

 [1]: http://www.baselinemag.com/c/a/Projects-Networks-and-Storage/Inside-MySpacecom/
 [2]: http://www.mayasmom.com/
