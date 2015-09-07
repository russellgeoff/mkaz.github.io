#!/usr/bin/env python

import os, sys

max = 1000

# -----------------------------------------------
# find all primes up to and including the number 
# -----------------------------------------------
# seed the prime list
primes = [2, 3]

# the sieve 
for n in range(4, max+1):
    nap = 0
    for prime in primes:
        if (n % prime) == 0:
            nap = 1
            break
        if prime*prime > n:
            break
    if nap != 1:
        primes.append(n)


# -----------------------------------------------
# get prime factors
# -----------------------------------------------
def get_prime_factors(num):
    factors = []
    n = num
    if num in primes:
        return [num]

    while (1):
        for prime in primes:
            if (num % prime) == 0:
                factors.append(prime)
                num = num / prime                
                break
        if (num == 1):
            break

    return factors
    
# -----------------------------------------------
# sum list of numbers
# -----------------------------------------------
def sum_list(l):
    sum = 0
    for n in l:
        sum = sum + n
    return sum

# start the seed
a1 = get_prime_factors(2)

for c in range(3,max):
    a2 = get_prime_factors(c)
    
    if (sum_list(a1) == sum_list(a2)):
        a1.sort()
        a2.sort()    
        print ""
        print "Numbers: %d, %d" % (c,c+1)
        print "    Prime Factors %d: %s" % (c, a1)
        print "    Prime Factors %d: %s" % (c+1, a2)

    a1 = a2        
print ""


"""
Timing Scenarios:  

1st Rev: Initial Working Script

2nd Rev: Find Prime Factors in easier way; fix sieve

3rd Rev: use a seed, so we don't get_prime_factors twice
         since we are working on consecutive numbers we 
         know the previous prime factors

20,000
  -Script 1st Rev-
    Timing [1]: 1' 7"
    Timing [2]: 1' 5"
    
  -Script 2nd Rev-
    Timing [1]: 13s
    Timing [2]: 13s

50,000
  -Script 2nd Rev-
    Timing [1]: 5m 39s
    
  -Script 3rd Rev-
    Timing [1]: 50s
"""
