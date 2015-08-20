---
id: 732
title: GNU Screen Utility
author: Marcus Kazmierczak
layout: post
guid: http://ebeab.com/?p=732
permalink: /2008/05/01/gnu-screen-utility/
categories:
  - solutions log
tags:
  - linux
  - screen
---
**GNU Screen** is a &ldquo;window&rdquo; manager for the terminal. Similar in concept to tabbed browsing in Firefox, but without the GUI, all command-line. It allows you to have multiple terminal sessions open while only taking up one on your desktop.

The screen utility also allows you to detach and leave the session running in the background. So you can exit the terminal; log back in; and reattach exactly how you left it, running processes and all. Great for remote server work, or if you accidentally disconnect or close the wrong window.

### Basics

The GNU screen command is simply: `$ screen`

Once you&rsquo;re in a screen, you can issue commands using ctrl-a (default), or you can map another key. Emacs and bash use ctrl-a, so you may want to map the escape key to a different key. To map to Ctrl-w use `escape "^Ww"` (see .screenrc below)

#### Screen Commands

<table cellpadding="6">
  <tr>
    <td>
      ctrl-a ctrl-c
    </td>
    
    <td>
      Create New Window
    </td>
  </tr>
  
  <tr>
    <td>
      ctrl-a ctrl-a
    </td>
    
    <td>
      Cycle Window
    </td>
  </tr>
  
  <tr>
    <td>
      ctrl-a ctrl-n
    </td>
    
    <td>
      Next Window
    </td>
  </tr>
  
  <tr>
    <td>
      ctrl-a ctrl-p
    </td>
    
    <td>
      Previous Window
    </td>
  </tr>
  
  <tr>
    <td>
      ctrl-a 0-9
    </td>
    
    <td>
      Switch to Window #
    </td>
  </tr>
  
  <tr>
    <td>
      ctrl-a d
    </td>
    
    <td>
      Detach from current screen (it's still there)
    </td>
  </tr>
</table>

#### Detach and Reattach

You can detach from a screen session using `ctrl-a d ` ; All your screens will still exist, with all running processes. You can even close your terminal sesssion, ie. disconnect if you were logged in remotely.

You can reattach using: `$ screen -r`

After reattaching, everything will be as you left it. All screens available and running processes. See the [screen man page][1] for multiple options on reattaching, I find using ` -RR ` works best.

#### Navigating and Scrolling

GNU Screen is its own window manager and operates outside of the system windowing, which makes scrolling and using the mouse a bit more difficult. First make sure you define a good chunk of lines to scrollback in your screenrc. Set using `defscrollback 5000`

Next to enter scrollback mode use `ctrl-a [` and then to control scrolling it is standard vim commands.

    h,j,k,l - cursor movement
    ctrl-b  - back a page
    ctrl-f  - forward a page
    /       - search forward
    ?       - search backward
    

#### Starting Screen Automatically

I have the following set up to start gnu sreen automatically when I log in to my server. You should place it in your shell startup (.bashrc or .bash_profile), this checks to make sure your not running screen and then starts it. When you detach from screen using `ctrl-a d` you will also disconnect if logged in to a remote server.

<pre><code class="bash">
if [ $SSH_TTY ] && [ -z $STY ]; then
    exec /usr/bin/screen -d -RR -A
fi
</code></pre>

### Using Multiple Windows

My typical usage is to have multiple full screen remote windows open using screen, for example one used as a file browser and run commands, another for vim open and editing, another tailing logs, etc&hellip; I then switch between the screens using `ctrl-a ctrl-a` which is really just holding down `ctrl` and hitting `&ldquo;a&rdquo;` twice this walks through the screens.

You can map keys to navigate between the different screens, here&rsquo;s how to set the key bindings:

<pre><code class="bash"># bind F5 and F6 to previous and next screen window
bindkey -k F5 prev
bindkey -k F6 next
</code></pre>

#### Using Titles for Your Windows

I setup my .screenrc file to display all open windows in the bottom status bar, see my config below. So using this I can set names for each of my windows to navigate through. To set a title use `ctrl-a : ` which enters command mode and then type `title YourWindowTitle`

#### Split Windows

Also, using gnu screen you can split the screen up into different panels, which is not really part of my workflow, since I do in vim, but an incredibly useful feature. Here&rsquo;s how to split windows in screen and navigate between:

<table cellpadding="6">
  <tr>
    <td>
      ctrl-a S
    </td>
    
    <td>
      Split screen horizontally
    </td>
  </tr>
  
  <tr>
    <td>
      ctrl-a |
    </td>
    
    <td>
      Split screen vertically
    </td>
  </tr>
  
  <tr>
    <td>
      ctrl-a tab
    </td>
    
    <td>
      Navigate between splits
    </td>
  </tr>
  
  <tr>
    <td>
      ctrl-a X
    </td>
    
    <td>
      Remove current split
    </td>
  </tr>
  
  <tr>
    <td>
      ctrl-a Q
    </td>
    
    <td>
      Remove all other splits
    </td>
  </tr>
  
  <tr>
    <td>
      ctrl-a :resize
    </td>
    
    <td>
      Resize Screen (prompts for lines)
    </td>
  </tr>
</table>

#### Collaborative Coding &#8211; Window Sharing

You can use GNU screen to share interactive sessions, allowing people to see and type in the same shared terminal. This could be a nice way to do pair-programming remotely or walk through a command-line demo.

Try the following:

  1. Start up to two terminal sessions, A and B, via ssh, telnet or even local.</li> 

  2. In Terminal-A, start up screen: `$ screen`</li> 

  3. In Terminal-B, connect to screen already established: `$ screen -x`</li> 

  4. Now whatever you type in either terminal will show up on both. They are actual the same screen shared.</li> 

This sharing can be done a few different ways with multiple people. At work, since most of us have admin rights, we simply &ldquo;su&rdquo; to the other person and connect to the screen as them.

Another way is to set the permissions on your pts/tty session, location is usually in /dev somewhere depending on your unix environment. Or use `$ mesg y` to set your tty session as writable.

### Background Color in Vim 

I had some problems with the background color in vim not highlighting and working properly when in a screen session. I was able to fix it by adding  
`term screen-256color` to my .screenrc and adding the following to my .vimrc file

    
    set t_Co=256
    highlight Normal ctermbg=NONE
    highlight nonText ctermbg=NONE
    

### My screenrc config

<pre><code class="bash"># screenrc
startup_message off
escape "^Aa"
defscrollback 5000

# add status lines
caption always "%{= bb}%{+b w}Screen: %n | %h %=%t %c"
hardstatus alwayslastline "%-Lw%{= BW}%50&gt;%n%f* %t%{-}%+Lw%&lt;&quot;

term screen-256color

</code></pre>

### TMUX &#8211; Terminal Multiplexer

There is a new improved window manager in town, I&rsquo;ve been trying out **TMUX** as a replacement for screen. It is a bit more refined and easier to configure and use, but I&rsquo;ve run into a few issues so far. Plus not a default in most distributions so may not be everywhere you login to. See [my notes on TMUX.][2]

### Additional Resources

  * [The Antidesktop][3] &#8211; another person's work flow, including his screen configuration

  * [The Power of Screen][4] &#8211; Mac OS X Hints article

  * If not installed and you need to download screen [GNU Screen Download][5] [mirror]

  * [Xterm Color Chart][6] &#8211; My article for customizing xterm and terminal

 [1]: http://www.gnu.org/software/screen/manual/screen.html
 [2]: https://mkaz.com/2012/07/27/tmux-terminal-multiplexer/
 [3]: http://palm.freecode.com/articles/the-antidesktop/
 [4]: http://hints.macworld.com/article.php?story=20021114055617124
 [5]: http://mirror.anl.gov/pub/gnu/screen/
 [6]: https://mkaz.com/2010/04/04/xterm-colors/