---
id: 465
title: Use Python + Selenium to Automate Web Timing
author: Marcus Kazmierczak
layout: post
guid: http://ebeab.com/?p=465
permalink: /2012/03/07/use-python-selenium-to-automate-web-timing/
categories:
  - python
tags:
  - selenium
---
I've been hearing a lot recently about the Navigation Timing spec, which sets a multitude of timing events as javascript properties. There are numerous events in the flow, from the very first navigation event, which could be when the user clicks a search result in Google, to DNS timing to Dom parsing etc. [See the full Navigation Timing spec for details.][1]

### Automate

I wanted a way to be able to automate the capturing of these timings, what better way than to use Selenium. Selenium can execute javascript and return the results to your script, so it is relatively straight-forward.

Here's a basic script which will fetch the page and calculate two timings. The back-end performance which is from when the user starts the navigation to when the first response starts. The second timing, you could probably guess, is front-end performance, which is from when the user starts receiving the first response until the DOM is complete.

<pre class="brush: python; title: ; notranslate" title="">"""
Use Selenium to Measure Web Timing
Performance Timing Events flow
navigationStart -&gt; redirectStart -&gt; redirectEnd -&gt; fetchStart -&gt; domainLookupStart -&gt; domainLookupEnd
-&gt; connectStart -&gt; connectEnd -&gt; requestStart -&gt; responseStart -&gt; responseEnd
-&gt; domLoading -&gt; domInteractive -&gt; domContentLoaded -&gt; domComplete -&gt; loadEventStart -&gt; loadEventEnd
"""

from selenium import webdriver

source = "http://www.babycenter.com/"
driver = webdriver.Chrome()
driver.get(source)

navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
responseStart = driver.execute_script("return window.performance.timing.responseStart")
domComplete = driver.execute_script("return window.performance.timing.domComplete")

backendPerformance = responseStart - navigationStart
frontendPerformance = domComplete - responseStart

print "Back End: %s" % backendPerformance
print "Front End: %s" % frontendPerformance

driver.quit()
</pre>

You will have to install the Selenium drivers, which if you use **pip** should be a straight-forward  
`$ pip install selenium`

This is a basic Python example, the same `execute_script` command is available in your language of choice.

 [1]: https://dvcs.w3.org/hg/webperf/raw-file/tip/specs/NavigationTiming/Overview.html
