---
id: 730
title: Ubuntu Guide for Mac Converts
author: Marcus Kazmierczak
layout: post
permalink: /2013/01/13/ubuntu-guide-for-mac-converts/
categories:
  - solutions log
tags:
  - linux
  - ubuntu
---
Here are some tips and tricks I've collected to help Mac users adjust to Ubuntu and Linux. Since OS X was released in 2001, Mac was my primary system; however, I'm not fond of the direction it is heading and switched my daily work computer to Ubuntu.

This guide is focused on development and business apps, getting work done. I do still use a Mac desktop at home, mainly for photo stuff, there is still nothing close to Adobe Lightroom in open source world.

### Equivalent Command-line Utilities

The Mac has two great built in functions **pbcopy** and **pbpaste** which allows you to pipe content to and from the clipboard. So you can pipe the output of a command to pbcopy and it will place it in the clipboard, which you can paste elsewhere. Here's the linux equivalent, once the aliases are setup they are used the same as the Mac.

```
alias pbcopy="xclip -selection clipboard"
alias pbpaste="xclip -selection clipboard -o"
```

The Mac command **open** will open a file using its default application, the linux equivalent is simply **xdg-open**, used the same way. The following will open the image filename.png in the default image viewer.

`$ xdg-open filename.png`

### Screen Capture

There are numerous screen capture tools available on Ubuntu, it comes packages with **screenshot** which maps nicely to my &#8220;Print Screen" key on my keyboard. You can script screen capture by using ImageMagick's **import**. Calling import with a filename will be the equivalent of Mac's Command-Shift-4, which you can select the area you want to capture.

`$ import my-screenshot.png`

Since its just a simple command, it can be scripted, this example will sleep for 10 seconds and then take a screenshot of the entire desktop.

`$ sleep 10; import -window root ScreenShot.png`

And even a slightly more powerful script, this will take a screnshot and upload to CloudApp in one command, [cloudshot.py][1]

See [my command-line tips][2] for more examples and ways to script on the command-line.

### Color Picker

If you want to lift a color from somewhere on screen, you can use the **gpick** utility. The package is available in the standard repository. Install: `$ apt-get install gpick`

<div id="attachment_941" class="wp-caption aligncenter" >
<img src="/images/gpick-screenshot.jpg" alt="Screenshot of GPick Color Picker" width="500" height="270" class="size-full wp-image-941" />

<p class="wp-caption-text">
GPick Color Picker
</p>
</div>

### How to Install a Font in Ubuntu

If you download a font and want to install it, an easy way to do so is use **gnome-font-viewer** which should be installed by default in Gnome desktops.

`gnome-font-viewer FONTFILE.ttf`

and then while in viewer click on Install.

### Application Launchers

The Mac has a few great apps for quick search and launching applications, Spotlight, Quicksilver and Alfred are three that I used on the Mac. Ubuntu has the same equivalent apps. Ubuntu **Unity Dash** is like Spotlight in OS X, the Dash launcher is built-in and does a good job launching apps and searching.

If you are looking for the equivalent of Alfred on Ubuntu, you should try out **Synapse**, it does all the searching, built-in calculation and extendable through plug-ins. If you prefer Quicksilver, **Kupfer** is the Linux match. One other to try is **Gnome Do**, each of the launchers are slightly different, but more extendable then the base Dash, which is similar to how Alfred is to Spotlight.

<div id="attachment_995" class="wp-caption aligncenter" >
<img src="/images/synapse-screenshot.png" alt="Screenshot of Synapse Application Launcher " title="Synapse Launcher" width="415" height="120" class="size-full wp-image-995" />

<p class="wp-caption-text">
Synapse Launcher
</p>
</div>

### Time Savers and Shortcuts

**TextExpander** is another great Mac time saver, the Linux equivalent is **AutoKey**. AutoKey does a good job expanding text and also easy to extend, you can use the shortcuts to trigger python scripts to do even more. Install: `apt-get install autokey-gtk`

### Applications

I had to switch from **1Password** to [**LastPass**][3] for password management, since there is no full client for 1Password available on Linux. LastPass supports importing of a 1Password export so transitioning was easy. Note: You can access 1Password on Linux by using Dropbox and [1PasswordAnywhere][4] but it is only read access, you can't create passwords or auto-fill.

Here is a much larger list of [Linux equivalents for OS X Apps][5]

### Graphics and Media

The one area still lagging a little with Linux is the overall graphics and media management. As a Photoshop stand-in, there is ** Gimp **, but it is complicated and still after many years difficult to learn. I'm been using the online photo editor [Pixlr][6] which actually is quicker to use since it is more intuitive for me.

For photo management, **Shotwell** is the best solution, but still far from Lightroom. This is one area that Mac and Windows have a lock-in and non-equivalent is on the horizon. If I was interested in fully cutting over, I would probably run Lightroom within a Windows VM.

### Cross-Platform Applications

The following are cross-platform applications that I use on both Mac and Linux.

  * Firefox
  * Sublime Text
  * vim
  * Skype
  * Pidgin (IM)
  * RescueTime



Have you switched? Leave a comment to help me and others out with any other tips or tricks you use.

### Related Links

  * [Command-line Basics and Tips][2]

  * [My Vim Cheat Sheet][7] &#8211; tips for using vim

  * [How to use GNU Screen][8]

  * [Xterm Colors Chart][9] &#8211; for customizing xterm and system colors

 [1]: https://gist.github.com/4525050
 [2]: /2013/12/29/command-line-basics-and-tips/
 [3]: https://lastpass.com/
 [4]: http://help.agilebits.com/1Password3/1passwordanywhere.html
 [5]: https://help.ubuntu.com/community/OSXApplicationsEquivalents
 [6]: http://pixlr.com/
 [7]: /2011/08/31/vim-cheat-sheet/
 [8]: /2008/05/01/gnu-screen-utility/
 [9]: /2010/04/04/xterm-colors/
