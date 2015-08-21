---
id: 720
title: Using Regular Expressions in Scala
author: Marcus Kazmierczak
layout: post
permalink: /2011/05/24/using-regular-expressions-in-scala/
categories:
  - scala
---
The easiest way of creating a regular expression in scala is by simply applying the <tt>.r</tt> method to a string. This creates a regular expression object, which then can be used to match and/or replace. See [Regex API][1] for available methods.

### Regular Expression &#8211; Linkify a string

This regular expression will find a URL in a string and autolink it, replacing it with an HTML version of the link.

<pre><code class="scala">var linked = "Some text. https://mkaz.com/ and a link"
val regexUrl = """http://[A-Za-z0-9-_]+.[A-Za-z0-9-_:%&?/.=]+""".r
linked = regexUrl.replaceAllIn(linked, "&lt;a href="$0"&gt;$0&lt;/a&gt;")
</code></pre>

### Regular Expression &#8211; check if there is a match

Here is a function I wrote to return a flag if the string matched a word list, I needed a case insensitive match otherwise I could have simply used `contains`. I&rsquo;m not sure if my solution is the most efficient way of doing this one, feels a bit ugly to me, but it works. I&rsquo;m open for improvements.

<pre><code class="scala">def existsFlag(str: String) = {
    var rtn = 0
    val words = List("dress", "choir", "youtube")
    words foreach { word =&gt;
        val rx = ("(?i)"+word).r   // (?i) is used for case insensitive
        rx.findFirstMatchIn(str) match {
            case Some(thing) =&gt; rtn = 1;
            case _ =&gt; 0  // I dont want to do anything with this case
        }
        rtn
    }
}
</code></pre>

 [1]: http://www.scala-lang.org/api/current/scala/util/matching/Regex.html
