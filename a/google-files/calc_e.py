#!/usr/bin/python

# Calculate digits of e
# Marcus Kazmierczak, marcus@mkaz.com
# July 29th, 2004

# the formula
#  e = 1/0! + 1/1! + 1/2! + 1/3! + 1/4! + ... 1/N!

# You should chop off the last five digits returned
# they aren't necessarily accurate



# precision library 
import gmpy

# how many digits (roughly)
N = 1000


gmpy.set_minprec(int(N*3.5+16))
e = gmpy.mpf('1.0')
    
for n in range(1,N+3):
    e = gmpy.fdigits(gmpy.mpf(e) + (gmpy.mpf('1.0') / gmpy.fac(n)))

print e
