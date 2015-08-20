---
id: 3612
title: Needlebase and playing with movie data
author: Marcus Kazmierczak
layout: post
guid: https://mkaz.com/?p=3612
permalink: /2011/02/11/needlebase-and-playing-with-movie-data/
categories:
  - dataviz
---
**Updated:** Needlebase was acquired by Google and as so many acquisitions go, the service was shutdown. More info and [possible alternatives discussed here][1]

After hearing Marshall Kirkpatrick at a recent talk describe **Needlebase**, as a simple way to scrape sites and create a database of info, I had to try it out. With the Oscar season coming up, I figured movie data would be a good set to play with and imdb a great source of movie data.

There are a few tools available to query IMDB data, [an API][2] and the [raw data files][3], but both have their limitations. The API I found only accepts 20 requests an hour and the raw data files are far too raw, a good example where too much data is too much, clean data is better.

My thought was to chart box office gross to movie ratings, so using Needlebase and the [advanced IMDB search][4], I was able to create a database of movies released in 2010 with their box office numbers and ratings. You can [download CSV of 2010 Movie data][5]

So I threw the data into R and got a nice chart out of it, but didn't really turn up too many patterns.

<div align="center">
  <img src="https://mkaz.com/wp-content/uploads/2011/02/movie_chart_r.png" alt="" title="movie_chart_r" width="504" height="504" class="alignnone size-full wp-image-1596" />
</div>

I figured the chart would be a lot more interesting as an interactive tool, so you can see which movies are what. So using <s>Protovis</s>, [Highcharts][6], a javascript graphing and visualization library. I created this view which allows some basic interaction, a bit better way to explore this data.

Note: Protovis does not work with IE browers, so switch to Highcharts. <small>Feb 15, 2011</small>

 [1]: http://www.reporterslab.org/needlebase-dead/
 [2]: http://deanclatworthy.com/imdb/
 [3]: http://www.imdb.com/interfaces
 [4]: http://www.imdb.com/search/title
 [5]: /a/dataviz/Movies-Released-in-2010.csv
 [6]: http://www.highcharts.com/