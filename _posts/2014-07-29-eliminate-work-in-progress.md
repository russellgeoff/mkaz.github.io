---
id: 3784
title: Eliminate Work in Progress
author: Marcus Kazmierczak
layout: post
permalink: /2014/07/29/eliminate-work-in-progress/
categories:
  - technology
tags:
  - methodology
  - software development
  - work in progress
---
I was listening to the recent [Bootstrapped with Kids podcast][1] and they were talking about doing too many things at once and the pain it was having on the business.

A good listen to hear how development methodology effects the business. A few key tenets of software development; doing small releases, eliminate work in progress and deploy frequently. If you have finished code, don't wait and sit on it, deliver it to your customers. Deploy.

Here is an example my colleague Ken and I would use to explain on why doing too many things at once is not ideal.

### Three Projects Illustrated

Imagine you have three projects each of which is about the equal amount of time and each will deliver some value at their completion. For the sake of argument, let's say each takes a month to complete and each will deliver a $1,000/mo.

#### Scenario One: Asynchronous &#8211; Multi-Tasking

One way of attacking these projects, it to break them up into small chunks and start work on them simultaneously. If you were orderly and consistent, the work might look like this.

<img src="/images/work-in-progress-1.svg" style="width:575px" />

Each project gets a little bit of time and at the end of the three months all projects are complete. This process is most commonly used when trying to optimize resources, you might hear &#8220;We can't have anyone not working, have them start next thing while they wait"

#### Scenario Two: Synchronous &#8211; One after the Other

An alternate scenario is to tackle each project until it is complete and shipped; not starting the next one until it is out the door. This scenario would look like this.

<img src="/images/work-in-progress-2.svg" style="width:575px" />

Notice, after month one Project A starts realizing value and earns $1,000 in month two and another $1,000 in month three. Project B would get completed in month two and earns $1,000 in month three. At the end of three months, all projects are complete, but doing the projects one-at-a-time delivered an extra $3,000 since it was shipping completed Project A and B.

### In Reality

Most people do realize this and a true Scenario One is not really attempted. Here is a more realistic scenario, a team starts off on the same project together. As people finish and hand-off their piece, they move on to the next.

For example Design finishes mocks and hands to Engineering, so Design starts on next project. However, if Engineering asks a question or needs the mocks updated with new requirement, the Design team is busy. So Engineering submits a design request and instead of being idle they start on the next project.

This might look like:

<img src="/images/work-in-progress-3.svg" style="width:575px" />

This ends up delivering the same results as the first scenario, which is none until the end of the three months. The real killer is when there are a bunch of projects almost done and just need that little bit more to finish up, be it a approval, production environment, wordsmithing or whatever.

Worrying about the &#8220;idle" time. Management gets worried when people appear to be idle, but there is always work to be done. Odd requests from last project, clean up work, polishing up hacks or helping colleagues. All this needs to get done and rarely scheduled. Also a little down time allows people to recoup, tidy up your own work environment, learning a new tool or tutorial. All beneficial.

A way I've seen successful is when teams are organized not by function, but by project. So there is no Design or Engineering team but X product team which has all the necessary team members. This works well because as a team they have one goal and will work to complete the overall goal and not just the bits and pieces of work in progress.

### Summary

In summary, try to eliminate as much work in progress. Focus the entire team to deliver value in smaller chunks and at a faster rate. Finish up those little bits and get it shipped. This delivers value quickly to your customers and you start realizing it sooner.

 [1]: http://www.bootstrappedwithkids.com/take-smaller-bites/
