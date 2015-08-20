---
id: 471
title: 'Rich Text Editor &#8211; IE, Firefox, Safari ?'
author: Marcus Kazmierczak
layout: post
guid: http://ebeab.com/?p=471
permalink: /2007/01/17/rich-text-editor-ie-firefox-safari/
categories:
  - technology
---
**Things should be easier.**

Why can't I do the following with HTML:

```
    <textarea 
        richtext="yes" 
        buttons="bold,italic,copy,cut,paste,lists" 
        resizable="yes" ... >
    </textarea>
```

It would display a nice rich text editor, native to the browser with all the necessary controls and shortcuts.


When submitting the rich textarea it would simply POST well-formatted HTML as you would expect. You wouldn't need a huge download, buggy javascript, different editor widgets for each site. You could have the same consistent spell checker every where.

Instead I'll use [Moxie's Tiny-MCE][1] with it's little idiosyncracies.

Next Up: W3C, where's my drag-and-drop image upload standard?

 [1]: http://www.tinymce.com/
