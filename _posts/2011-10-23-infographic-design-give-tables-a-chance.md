---
id: 3590
title: Infographic design, give tables a chance
author: Marcus Kazmierczak
layout: post
permalink: /2011/10/23/infographic-design-give-tables-a-chance/
categories:
  - dataviz
tags:
  - infographics
---
There has been a recent backlash against infographics lately, justified as [this graphic illustrates][1]. Infographics have lost their way, their main purpose should be to make data easier to read by adding a visual perspective to the information shown. For example, using visuals can show the difference in sizes or distance better than abstract numbers.

However, the creation of infographics have been co-opted by designers and the primary goal now is aesthetics and not telling a story using data and visuals. It is time now for us math geeks to steal them back!

<div style="float:right">
  <img style="float:right" src="/images/tweet-o-meter-uptodatenew.gif" width="267" height="333" /><br /> <small>Original Graphic</small>
</div>

Smashing Magazine recently published an article on infographic design which illustrates how flawed designers think when building graphics. Here are links to the articles, the [original article][2] which had so many flaws they published a [follow-up article][3] which really wasn't much better.

The main example used was data around the Top 5 Active Twitter Moments. This is a fairly small and simple set of data to force into a infographic; there are only five data points, of relatively non-complex data, not much need for exploration.

Compare the example displayed from the article (right) with the two simplified versions I created below. In the original graphic the labels are disconnected from the data, a poor color palette distracts from readability and superflous graphics do not add to visual comprehension.  
<br clear="all" />

<div class="clear">
  <div style="float:left;width:50%">
    <table class="datatable">
      <tr>
        <th>
          Event
        </th>

        <th>
          Tweets/sec
        </th>
      </tr>

      <tr>
        <td>
          Women's World Cup Final
        </td>

        <td class="tdr">
          7,196
        </td>
      </tr>

      <tr>
        <td>
          New Year's Eve
        </td>

        <td class="tdr">
          6,939
        </td>
      </tr>

      <tr>
        <td>
          Japanese Tsunami
        </td>

        <td class="tdr">
          5,530
        </td>
      </tr>

      <tr>
        <td>
          Osama Bin Laden's Death
        </td>

        <td class="tdr">
          5,106
        </td>
      </tr>

      <tr>
        <td>
          Super Bowl 2011
        </td>

        <td class="tdr">
          4,064
        </td>
      </tr>
    </table>
  </div>

  <div style="float:left;width:50%">
    <img src="/images/tweets_per_second.png" title="Tweets per second" alt="horizontal bar chart" />
  </div>
</div>

<br clear="all"/>

### Data Comparison

Here's another example infographic where table data would get the information across much easier, [Perks of Working at Google, Facebook, Twitter&#8230;][4] This graphic makes it practically impossible to actually compare the companies and who offers what, click link to see, image is too large to embed.

A normal table such as this would work so much better

<table class="datatable">
  <tr>
    <th>
      Perk
    </th>

    <th>
      Google
    </th>

    <th>
      Facebook
    </th>

    <th>
      LinkedIn
    </th>

    <th>
      Twitter
    </th>
  </tr>

  <tr>
    <td>
      Massages
    </td>

    <td class="center">
      X
    </td>

    <td class="center">
    </td>

    <td class="center">
      X
    </td>

    <td class="center">
    </td>
  </tr>

  <tr>
    <td>
      Yoga
    </td>

    <td class="center">
      X
    </td>

    <td class="center">
    </td>

    <td class="center">
      X
    </td>

    <td class="center">
      X
    </td>
  </tr>

  <tr>
    <td>
      Foosball
    </td>

    <td class="center">
      X
    </td>

    <td class="center">
      X
    </td>

    <td class="center">
      X
    </td>

    <td class="center">
      X
    </td>
  </tr>
</table>



### Summary

So next time you are tasked at creating a graphic, make a chart, or present data in some way; think first, can I present this information simply in a table and let people see the data. Will graphics or fancy visuals add to the story, or detract?

Can you imagine a baseball box score as an infographic, yikes!  
<br clear="all" />

### Further Reading

  * [Edward Tufte Highlights Good Infographics][5]

  * [Stop Already with the F!cking Infographics][6]

  * [Massive Burden of Pie Charts][7]

  * [Shaking our heads won’t make visualization any better][8]

 [1]: http://www.nytimes.com/interactive/2011/10/09/magazine/09-mag-direstraits.html
 [2]: http://www.smashingmagazine.com/2011/10/14/the-dos-and-donts-of-infographic-design/
 [3]: http://www.smashingmagazine.com/2011/10/21/the-do%E2%80%99s-and-don%E2%80%99ts-of-infographic-design-revisited/
 [4]: http://mashable.com/2011/10/17/google-facebook-twitter-linkedin-perks-infographic/
 [5]: http://www.edwardtufte.com/bboard/q-and-a-fetch-msg?msg_id=0002w4&topic_id=1&topic=
 [6]: http://gizmodo.com/5846087/stop-already-with-the-fcking-infographics
 [7]: http://junkcharts.typepad.com/junk_charts/2011/10/the-massive-burden-of-pie-charts.html
 [8]: http://fellinlovewithdata.com/reflections/shaking-heads
