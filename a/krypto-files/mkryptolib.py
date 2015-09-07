# Marcus Kazmierczak, marcus@mkaz.com
# http://mkaz.com/math/krypto/
# Feb 24, 2002

#-----------------------------------------------------------------------------
# Krypto Solver Library
# $Revision: 1.9 $
# $Date: 2002/03/16 18:52:19 $
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
from math import floor
from string import replace
from array import array

#-----------------------------------------------------------------------------
# Permutation Machine
#    From Programming Python Ch17 Ex: 17-23
#-----------------------------------------------------------------------------
def permute(list):
    if not list:                                        # shuffle any sequence
        return [list]                                   # empty sequence
    else:
        res = []
        for i in range(len(list)):
            rest = list[:i] + list[i+1:]                # delete current node
            for x in permute(rest):                     # permute the others
                res.append(list[i:i+1] + x)             # add node at front
        return res

#-----------------------------------------------------------------------------
# Choose - Supposed to give back all possible combinations (with replacement)
# of list choosing c number.
#-----------------------------------------------------------------------------
def choose(list, c, type):
    cs = [];
    add = cs.append
    loop_length = pow(len(list),c)
    for i in range(0,loop_length):
        w = array(type)
        for j in range(1,c+1):
            # period of repeating item per column
            period = pow(len(list), c-j)
            
            # i//period = floordiv(i/p)
            # Modulo len(list) gives us the item 
            w.append(list[(i//period) % len(list)])
        add(w)
    return cs
#-----------------------------------------------------------------------------
        
        

#-----------------------------------------------------------------------------
# Parenthesize -- accepts list of 5 numbers and 4 operations and
#                 returns a list of the 14 equations to be evaluated
#
#   14 possible arrangments of parentheses
#
#   Note: Does NOT take into account commutative
#         operations so there are equivalent statements
#         duplicated 
#
#-----------------------------------------------------------------------------
def  parenthesize(x, op):
    # equi-commutative operators
    eqops = ['+','-']

    if ((min(op) == max(op)) and (op[0] != "/")):
        return [("%d %s %d %s %d %s %d %s %d") % (x[0], op[0], x[1], op[1], x[2], op[2], x[3], op[3], x[4])]
    
    if ((op[0] in eqops) and (op[1] in eqops) and (op[2] in eqops) and (op[3] in eqops)):
        return [("%d %s %d %s %d %s %d %s %d") % (x[0], op[0], x[1], op[1], x[2], op[2], x[3], op[3], x[4])]

    eqs = []
    add = eqs.append
    add((" %d %s ( %d %s ( %d %s ( %d %s %d ))) ") % (x[0], op[0], x[1], op[1], x[2], op[2], x[3], op[3], x[4]))
    add((" %d %s ( %d %s (( %d %s %d ) %s %d )) ") % (x[0], op[0], x[1], op[1], x[2], op[2], x[3], op[3], x[4]))
    add((" %d %s (( %d %s %d ) %s ( %d %s %d )) ") % (x[0], op[0], x[1], op[1], x[2], op[2], x[3], op[3], x[4]))
    add((" %d %s (( %d %s ( %d %s %d )) %s %d ) ") % (x[0], op[0], x[1], op[1], x[2], op[2], x[3], op[3], x[4]))
    add((" %d %s ((( %d %s %d ) %s %d ) %s %d ) ") % (x[0], op[0], x[1], op[1], x[2], op[2], x[3], op[3], x[4]))
    add((" ( %d %s %d ) %s ( %d %s ( %d %s %d )) ") % (x[0], op[0], x[1], op[1], x[2], op[2], x[3], op[3], x[4]))
    add((" ( %d %s %d ) %s (( %d %s %d ) %s %d ) ") % (x[0], op[0], x[1], op[1], x[2], op[2], x[3], op[3], x[4]))
    add((" ( %d %s ( %d %s %d )) %s ( %d %s %d ) ") % (x[0], op[0], x[1], op[1], x[2], op[2], x[3], op[3], x[4]))
    add((" ( %d %s ( %d %s ( %d %s %d ))) %s %d ") % (x[0], op[0], x[1], op[1], x[2], op[2], x[3], op[3], x[4]))
    add((" ( %d %s (( %d %s %d ) %s %d )) %s %d ") % (x[0], op[0], x[1], op[1], x[2], op[2], x[3], op[3], x[4]))
    add((" (( %d %s %d ) %s %d ) %s ( %d %s %d ) ") % (x[0], op[0], x[1], op[1], x[2], op[2], x[3], op[3], x[4]))
    add((" (( %d %s %d ) %s ( %d %s %d )) %s %d ")  % (x[0], op[0], x[1], op[1], x[2], op[2], x[3], op[3], x[4]))  
    add((" (( %d %s ( %d %s %d )) %s %d ) %s %d ") % (x[0], op[0], x[1], op[1], x[2], op[2], x[3], op[3], x[4]))
    add((" ((( %d %s %d ) %s %d ) %s %d ) %s %d ") % (x[0], op[0], x[1], op[1], x[2], op[2], x[3], op[3], x[4]))
    
    return eqs

#-----------------------------------------------------------------------------



#-----------------------------------------------------------------------------
# Calculate Time
#-----------------------------------------------------------------------------
def calc_time(start, stop):
    te = stop - start
    h = 0; m = 0; s = 0;
    
    if te > 3600:
        h = floor(te/3600)
        te = te - h*3600
            
    m = floor(te/60)
    s = te - m*60
    
    if h:
        rs = "%dh %dm %ds" % (h, m, s)
    else:
        rs = "%dm %ds " % (m, s)
    
    return rs
#-----------------------------------------------------------------------------
def format_eq(eq):
    # remove .0 from equation
    eq = replace(eq, "00", "")
    return replace(eq, ".0", "")
    
