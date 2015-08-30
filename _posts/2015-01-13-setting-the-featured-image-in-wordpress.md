---
id: 5884
title: Set the Featured Image in WordPress
author: Marcus Kazmierczak
layout: post
permalink: /2015/01/13/setting-the-featured-image-in-wordpress/
categories:
  - solutions log
tags:
  - featured image
  - rest api
  - wordpress
  - wp-cli
---
I started my photo blog in 2005 and over the past 10 years run it on several different platforms, hosts and software. I started with a bunch of scripts I created myself, bounced around from self-hosted WordPress to Tumblr, back to self-hosted WordPress, back to custom scripts to WordPress.com and now once again back to self-hosted WordPress.

Amazingly, I've kept all the photos throughout the time, a total of 657 posts, but they have developed some cruft; different formatting, image location and how they were uploaded.

The latest theme I've developed for my site relies on featured images on [my new swank home page][1]. However, only a small handful of photos that I posted had featured images set.

So here are the scripts and how I set the rest of the 600+ images to have a featured image.

## WordPress Image Attachement

The easiest batch to fix were the ones which were uploaded as a WordPress attachment. So the photo was already in the WP system, it just needed to be assigned as the feature image.

See the linked script below for the process basically it finds all the posts without featured images and compares that image to images already uploaded and sets when matched. I ran on the server using the awesome [WP command-line tool][2].

Script on Github: [set-featured-image.php][3]

## External Image to WordPress

The bit tricker part involved posts which referred to images that live simply on the server's file system and not within WordPress. The way WP handles featured images is by setting the `attachment_id` of the image which is featured. This requires it to be a proper attachment within WP.

So after a bit of noodling, I handled it in two parts. One was to extract all the posts which did not have a thumbnail and the first image within those posts. The second script used this list to upload the image to WordPress and then associate the attachment id to the proper post id.

I modified the script above to grab all posts that don't have a featured image already set and to output the post id and the first image in the post. See [get-posts-no-imgs.php][4]

I couldn't quite figure out how to do the upload using wp cli, so I wrote a quick python script that I ran locally that uses the [WordPress.com REST API][5] and uploads the file. This requires running [Jetpack][6] on your site and having the JSON API module enabled.

Also the annoying step is you need an auth token which you can obtain from [rest-access.test.apokalyptik][7] which was created by a co-worker and a long time employee at Automattic. We still need to develop an oauth way for command line access.

Script to upload and set: [wpcom-set-featured-image.py][8]

Hope it gives you a couple of starting points if you were trying to get the same thing done setting featured images. Or maybe just a couple of tips on using wp-cli or the REST API.

 [1]: https://mkaz.com
 [2]: http://wp-cli.org/
 [3]: https://gist.github.com/mkaz/89aa966c240c8b33d8f2
 [4]: https://gist.github.com/mkaz/33e41f0acb77ee1adcf5
 [5]: https://developer.wordpress.com/docs/api/
 [6]: https://jetpack.me
 [7]: https://rest-access.test.apokalyptik.com/
 [8]: https://gist.github.com/mkaz/53e19322e0313bf3878c
