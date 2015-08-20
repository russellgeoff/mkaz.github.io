---
id: 683
title: Python Script to Watch and Sync Directory
author: Marcus Kazmierczak
layout: post
guid: http://ebeab.com/?p=683
permalink: /2013/03/09/python-script-to-watch-and-sync-directory/
categories:
  - solutions log
tags:
  - python
  - sync
---
At work we have a rather complex setup which is prohibitive to running a full working environment locally, so we have sandboxes on remote servers that run our development code. However, as much as I love vim, it can be challenging at times to do development on a remote server full-time.

You are limited to just command-line tools or an extra step to upload when saving locally. There are a few solutions, some are use [Sublime Text][1] and the [SFTP plug-in][2] which auto-uploads on save, a few are using [PhpStorm IDE][3] which also has the ability to upload on save.

Both are fine tools, but I want a way to use tool and automatically upload any changes to the remote server. I always like to try out the latest and greatest, though the funny thing is the main editor I'm using is MacVim.

I discovered the FSEvents and [Python bindings][4] which is a Mac OS X system library that can monitor a directory for file change events. Here's a brief example of how to use.

<pre><code class="python">from fsevents import Observer, Stream

def event_callback(event):
    filename = event.name
    print "Filename: ", event.name

def clean_exit(signal, frame):
    global observer, stream
    observer.unschedule(stream)
    observer.stop()

observer = Observer()
observer.start()
stream = Stream(event_callback, "~/tmp/", file_events=True)
observer.schedule(stream)

# run until ctrl-c
signal.signal(signal.SIGINT, clean_exit)
signal.pause()
</code></pre>

I created a full script that triggers an rsync command to copy my local file to the remote host on file change. This makes it a pretty nice way to use a file system event to trigger whatever you want.

Download from here: <https://github.com/mkaz/fswatch>

Also, anyone know why I can't always get a clean exit with ctrl-c using signal.pause()?

 [1]: http://www.sublimetext.com/
 [2]: http://wbond.net/sublime_packages/sftp
 [3]: http://www.jetbrains.com/phpstorm/
 [4]: https://pypi.python.org/pypi/MacFSEvents