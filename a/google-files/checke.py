#!/usr/bin/python

# check chunk values of e if prime

# Marcus Kazmierczak, marcus@mkaz.com
# July 29th, 2004

import string, os

#--- SETTINGS
efile = "e.10digit.chunks";
pfile = "primes.sm";

# read values in from e file
# file 10 digit chunks of e
f=open(efile, 'r')
nums = f.readlines()
f.close

# read all primes in, used for checking
f = open(pfile, 'r')
primes = f.readlines()
f.close

for num in nums:
    num = int(num);
    #intialize not-a-prime as false
    nap = 0

    # cycle through list of known primes
    for prime in primes:
        prime = int(prime);
        # check if a previous prime divides evenly
        # into the current number -- if so the number
        # we are checking (num) is not a prime
        if (num % prime) == 0:
            nap = 1
            break
        # if prime squared is bigger than the number 
        # than we don't need to check any more
        if prime*prime > num:
           break

    # did we determine it's not a prime
    # if not, then we found a prime
    if nap != 1:
        print num
        #break
