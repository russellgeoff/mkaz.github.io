---
id: 708
title: 10 Scala One Liners to Impress Your Friends
author: Marcus Kazmierczak
layout: post
guid: http://ebeab.com/?p=708
permalink: /2011/05/31/10-scala-one-liners-to-impress-your-friends/
categories:
  - solutions log
tags:
  - scala
---
Here are 10 one-liners which show the power of scala programming, impress your friends and woo women; ok, maybe not. However, these one liners are a good set of examples using functional programming and scala syntax you may not be familiar with. I feel there is no better way to learn than to see real examples.

**Updated: June 17, 2011** &#8211; I&rsquo;m amazed at the popularity of this post, glad everyone enjoyed it and to see it duplicated across so many languages. I&rsquo;ve included some of the suggestions to shorten up some of my scala examples. Some I intentionally left longer as a way for explaining / understanding what the functions were doing, not necessarily to produce the shortest possible code; so I&rsquo;ll include both.

### 1. Multiple Each Item in a List by 2

The `map` function takes each element in the list and applies it to the corresponding function. In this example, we take each element and multiply it by 2. This will return a list of equivalent size, compare to other examples which use `reduceLeft` and `foldLeft` those functions return only a single value not a list.

<pre><code class="scala">(1 to 10) map { _ * 2 }
</code></pre>

### 2. Sum a List of Numbers

The most common example using `reduceLeft` is summing a list of numbers. This example sums the numbers 1 to 1000 using the range function to create our list of numbers and reduceLeft iterates and sum together returning a single value. Added simpler example using built-in sum function.

<pre><code class="scala">(1 to 1000).reduceLeft( _ + _ )
(1 to 1000).sum
</code></pre>

### 3. Verify if Exists in a String

This example returns a boolean if a word in a list exists in a string. I used this example for checking if a tweet contains a word I&rsquo;m interested in. I suppose technically it is three lines, but the first two are just setting variables.

<pre><code class="scala">val wordList = List("scala", "akka", "play framework", "sbt", "typesafe")
val tweet = "This is an example tweet talking about scala and sbt."

(wordList.foldLeft(false)( _ || tweet.contains(_) ))
wordList.exists(tweet.contains)
</code></pre>

### 4. Read in a File

This one-liner might only be impressive if you are coming from a Java background, it is pretty common now to be able to read a file in with one line of code. Here are two examples of reading in a file, one reads entire file in to a string, the other reads in each line as an entry in a List.

<pre><code class="scala">val fileText = io.Source.fromFile("data.txt").mkString

val fileLines = io.Source.fromFile("data.txt").getLines.toList
</code></pre>

### 5. Happy Birthday to You!

A common one-liner which prints out the Happy Birthday song. This illustrates scala&rsquo;s ternary operator as well as combining `map` and `foreach`.

<pre><code class="scala">(1 to 4).map { i =&gt; "Happy Birthday " + (if (i == 3) "dear NAME" else "to You") }.foreach { println }
</code></pre>

### 6. Filter list of numbers

Filter a list of numbers into two categories based on a criteria using `partition`.This example creates two lists of students based on their test scores.

<pre><code class="scala">val (passed, failed) = List(49, 58, 76, 82, 88, 90) partition ( _ &gt; 60 )
</code></pre>

### 7. Fetch and Parse an XML web service

Since XML is a native structure to scala, parsing an XML feed comes with no effort. Here&rsquo;s an example fetching the Twitter search feed.

<pre><code class="scala">val results = XML.load("http://search.twitter.com/search.atom?&q=scala")
</code></pre>

### 8. Find minimum (or maximum) in a List

Another couple of examples using `reduceLeft` to iterate through a list and apply a function. Added simpler examples of the method min/max on the list.

<pre><code class="scala">List(14, 35, -7, 46, 98).reduceLeft ( _ min _ )
List(14, 35, -7, 46, 98).min

List(14, 35, -7, 46, 98).reduceLeft ( _ max _ )
List(14, 35, -7, 46, 98).max
</code></pre>

### 9. Parallel Processing

Scala 2.9 introduced a new collection type called &ldquo;parallel collections&rdquo; which utilize multi-core processors when performing bulk operations such as `foreach`, `map`, `filter`, etc&hellip; Here&rsquo;s a [video of Aleksandar Prokopec explaining parallel collections][1] at Scala Days 2010.

This example is not quite a copy-and-paste into the REPL, but it illustrates how to use parallel collections. Imagine you had a set of data defined in a list `dataList` and a function `processItem` which was very cpu intense. The following one-liner would give you parallel processing over the list.

<pre><code class="scala">val result = dataList.par.map( line =&gt; processItem(line) )
</code></pre>

### 10. Sieve of Eratosthenes

Ok, this one isn&rsquo;t quite practical and technically is not a one-liner since it relies on a operator being previously defined, but it is still pretty darn cool, even if it is unreadable. [Daniel Sobral][2] created the Sieve of Eratosthenes which is a algorithm used to [determine if a number is prime][3].

<pre><code class="scala">(n: Int) =&gt; (2 to n) |&gt; (r =&gt; r.foldLeft(r.toSet)((ps, x) =&gt; if (ps(x)) ps -- (x * x to n by x) else ps))
</code></pre>

Requires definition of |> operator, a syntax borrowed from F#. See [Steve Gilham&rsquo;s blog][4] for an example.

 [1]: http://days2010.scala-lang.org/node/138/140
 [2]: http://dcsobral.blogspot.com/2010/12/sieve-of-eratosthenes-real-one-scala.html
 [3]: https://mkaz.com/math/primes/prime_numbers.html
 [4]: http://stevegilham.blogspot.com/2009/01/pipe-operator-in-scala.html