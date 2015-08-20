---
id: 1031
title: The Command-Line Office
author: Marcus Kazmierczak
layout: post
guid: http://ebeab.com/?p=1031
permalink: /2014/03/04/the-command-line-office/
publicize_google_plus_url:
  - https://plus.google.com/115308324500133456489/posts/bhhmeF78WhJ
publicize_twitter_user:
  - mkaz
publicize_twitter_url:
  - http://t.co/shpSXLnmKm
geo_public:
  - 0
categories:
  - technology
tags:
  - command-line
  - office suite
---
Live your life on the command-line, this week we take a look at a suite of command-line office tools and utilities.

**Updated:** This article received a little bit of extra attention and comments which brought some great suggestions and alternatives. I've tested a few of them out and included additions below, also check out the comments for even more. Thanks everyone!

## Basics

First, a gentle introduction, word processing is a bit of a no-brainer on the command-line. You have the trusty favorites of **vim** and **emacs** as well as the gentler **nano** editor. For spell checking files on the command-line, use [aspell][1].

I create all of my documents in Markdown which is a nice plain text format which can easily be convert to HTML using [pandoc][2] utility. Plain text is simple, easy to work with and future proof &#8211; I won't ever have to worry if I have an app that can read it.

Keep track of your todo items using [Todo.txt][3] a system development by Gina Trapani. A simple way that uses plain text files to track todo lists and a todo.sh script to manage it all. Now extended to mobile and available for numerous languages and platforms.

Another great command-line todo manager is [Task Warrior][4] which has a little bit richer set of features and more add-ons and third party apps which can view and manipulate, see the [tools section][5]. I like **vit** which is a curses based front-end.

## Presentations

My favorite tool for building presentations is the ultimate converter app, [pandoc][2]. Pandoc is as mentioend above is a utility to convert file formats, some of the export formats include various HTML presentations. Formats supported: [Slidy][6], [reveal.js][7], [Slideous][8], [S5][9], or [DZSlides][10]. So you can create your slides in markdown and output a presentation.

If you want a more pure command-line experience, there is [terminal power point][11] which is a ruby script which displays the slides within the command-line. Unfortuntaely, as with all ruby scripts for me, I couldn't finagle dependencies and versions to get it working. Your mileage may vary.

## Spreadsheeting

The days of Lotus notes on the terminal are not quite over, ok its not Lotus 1-2-3 but you can still do some spreadsheeting in the terminal using the [spreadsheet calculator **sc**][12]. The sc program provides the familiar grid spreadsheet with vim bindings and basic calculations and functionality.

More tools and resources exist for charting and graphics, the most popular being [gnuplot][13] but [matplotlib][14] for Python is gaining popularity with the recent data science revival

If you just want to do some quick calculations, check out **bc**, a standard precision calculator installed on most distributions, or typically I'll just use the Python REPL or even the newer iPython. iPython is pretty nice because it always stores the results in an array that you can access.

## Calendaring

[remind][15] is a nice reminder utility, which you can use to remind you of various dates, for example birthdays. It has a powerful scripting language which allows for just about any date formatting/calculation. See [LifeHacker article][16] for more.

If you are looking for a little more from your terminal calendar, check out [calcurse][17]. Calcurse is a curses based calendar and task manager with customizable interface and suppots iCal and more formats, closer to an Outlook replacement.

As always, if you just need a month calendar, just do a quick **cal** on the command-line.

## Apps & Utilities

For password management, I now use [pass][18] command-line tool. Pass uses simple gpg-encrypted files and far quicker and easier to use, though no browser integration. Combined with [BitTorrent Sync][19] makes for a nice synchronized password system, also it uses just basic files so you can have multiline text.

If you are looking for a command-line RSS reader, check out [Canto][20] and  
[Newsbeuter][21] which claims to be the mutt of RSS readers.

Twitter, may or may not be part of the new office suite, but anything with a command-line client is a win in my book, check out [python twitter tools (ptt)][22]

A bit of a coincidence, my company just released a open source [command-line tool for Cloudup][23], which allows uploading files, photos and more to share online quickly. Ping me if you want an invite, I know some people.

 [1]: http://aspell.net/
 [2]: http://johnmacfarlane.net/pandoc/
 [3]: http://todotxt.com/
 [4]: http://taskwarrior.org/
 [5]: http://taskwarrior.org/tools/
 [6]: http://www.w3.org/Talks/Tools/Slidy
 [7]: http://lab.hakim.se/reveal-js/
 [8]: http://goessner.net/articles/slideous/
 [9]: http://meyerweb.com/eric/tools/s5/
 [10]: http://paulrouget.com/dzslides/
 [11]: https://github.com/cbbrowne/tpp
 [12]: http://www.linuxjournal.com/article/10699
 [13]: http://www.gnuplot.info/
 [14]: http://matplotlib.org/
 [15]: http://www.roaringpenguin.com/products/remind
 [16]: http://lifehacker.com/186661/geek-to-live--keep-your-calendar-in-plain-text-with-remind
 [17]: http://calcurse.org/
 [18]: http://www.zx2c4.com/projects/password-store/
 [19]: http://www.bittorrent.com/sync
 [20]: http://codezen.org/canto-ng/
 [21]: http://www.newsbeuter.org/
 [22]: http://mike.verdone.ca/twitter/
 [23]: https://cloudup.com/blog/share-from-the-command-line-with-up