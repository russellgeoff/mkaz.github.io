---
id: 714
title: How to Convert XML to JSON
author: Marcus Kazmierczak
layout: post
permalink: /2011/05/23/how-to-convert-xml-to-json/
categories:
  - scala
---
Download lift-json jar from <http://scala-tools.org/repo-releases/net/liftweb/>

Be sure to grab the proper library for your Scala version, at time of this post the latest was located at [http://scala-tools.org/repo-releases/net/liftweb/lift-json_2.8.<sup>1</sup>&frasl;<sub>2</sub>.3-RC5/][1]

<pre><code class="scala">import net.liftweb.json._
import net.liftweb.json.JsonAST._

val data = xml.XML.loadFile("quotie.xml")
val str = Printer.pretty(render(Xml.toJson(data)))

var out_file = new java.io.FileOutputStream("quotie.json")
var out_stream = new java.io.PrintStream(out_file)

out_stream.print(str)
out_stream.close
</code></pre>

 [1]: http://scala-tools.org/repo-releases/net/liftweb/lift-json_2.8.1/2.3-RC5/
