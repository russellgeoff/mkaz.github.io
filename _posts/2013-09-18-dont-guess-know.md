---
id: 616
title: Don't Guess, Know
author: Marcus Kazmierczak
layout: post
permalink: /2013/09/18/dont-guess-know/
categories:
  - technology
tags:
  - programming
---
Most bugs I create come from not really understanding the system I'm working in. The system might be a framework, programming language, a standard or whatever.

A very common example, and I suspect the origin of 98% of all code, is the copy-paste-tweak methodology. This is how the web got started, View Source was the best teacher on the web for a long time, sadly now it is mostly useless.

The methodology is find something close to what you want to build; copy-and-paste the code and tweak until its doing what you want. This is a good way to get your development started but be wary, bugs will creep up and the less you know about what's going on the harder it will be to squash them.

**Here's an example using CSS** I was working on creating a new layout and design and I saw something close on a site I liked. So I used their CSS as a starting point but didn't like all the nested DIVs and wanted to tweak the widths, so hacked away on it.

I ended up doing all sorts of tweaking of paddings, margins and widths and was really struggling getting what I wanted. After wasting too much time with that, I finally stopped asked myself *what am I trying to accomplish?*. After knowing this, I refreshed myself on how the css box model works and with that understanding, I then was quickly able to set it up exactly how I intended and it worked.

Now many times a developer will get it &#8220;close enough&#8221; from tweaking and release it. Bugs will come in due to cross-browser issues, unintended input, etc. The developer goes back and tweaks for that case, and repeat. The end result is a whole lot of fragile code.

Another example, I see this is in character encoding and special characters, which is rather complex. If you just tweak and handle edge cases, and not really setup and understand properly, then you'll continually be chasing your tail.

I see this same base problem pop up in many scenarios where a little deeper understanding can go a long way &#8212; from understanding security implications, database indexes, layouts, scalability and so forth.
