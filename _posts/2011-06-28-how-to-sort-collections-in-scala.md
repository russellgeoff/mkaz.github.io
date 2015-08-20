---
id: 716
title: How to Sort Collections in Scala
author: Marcus Kazmierczak
layout: post
guid: http://ebeab.com/?p=716
permalink: /2011/06/28/how-to-sort-collections-in-scala/
categories:
  - scala
---
Here is a list of examples sorting different data structures in Scala, Lists and Arrays

<pre><code class="scala">// data structures working with
val s = List( "a", "d", "F", "B", "e")
val n = List(3, 7, 2, 1, 5)
val m = Map(
    -2 -&gt; 5,
    2 -&gt; 6,
    5 -&gt; 9,
    1 -&gt; 2,
    0 -&gt; -16,
    -1 -&gt; -4
)
</code></pre>

Using the built-in <tt>sorted</tt> method

<pre><code class="scala">s.sorted
res0: List = List(B, F, a, d, e)

n.sorted
res1: List[Int] = List(1, 2, 3, 5, 7)

// NOTE: map object does not have sorted method
</code></pre>

### Case Insensitive Search

Use <tt>sortWith</tt> to create a custom comparison function for sorting case-insensitive.

<pre><code class="scala">/* sort alphabetical and ignoring case */
def compfn1(e1: String, e2: String) = (e1 compareToIgnoreCase e2) &lt; 0

/* sort alphabetical and ignoring case: alternate */
def compfn2(e1: String, e2: String) = (e1.toLowerCase &lt; e2.toLowerCase)

s.sortWith(compfn1)
res2: List = List(a, B, d, e, F)

s.sortWith(compfn2)
res3: List = List(a, B, d, e, F)

/* Or you can do so using anonymous function (Thanks Rahul) */
s.sortWith(_.toLowerCase &lt; _.toLowerCase)
res4: List = List(a, B, d, e, F)
</code></pre>

### How to Sort a Map by Key or Value

<pre><code class="scala">// sort by key can use sorted
m.toList.sorted foreach {
    case (key, value) =&gt;
        println(key + " = " + value)
}

// sort by value
m.toList sortBy ( _._2 ) foreach {
    case (key, value) =&gt;
        println(key + " = " + value)
}
</code></pre>
