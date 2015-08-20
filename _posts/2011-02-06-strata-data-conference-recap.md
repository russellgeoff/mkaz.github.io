---
id: 3614
title: Strata Data Conference Recap
author: Marcus Kazmierczak
layout: post
guid: https://mkaz.com/?p=3614
permalink: /2011/02/06/strata-data-conference-recap/
categories:
  - dataviz
tags:
  - strata
---
This last week I attended the inaugural Strata Conference, a conference titled &#8220;making data work&#8221;. It broke into a few different tracks, (1) **handling big data**, scaling infrastructure, for example hadoop and cassandra systems, (2) **data visualizations**, how to present data, graphics and tons of examples and (3) **data sets and cool shit you can do with data**. I focused most of my time around (2) and (3), I'm no longer geek enough to hang with the big data boys and girls, but I prefer the analyzing and doing something with the data more.

Here's a brief recap of the conference from my view plus links to good information and further exploration. The next Strata conference is in New York in September and they already plan to bring it back to the Bay Area next year. [More info at O'Reilly][1]

### Data Visualizations

I went to several talks on presenting data and visualizations, unfortunately most were around advice and theory and less specifics around the tools and how they do it. The talks were still really informative and inspiring to see so many of the great things being worked on and developed. The main advice was to **Have a Message**, the data itself is not the message, but can help reveal it. Don't focus so much on data, but on the story it tells or the action it motivates.

> &#8220;data is a dish best served raw&#8221; 

A slightly contrarian view to having a message was to provide the user with the tools to explore the data. Allow the user to be able to create their own stories from the data. This all depends on the data set, do not expect users to derive the same message from the same data. Everyone brings different views and analytical abilities when looking at data and visualizations.

Exploration works better when the user can create their own story by focusing on area that concerns them, for example their own geographic region. If you are trying to convince a decision maker for a specific result, raw data and exploration is probably not your tool.

**Keep it Simple** &#8211; Reduce chart and table junk from your graphics, increase the data-to-ink ratio. Here's an example the Juice Analytics people showed on simplifying a table of MLB Team salaries. You can see below even at this smaller size which one would be easier to read.

<img src="https://mkaz.com/wp-content/uploads/2011/02/table_chart.gif" alt="" title="Baseball Salary Table Example" width="750" height="267" class="alignnone size-full wp-image-1560" />  


Here are a couple of pretty cool visualizations from the Guardian, who also provide the raw data alongside. It is really worth checking out their [data site and blog][2] for inspiration as well as data to play with, a great resource. The Carbon Calculator is particularly interesting tool to use and play around with.

<div class="clear">
  <div style="float:left;width:325px;margin:10px">
    <a href="http://www.theguardian.com/news/datablog/2011/jan/31/world-carbon-dioxide-emissions-country-data-co2"><img src="https://mkaz.com/wp-content/uploads/2011/02/guardian1.gif" alt="" title="guardian1" width="300" height="180" class="alignnone size-full wp-image-1564" /><br /> World Carbon Dioxide Emissions</a>
  </div>
  
  <div style="float:left;width:325px;margin:10px">
    <a href="http://www.theguardian.com/environment/interactive/2010/apr/21/national-carbon-calculator"><img src="https://mkaz.com/wp-content/uploads/2011/02/guardian2.jpeg" alt="" title="guardian2" width="300" height="180" class="alignnone size-full wp-image-1565" /><br /> Carbon Footprint Calculator</a>
  </div>
</div>

Finally in the Data Visualization category, I leave with you [Data as Art][3] which is a great collection of beautiful data visualization examples put together by JJ Toothman. Explore his presentation and the collection of links he put together.

<div id="divider">
</div>

### Advice

Clean data > More Data > Fancy Math &#8211; this is the order which makes data easier and better to work with. Clean data will be easier to work with and provide best results. If your data isn't clean, it is better to have more data than having to resort to fancy math. Using higher order statistical processing, why workable as a last resort, will require longer to develop, difficult algorithms and harder to maintain. So best place to focus is to start with clean data.

> Optimize for Programmer Joy 

There is a ton of data already existing in your organization, start collecting and categorizing it now. One way is to gather a data dictionary which could be as simple as just a list on the wiki of data information and links to their source.

Standardize &#8211; &#8220;We threw out non-Hadoop code that was faster&#8221; at LinkedIn. The code might of been faster but standardization was more important when the teams were all using the same code; communication and sharing was easier and productivity improved.

### Examples 

Drew Conway, Joseph Adler and Hilary Mason ran a cool data bootcamp tutorial, I only caught the second half after I walked out of one of the few poor talks. I wish I was in the data bootcamp all-day. I had that feeling a lot, there were just so many good talks going on all at once. They covered several examples of what you can do with data, from analyzing to graphing and mapping. You can download the entire [Strata Bootcamp Code][4] which includes all the data, code and their slides.

One example they showed was analysis of bit.ly links to the Strata conference site and graphed it onto a map, from the latitude and longitude where the links came from. The code, in R, is included in the github download, linked above.  
<img src="https://mkaz.com/wp-content/uploads/2011/02/strata_map-copy.png" alt="" title="strata_map copy" width="460" height="293" class="alignnone size-full wp-image-1574" />

Hilary demoed something similar with bit.ly links coming out of Egypt, this was done in almost real-time, she made the graph an hour before her keynote talk, also done using R.  
<img src="https://mkaz.com/wp-content/uploads/2011/02/clicks_from_egypt.jpg" alt="" title="clicks_from_egypt" width="460" height="348" class="alignnone size-full wp-image-1573" />

They also demoed some interesting tools for analyzing and classifying GMail. I need to dig more into their code to pick up on what I missed there.

LinkedIn demoed a mapping tool, which allows you to create a map of your professional network. Clustering common and inter-connections, which makes it easy to spot different companies and groupings of people. The tool was custom built using [Processing][5]. You can see my map below, or create your own at: [LinkedIn Maps][6]

<div align="center">
  <a href="http://inmaps.linkedinlabs.com/share/Marcus_Kazmierczak/278297880179406214390994361051892026692"><img src="https://mkaz.com/wp-content/uploads/2011/02/inmap-600x374.gif" alt="" title="Marcus Kazmierczak LinkedIn graph" width="600" height="374" class="alignnone size-medium wp-image-1576" /></a>
</div>

<div id="divider">
</div>

### Tools

Here are a few links to some of the tools used, demoed or talked about:

  * [R Language][7] &#8211; A statistical programming system including graphing and an extensive library to extend 
  * [Choose the Right Chart][8] &#8211; A simple tool to help you decide what type of chart to use.
  * [Wordle][9] &#8211; A service to create beautiful word clouds 
  * [Needlebase][10] &#8211; An interesting tool that Marshall Kirkpatrick uses to scrape and categorize web sites, sounded awesome another thing to dig into.

### People

Here are a few links to some of the presenters and interesting people I met or saw:

  * Joseph Adler, [@jadler][11]
  * Hilary Mason, [@hmason][12], <http://www.hilarymason.com/> 
  * Drew Conway, [@drewconway][13], [http://www.drewconway.com/zia/][14]
  * Mark Madsen, [@markmadsen][15], [http://thirdnature.net/][16]
  * Simon Rogers, [@smfrogers][17], <http://www.theguardian.com/data>
  * Jer Thorp, [@blprnt][18], <http://blog.blprnt.com/>
  * JJ Toothman, @jjtoothman, <http://nasawebdude.com/></li> </ul> 
    
    ### Keynotes
    
    The whole conference was recorded, I'm not sure if any of the individual sessions are publicly available but here are a few of the great keynotes, I'll skip the blatant sales pitch ones, which unfortunately there were a couple.
    
      * Mark Madsen, ThirdNature [The Mythology of Big Data][19] <small>[YouTube]</small>
      * DJ Patil, LinkedIn [Innovating Data Teams ][20] <small>[YouTube]</small> 
      * Hilary Mason, bit.ly [What Data Tells Us ][21] <small>[YouTube]</small> 
      * Werner Vogels, CTO Amazon [Data Without Limits ][22] <small>[YouTube]</small> 
    
    ### Recommended Reading
    
      * Bill Cleveland: <http://www.stat.purdue.edu/~wsc/>
      * [Visualizing Data][23]<img src="http://www.assoc-amazon.com/e/ir?t=mkazcom-20&#038;l=as2&#038;o=1&#038;a=0963488406" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" /> by Bill Cleveland <small>[Book, Amazon.com]</small>
      * [The Fourth Paradigm: Data-Intensive Scientific Discovery][24]<img src="http://www.assoc-amazon.com/e/ir?t=mkazcom-20&#038;l=as2&#038;o=1&#038;a=0982544200" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" /> <small>[Book, Amazon.com]</small>
      * [R in a Nutshell: A Desktop Quick Reference][25]<img src="http://www.assoc-amazon.com/e/ir?t=mkazcom-20&#038;l=as2&#038;o=1&#038;a=059680170X" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" /> by Joseph Adler <small>[Book, Amazon.com]</small>
      * [The Data Deluge][26] <small>[Economist] </small>
      * [Juice Analytics &#8211; Make People Fall in Love with Your Data][27] [PDF, Slides]
    
    ### Public Data Sets
    
    Now you've done all your research, read about visualizations and want to play with some data. Here are a list of a few sources of publicly available data.
    
      * [Amazon Public Datasets][28]
      * [US Government Data][29]
      * [Guardian Datastore ][2]
      * [Nasdaq][30]
      * [Infochimps Datamart][31]
    
    This was just my view of the conference, like I said at the beginning there were many tracks and many more sessions than I could attend. If you were at the conference, feel free to include any additional information or links in the comments. Thanks to O'Reilly for putting on the first of what I hope to many interesting data conferences to come.

 [1]: http://strataconf.com/strata2011
 [2]: http://www.theguardian.com/data
 [3]: http://nasawebdude.com/2011/02/data-as-art-presentation-at-strata-conference/
 [4]: https://github.com/drewconway/strata_bootcamp
 [5]: http://processing.org/
 [6]: http://inmaps.linkedinlabs.com/
 [7]: http://www.r-project.org/
 [8]: http://labs.juiceanalytics.com/chartchooser/index.html
 [9]: http://www.wordle.net/
 [10]: /2011/02/11/needlebase-and-playing-with-movie-data/
 [11]: https://twitter.com/jadler
 [12]: https://twitter.com/hmason
 [13]: https://twitter.com/drewconway
 [14]: http://drewconway.com/zia/
 [15]: https://twitter.com/markmadsen
 [16]: http://thirdnature.net
 [17]: https://twitter.com/smfrogers
 [18]: https://twitter.com/blprnt
 [19]: http://www.youtube.com/watch?v=HwVPxYWDO4w
 [20]: http://www.youtube.com/watch?v=NXgS1ZQ-Uw0
 [21]: http://www.youtube.com/watch?v=KWszSUm-x2Y
 [22]: http://www.youtube.com/watch?v=oNTp5spjv0w
 [23]: http://www.amazon.com/gp/product/0963488406?ie=UTF8&tag=mkazcom-20&linkCode=as2&camp=1789&creative=390957&creativeASIN=0963488406
 [24]: http://www.amazon.com/gp/product/0982544200?ie=UTF8&tag=mkazcom-20&linkCode=as2&camp=1789&creative=390957&creativeASIN=0982544200
 [25]: http://www.amazon.com/gp/product/059680170X?ie=UTF8&tag=mkazcom-20&linkCode=as2&camp=1789&creative=390957&creativeASIN=059680170X
 [26]: http://www.economist.com/node/15579717
 [27]: http://bit.ly/JuiceStrata2011
 [28]: http://aws.amazon.com/datasets
 [29]: http://www.data.gov/
 [30]: https://data.nasdaq.com/
 [31]: http://www.infochimps.com/