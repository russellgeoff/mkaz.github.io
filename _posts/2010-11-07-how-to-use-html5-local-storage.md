---
id: 702
title: How to use HTML5 local storage
author: Marcus Kazmierczak
layout: post
permalink: /2010/11/07/how-to-use-html5-local-storage/
categories:
  - solutions log
tags:
  - html5
  - javascript
---
A quick example on how to use HTML5 local storage, I was surprised on how easy it is to use. HTML5 introduces two new methods of storing local information on a user's browser, **localStorage** and **sessionStorage**. They are both used the same way, however localStorage persists while sessionStorage, as you would imagine only lasts as long as the browser's session.

Previously the only way to store data on a local desktop was to use cookies, which are limited in how much you can store. So the typical usage became storing a unique identifier for a user in the cookie, and using that to query a remote server to retrieve any data for that user. With local storage, you can avoid some back and forth, speed up the experience and possibly provide better security. More on that later, lets jump into the code.

There are two basic methods, one for setting an item in storage and one for getting that item, they are:

<pre><code class="javascript">// store item
localStorage.setItem("item_key", "value I am storing");

// retrieve item
var data = localStorage.getItem("item_key");
</code></pre>

That's it.

The storage saves values as strings, so if you want to store a different type of data object, such as an array or javascript object. You will need to JSONify it before storing. Here's an example storing an array.

<pre><code class="javascript">var listdata = [1, 2, 3];

// store array back to localstorage
localStorage.setItem("list_data_key",  JSON.stringify(listdata));

// retrieve jsonified stored data and convert
var storedData = localStorage.getItem("listData");
if (storedData) {
    listdata = JSON.parse(storedData);
}
</code></pre>

There are a few other helper functions that you will probably use:

Remove Single Key: `localStorage.removeItem("item_key");`

Clear All Local Storage: `localStorage.clear()`

Check if localStorage is supported:

<pre><code class="javascript">if (window.localStorage) {
    // yes!
}</code></pre>

Those are the basics of local storage.

Local storage is very similar to cookies in that the data is shared across all pages on the same domain. You'll have to weigh browser compatibility if you plan to use it, localStorage and sessionStorage are supported by Firefox 3.5, Safari 4.0, and IE8. Check [quirksmode.org][1] for details.

 [1]: http://quirksmode.org