---
id: 726
title: Run script at start on Debian
author: Marcus Kazmierczak
layout: post
permalink: /2013/07/03/run-script-at-start-on-debian/
categories:
  - solutions log
tags:
  - debian
  - linux
  - script
  - startup
---
Using Debian, there are a few ways to automatically run a script when your system starts up. The following illustrates how to do so at the system level on boot. There are other ways to run scripts in other scenarios for example, when you login.

I run a straight debian install, but the following should also work for all debian based systems such as Ubuntu or Crunchbang.

### Run script on system boot

First you need to create the script to run, here is a template, modify the example commands in the start and stop sections.

<pre><code class="bash">#! /bin/sh

### BEGIN INIT INFO
# Provides:          foobar
# Required-Start:    $local_fs $network
# Required-Stop:     $local_fs
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: foobar
# Description:       more foo for your bars
### END INIT INFO

# Carry out specific functions when asked to by the system
case "$1" in
  start)
    echo "Starting foobar "

    # example 1 - system service
    # /usr/bin/foobar --config /etc/foo.conf start

    # example 2 - run script as user
    # su --login mkaz --command "/home/mkaz/bin/my-script --cmd-args"

    ;;
  stop)
    echo "Stopping foobar"

    # example 1
    # /usr/bin/foobar --config /etc/foo.conf stop

    ;;
  *)
    echo "Usage: /etc/init.d/foobar {start|stop}"
    exit 1
    ;;
esac

exit 0
</code></pre>

Save this file and move to `/etc/init.d` for example if I named my file `foobar`

<pre><code class="bash">sudo mv foobar /etc/init.d/       # move to init.d
sudo chmod 755 /etc/init.d/foobar # make executable
</code></pre>

The way linux runs script is it goes through different run levels and runs the scripts for each level. You can see these in the run level directories `ls /etc/rc*`. There exist links to each script to run at what level.

You could manually create the proper links to your new script, or there is a convenience script `update-rc.d` which is much easier. To create the links:

<pre><code class="bash">sudo update-rc.d foobar defaults  
</code></pre>

If you wish to remove the links, this still keeps the script:

<pre><code class="bash">sudo update-rc.d -f foobar remove
</code></pre>

Once added you can test starting your service using:

<pre><code class="bash">sudo service foobar start
</code></pre>

### Error or Issue

If you see this warning

    insserv: warning: script 'foobar' missing LSB tags and overrides


You probably did not includ the INIT INFO block, see template above. Your script will still run, just does not have the dependency info used by insserv program to try to start items in proper order.
