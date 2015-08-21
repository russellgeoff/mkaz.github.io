---
id: 985
title: Disable Caps Lock in Ubuntu
author: Marcus Kazmierczak
layout: post
permalink: /2014/02/08/disable-caps-lock-in-ubuntu/
publicize_google_plus_url:
  - https://plus.google.com/115308324500133456489/posts/AM4c2Ppkrra
publicize_twitter_user:
  - mkaz
publicize_twitter_url:
  - http://t.co/EoDGJIjmwB
video_url:
  - 
quote_content:
  - 
quote_attribution:
  - 
categories:
  - solutions log
tags:
  - caps lock
  - linux
  - ubuntu
---
One of the first things I do on after any new Linux install is disable the caps lock key, it is useless, oddly though I never map it to anything else. Here's how to disable caps lock on Ubuntu.

## Disable Caps Lock on Ubuntu 13.10

The upgrade to 13.10 actually made it a bit more difficult to disable capslock. The easiest way to do so is to install the **Tweak Tool** and use the settings there.

The Gnome Tweak Tool is in the standard repository, so you can install using apt-get, like so:

<pre class="brush: plain; title: ; notranslate" title="">sudo apt-get install gnome-tweak-tool
</pre>

You can then run Tweak Tool, select **Typing** and set **Caps Lock key behavior** to **Caps Lock is disabled**. See screen shot below.

<img src="https://mkaz.com/wp-content/uploads/2014/02/tweak-tool-disable-capslock.png" alt="Tweak Tool Disable Caps Lock Screenshot" width="620" height="328" class="aligncenter size-full wp-image-987" />

## Disable Caps Lock on Ubuntu 13.04

If you are running a previous version of Ubuntu, you don't need to install a separate tool, but it does require a little hunting. You can find the setting for Caps Lock behavior in:

System Settings &#187; Region and Language &#187; Layouts &#187; Options &#187; Caps Lock Behaviour

## Other OS?

  * [How to disable Caps Lock in Linux Mint][1]

  * [How to disable Caps Lock in Mac OS X][2]

 [1]: https://mkaz.com/2013/12/08/disable-capslock-on-linux-mint/
 [2]: https://mkaz.com/2005/07/28/disable-caps-lock-on-mac-os-x/