---
id: 480
title: Backbone, Go and GAE starter app
author: Marcus Kazmierczak
layout: post
permalink: /2013/06/23/bongo-app-backbone-go-app-engine/
categories:
  - technology
tags:
  - backbonejs
  - golang
---
Bongo App is an example todo app using Backbone.js, Go and Google App Engine. I wanted an example app to learn Backbone.js and it seems like the todo app is the example du jour. This app also gives me an excuse to play more with golang which I really enjoy. However, I'm tired of setting up databases and web servers so decided to just use [Google App Engine][1] which also works with Go nicely.

[Backbone.js][2] is a front-end framework which handles routing, fetching, rendering and other front-end aspects of a web application. Backbone communicates to the back-end using a REST JSON interface, this works really well with Go. Since Go is not really intended as a web framework language but a services and system language, perfect for creating web service APIs.

It is not quite full feature, but I'm actually using it as my todo list. I welcome any help contributing and expanding the features, or just suggestions on how to improve since this is my first Backbone app and lots of learning as I set it up.

You can check out how I setup Backbone and Go. There were a few tricky bits with routing, setting up Backbone and Datstore Ids but all in all the two work really well together.

Code and install instructions: [https://github.com/mkaz/bongoapp](https://github.com/mkaz/bongoapp)

### Screenshot

![Bongo App Screenshot][3]

### Related Resources

  * [High Performance Apps with Go on App Engine][4]

  * [Todo.js][5] &#8211; example backbone app using localStorage backend

  * [Writing Web Applications in Go][6]

 [1]: http://appengine.google.com/
 [2]: http://backbonejs.org/
 [3]: https://raw.github.com/mkaz/bongoapp/master/static/bongo-screenshot.png
 [4]: https://www.youtube.com/watch?v=fc25ihfXhbg
 [5]: http://backbonejs.org/docs/todos.html
 [6]: http://golang.org/doc/articles/wiki/
