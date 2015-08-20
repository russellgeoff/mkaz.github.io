---
id: 722
title: Date Calculations in Scala
author: Marcus Kazmierczak
layout: post
guid: http://ebeab.com/?p=722
permalink: /2011/05/24/date-calculations-in-scala/
categories:
  - solutions log
tags:
  - date
  - jodatime
  - scala
---
A couple of solutions for formatting and calculating dates. These examples use the joda library, included with Play by default.

<pre><code class="scala">  import org.joda.time.DateTime
  import org.joda.time.format.DateTimeFormatter
  import org.joda.time.format.DateTimeFormat

  // create new date, yr, mon, day, hr, min, sec, ms
  val myDate = new DateTime(2010, 3, 1, 0, 0, 0, 0)

  // date calculations
  val oneMonthLater = myDate.plusMonths(1)
  val twoMonthsBefore = myDate.minusMonths(2)
  val twoDaysLater = myDate.minusDays(-2) // accepts negative values

  // formatting
  println(myDate.toString("yyyy-MM-dd")

  DateTimeFormatter fmt = ISODateTimeFormat.dateTime()

  println(myDate.toString(fmt))
</code></pre>

See [API][1] for additional info.

Plus [User Guide][2] and documentation for [Field Accessors][3].

 [1]: http://joda-time.sourceforge.net/apidocs/index.html
 [2]: http://joda-time.sourceforget.net/userguide.html
 [3]: http://joda-time.sourceforget.net/field.html