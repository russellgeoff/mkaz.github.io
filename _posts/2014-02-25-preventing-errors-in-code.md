---
title: Preventing Errors in Code
author: Marcus Kazmierczak
layout: post
categories:
  - technology
---

This week looking at preventing errors when coding:

<h3>An ounce of prevention</h3>

If you don't read anything else, read <a href="http://www.joelonsoftware.com/articles/fog0000000043.html">the Joel Test</a> to make sure your development practices follow the basics. If you can't pass the test there's your todo list, Joel Spolsky wrote it over a dozen years ago and still just as valid today.

Pete Warden writes an observant counter to argument against open-offices, <a href="http://petewarden.com/2014/02/24/writing-code-is-not-most-programmers-primary-task/">Writing code is not most programmers primary task</a> which is worth a read. I include it as a reminder, many errors occur by not asking questions and understanding the goal of what you're doing. <em>No number of unit tests will fix misunderstood problems.</em>

Be consistent, use a checklist. If you find yourself repeating a complex process look at creating a checklist to help your memory. <a href="http://www.amazon.com/The-Checklist-Manifesto-Things-Right/dp/0312430000">Pilots and doctors are doing it</a> why not your iPhone app deployment.   I saw Matthew Eppelsheimer give a good <a href="http://wordpress.tv/2013/08/22/matthew-eppelsheimer-checklists-a-path-to-mistake-free-development-and-publishing/">flash talk on using checklists</a> at WordCamp Portland.

<h3>Accidents Happen</h3>

Why? Why? Why? Why? Why? The five why methodology is used to discover the root cause analysis and not just fix the current problem, but prevent it from ever happening again. Eric Ries wrote a good article about <a href="http://blogs.hbr.org/2010/04/the-five-whys-for-startups/">Five Whys for Start-Ups</a> or if you prefer a bit older look at the methodology:

<blockquote>
For want of a nail a shoe was lost, <br>
for want of a shoe a horse was lost, <br>
for want of a horse a rider was lost, <br>
for want of a rider an army was lost, <br>
for want of an army a battle was lost, <br>
for want of a battle the war was lost, <br>
for want of the war the kingdom was lost, <br>
and all for the want of a little horseshoe nail. <br>
</blockquote>

<h3>In case of emergency</h3>

Accidents do happen and downtimes occur, don't hide but be up front and honest with your users. Communicate the results, <a href="http://www.google.com/appsstatus">Google</a> and <a href="http://status.aws.amazon.com/">Amazon</a> have dashboards for their service outages why should you be embarassed. Create your own check out open source project <a href="http://www.system-status-dashboard.com/">System Status Dashboard</a> or maybe <a href="https://www.statusdashboard.com/">the hosted SaaS solution</a> if your site is down, your alert system might be too.

<h2>Bits &amp; Bytes</h2>

<ul>
<li><p>Selenium is the best functional testing framework for web applications. You can see my <a href="https://mkaz.com/2012/03/07/use-python-selenium-to-automate-web-timing/">selenium example using python</a> but better yet read up on <a href="https://saucelabs.com/">Sauce Labs</a> hosted selenium testing, lots of <a href="https://saucelabs.com/docs/code-examples">examples and code samples</a>.</p></li>
<li><p>Tarek Ziade has a tool aptly named <a href="https://github.com/tarekziade/boom">Boom!</a> which is a command-line tool to generate load against a website, intended as a replacement for Apache Benchmark.</p></li>
<li><p>If using a local server to generate load is a bit pedestrian, you can always turn to the cloud, with a service like <a href="http://loadstorm.com/">LoadStorm</a> you can summon a 50,000 user Typhoon (name of the service level) and descend it against your website. <a href="https://www.blitz.io/">Blitz</a> is another popular load testing cloud service.</p></li>
</ul>

