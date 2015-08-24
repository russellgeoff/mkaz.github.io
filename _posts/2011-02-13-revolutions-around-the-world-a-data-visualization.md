---
id: 3609
title: Revolutions around the World, a data visualization
author: Marcus Kazmierczak
layout: post
permalink: /2011/02/13/revolutions-around-the-world-a-data-visualization/
categories:
  - dataviz
---
The recent events in Tunisia and Egypt got me thinking about revolutions across history. They tend to cluster together both in geography and time. So being on the current data visualization kick I'm on, it sounded like a fun little project. You can view the results here:

<div align="center" class="highlight">
  <a href="/a/dataviz/revolutions/"><img src="/a/dataviz/revolutions/screenshot.png" border="0" width="550" height="328" alt="Screenshot of Revolutions data visualization" /></a>
</div>



The data was collected from Wikipedia, in particular their [List of Revolutions][1]. Unfortunately, the list is quite long and contains a list of minor revolts, failed coups and other less notable events. Once again proving that data gathering is the hardest part of any data visualization project. I'm not a historian, so forgive me if I left any off or made any mistakes.

Once I gathered up the data, I tried out a couple of Javascript libraries to map them. Initially I attempted using the [Google Geomap Visualization][2], I was able to get the mapping down, but had trouble with animating it as a timeline.

I ended up working with a [World Map created by John Emerson][3] using [Raphael JS][4]. The mapping was already there and working with animating the data was fairly straightforward.

[Code available on Github.][5]  
Enjoy.

 [1]: http://en.wikipedia.org/wiki/List_of_revolutions_and_rebellions
 [2]: https://developers.google.com/chart/interactive/docs/gallery/geomap
 [3]: http://backspace.com/mapapp/javascript_world/
 [4]: http://raphaeljs.com/
 [5]: https://github.com/mkaz/dataviz/tree/gh-pages/revolutions
