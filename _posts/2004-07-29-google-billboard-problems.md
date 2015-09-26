---
id: 3468
title: Google Billboard Problems
author: Marcus Kazmierczak
layout: post
permalink: /2004/07/29/google-billboard-problems/
categories:
  - math
---
A mysterious billboard appeared on 101-southbound which I passed each day to work. The billboard said:

> { the first 10-digit prime in consecutive digits of *e* }.com 

I passed by the billboard numerous times before I realized it wasn't an advertisement for a company, it wasn't touting some servers new ability, it was actually a question. A problem to be solved. As I've [shown before][1] I'm always up for a good problem, I got right on it.

## Problem #1

My first intrepretation of the problem was to find the first 10-digit prime, the first being 1,000,000,007 and the next being 1,000,000,009 and seeing if they are in *e*. So I've already created a [few primes scripts before][2] but not up to 10-digits, so I modified it a touch and started that cranking out some big primes.

Now as I started to think about it more I realized that this intrepretation doesn't make sense, since it is wholly dependent on the length of *e* that you are using to check. It's possible you can extend *e* long enough to have any 10-digit prime show up.

Well, I had left my big prime number generator cranking and it turned out 105 million prime numbers, up to 2.1 billion. This file of consecutive primes ended up being 1 gig! This took about 4-hours on an Opteron 64-bit 2ghz box. Thankfully I wouldn't need it.

So on to the second, and real interpretation, of the question, take 10-digit chunks of *e*, starting at the beginning and check if those are prime. This turns out to be a much easier problem.

Now, the largest number it could be is 9,999,999,999, so the largest prime we need to check is the square root of that, which is roughly 100,000. Now the list of primes up to 100,000 is quick and easy to generate. [[again previous scripts][2]]

So grabbing the first ~2,500 digits of *e*, from [this site][3] [nasa.gov], I was guessing 2,500 would be enough. I could always go back for more. Moving them onto one line for ease of use I ended up with this file [[e.0][4]]

I wrote this script [[util_chunkify.py][5]] to chunkify it into 10-digit pieces that are possibly primes, stripping out digits that end with an even number or 5. This left me with the following file [[e.10digit.chunks][6]]

So I then wrote a script which reads in the primes from this file [[primes.sm][7]] and puts them in an array. This is what is used to check if our 10-digit e-chunks are prime, using this script [[checke.py][8]]

Here are the first ten, the first one of course is the correct answer:

  1. ** 7427466391 **
  2. 7413596629 
  3. 6059563073 
  4. 3490763233 
  5. 2988075319 
  6. 1573834187 
  7. 7021540891 
  8. 5408914993 
  9. 6480016847 
 10. 9920695517 

So going to: <http://www.7427466391.com/> brings up a second problem.

* * *

## Problem #2

Here's the second problem:

    
    f(1) =  7182818284 
    f(2) =  8182845904 
    f(3) =  8747135266 
    f(4) =  7427466391 
    f(5) =  ??? 
    

**First Idea**  
The first thought was to solve it using a 3rd degree polynomial which will give us an equation which will fit the four points and we can plug in the 5th value, **5**, and get the answer. After struggling with Excel, which could graph and forecast the polynomial and even give us an equation it would not give us the forecasted value. dumb. Abandoning Excel, since it's equation wasn't even all that accurate.

Using: `a * x^3 + b * x^2 + c * x + d = y `

Gives us the following 4-equations and 4-unknowns:

> <table>
>   <tr>
>     <td>
>       1a +
>     </td>
>     
>     <td>
>       1b +
>     </td>
>     
>     <td>
>       1c +
>     </td>
>     
>     <td>
>       d =
>     </td>
>     
>     <td>
>       7182818284
>     </td>
>   </tr>
>   
>   <tr>
>     <td>
>       8a +
>     </td>
>     
>     <td>
>       4b +
>     </td>
>     
>     <td>
>       2c +
>     </td>
>     
>     <td>
>       d =
>     </td>
>     
>     <td>
>       8182845904
>     </td>
>   </tr>
>   
>   <tr>
>     <td>
>       27a +
>     </td>
>     
>     <td>
>       9b +
>     </td>
>     
>     <td>
>       3c +
>     </td>
>     
>     <td>
>       d =
>     </td>
>     
>     <td>
>       8747135266
>     </td>
>   </tr>
>   
>   <tr>
>     <td>
>       64a +
>     </td>
>     
>     <td>
>       16b +
>     </td>
>     
>     <td>
>       4c +
>     </td>
>     
>     <td>
>       d =
>     </td>
>     
>     <td>
>       7427466391
>     </td>
>   </tr>
> </table>

This solves to:

> <table>
>   <tr>
>     <td>
>       a =
>     </td>
>     
>     <td>
>       -241369996.5
>     </td>
>   </tr>
>   
>   <tr>
>     <td>
>       b =
>     </td>
>     
>     <td>
>       1230350850
>     </td>
>   </tr>
>   
>   <tr>
>     <td>
>       c =
>     </td>
>     
>     <td>
>       -1001434954.5
>     </td>
>   </tr>
>   
>   <tr>
>     <td>
>       d =
>     </td>
>     
>     <td>
>       7195272385
>     </td>
>   </tr>
> </table>

Plugging into the above for f(5) = **2775619365**

Testing this does not work, but since this section was labeled, First Idea, you should of seen that it would've been wrong.

**Second Idea**

After giving up the the polynomial fit and looking at the numbers a little more the first number looked very much like the beginning of *e*. It turns out to be the first segment of *e* and the other numbers also are all segments of *e*. They looked like this:

<pre>2718281828459045235360287471352662497757247093699959574966967627724076630353547594571382178525166427427466391
7182818284
8182845904
               8747135266
                                                                                           7427466391
</pre>

The first number mapped to the 2 spot of e, the 2nd number to the 6th spot, the 3rd number to the 24th spot and the 4th number to the 100th spot. This gave me the new functions:  
k

    
      f(1) = 2 
      f(2) = 6         
      f(3) = 24 
      f(4) = 100 
    

Numerous attempts were made to try to figure out a patern here, which turns out to be very close to a factorial series, `f(x) = (x+1)! ` but not quite, the 100 would need to be 120. After awhile looking at this it was abandoned and back to the original numbers.

    
      f(1) =    7182818284 
      f(2) =    8182845904 
      f(3) =    8747135266 
      f(4) =    7427466391 
      f(5) =    ??? 
    

Trying out various things on them, the following turned up which seemed a little too coincendental to be a coincendence:

                                    
          7+1+8+2+8+1+8+2+8+4 = 49 
          8+1+8+2+8+4+5+9+0+4 = 49 
          8+7+4+7+1+3+5+2+6+6 = 49 
          7+4+2+7+4+6+6+3+9+1 = 49 
    

So a quick script [[sum_checke.py][9]] to check if these are the first 4 values of 10-digit chunks of *e* that sum to 49, which they turned out to be. The script turned up:

1. 7182818284 
1. 8182845904 
1. 8747135266 
1. 7427466391 
1. **5966290435** 
1. 2952605956 
1. 0753907774 
1. 0777449920 
1. 3069697720 
1. 1252389784 

The 5th one being the correct answer.

Following the directions, it turned out to be a recruitment tool for Google Labs, looking for the best and brightest. It was pretty fun and good idea for them. Unfortunately, their search engine is too good and anyone can look up answers to them, so I'm not sure how valid of a test it is. I did send them the link to my resume, encoded of course.

## Calculating *e*

I felt like it was cheating downloading some one else's calculated digits of *e*. So using the formula:


e = 1/0! + 1/1! + 1/2! + 1/3! + 1/4! + ... 1/N!


I wrote the following script, [calc_e.py][10] to calculate the digits of *e*, the script uses the GMP libraries for precision.

## Related Links

* Initial Introduction: [Google Blog][11]

* Dr. Math's About *e*</p> </li> 

* [GMP: GNU Multiple Precision Arithmetic Library][12] : the fastest bignum library on the planet!

* [General Multiprecision PYthon project (GMPY)][13]</ul>

 [1]: /krypto-analysis/
 [2]: /prime-numbers/
 [3]: http://antwrp.gsfc.nasa.gov/htmltest/gifcity/e.2mil
 [4]: /a/google-files/e.0
 [5]: /a/google-files/util_chunkify.py
 [6]: /a/google-files/e.10digit.chunks
 [7]: /a/google-files/primes.sm
 [8]: /a/google-files/checke.py
 [9]: /a/google-files/sum_checke.py
 [10]: /a/google-files/calc_e.py
 [11]: http://www.google.com/googleblog/2004/07/warning-we-brake-for-number-theory.html
 [12]: http://www.swox.com/gmp/
 [13]: http://gmpy.sourceforge.net/
