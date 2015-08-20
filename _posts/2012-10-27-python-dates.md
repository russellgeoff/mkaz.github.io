---
id: 686
title: Python Dates
author: Marcus Kazmierczak
layout: post
guid: http://ebeab.com/?p=686
permalink: /2012/10/27/python-dates/
categories:
  - solutions log
tags:
  - dates
  - python
---
Python Dates  
10/27/2012 08:13:00PM

A set of examples using Python date and time functions, including formatting dates, date calculations and other bits in datetime package, similar to my [string format examples][1].

First off, all examples use the following import, any additional imports needed will be shown with the example.

<pre><code class="python">from datetime import datetime
</code></pre>

### Creating Date Objects

<pre><code class="python"># now
now = datetime.now()

# specific date
dt1 = datetime(2011, 8, 29)
dt2 = datetime(year=2012, month=3, day=2)

# create a date from a known format
str = "2012-10-20"
dts = datetime.strptime(str, '%Y-%m-%d')

# create a date from unix timestamp
ts = 1294204471
dtu = datetime.fromtimestamp(ts)
</code></pre>

### Date Formats

Printing dates in various formats is relatively straight forward, here's one example. Refer to the table below for available formatting symbols and samples.

<pre><code class="python">print dt1.strftime("%b %d, %Y")
&gt;&gt; Jan 15, 1999
</code></pre>

<table>
  <tr>
    <th>
      Symbol
    </th>
    
    <th>
      Definition
    </th>
    
    <th>
      Example
    </th>
  </tr>
  
  <tr>
    <td>
      %a
    </td>
    
    <td>
      Weekday name abbreviated
    </td>
    
    <td>
      Sun, Mon, Tue, &#8230;
    </td>
  </tr>
  
  <tr>
    <td>
      %A
    </td>
    
    <td>
      Weekday name full
    </td>
    
    <td>
      Sunday, Monday, Tuesday, &#8230;
    </td>
  </tr>
  
  <tr>
    <td>
      %b
    </td>
    
    <td>
      Month name abbreviated
    </td>
    
    <td>
      Jan, Feb, Mar, &#8230;
    </td>
  </tr>
  
  <tr>
    <td>
      %B
    </td>
    
    <td>
      Month name full
    </td>
    
    <td>
      January, February, &#8230;
    </td>
  </tr>
  
  <tr>
    <td>
      %c
    </td>
    
    <td>
      A &#8220;random&#8221; date and time representation.
    </td>
    
    <td>
      Fri Jan 15 16:34:00 1999
    </td>
  </tr>
  
  <tr>
    <td>
      %d
    </td>
    
    <td>
      Day of the month
    </td>
    
    <td>
      [ 01, 31 ]
    </td>
  </tr>
  
  <tr>
    <td>
      %f
    </td>
    
    <td>
      Microsecond
    </td>
    
    <td>
      [ 000000, 999999 ]
    </td>
  </tr>
  
  <tr>
    <td>
      %H
    </td>
    
    <td>
      Hour (24h)
    </td>
    
    <td>
      [ 00, 23 ]
    </td>
  </tr>
  
  <tr>
    <td>
      %I
    </td>
    
    <td>
      Hour (12h)
    </td>
    
    <td>
      [ 01, 12 ]
    </td>
  </tr>
  
  <tr>
    <td>
      %j
    </td>
    
    <td>
      Day of the year
    </td>
    
    <td>
      [ 001, 366 ]
    </td>
  </tr>
  
  <tr>
    <td>
      %m
    </td>
    
    <td>
      Month
    </td>
    
    <td>
      [ 01, 12 ]
    </td>
  </tr>
  
  <tr>
    <td>
      %M
    </td>
    
    <td>
      Minute
    </td>
    
    <td>
      [ 00, 59 ]
    </td>
  </tr>
  
  <tr>
    <td>
      %p
    </td>
    
    <td>
      Locale's equivalent of either AM or PM.
    </td>
    
    <td>
      [ AM, PM ]
    </td>
  </tr>
  
  <tr>
    <td>
      %S
    </td>
    
    <td>
      Second
    </td>
    
    <td>
      [ 00, 61 ]
    </td>
  </tr>
  
  <tr>
    <td>
      %U
    </td>
    
    <td>
      Week number of the year (Sunday first)
    </td>
    
    <td>
      [ 00, 53 ]
    </td>
  </tr>
  
  <tr>
    <td>
      %w
    </td>
    
    <td>
      Weekday number (Sunday=0)
    </td>
    
    <td>
      [ 0, 6 ]
    </td>
  </tr>
  
  <tr>
    <td>
      %W
    </td>
    
    <td>
      Week number of the year (Monday first)
    </td>
    
    <td>
      [0, 53 ]
    </td>
  </tr>
  
  <tr>
    <td>
      %x
    </td>
    
    <td>
      Locale date
    </td>
    
    <td>
      01/15/99
    </td>
  </tr>
  
  <tr>
    <td>
      %X
    </td>
    
    <td>
      Locale time
    </td>
    
    <td>
      16:34:00
    </td>
  </tr>
  
  <tr>
    <td>
      %y
    </td>
    
    <td>
      Year without century
    </td>
    
    <td>
      [ 00, 99 ]
    </td>
  </tr>
  
  <tr>
    <td>
      %Y
    </td>
    
    <td>
      Year with century
    </td>
    
    <td>
      1999
    </td>
  </tr>
  
  <tr>
    <td>
      %z
    </td>
    
    <td>
      UTC offset in the form +HHMM or -HHMM or empty string
    </td>
    
    <td>
    </td>
  </tr>
  
  <tr>
    <td>
      %Z
    </td>
    
    <td>
      Time zone name or empty string
    </td>
    
    <td>
      &nbsp;
    </td>
  </tr>
  
  <tr>
    <td>
      %%
    </td>
    
    <td>
      A literal &#8216;%' character.
    </td>
    
    <td>
      &nbsp;
    </td>
  </tr>
</table>

### Date Calculations and Timedelta

<pre><code class="python">from datetime import timedelta

week_later = dt + timedelta(days=7)
last_week = dt - timedelta(days=7)
in_five_minutes = dt + timedelta(minutes=5)
</code></pre>

Valid timedelta properties are:  
` weeks, days, hours, minutes, seconds, microseconds, milliseconds `

You might notice that a &#8220;year&#8221; timedelta is absent, don't b tempted to do days=365, this would be off for leap-years. I would recommend something like the following:

<pre><code class="python">st = datetime(year=2011, month=3, day=17)
next_year = datetime(year=st.year+1, month=st.month, day=st.day)
</code></pre>

### Adding and Subtracting Dates

You can add and subtract date objects when doing so they return timedelta objects. Using the timedelta object, you can access the same properties above.

<pre><code class="python">dt1 = datetime(year=2012, month=8, day=23)
dt2 = datetime(year=2012, month=8, day=28)
td = dt2 - dt1
td.days
&gt;&gt; 5
</code></pre>

### Common Date Functions

Here are a few date functions which are commonly needed, I made the examples a little more explicit so it is easier to follow the calculation, you may want to shorten up some when used.

#### Last Day of the Month 

Two solutions, first using datetime and going to the first day of next month and subtracting a day.

<pre><code class="python">from datetime import timedelta
now = datetime.now()
next_month = datetime(year=now.year, month=now.month+1, day=1)
last_day_month = next_month - timedelta(days=1)
</code></pre>

Second solution to determine the last day of the month using the calendar object

<pre><code class="python">import calendar
now = datetime.now()
range = calendar.monthrange(now.year, now.month)
last_day_month = now.replace(day=range[1])
</code></pre>

#### Next Thursday 

<pre><code class="python">today = datetime.now()
thursday_dow = 4
today_dow = first_day_of_month.strftime("%w")
adjustment = ( 7 + thursday_dow - int(today_dow)) % 7
next_thursday = today + timedelta(days=adjustment)
</code></pre>

#### First Monday of the Month 

<pre><code class="python">today = datetime.now()
first_day_of_month = today.replace(day=1)
day_of_week = first_day_of_month.strftime("%w")
adjustment = (8 - int(day_of_week) ) % 7
first_monday = first_day_of_month + timedelta(days=adjustment)
</code></pre>

## Reference

  * [Python Docs &#8211; Datetime][2]
  * [strftime.org][3] &#8211; clean date format reference</a>

 [1]: https://mkaz.com/solog/python/python-string-format.html
 [2]: http://docs.python.org/2/library/datetime.html
 [3]: http://strftime.org/