---
id: 3606
title: Strata 2012 Attendee Analysis
author: Marcus Kazmierczak
layout: post
permalink: /2012/02/22/strata-2012-attendee-analysis/
categories:
  - dataviz
tags:
  - data
  - strata
---
[<img src="https://mkaz.com/img/strata2012_before_nolabels.png" title="Strata 2012  Graph" alt="Graph" style="width:100%" />][1]

The [Strata Conference][2] is next week, so I was browsing the attendee directory curious to see who I know is going or looking for interesting companies to meet with. This got me thinking about the overall connectedness of the attendee list. So&#8230;

A few scripts later and a bit of analysis I produced the following data, which probably could get thrown into a fancy infographic with 64pt fonts and cute icons, if that's how you roll. Here's a few stats and the process and tools used.

### Stats:

1,463 attendees in directory<sup>1</sup>

**Most Popular Titles**

  1. CEO (61) 
  2. Software Engineer (55) 
  3. CTO (45) 
  4. Founder (35) 
  5. Data Scientist (33) 

<small>Note: Title data is very wonky due to no standards and multiple entries per line such as &#8220;Founder/CEO and Data Scientist" and people getting cute such as &#8220;CIO at Large" &#8211; I massaged a little, removing ranks (Senior, Sr., Principal, Lead) separating roles, etc&#8230; but gave up after awhile too chaotic.</small>

* * *

**Top Companies Attending**

  1. Microsoft (48)
  2. EMC (19)
  3. Cloudera (14)
  4. Google (14)
  5. Karmasphere (11)
  6. LinkedIn (11)

<small>Microsoft is obviously taking big data seriously, or just has a large training budget.</small>

* * *

### Twitter Analysis

The attendees also could include their twitter accounts, 454 of them did<sup>1</sup>. Analyzing the Twitter accounts of who follows who between attendees, gave me the above graph and some more interesting stats, such as the level of connectedness between conference attendees.

    Average Degree: 9.615 
    

The degree is the average number of connections per node, a node being a person in the graph. It will be interesting to see what the numbers look like after the conference to see to what level this connectedness changes.

[<img src="https://mkaz.com/img/thms/strata2012_zoom_hmason_thm.png" title="Strata 2012 Zoom Graph" alt="Graph" width="500" height="365" style="float:right;border:1px solid #CCC;margin-top:10px" />][3]

**Largest Twitter Hubs**

  1. [hmason][4]
  2. [google][5]
  3. [edd][6]
  4. [cloudera][7]
  5. [acroll][8]
  6. [peteskomoroch][9]
  7. [dpatil][10]
  8. [mrflip][11]
  9. [tableau][12]
 10. [digiphile][13]

<br clear="all" />

## Process

First I created a quick ruby script to suck down all the attendees and their Twitter accounts. I used the [Watir Webdriver][14] tool which is intended for functional testing of web sites; but works quite well as a screen scraper since it has complex parsing and selectors.

This gave me a list of 1,463 attendees in the directory of which 454 listed twitter accounts.

I used this list of twitter accounts to feed a script which fetched who they follow. This was a bit of a pain due to rate limiting by Twitter to only 150 requests per hour. The graph of the twitter connections contains 454 nodes with 2,778 connections, or edges.

I created a [GraphML][15] file of the twitter data and pulled that into [Gephi][16] to create the graph. Gephi is a really cool tool, made it super easy to graph and calculate various data such as the degree. I need to brush up more on my [graphy theory][17] to understand it all.

My typical process is to write everything to local data files, this allows for easier manipulation and wider variety of tools can be used to massage the data. So even the initial HTML I sucked down from the attendee directory once and then tweaked my script to get it to parse properly. Otherwise I'd be hitting the server frequently which would just be annoyingly slow, since it takes me about 100 iterations to parse anything properly.

For the twitter accounts, I created a file for each user and stored the IDs of who they followed. I could then run various scripts against that. A simple `wc -l` on the directory tells me who follows the most users.

In files, I can also easily massage the data using many standard unix functions such as awk, cut and vim.  
For example the initial listing I spit out into a pipe delimited format:

    Name | Position | Company | Twitter
    

I used `cut` to pull out twitter accounts and then `vim` to delete blank lines

    cut -d'|' -f4 > twitter.txt 
    vim twitter.txt
    :g/^\s*$/d
    

The GraphML format turned out to be one of the easiest parts, basically each person is a node and each connection another node. So putting it together was just outputting one XML file:

<pre>&lt;graphml&gt;
    &lt;graph&gt;
        &lt;node id="mkaz"/&gt;
        &lt;edge source="mkaz" target="edd"/&gt;
        &lt;edge source="mkaz" target="cutting"/&gt;
        ...
    &lt;/graph&gt;
&lt;/graphml&gt;
</pre>

* * *

<a name="foot1"></a>  
<sup>1</sup> All data gathered on Weds, Feb 22, 2012

 [1]: https://mkaz.com/img/strata2012_before_nolabels.png
 [2]: http://strataconf.com/strata2012
 [3]: https://mkaz.com/img/strata2012_zoom_hmason.png
 [4]: https://twitter.com/hmason
 [5]: https://twitter.com/google
 [6]: https://twitter.com/edd
 [7]: https://twitter.com/cloudera
 [8]: https://twitter.com/acroll
 [9]: https://twitter.com/peteskomoroch
 [10]: https://twitter.com/dpatil
 [11]: https://twitter.com/mrflip
 [12]: https://twitter.com/tableau
 [13]: https://twitter.com/digiphile
 [14]: http://watirwebdriver.com/
 [15]: http://graphml.graphdrawing.org/
 [16]: http://gephi.org/
 [17]: http://en.wikipedia.org/wiki/Graph_theory