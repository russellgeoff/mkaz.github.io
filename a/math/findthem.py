#!/usr/local/bin/python
import os, string

max = 1000000
filename = "primes.txt"
primes = []

# check if primes.txt exists
if os.path.isfile(filename):
    using_file = 1
    
    # read in all previous primes
    # convert to numbers
    f = open(filename,'r')
    snums = f.readlines()
    f.close()
    
    for sn in snums:
        n = string.atoi(sn)
        primes.append(n)
    
    start = primes[len(primes)-1]+1

else:
    # seed list with first two primes
    using_file = 0
    primes = [2,3]
    start = 4
    
# print out intial 
if using_file:
    pass
else:
    for p in primes:
        print "",p

# range of numbers searching for primes
for num in range(start, max):
    #intialize not-a-prime as false
    nap = 0

    # cycle through list of known primes
    for prime in primes:    
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
        # add prime to list of known primes
        primes.append(num)
        print "",num




