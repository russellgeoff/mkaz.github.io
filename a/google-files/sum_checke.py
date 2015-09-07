#!/usr/bin/python

# take e, break up into 10 digit chunks
# sum the digits of the chunks and check
# if they total 49

# Marcus Kazmierczak, marcus@mkaz.com
# July 29th, 2004

import string, os

# 2,399 digits of e
efile = "e.0";

# read file
f=open(efile, 'r')
e = f.readline()
f.close

sp = 0
mc = 0
while (sp < 2388 ):
    num = e[sp:sp+10]
    sum = 0

    for i in range(0,10):
        sum = sum + int(num[i])

    if (sum == 49):
        print "Match: %s" % num
        mc = mc + 1
        if (mc > 10):
            break
    
    sp = sp + 1
