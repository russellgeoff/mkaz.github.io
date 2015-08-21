---
id: 501
title: Computers, we have a long way to go
author: Marcus Kazmierczak
layout: post
permalink: /2007/01/16/computers-we-have-a-long-way-to-go/
categories:
  - classics
---
After trying to remember the HTML character code for the fancy quote mark for the 1,00th time, I realized we have a long way to go with interactions with computers. I'm not talking just pretty GUI's and simple keyboard and mouse interfaces but the whole [HCI][1] gambit; computers are supposed to be smart and make things easier right?

Programming today is still plain ridiculous, yeh it's a step up from doing assembly code, but 10-20 years from now progamming in PHP, Java or C will seem as archaic as the punch cards of old. How come a compiler needs to crap out with a missing semi-colon &#8212; it even tells me and knows exactly where it is missing. Just fix it, shut up and move on.

I think the overall problem is things just aren't good enough to just do it. So there ends up being lots of extra checks, confirmations and annoyances. Libaries aren't abstracted enough, languages aren't at a high enough level, doing things that should be simple, aren't.

An example, it is a pain to just parse user input, store it in a database and display back to the user. It sounds like a stupid easy problem, being done everywhere right. It isn't, ask a engineer to try this: parse a block of text for links, the text may or may not contain HTML code, the links may or may not start with &#8220;http://" or &#8220;www." and create links for them, but don't mess up any of the HTML code which may have images, embeds or links themselves.

Don't forget to fix all special characters, encoding types plus any weird stuff Word throws in when people copy and paste from which ends up losing all of their formatting. Here's the WordPress code to [convert and format user input][2], how many different peple across all the sites have written this same type of shit. I know I have, a few times.

Programming tends to be difficult and complex so engineers end up focusing on all these little things and spending time getting things just to work instead of building really easy interfaces for people to use. Such as:

*Computer, I just took a photo, please share it with my friends. It's the last one on my camera. *

No wires, No connections, No programs. Just do it. The computer could use voice, wireless and contact/preference info all of which are available today. All should work together. It just sends the photo to my friends in whatever format they want: cellphone, e-mail, web link, whatever. Just do it.

 [1]: http://en.wikipedia.org/wiki/Human-Computer_Interaction
 [2]: http://core.trac.wordpress.org/browser/trunk/wp-includes/formatting.php
