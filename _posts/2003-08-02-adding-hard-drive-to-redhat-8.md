---
id: 455
title: Adding hard drive to RedHat 8
author: Marcus Kazmierczak
layout: post
guid: http://ebeab.com/?p=455
permalink: /2003/08/02/adding-hard-drive-to-redhat-8/
categories:
  - classics
---
It appears an older Linux box of mine crapped out. I'm still not sure the exact diagnosis but it shut itself off and didn't want to turn back on. My punishment for the box was to strip it of it's hard drive and memory and put these parts in my newer Dell box running Redhat 8.0.

This was the first new hardware I've added to the Dell box and only the second time I've opened the case. The first was just to peek under the hood and probably void all the warranties.

Adding the hard drive was a cinch. I was quite impressed with the layout and rail system they have built-in. They included the extra plastic rails in the case and even with the screws to attach to the hard drive and it then just slides right in. Pretty easy.

Now you know I wouldn't be writing if everything went perfectly. After setting the jumpers properly and getting BIOS to detect the new drive with out a problem, booting into Linux fails. Now what should be the easiest part, boot into Linux and simply mount the old partitions, but it fails on boot. For some reason it decides to mount all the old partitions as read-only and freezes when starting up the system logger because it can't write to /var.

Fortunately, I've been playing with [Knoppix][1] and [LNX-BBC][2] which are two Linux distros, self-contained and bootable off a cd-rom. So I pop one in and it boots up so I can snoop around the drives and see what's up. Both drives and all partitions are there and look fine.

After several reboots trying to read the error messages, which aren't logged anywhere and after looking at numerous configs and lots of googling. I decide that the weird LABEL stuff in the /etc/fstab should be removed. So I run the box off just the original drive and edit it's /etc/fstab. I change the `LABEL=/` to the actual drive mapping `/dev/hda1`. Re-hooked up both drives, rebooted and everything worked great.

Now my Dell box has a gig of ram and 120gb drive space. sweet!

 [1]: http://www.knopper.net/knoppix/
 [2]: http://www.lnx-bbc.org/
