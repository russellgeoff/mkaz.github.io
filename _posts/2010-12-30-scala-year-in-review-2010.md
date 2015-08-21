---
id: 483
title: Scala Year in Review 2010
author: Marcus Kazmierczak
layout: post
permalink: /2010/12/30/scala-year-in-review-2010/
categories:
  - scala
---
A year in review for Scala, 2010 was a great year for continued expansion of Scala. Here are a few highlights from major releases to new books and further adoption. 2011 looks poised to have an even bigger break out year.

### Major Releases

The biggest news of the year is the finalized release of **Scala 2.8**. The 2.8 version wraps up a major effort by the Scala Team and lays out the ground work for further growth. Scala 2.8 created some binary incompatibility with previous versions, but planned to be stabilized going forward. A few of the major changes to sub-systems include [Scala Collections][1], [Scala Actors][2], and [Scala Package Objects][3]. Plus a bunch more, see [Release Announcement 7/14/2010][4]

Two major **web frameworks** also were updated. The fantastic [Play Framework][5] released version 1.1 with [built-in Scala support][6]. You can read [my previous article on the Play Framework][7], which I describe why I like it so.

Also [Lift][8] released a major version 2.0. Founder David Pollak described Lift 2.0 as radically more developer friendly with new features including CouchDB support, OAuth support (thanks to our friends from FourSquare), OSGi support, LDAP support and much more. Development on Lift continues at an astounding rate with numerous additional features being added what seems daily.

### News and Events

Martin Odersky started **ScalaSolutions** a company to provide support, consulting, training and enterprise tools around Scala. An important event because it clearly and tangibly demonstrates that Odersky does not view Scala as just an &#8220;academic" language, criticism it often receives. [Press Release Oct 4, 2010][9]

**Scala recognition continues to grow** &#8211; This survey on Java Net Blog shows that Scala is succeeding growing into a widely used mainstream language. [Survey Results][10]

One of the coolest tools of the year, a [PHP to Scala Migration Tool][11]. Unfortunately, I haven't implemented it at my work but if we were to ever do that migration, it could be a huge help.

### Scala Usage

Just a couple of big name companies and projects using scala:

**LinkedIn's** scala usage continues with at least two major projects publicized, LinkedIn Signal a new social search tool using Scala + JRuby + Voldemort architecture [[Interview][12]] and the Norbert framework built to make it fast and easy to write asynchronous message based apps  
[[Slide presentation][13]]

**Guardian Open Platform** uses Scala to power their API to access their repository of media with over a million articles, video clips, photographs and audio tracks. Read the [news story][14], see [slides on system architecture][15] or read more about Guardian's [Open Platform][16]

**NASA's Jet Propulsion Laboratory** is using Scala to explore the use of DSLs in shuttle and toher space mission launch control applications. [More information][17], or [read the research paper][18], or you can [watch the presentation at ScalaDays 2010][19].

### Books Released in 2010

This year was a little quieter for new books on Scala, below are the two (English language) books released, but if you check out the [Scala books reference page][20] it looks like 2011 might be a banner year for Scala in the bookstore.

  * Steps in Scala: An Introduction to Object-Functional Programming [[<small>Buy now on Amazon</small>][21]]
  * Pro Scala: Monadic Design Patterns for the Web [[<small>Buy now on Amazon</small>][22]]



A Year in Review for Scala, please leave a comment or contact me if I missed something significant which I'm sure I have, considering I only started diving into Scala mid-way through this year. Interested in learning Scala? Check out [Graham's Guide to Learning Scala][23].

 [1]: http://www.scala-lang.org/docu/files/collections-api/collections-impl.html
 [2]: http://www.scala-lang.org/docu/files/actors-api/actors_api_guide.html
 [3]: http://www.scala-lang.org/node/7630
 [4]: http://www.scala-lang.org/node/7009
 [5]: http://www.playframework.com/
 [6]: http://www.playframework.com/modules/scala
 [7]: https://mkaz.com/archives/1312/scala-and-the-play-framework/
 [8]: http://liftweb.net/
 [9]: http://www.scala-lang.org/node/7812
 [10]: http://weblogs.java.net/blog/editor/archive/2010/03/12/scala-recognition-continues-grow
 [11]: http://code.google.com/p/php-to-scala-migration-helper/
 [12]: http://www.infoq.com/articles/linkedin-scala-jruby-voldemort
 [13]: http://days2010.scala-lang.org/node/138/159
 [14]: http://www.scala-lang.org/node/6508
 [15]: http://www.slideshare.net/openplatform/the-guardian-open-platform-content-api-implementation
 [16]: http://www.guardian.co.uk/open-platform/what-is-the-open-platform
 [17]: http://www.scala-lang.org/node/6605
 [18]: http://www.havelund.com/Publications/scala-days-2010-dsl.pdf
 [19]: http://days2010.scala-lang.org/node/138/143
 [20]: http://www.scala-lang.org/node/959
 [21]: http://www.amazon.com/gp/product/0521747589?ie=UTF8&tag=mkazcom-20&linkCode=as2&camp=1789&creative=390957&creativeASIN=0521747589
 [22]: http://www.amazon.com/gp/product/143022844X?ie=UTF8&tag=mkazcom-20&linkCode=as2&camp=1789&creative=390957&creativeASIN=143022844X
 [23]: http://grahamhackingscala.blogspot.com/2010/12/guide-to-learning-scala-by-graham.html
