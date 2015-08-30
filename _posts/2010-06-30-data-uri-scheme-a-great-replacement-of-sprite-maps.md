---
id: 693
title: Data URI to replace sprite maps
author: Marcus Kazmierczak
layout: post
permalink: /2010/06/30/data-uri-scheme-a-great-replacement-of-sprite-maps/
categories:
  - solutions log
tags:
  - data uri scheme
  - images
  - sprite maps
---
One of my colleagues recently forwarded this slide presentation about Mobile Web Performance that he saw at the Velocity Conference. I'm leading a large mobile web project at our company, which conveniently enough, we were just discussing the need for sprite maps to reduce the number of requests.

So taking one of my engineer's suggestion and the above presentation I learned about *Data URI Scheme*, which is a way to use encoded data sent to the browser as text instead of a separate file, such as an image file.

Here's an example of a simple red square:

    data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABkAAAAZCAMAAADzN3VRAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAAZQTFRF/wAAAAAAQaMSAwAAABJJREFUeNpiYBgFo2AwAIAAAwACigABtnCV2AAAAABJRU5ErkJggg==


You can display directly by putting that in an IMG tag:

    <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABkAAAAZCAMAAADzN3VRAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAAZQTFRF/wAAAAAAQaMSAwAAABJJREFUeNpiYBgFo2AwAIAAAwACigABtnCV2AAAAABJRU5ErkJggg==" />


This will work in Firefox, Safari or Chrome and should work in IE9 and greater.

So once again our cool new fancy technique can't be used because of browser support, right? Wrong, IE is a fraction of the mobile web market. It is dominated by webkit browsers, which do support it. Particularly nice since mobile is an area where every requests makes a difference, considering the spotty networks and under powered phones (compared to a desktop browser)

### Using with CSS

Now, you don't necessarily want to include the data in an HTML file, because you won't get the benefit of **caching**. Here's an example of the Data URI Scheme used within CSS:

    .red_square {
        background url('data:image/png;base64,[encoding]');
        width: 25; height: 25;
    }

Replacing [encoding] with the large string, no line breaks or spaces, but keep the quotes. Than any where you want to use that image, just reference the CSS;

     <div class="red_square"></div>


You can collect up similar and common items that you might of previously put in a sprite map in a single css file. If you use a [CDN][1], such as Akamai, or even just using the browser cache, you'll end up delivering multiple images in a single request which can be cached. Just like a sprite map.

Using the Data URI Scheme it is easy to update a single image, which in a sprite map is tricky. Also it simplifies the reference of the images without requiring a more complex coordinate selection of images which is typically done in [CSS sprites][2].

### Summary

I think this is a great technique to reduce complexity for accessing images and provide greater performance to mobile users. I recommend checking it out, at my work we've already started implementing across our mobile sites.

### Further Reading

  * [Mobile Web Performance][3] presentation by Maximiliano Firtman
  * [Data URI Scheme][4] (Wikipedia)
  * [Base64 Unix Utility][5]
  * [Online Base64 Generator][6] (MobileFish)

 [1]: http://en.wikipedia.org/wiki/Content_delivery_network
 [2]: http://alistapart.com/article/sprites
 [3]: http://www.slideshare.net/firt/mobile-web-high-performance"
 [4]: http://en.wikipedia.org/wiki/Data_URI_scheme
 [5]: http://www.fourmilab.ch/webtools/base64/
 [6]: http://www.mobilefish.com/services/base64/base64.php
