---
id: 800
title: Command-line Basics and Tips
author: Marcus Kazmierczak
layout: post
guid: http://ebeab.com/?p=800
permalink: /2013/12/29/command-line-basics-and-tips/
publicize_twitter_user:
  - mkaz
publicize_twitter_url:
  - http://t.co/VX0PB5TIVY
categories:
  - solutions log
tags:
  - command-line
  - linux
  - mac os x
  - unix
---
A collection of tips to help you on the command-line using Linux, Mac OS X or other unixy command-line system. You might already know most but hopefully there are a few new ones or helpful tips on how to save time and use in productive ways. I've tried to include real and useful examples for each.

## Setup

First up, **use source control** to help manage all of your configs so its easier to setup new systems and to track changes. I have a &#8220;dotfiles&#8221; repository where I keep my stuff. I then create symlinks from the repo to the proper spot, so the repo version is always current. A symlink example of my main profile:  
`ln -s ~/dotfiles/profile ~/.profile`

With a repository, I can then check out my dotfiles to whatever new machine and have my setup all ready. Here is a two step setup of a remote subversion repository.  
`svnadmin create /opt/svn/repo-name  # remote server`  
`svn co svn+ssh://remote.server.com/opt/svn/repo-name  # local checkout`

Secondly, what files do you put all this good stuff in. I have a main profile file which I put common pieces and since I bounce between Macs and Linux, I also have system specific profiles. Additionally, I create host specific files for each server, your mileage may vary. Here's how I source the other files from the main profile:

<pre class="brush: bash; title: ; notranslate" title="">SYS_OS=`uname -a`   # linux or mac
SHORT_HOSTNAME=`hostname -s`

# system aliases
if [[ "$SYS_OS" == &#039;Linux&#039; ]]; then
     PATH="..LINUX PATH..."
     source ~/dotfiles/aliases.lx
 else
     PATH="... MAC PATH..."
     source ~/dotfiles/aliases.mac
fi

 # run host specific profile
 if [[ -e ~/dotfiles/profile.$SHORT_HOSTNAME ]]; then
     source ~/dotfiles/profile.$SHORT_HOSTNAME
 fi
</pre>

## Use Aliases and Functions

The most common time saving tip is to use aliases for common commands and options, save yourself typing and remembering them. Here's one for tailing a log file which I do often. This is especially useful per host which may have log files in different spots, but I can always use `alog` to tail apache logs.  
`alias alog="tail -f /var/log/apache2/error.log"`

If you need permission, include sudo in the alias  
`alias alog="sudo tail -f /var/log/apache2/error.log"`  
`alias apt='sudo aptitude'`

Be observant of common tasks and commands that you do, particularly ones that you might make mistakes and create aliases for them. For example, different systems use different flags for `ps` command, create a common alias that works across all or combine grep within the command.  
`alias xps='ps -ax '`  
`alias xpsg='ps -ax | grep -i'`

If you have an alias, but want to run the normal command, put a `` in front:  
`ls`

You can use functions to use arguments in different spots or do a little more than an alias. Here's an alias which gives me the last 10 items in the current directory.  
`alias lsr="ls -lrt | tail -n 10"`

However, that only works in the current directory, using a function you can set it up to work by passing in any directory, the `$@` is the arguments passed into the function:  
`function lsr() { ls -lrt $@ | tail -n 10 ;}`  
`$ lsr /etc/`

## Navigate Directories Quickly

A couple of quick tips on navigating around using the command-line.

`cd` : goes straight to home directory  
`cd -` : cd with a dash returns to previous directory

I also create the following aliases to save time moving up directories:  
`alias cd.. = cd ..`  
`alias cd... = cd ../../`  
`alias cd.... = cd ../../../`

One of the best little utilities is **z.sh** which tracks your most common directories and then you can type `z dir` and it will take you directly there. For example, if you are always editing files in `/var/local/www/htdocs` just typing `z htdocs` will take you there. See [rupa's github repo][1] to download and setup.

There are mysterious functions called `pushd`, `popd` and `dirs` which use a stack to manage directories pushing them on and off the stack and changing directories as you go. I don't quite get how to use in real life. Drop in a comment if you do use them and in what setting.

## Learn Vim

Vim is a powerful text editor, there is way too much to go into in this article, so I'll link to some pointers. Becoming efficient with vim saved me the most time over anything, especially if you do a lot of work text editing or work on remote systems.

  * [Derek Wyatt Vim Tutorials][2] &#8211; fun and useful videos, I like Derek's style
  * [Vimcasts][3] &#8211; another video series
  * [Vim Cheat Sheet][4] &#8211; my vim cheat sheet 

## Common Commands

Use `**` to recurse through all sub-directories, for example to find all jpg files recursing all directories  
`ls -l **/*.jpg`

Redirect output to a file, the > operator will redirect the output of a command to a file, creating file if needed, overwriting file if exists.  
`ls -1 > file-list.txt`

Append output to a file, the >> operator will redirect the output of a command and append to an existing file, or create if needed  
`ls -lrt >> file-list.txt`

I use this to create scratch files to keep random notes:  
`echo "quick notes" >> ~/jots/notes.md`  
`svn commit -m "Awesome commit message" >> ~/jots/commits.log`

You can also redirect to /dev/null to ignore output:  
`python chatty-script.py > /dev/null       # standard errors show`  
`python chatty-script.py > /dev/null 2>&1  # errors and output to /dev/null `

The pipe operator, `|` takes output of one command and passes it as STDIN to the next command, the pipe is the magic glue of unix.  
`ls -l | grep myfile`

The `xargs` commands takes a piped in list and reverses it to be command line arguments to the next command  
`ls -1 | xargs touch`

Now you can start combining in various ways. For example, list all files installed, grab only the ones marked as &#8220;deinstall&#8221; and pass that list into aptitude to purge  
`dpkg —get-selections | grep deinstall | xargs aptitude purge`

This will delete all subversion files and directories, I never remember the syntax for the find command, so often pipe it into grep.  
`find . | grep .svn | xargs rm -rf`

Changing permissions using chmod can be tedious at times, but there are a few short cuts to use besides the octal numbers. Short cuts for **u**ser, **g**roup, **o**ther and **a**ll exist. Other is not user, not group. All is all three. So you can do the following

    chmod -R a+r *    # recursively give read rights to everyone
    chmod -R o-r *    # recursively remove read rights from other
    chmod u+rw *      # give user read + write access 
    chmod -R a+rX *   # sets all directories as read-executable
    

## Text Processing

Don't open a file just to see the first or last few lines  
`head file.txt   # first 10 lines`  
`tail file.txt   # last 10 lines`

Or if the file is short you, cat will ouput it all:  
`cat file.txt`

If I want to peek in a file I use `less`, because it will paginate if too big, is searchable, and easy to quit, plus no chance of editing if I'm just looking.  
`less file.txt`

Count lines in a file:  
`wc -l file.txt`

Count words in a file:  
`wc -w files.txt`

`grep` is one of my most used utilities, I use it often to filter on commands, as I've shown a few times above. The most common options I use are -i and -r for case-insensitive and recursive, but there are a few other nifty bits.

Use `-v` to show those that do not contain &#8220;match&#8221;:  
`grep -v match file.txt`

Use `-c` to count how many matches:  
`grep -c match file.txt`

Show list of files that match:  
`grep -rl match *`

Number of lines to show before and after match:  
`grep -B 2 -A 2 match file.txt`

If you search source code often, you really should use [ack-grep][5], it is super fast custom built for searching code. It automatically ignores subversion, git files and great for large projects with multiple languages such as PHP, JS, CSS, SQL. You can do custom searches for something in one language or all.

Example find mentions of jquery excluding javascript files:  
`ack-grep —nojs jquery`

I use the alias `ff` for my ack-grep, fast-find in my mind, because on Macs it installs as `ack` and on Linux as `ack-grep`  
`alias ff='ack-grep'`

I also have the following aliases setup to help search for functions or classes, hat tip to @martinremy for these:  
`function fff() { ack-grep --color-match=red -A 6 "function $1"; }`  
`function ffc() { ack-grep --color-match=red -A 6 "class $1"; }`

The amazing `awk`, `sed`, `cut`, `sort` and more can be used to process text in every which way. However, I mostly find their commands cryptic and tend to use on limited basis. A couple of easier ones that I can keep track of:

Remove duplicate lines:  
`sort -u file.txt > FILE.new`

`cut` displays columns using `-d` for delimiter, and `-f` the column numbers to grab.  
`cut -d ":" -f 1 /etc/passwd    # column 1`  
`cut -d ":" -f 1,3 /etc/passwd  # columns 1 and 4`  
`cut -d ":" -f 4- /etc/passwd   # columns 4 to end`

Substitute in file, outputting results:  
`sed s/foo/bar/ file.txt`

Substitute in file but saving to file:  
`sed -ie s/foo/bar/ file.txt`

Print lines 10 thru 20 of file:  
`sed -n '10,20p' file.txt`

However, that p argument in sed is just enough that I can't remember and I'm more likely to use head-tail by grabbing first 20 lines using head and pipe into tail which only shows last 10, not as efficient but I can remember how:  
`head -n 20 file.txt | tail`

A few pointers on learning more about these commands:

  * [Tutorial: Sed and Awk][6]
  * [Unix School: awk & sed][7]
  * [Useful Unix Commands for Data Science][8]

## Automate

**Use loops to run repetitive tasks**

You can use a loop on the command-line to do some simple tasks, an example creating a backup copy of all txt files:  
`$ for file in *.txt ; do cp $file $file.bak; done`

Also, I find myself using small bash scripts to run repetitive tasks. It is often quickest to copy-paste-edit commands in a text file, you can also add loops and logic to the script. Bash programming is pretty powerful, a little cryptic but learning a few basics can really help. See this [Bash Guide for Beginners][9]

A loop example, create a file called `loop.sh` with the following

    for VARIABLE in file1 file2 file3
    do
        echo $VARIABLE
    done
    

Run using: `$ bash loop.sh`

**Use cron to schedule tasks**  
Use cron to schedule routine tasks, such as backups, updates or other scripts you may want to run on a set basis. Cron is pretty powerful and can run things on just about an schedule, for example hourly, every other day, first monday of month, etc&#8230; I have a tutorial on [how to use unix crontab][10]

**Time an Event**  
If you want to see how long a script takes to run, you can use `time`. You simply type it before your command or script.  
`time sleep 5`

**Delay an Event**  
There is a sleep command, which I used above which allows you to delay something to be run, for example a screenshot, reminder, or something else you may want to run shortly, number in seconds.  
`sleep 5; echo "Foo"`

## Command-line Options and Tips

Create directories all the way down, use `-p` and it will create all the in-between directories as needed.  
`mkdir -p ~/Documents/dir1/dir2/dir3`

If you want this to be always the case:  
`alias mkdir="mkdir -p"`

Unzip and Extract in one command  
`tar xvfz tarball.tar.gz`  
`tar xvfj tarball.tar.bz2`

The `!!` command will run the previous command, by itself it isn't that useful since an up arrow will show previous command, but combined with `sudo` you can run previous command with sudo permission like so:  
`sudo !!`

For vim, add this to your vimrc, allow you to use `:w!!` to save using sudo

    " sudo write
    ca w!! w !sudo tee &gt;/dev/null "%"
    

Use `ctrl-r` on the command-line and start typing to search back for previous commands

A clever idea with `ctrl-r` is to use comments to tag a command, making it easier to search in the future. So when I type the original command like so:  
`dd if=debian.img of=/dev/disk2 bs=1m  # bootable-usb`

I can use `ctrl-r` and search on `bootable-usb` and it will bring it back, takes a little foresight that you'll want to search for the command again.

You can use `{` and `}` to specify a range of items for example

    $ echo {one,two,three}-alligator
    one-alligator two-alligator three-alligator
    

This is useful in various ways to save running the same command with a minor difference, I use this often when creating a set of directories, the following creates five directories:  
`mkdir -p app/storage/{cache,logs,meta,sessions,views}`

You can use `!(pattern)` to do something with everything except, so for example if you want to delete all files except .txt files:  
`rm !(*.txt)`

**Use SSH Config and SSH Keys**  
If you log in to various servers often, use ssh config for those servers, you can configure user and shortcuts to make it easier. For example, `ssh -l marcus.kaz remote.server.location.com` can turn into just `ssh remote`. See this article [Simplify Your Life with an SSH Config file][11]

Here's an article on [how to setup ssh keys and use ssh-agent][12]. Using ssh keys can be more secure than basic passwords and using ssh-agent makes using ssh keys easier by caching your password, so you don't have to retype frequently.

## Unix Utilities

You can use `rename` to batch rename a set of files, it uses a regex for syntax  
`rename "s/JPG/jpg/" *.JPG`

Rename files with spaces to dashes  
`rename "y/ /-/" *`

If you're working on the command-line and need a calendar, simply type `cal`

    $ cal
       December 2013
    Su Mo Tu We Th Fr Sa
     1  2  3  4  5  6  7
     8  9 10 11 12 13 14
    15 16 17 18 19 20 21
    22 23 24 25 26 27 28
    29 30 31
    

You can get also get any full year: `cal 2013`, `cal 1970`, `cal 1776`

The utility `shuf` can grab random lines from a file. This example will grab a single random line  
`shuf -n 1 quotes.txt`

Use curl to dump headers of a web server  
`curl -I http://wordpress.com/`

I use LastPass, but if you want a password generator, `pwgen` is a nice utility  
`pwgen 32`

**Use pandoc to convert text files**  
In the past year or so I discovered the **pandoc** utility which can convert numerous text file formats, it works great. For example if you want to convert Markdown to HTML. I also use it often to convert Markdown to slides. It also supports PDF, ebooks and many other, see [pandoc site][13] for supported formats.

**Use htop instead of top**  
`htop` gives a better interface into top processes running and cpu usage, probably not installed by default but in most package repositories. Setup an alias and you won't have to remember to type it.  
`alias top=htop`

**Rsync for Copying Files**  
I have a pretty simple [personal site][14], so I use **rsync** as my deployment tool to copy the files up there. I use the following command  
`rsync -avzC -e ssh ./htdocs/ mkaz@mkaz.com:/sites/mkaz.com/htdocs`

I then drop this in a file called `publish.sh` which I run and it copies it out. Rsync is pretty powerful tool, it is also commonly used as backup tool. See these [rsync examples][15] for more.

**Format JSON string **  
`<br />
echo '{"long": "yes", "complex": "yes", "format": { "none": true} }' | python -m json.tool<br />
`

## Send Email from Command-line

Something I don't use often enough is sending e-mail from the command-line, I think because I never know if an environment is configured to send mail. It's always a bit tricky, but for my main debian setup, I configured `msmtp` to use Gmail by following this [msmtp guide][16]. Another alternate mail agent is [ssmtp][17] which can also use Gmail as a transport.

Once mail is configured you can use `mail` or `mailx` command to send email, depending on your system, both work the same. The commands take the body of the message as STDIN (piped in), which makes it real easy to send results of a command via email:  
`command  | mail -s "subject" user@domain.com`

You can send the contents of a file as the body message using  
`mail -s "subject" user@domain.com < file.txt`

Or if you want to send a file as an attachment  
`echo "Attached" | mail -s "subject" -a file.txt user@domain.com`

## Combine it all together

The real power in unix and the command-line is the ability to tie everything together. So you can create a script, which performs a task, schedule it using cron and have it email you the results, though cron emails results by default, just to illustrate the point.

An example of a quote sent via text each day, create text file with quotes in it, one per line.  
`shuf -n 1 quotes.txt | mail -s "quote" 4155551212@vtext.com`

The above line will do the random quote and sending, so all that is needed is to schedule in cron, by adding the following line in your crontab

`0 9 * * * shuf -n 1 quotes.txt | mail -s "quote" 4155551212@vtext.com`

## Summary

Hopefully this guide helped save you some time and make you a bit more productive on the command-line. Remember to be observant of what you do repetitively or frequently and automate them away the unix way. You can look at your `history` to see what commands you are running the most.

You can use this to see a list of your top commands from your history file  
`history | awk '{ print $2 }' | sort | uniq -c | sort -rn | head`

You might be interested in my [Ubuntu Guide for Mac Converts][18], which includes a few tips for Mac users moving to Linux. I've switched to Debian but the same tips all apply for both environments.

 [1]: https://github.com/rupa/z
 [2]: http://www.derekwyatt.org/vim/vim-tutorial-videos/
 [3]: http://vimcasts.org/
 [4]: https://mkaz.com/2011/08/31/vim-cheat-sheet/
 [5]: http://beyondgrep.com/
 [6]: http://quickleft.com/blog/command-line-tutorials-sed-awk
 [7]: http://www.theunixschool.com/p/awk-sed.html
 [8]: http://www.gregreda.com/2013/07/15/unix-commands-for-data-science/
 [9]: http://www.tldp.org/LDP/Bash-Beginners-Guide/html/Bash-Beginners-Guide.html
 [10]: http://ebeab.com/2006/05/29/unix-crontab/
 [11]: http://nerderati.com/2011/03/simplify-your-life-with-an-ssh-config-file/
 [12]: http://mah.everybody.org/docs/ssh
 [13]: http://johnmacfarlane.net/pandoc/
 [14]: https://mkaz.com
 [15]: http://www.thegeekstuff.com/2010/09/rsync-command-examples/
 [16]: https://wiki.archlinux.org/index.php/msmtp
 [17]: https://wiki.debian.org/sSMTP
 [18]: https://mkaz.com/2013/01/13/ubuntu-guide-for-mac-converts/