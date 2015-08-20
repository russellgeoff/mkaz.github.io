---
id: 1105
title: Lanyon, a markdown web server
author: Marcus Kazmierczak
layout: post
guid: http://ebeab.com/?p=1105
permalink: /2014/05/07/lanyon-a-markdown-web-server/
geo_public:
  - 0
publicize_google_plus_url:
  - https://plus.google.com/115308324500133456489/posts/1wjCw9dQibr
publicize_twitter_user:
  - mkaz
publicize_twitter_url:
  - http://t.co/CJDvMk5dve
categories:
  - technology
tags:
  - golang
  - markdown
  - web server
---
I've just released a new bit of software I've been developing. **Lanyon** is a simple web server, which reads directories of markdown files and converts them to HTML and serves. An intuitive and easy way to create a website. It is open source and available on Github at [github.com/mkaz/lanyon][1]

Lanyon was derived from my static site generator, [Hastie][2] which is also written in Go. I grew tired of the multiple steps involved for static sites from creating the content, generating and publishing. Also, a static site generator has a duplicate source tree and a generated tree, with some assets in each. I wanted something to simplify that.

The server is very basic and probably only useful for the most basic of sites. One that is simply pure content organized by directories of files with markdown in it. I am running my personal site [mkaz.com][3] using it and it works well for that one case.

I've enjoyed playing with Go and really like it especially for command-line and systems type applications. I think using it as a web framework is a bit of a stretch, for example the templating is still relatively limited, but for this case as a server works well. The standard library is great and very complete, made writing a web server easy and only one external library is used and that is for the markdown conversion.

[Check it out][1] and let me know what you think.

 [1]: https://github.com/mkaz/lanyon
 [2]: https://github.com/mkaz/hastie
 [3]: http://www.mkaz.com/