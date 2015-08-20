---
id: 481
title: 'XML: Scalability Limitations'
author: Marcus Kazmierczak
layout: post
guid: http://ebeab.com/?p=481
permalink: /2003/01/27/xml-scalability-limitations/
categories:
  - technology
---
XML is not the answer to all data storage and transport problems that many claim it to be. XML works ok for small amounts of data, when files are small it is much quicker and easier to parse. The real limitation of XML comes when dealing with large amounts of data.

I have seen this happen at work with services that return around 300kb of XML data, parsing and processing this to extract just a little bit of the required data takes an inordinate amount of time.

I have also seen this with Apple's iTunes application which stores the music library as XML files. I have a few thousand songs in iTunes selecting and updating of the meta-data has slowed down tremendously as my collection has grown. It worked fast and was quite responsive when I had a much smaller amount of data.

The problem arises because these programs stores all of their data in XML files instead of using a relational database. These XML files need to be read in completely and fully parsed to update any one field. Depending on what the parsing method used it can even require walking through all nodes to find the specific one you're looking for. Not a big deal when dealing with a small amount of data, but when dealing with thousands of records it's a whole other matter.

Relational databases such as MySQL can easily store hundreds of thousands of records and retrieve and update single records without bogging down at all. Years of database design and optimizations went into databases retrieve information quickly, compartively XML is an infant.

### File Size

Another problem that arises with XML is the excessively large data records. The tags and formatting of the data adds many bytes to what is usually simple data. What previously was comma or tab separated data now is wrapped with extraneous tags. Also each and every record in a file contains the same data definitions.

Here's a simple address book example, note the data definition is only included once on the first line:

    
    Comma Separated Example
    First Name, Last Name, Phone Number
    John, Doe, 555-1234
    Jane, Doe, 555-1234
    

Here's the same data expressed in common XML format:

<pre><code class="xml">
&lt;addressbook&gt;
&lt;record&gt;
&lt;firstname&gt;John&lt;/firstname&gt;
&lt;lastname&gt;Doe&lt;/lastname&gt;
&lt;phone&gt;555-1234&lt;/phone&gt;
&lt;/record&gt;
&lt;record&gt;
&lt;firstname&gt;Jane&lt;/firstname&gt;
&lt;lastname&gt;Doe&lt;/lastname&gt;
&lt;phone&gt;555-1234&lt;/phone&gt;
&lt;/record&gt;
&lt;/addressbook&gt;
</code></pre>

The above two examples have the exact same amount of data. The comma-separated format is only 76 bytes whereas the XML format is 210 bytes not counting whitespace. That's 2.75 times more data!! And that's just a simple example, I've seen with larger examples and more data this grow to be 50x more data! This extra data has to be stored and most likely moved around the network.

Storage is not really a big issue, especially with the 120gb drives today, but network and transporting of this data still takes time. Plus parsing comma delimited data is dead simple, usually one split command already built into the language. To parse XML you need external libraries and it still takes a few methods to parse the data properly.

I'm not recommending to move everything to comma separated files but sometimes they can be the appropriate solution especially for simple solutions. More complex and hierarchial data structures can be better represented using XML but usually at a cost of performance.

### Summary

XML is great for sharing small amounts of complex data in a well defined manner, for example when using in web services with published schemas. XML in place of a large relational database or very really simple data just doesn't quite cut it.

And XML as a scripting language, whoa.. that's going to takes it's own whole article.

### Related Links:

  * [XmlSuck.com][1] is a web site covering essential issues, opinions, and programming advice from the XML developer community, without the unbridaled hype and blind devotion.

  * [Why XML is Awful?][2] An article discussing why XML is awful, harmful and crap. A good read, not just troll crap spouting off.

  * [XML Quotes 2003][3] Quotes about XML throughout the year, I leave it to the user to figure out how to find 1998 thru 2002 quotes. Hint: Look at the URL.

 [1]: http://xmlsuck.com/
 [2]: http://web.archive.org/web/20090621075848/http://www.itee.uq.edu.au/~leonard/essay/xml.html
 [3]: http://web.archive.org/web/20090621075848/http://www.ibiblio.org/xml/quotes2003.html