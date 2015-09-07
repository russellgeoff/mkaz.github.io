---
title: Prime Factors
author: Marcus Kazmierczak
layout: post
categories:
  - math
---

In number theory, the <b>prime factors</b> of a positive integer are the prime numbers that divide into that integer exactly, without leaving a remainder.

A few examples make it clear:

<pre>
  The prime factors of 6 are (2, 3); since 2 x 3 = 6 
  The prime factors of 12 are (2, 2, 3); since 2 x 2 x 3 = 12 
  The prime factors of 100 are (2, 2, 5, 5); since 2 x 2 x 5 x 5 = 100 
</pre>


This is all just an introduction, to this article a friend sent me; about math, numbers and even a little baseball. (link rot)  The article discusses a class of numbers called Ruth-Aaron pairs, which are consecutive numbers where the sum of their prime factors are equal.  The first few Ruth-Aaron pairs are:

<table>
<tr><th>Pair</th><th>Prime Factors / Sums </th></tr>
<tr><td>5, 6    </td><td> 5 = 2 + 3 </td></tr>
<tr><td>8, 9 	</td><td> 2 + 2 + 2 = 3 + 3 = 6 </td></tr>
<tr><td>15, 16 	</td><td> 3 + 5 = 2 + 2 + 2 + 2 = 8 </td></tr>
<tr><td>77, 78 	</td><td> 7 + 11 = 2 + 3 + 13 = 18 </td></tr>
<tr><td>125, 126 </td><td> 5 + 5 + 5 = 2 + 3 + 3 + 7 = 15 </td></tr>
<tr><td>714, 715 </td><td> 2 + 3 + 7 + 17 = 5 + 11 + 13 = 29 </td></tr>
</table>

The name of the pairs come from the number 714, being the total number of home runs hit by Babe Ruth and 715 the number Aaron hit to surpass him; hence Ruth-Aaron Pair

So I had to write my little script to find more of these. Finding prime factors is fairly straightforward.  For the number you are factoring, go through the list of primes and check if each one divides it. In programming that means (num % prime == 0)

If the prime divides the number, it is a prime factor. Then divide the number by this prime factor and start over, checking the remainder for prime factors. Continue until the remainder is equal to 1. This is sometimes called <i>reverse division</i>. It looks something like this, for finding the prime factors of <b>60</b>

<pre>
2 | 60
 ----
 2 | 30
   ----
   3 | 15
     ----
      5 | 5
        ---
          1
</pre>

Prime Factors: 2 x 2 x 3 x 5

	  
Here's my python script to find Ruth-Aaron Pairs: <a href="/a/math/ruth-aaron.py">ruth-aaron.py</a>

It took my G5 2.0ghz PowerMac 5 hrs 3 minutes to find the 149 pairs up to 1,000,000. [<a href="/a/math/ruth-aaron.txt">ruth-aaron.txt</a>]

I leave it as an exercise to re-write in C to get some real performance.



## Related Links

* <a href="http://en.wikipedia.org/wiki/Ruth%E2%80%93Aaron_pair">Ruth-Aaron Pairs</a> on Wikipedia

* My <a href="/prime-numbers/">Prime Numbers</a> page with a few scripts on finding primes using the Sieve of Eratosthenes.  The same method I use in this script to find the listing of primes.

