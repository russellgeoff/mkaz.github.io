---
id: 3603
title: Strata Data Conference Recap 2012
author: Marcus Kazmierczak
layout: post
guid: https://mkaz.com/?p=3603
permalink: /2012/03/05/strata-data-conference-recap-2012/
categories:
  - dataviz
tags:
  - data
  - strata
---
This article is a recap of the [Strata 2012 data conference][1] I went to. I did some [previous analysis on the attendee directory][2], so I am also including the results of the connectedness change before and after the conference.

### Update on Twitter Attendee Analysis

From the list of twitter attendees generated before the conference, I measured the connectedness between attendees sampling their followers before and after the conference. <sup>1</sup> The overall number of connections went up as you would expect with on average two additional connections throughout. This will be obviously unbalanced connections to the main hubs, see below.

    Average Degree before Conference: 9.615
    Average Degree after Conference: 11.606
    

Here are the data files, anyone can extend and do additional analysis, shoot me a link ([@mkaz][3]) if you do anything with it.   
**Download**: [strata_before.graphml][4], [strata_after.graphml][5]

### Largest Twitter Hubs

The biggest change in the twitter hubs was a focus on people over corporations. Google which was barely represented at the conference dropped from #2 before to off the list, Tableau which was at the conference also dropped off the list. Also a little reshuffling and three new people added.

<div class="clear">
  <div style="width:49%;float:left">
    <h4>
      Before
    </h4>
    
    <p>
      1. <a href="https://twitter.com/hmason">hmason</a><br /> 2. <a href="https://twitter.com/google">google</a><br /> 3. <a href="https://twitter.com/edd">edd</a><br /> 4. <a href="https://twitter.com/cloudera">cloudera</a><br /> 5. <a href="https://twitter.com/acroll">acroll</a><br /> 6. <a href="https://twitter.com/peteskomoroch">peteskomoroch</a><br /> 7. <a href="https://twitter.com/dpatil">dpatil</a><br /> 8. <a href="https://twitter.com/mrflip">mrflip</a><br /> 9. <a href="https://twitter.com/tableau">tableau</a><br /> 10. <a href="https://twitter.com/digiphile">digiphile</a>
    </p>
  </div>
  
  <div style="width:49%;float:left">
    <h4>
      After
    </h4>
    
    <p>
      1. <a href="https://twitter.com/hmason">hmason</a><br /> 2. <a href="https://twitter.com/peteskomoroch">peteskomoroch</a><br /> 3. <a href="https://twitter.com/dpatil">dpatil</a><br /> 4. <a href="https://twitter.com/edd">edd</a><br /> 5. <a href="https://twitter.com/acroll">acroll</a><br /> 6. <a href="https://twitter.com/cloudera">cloudera</a><br /> 7. <a href="https://twitter.com/mrflip">mrflip</a><br /> 8. <a href="https://twitter.com/petewarden">petewarden</a><br /> 9. <a href="https://twitter.com/mikeolson">mikeolson</a><br /> 10. <a href="https://twitter.com/cutting">cutting</a>
    </p>
  </div>
</div>

<small><sup>1</sup> &#8211; Data collected Sunday, Mar 4, 2012</small>  


## Conference Recap

All in all a great conference, a wide diverse group using data in some many different businesses and fields, but many with the same problems of collecting, storing and analyzing the data to get insights. The biggest focus of the conference had to be Hadoop. Hadoop. Hadoop.

The amount of hadoop projects and talks were plentiful. Everyone seemed really focused on the **big** part of Big Data. I did skip most of these talks, I did go to an early tutorial which was supposed to be an intro to Hadoop but the talk was a bit of a disaster, I definitely picked the wrong one.

The reason I skipped the hadoop talks, I'm not really that interested in the hard-core infrastructure side of data, I never got my rocks off on EMC or NetApp storage arrays, likewise for databases, so distributed infrastructure doesn't interest me that much. Funny though I did work on a big distributed storage system in my past. [Haystack storage][6]

I'm interested in what insights can be gleamed from data and the analysis and visualization required. What questions are you trying to ask and what can be answered. What new products can be created from the data. How can you combine various sources of data together to tell a story.

Someone quoted to me at the conference that Zynga creates and stores a Petabyte of data a day. Crazy!

I went to last years Strata Conference and 2012 was definitely bigger and a lot more corporate sponsorship. Last years felt a bit smaller and more of a community of data hackers. This year felt more like a normal technology conference with big sponsors, not a bad thing just going mainstream.

There were so many good talks, I wish I could've been in two places at once. Thankfully they post the video from each session, so I can catch up on any of the ones I missed.

Most of the slides are available online at: [Strata Conference Speaker Slides][7]. Two of my favorite talks, which of course the slides aren't posted yet are:

**[Building a Data Narrative: Discovering Haight Street][8]** &#8211; Jesper Anderesen gave a great talk about analyzing Haight Street in San Francisco. What can a small street tell us. He grabbed sources from everywhere, crime data from [sfgov data][9], location data and check-ins from FourSquare. He grabbed map data from [Open Street Maps][10]. Analyzed Twitter feeds for language and sentiment and more sources which I've forgetting. He was able with very little initial info pull together and tell a story about Haight Street using just open data sources.

**[The Two Most Important Algorithms in Predictive Modeling Today][11]** &#8211; Jeremy Howard (Kaggle) and Mike Bowles presented about predictive modeling techniques and how to use them for predicting dependent variables. They were enthusiastic and good speakers, I wish they got more into the hands on and code side and was lighter on theory, but still enjoyable and enlightening.

 [1]: http://strataconf.com
 [2]: https://mkaz.com/dataviz/strata-attendee-analysis.html
 [3]: https://twitter.com/mkaz
 [4]: /a/dataviz/strata_before.graphml
 [5]: /a/dataviz/strata_after.graphml
 [6]: http://martingreen.typepad.com/forward_looking_statement/2006/06/more_on_haystac.html
 [7]: http://strataconf.com/strata2012/public/schedule/proceedings
 [8]: http://strataconf.com/strata2012/public/schedule/detail/22449
 [9]: https://data.sfgov.org/
 [10]: http://www.openstreetmap.org/
 [11]: http://strataconf.com/strata2012/public/schedule/detail/22658