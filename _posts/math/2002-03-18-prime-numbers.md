---
title: Prime Numbers
author: Marcus Kazmierczak
layout: post
categories:
  - math
---

<blockquote>
An integer is <b>prime</b> if its only positive divisors are itself and one. 
</blockquote>

Prime numbers have always been a keen interest to mathematicians for various reasons. One being there appears to be no rhyme or reason to the distribution of primes and there is no limit to finding new primes. The largest known prime was found in November 2001 and it is over 4 million digits long!  

### Finding Primes

Computers have made finding these large prime numbers possible. The faster computers can crunch numbers, the larger the primes will be found. Here's an interesting graph showing <a href="http://www.utm.edu/research/primes/notes/by_year.html#graph1">the largest known primes by year.</a>
 

##### Simple Method of Finding Primes

A prime number is one that has <b>no</b> prime factors. So a simple way of checking if a number is prime is by trying all known primes less than it and seeing if it divides evenly into that number.

<b>Example:</b> Finding the first couple of primes 

Starting off with the number 2, it is prime because the only divisors are itself and 1, meaning the only way to multiple two numbers to get 2 is 2 x 1. Likewise for 3.

So that starts us off with two known primes 2 and 3. To check the next number we can check if 4 modulo 2 equals 0. This means when divide 2 into 4 there is no remainder, which means 2 is a factor of 4. Specifically we know 2 x 2 = 4.  Thus 4 is not prime, since it has a prime factor.

Moving on to the next number: 5.  To check if 5 is prime, try (5 modulo 2) and (5 modulo 3), both of which equals 1. So 5 is prime, since all primes less than it are not factors of 5. So add 5 to our list of known primes and then continue on checking the next number. This rather tedious process for people is great for a computer.

## Speeding up our Search

This method can be a little slow when the number of primes gets large since you have to check every previous prime number. One way to speed this up is to stop checking when the prime squared is greater than the number.

For example if we are checking if 47 is prime, we can stop our check at 7, since 7 squared (49) is greater. If there were a larger factor that went into 47, it would have to be multiplied by a smaller prime number to give us 47, and we would have already found the smaller number earlier in our checks.

This method is called <b>the Sieve of Eratosthenes</b> (ca 240 BC), which is stated as:

<blockquote>
    Make a list of all the integers less than or equal to n (and greater than one). Strike out the multiples of all primes less than or equal to the square root of n, then the numbers that are left are the primes
</blockquote>



### My Python Script Implementing Sieve of Eratosthenes

The following python program will print out the primes from 2 to 1,000,000.  On my Mac OS X PowerPC G4 500mhz it took approximately 4 minutes when printing to screen, and only 1 minute when output directed to a file.

If you don't have python, consider it pseudo-code to review for learning purposes.

Download Python Script: <a href="/a/math/findthem.py">findthem.py</a>


### C Source Code

After working on my <a href="/krypto-game-analysis/">Krypto problem</a> I found that Python is really slow when compared to C. So I came back and wrote up a simple C version of this script. 

Download C Program: <a href="/a/math/findthem.c">findthem.c</a> - in just 12 minutes, I was able to generate the 5,761,453 primes below 100 million, which is a 54mb text file!

