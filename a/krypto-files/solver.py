#!/usr/local/bin/python

# Marcus Kazmierczak, marcus@mkaz.com
# http://mkaz.com/math/krypto/
# Feb 24, 2002

#-----------------------------------------------------------------------------
# Krypto Solver
# $Revision: 1.13 $
# $Date: 2002/03/16 18:52:19 $
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
from mkryptolib import *
from whrandom import randint

import sys, array, time
start_clock = time.clock()

print "\nKrypto Solver "
print "by Marcus Kazmierczak, marcus@mkaz.com\n"


# max number in range
max = 25

# operations
ops = ['+','-','*','/']

x = array.array('f')

#-----------------------------------------------------------------------------
# Read in Command Line Stuff
#-----------------------------------------------------------------------------

# check for verbose flag
if ('-v' in sys.argv): verbose = 1
else: verbose = 0

# flag to stop when solved
if ('-s' in sys.argv): stop_solved = 1
else: stop_solved = 0

if len(sys.argv) >= 7:
    x.append(float(sys.argv[1]))
    x.append(float(sys.argv[2]))
    x.append(float(sys.argv[3]))
    x.append(float(sys.argv[4]))
    x.append(float(sys.argv[5]))
    solv = float(sys.argv[6])

elif ('-r' in sys.argv):
    
    # Pick Random Cards cards
    for i in range(0, 5):
        x.append(float(randint(1,max)))

    # Pick Solution Card
    solv = float(randint(1,max))
    
else:
    print "Random Krypto: solver.py -r <options>"
    print "Solve Specific Krypto: solver.py x1 x2 x3 x4 x5 s <options>"
    print "OPTIONS: -r   Play Random Game"
    print "         -v   Verbose Output (Show all found solutions)"
    print "         -s    Stop when Solved"
    print ""
    sys.exit(1)
#-----------------------------------------------------------------------------

print ""
print "Krypto:   %d  %d  %d  %d  %d  :  %d" % (x[0], x[1], x[2], x[3], x[4], solv)
if verbose:
    print "(verbose on)"
print ""


# initialize 
solns = 0; its=0; solved = 0;
all_ops = choose(ops, 4, 'c')
perms = permute(x)

# cycle through all the permutions of the numbers
for px in perms:
    if solved and stop_solved: break
    # and cycle through permutations of the operations
    for o in all_ops:
        # and cycle through permutations of parentheses
        for feq in parenthesize(px, o):
            its += 1  # count iterations
            try:
                s = eval(feq)
            except ZeroDivisionError:
                s = -1
        
            if s == solv:
                solns += 1
            
                if verbose:
                    print "Solution #%d: %s" % (solns, format_eq(feq))
                    
                if not solved:
                    aneq = format_eq(feq)
                    solved = 1


## RESULTS

print "Total Iterations: ",its 
print "Total Solutions: ", solns
if not verbose:
    print "A Solution: ", aneq
    
stop_clock = time.clock()
print "Time Elapsed: %s" % calc_time(start_clock, stop_clock)

