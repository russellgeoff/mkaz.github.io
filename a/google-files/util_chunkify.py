#!/usr/bin/python

# loop through file break up into 10 char chunks
# remove units which are not prime, even or end in 5

# Marcus Kazmierczak, marcus@mkaz.com
# July 29th, 2004

import string, os

# file 2,399 digits of e
efile = "e.0"
chsize = 10
notp = ["0", "2", "4", "5", "6", "8",]

f=open(efile, 'r')
e = f.readline()
f.close

sp = 0
while (sp < len(e)-chsize ):
    num = e[sp:sp+chsize]
    if (num[chsize-1] not in notp ):
        print num
    sp = sp + 1
