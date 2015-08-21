---
id: 497
title: Goodbye XML, Hello JSON
author: Marcus Kazmierczak
layout: post
permalink: /2007/03/02/goodbye-xml-hello-json/
categories:
  - classics
tags:
  - json
  - xml
---
About four years ago I wrote an article on [ the limitations of XML][1], I'm here to back that up with some numbers. All of the same issues apply to XML today as they did then. It is still a bloated format, still requires external libraries and still takes plenty of code to parse.

Our search at [Maya's Mom][2] runs on Lucene/Tomcat and was returning XML to PHP over HTTP. I'm not quite sure my initial decision on this, probably so used to hearing Java with XML over HTTP it sounded fine at the time. Since we are working on improving our search and always one for embracing change, we switched Lucene to return [JSON.][3]

Now instead of using an external library and several routines to parse the data, it is done with the PHP JSON module and one command: [json_decode()][4]. The JSON module is a C module built in to PHP, which is one reason it is much quicker. The decode converts the data straight to PHP objects and arrays. One stroke done.

> deleting code is even better than writing code

The JSON format is far more terse than XML, reducing network load. Plus JSON gives us a bit more flexibility for search; we do some type-ahead stuff which requires Ajax to call a PHP page which performs the search, parses the results and encodes to JSON to hand back to Javascript. Now since search can return JSON, it can all be done straight from Javascript reducing the amount of code to write and maintain.

**Performance Numbers**  
Converting to JSON removed over 200 lines of code, which deleting code is even better than writing code. Your mileage will obviously vary, during the conversion there was some code clean up and refactoring

Speed Improvements: a round trip query and parsing in XML was 400+ milliseconds; now reduced to less than 20 milliseconds, a 20x improvement!

More info: there is [ a minor debate][5] about the [two interchange formats][6]. Plus [an article comparing the two][7].

To me, there is no comparison.

 [1]: https://mkaz.com/2003/01/27/xml-scalability-limitations/
 [2]: http://www.mayasmom.com/
 [3]: http://www.json.org/
 [4]: http://us2.php.net/manual/en/ref.json.php
 [5]: http://blogs.msdn.com/b/mikechampion/archive/2006/12/21/the-json-vs-xml-debate-begins-in-earnest.aspx
 [6]: http://www.infoq.com/news/2006/12/json-vs-xml-debate
 [7]: http://www.json.org/xml.html
