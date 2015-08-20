---
id: 691
title: How to Fix Double Posting
author: Marcus Kazmierczak
layout: post
guid: http://ebeab.com/?p=691
permalink: /2007/07/03/how-to-fix-double-posting/
categories:
  - solutions log
tags:
  - it can be easier
  - webdev
---
You see the following on order forms all the time

> &#8220;press the button only once or we may charge you double&#8221;</em> 

This is just laziness on the developers, there are a few easy techniques to avoid double processing a form. Plus if you have ever watched my mother-in-law use a computer, there is a fine line between clicking once and double (or even triple) clicking.

Here's one way to solve double posting. The process is:

  1. Generate a unique key for every HTML form
  2. When processing the form insert the unique key into a transaction database table
  3. For the transaction table, create a UNIQUE INDEX on the key field
  4. So when inserting the key, if there is a duplicate key it will fail
  5. If insert fails, don't reprocess form
  6. A clean up batch job can run daily to delete items from table to kept tidy

Next: how to eliminate spaces in pesky credit card forms