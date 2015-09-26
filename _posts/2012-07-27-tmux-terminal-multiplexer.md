---
title: 'Tmux - Terminal Multiplexer'
author: Marcus Kazmierczak
layout: post
permalink: /2012/07/27/tmux-terminal-multiplexer/
categories:
  - solutions log
tags:
  - linux
  - screen
  - tmux
---

**tmux** is a terminal multiplexer, or you can consider it a "window" or "tab" manager for the terminal. I've been a user of **screen** for a long time, but switched to tmux due to screen development being stale, it stayed stable but not as easy to use; leaving the door open for Tmux which is easier and more capable.

### Basics

Tmux is typically not installed by default, but is available in most package repositories. For Debian/Ubuntu, `apt-get install tmux` and for Mac brew users, `brew install tmux`

To start a session simply: `$ tmux`

Once started, you issue commands using `ctrl-b` (default), this is called the "prefix". You can also map another key, I'm used to using `ctrl-w` in screen, so I remap mine in tmux.

To rebind keys: create `~/.tmux.conf`

    set -g prefix C-w


After making a change to the .tmux.conf file you will need to either restart tmux, exit using `ctrl-d` or you can re-source it within tmux by typing the prefix `ctrl-b` and then `:` and the command `source-file ~/.tmux-conf`

#### Commands

<table cellpadding="6" cellspacing="0" border="1">
  <tr>
    <td>
      ctrl-w c
    </td>

    <td>
      Create New Window
    </td>
  </tr>

  <tr>
    <td>
      ctrl-w n
    </td>

    <td>
      Next Window
    </td>
  </tr>

  <tr>
    <td>
      ctrl-w p
    </td>

    <td>
      Previous Window
    </td>
  </tr>

  <tr>
    <td>
      ctrl-w 0-9
    </td>

    <td>
      Switch to Window #
    </td>
  </tr>

  <tr>
    <td>
      ctrl-w d
    </td>

    <td>
      Detach from current session (it's still there)
    </td>
  </tr>
</table>

#### Detach and Reattach

You can detach from a tmux session using `ctrl-w d` ; All your screens will still exist, exactly how you let them, with all running processes. You can even close your terminal sesssion, ie. disconnect if you were logged in remotely.

You can reattach using: `$ tmux attach`

After reattaching, everything will be as you left it. This is amazing when working with remote hosts, especially if you get dragged away to a meeting and unplug your network and forget to disconnect or lost connection due to flaky wifis. You can log back in, reattach and you're exactly how you left it.

#### Scrolling

Tmux is its own window manager and operateas outside of the system windowing, which makes scrolling a bit more difficult. To enter scrollback mode use `ctrl-w [` and then to control scrolling it is standard vim commands.

    h,j,k,l - cursor movement
    ctrl-b  - back a page
    ctrl-f  - forward a ag
    /       - search forward
    ?       - search backward


Hit enter to escape scrolling mode.

#### Split Windows

For me the most useful part of tmux is its ability to split windows. This allows me to configure the terminal with a tailed log, command section and a vim editor all in the same area.

The default split window commands are as follows:

<table cellpadding="6" cellspacing="0" border="1">
  <tr>
    <td>
      ctrl-w "
    </td>

    <td>
      Split screen horizontally
    </td>
  </tr>

  <tr>
    <td>
      ctrl-w %
    </td>

    <td>
      Split screen vertically
    </td>
  </tr>

  <tr>
    <td>
      ctrl-w o
    </td>

    <td>
      Navigate between splits
    </td>
  </tr>

  <tr>
    <td>
      ctrl-w X
    </td>

    <td>
      Remove current split
    </td>
  </tr>

  <tr>
    <td>
      ctrl-w Q
    </td>

    <td>
      Remove all other splits
    </td>
  </tr>

  <tr>
    <td>
      ctrl-w :resize
    </td>

    <td>
      Resize Screen (prompts for lines)
    </td>
  </tr>
</table>

However, these do not map well mentally for me, so I switch the bindings to `-` and `|` which map to horizontal and vertical splits. Here's how I bind those keys:

    bind - splitw -v -p 50
    bind | splitw -h -p 50


#### Navigating Windows

There are a few additional ways I navigate split windows, I map the Alt+Arrow keys to move around and also enable the mouse to resize and click into the areas. Here are my configs for these:

    # use alt+arrow to switch panes
    bind -n M-Left select-pane -L
    bind -n M-Right select-pane -R
    bind -n M-Up select-pane -U
    bind -n M-Down select-pane -D

    # set mouse modes
    set-window-option -g mode-mouse on
    set-option -g mouse-select-pane on
    set-option -g mouse-resize-pane on
    set-option -g mouse-select-window on


### Sharing Interactive Sessions

Just like in screeen, you can use tmux to share interactive sessions, which is great for code review or pair programming.

To share a tmux session, have a user login and create session storing socket in /tmp and setting permissive permissions.

    $ tmux -S /tmp/da_socket
    $ chmod 777 /tmp/da_socket


The second user logged in to the same machine, can now connect to that session

    $ tmux -S /tmp/da_socket attach


You are now in the same session, and will see and type what the other sees. Hack away!

### Additional Tips

You can also type extended commands for tmux, the command `ctrl-w :` will enter in a command-line mode. You can then issue various commands such as:

    # split window horizontally 50%
    splitw -h -p 50

    # split window vertically 80%/20%
    splitw -v -p 20


##### Escape Key Slow

I ran into an issue with the escape key having a noticeable delay, this was particularly annoying in vim. The follow config in tmux.conf removed the delay.

    # remove delay in escape (vim)
    set -s escape-time 0


##### Copy and Paste - Tmux / iTerm / Mac

I don't really understand the issue, you can Google to find out more but my solution was the following. First install utility using brew:

    brew install reattach-to-user-namespace

Next in tmux.conf include
    
    # copy-paste
    set-option -g default-command "reattach-to-user-namespace -l bash"

This more or less fixed it, one thing for selecting text, use Option + Mouse and then you can use cmd+c to copy.


### Additional Resources

  * [My tmux.conf configuration](https://github.com/mkaz/dotfiles/blob/master/rcfiles/tmux.conf)

  * [tmux home][1]

  * [tmux man page][2] &#8211; When in doubt, man out

  * [TMUX &#8211; The Terminal Multiplexer][3]

  * [Unix Screen Notes][4] &#8211; my notes on using screen

 [1]: http://tmux.sourceforge.net/
 [2]: http://manpages.ubuntu.com/manpages/precise/en/man1/tmux.1.html
 [3]: http://blog.hawkhost.com/2010/06/28/tmux-the-terminal-multiplexer/
 [4]: /2008/05/01/gnu-screen-utility/
