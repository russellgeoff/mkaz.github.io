---
id: 479
title: Scala and the Play Framework, Wow!
author: Marcus Kazmierczak
layout: post
permalink: /2010/06/07/scala-and-the-play-framework-wow/
categories:
  - scala
---
As I continue down the path of testing out the Scala language and compatible web frameworks, I came across the [Play Framework][1] and all I can say is Wow! Play is a very nice polished framework, which just feels right to me. I had the app up running and doing everything I wanted in a fraction of the time on any other technology I tested. Everything just worked, I didn't have to fuss with a bunch of settings, config files, library versions, or anything.

Play is a Java framework and with the 1.1 release (not final) they have added Scala support. They claim Scala is still experimental but it works better than most complete technologies I've tested recently. The console interface for installing, running and managing the app works great. One of the most impressive pieces is the testing framework which combines Selenium and Unit testing and managed through the browser.

I literally made more progress with Play in an hour than I did with everything else which took days or weeks. For example, after two weeks with StringTemplate and Scalasti I am still not able to loop through a result set within a template.

### Structure and Features

The Play structure is very intuitive and works well with the way I think. I come from a heavy PHP background and have been developing on a large Zend Framework app for the past 4+ years. We built our app structure off the Rails structure and Play continues along the same project structure (app, controllers, models, views). I don't come from a heavy Java background, so the Maven project hierarchy has never really quite gelled with me.

A few key features of Play:

  * Automatic Compiling and Reloading of Everything
  * Contextual and Relevant Error Codes
  * Testing Framework baked in
  * Fast getting started time
  * Good Documentation and Tutorials
I haven't used the Play ORM yet, but I don't really use Zend's either. Most apps and queries tend to require a little more customization and optimizations than any ORM can give. I'm sure I'll check it out, maybe they'll surprise me there too.

### Quick Start

Download the Play Framework 1.1 nightly build from: [download.playframework.com][2]

I downloaded and installed to: `/opt/play`. Add the directory you extracted play to your PATH.

Create New App:

<pre>play new testapp --with scala</pre>

oops.. you haven't installed Scala Module yet, it's as simple as

<pre>play install scala</pre>

Try to create your app again and it will generate the app structure and a working demo app.

Run App:

<pre>play run testapp</pre>

or from within the testapp directory just run

<pre>play run</pre>

A great little bonus is Play has built-in documentation, just go to a running instance: http://localhost:9000/@documentation &#8212; which is so useful, since I don't always have an internet connection, for example during a train ride [from SF to Chicago][3].

Kudos to the Play team, my search for a Scala Framework might be complete.

Further Reading:

  * [Play Framework: Scala Module][4]
  * [Scala + Play Quick Start Video][5] [vimeo]
  * []() </ul>

 [1]: http://www.playframework.com/
 [2]: http://download.playframework.com/
 [3]: http://kazmierczaks.com/2010/07/03/51-hours-to-chicago/
 [4]: http://www.playframework.com/modules/scala-0.6/home
 [5]: http://vimeo.com/7731173
