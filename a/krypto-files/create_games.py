#!/usr/local/bin/python

# Marcus Kazmierczak, marcus@mkaz.com
# March 11, 2002
# http://mkaz.com/math/krypto/

# Generate all possible krypto games
# and writes them out to a test file

# There's a total of 2,968,875 possible games
# You end up with a 45mb text file
# Which took 2 minutes on my G4 500mhz Powerbook


max = 25
i = 0

for n1 in range(1,max+1):
    for n2 in range(n1,max+1):
        for n3 in range(n2,max+1):
            for n4 in range(n3,max+1):
                for n5 in range(n4,max+1):
                    for s1 in range(1,max+1):
                        i += 1
                        print ("%d %d %d %d %d %d") % (n1, n2, n3, n4, n5, s1)

print "Total Games: ", i

