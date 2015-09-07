#! /usr/bin/env python

"""
Interpretation bottom one: runs in linear time (as input size increases by 10x the time it takes to run increases by 10x). It takes 12x as long to process a 10^6 len list of items that don't merge as compared to same size baseline list with all zeros.

Should be able to run on desktop python too since the normalized versions will take the faster processing into account and (theoretically) let you see the relative performance of the algorithm.

Generally speaking (to noone in particular), for help on improving your algorithm you can look to sites like these (site1, site2) for performance characteristics of different operations. O(N) means that the time it takes to perform the operation scales proportionally in the number of items, N (e.g. a for loop iterating over N items--iteration will happen N times, so as N gets bigger the code takes more time to process). If one iteration of a loop takes 2 seconds to complete, then two iterations will take 2*2=4 sec and N iterations will take N*2 sec. O(1) means that the operation is constant time. An example might be assigning something to a variable or appending an item to a list. The thing to remember with O(1) operations is that the time is constant but not necessarily equal to other O(1) operations. Appending to a list might take 10 times longer than assigning to a variable, even though both are O(1). A basic strategy for your code writing, then, might be to get rid of O(N)+ operations where possible, and then find the faster combinations of O(1) operations to use (trial and error based on specific implementation). Although, readability should (in general) take precedece when it comes to splitting hairs over O(1) operations .
"""

import time
import random
#import codeskulptor

#codeskulptor.set_timeout(60)
base_time = 1


def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    # replace this with your merge function code
    lst = [0]*len(line)
    for item in lst:
        if not item:
            continue
    return lst

def base_test(ntrials=1):
    """ 
    Find how long it takes on this machine to create list with  
    10^6 items and loop over it.
    
    Arguments:
        ntrials:(int) allows for finding average time over n trials
    
    """
    global base_time
    
    ln = [0]*1000000

    cnt = 0
    for n in xrange(ntrials):
        time1 = time.time()
        for i in ln:
            if not i:
                continue

        time2 = time.time()
        cnt += time2 - time1
        
    base_time = cnt/float(ntrials)
    print 'Baseline (10^6 items):\t%.5f s'%base_time

def main_test(title, ntrials, choices, size_as_exp=1, random_flag=True):
    """ 
    Find how long it takes on this machine to execute your merge fn  
    using the given settings
    
    Arguments:
        title:(str) name of the test
        ntrials:(int) allows for finding average time over n trials
        choices:(list of ints) values used to fill input line
        size_as_exp:(int) all sizes are multiples of 10. This is the exponent
        random_flag:(bool) set whether choices are selected randomly or ordered
    
    """
    if random_flag:
        ln = [random.choice(choices) for x in xrange(10**size_as_exp)]
    else:
        ln = choices*(10**size_as_exp/len(choices))

    cnt = 0
    for i in range(ntrials):
        time1 = time.time()
        merge(ln)
        time2 = time.time()
        cnt += time2 - time1
    
    tot = cnt/float(ntrials)
    print '%s (10^%d items):\t%.5f s'%(title, size_as_exp, tot), "(Normalized: %.5f)"%(tot/base_time)

    
#######################################
# Tests

print "All tests measured in seconds.\n"

# baseline
base_test(2)
print

# random tests
print "*Random tests using [0,0,1,2,4,8,16,32]"
rand = [0,0,1,2,4,8,16,32]    
main_test("1000", 50, rand, 3)
main_test("10000", 25, rand, 4)
main_test("100000", 4, rand, 5)
main_test("1000000", 1, rand, 6)
print

# All zeros
main_test("All zeros", 1, [0], 6, False)

# All numbers merge
main_test("All merge", 1, [8], 6, False)

# None of the numbers merge
main_test("Non merge", 1, [1,2], 6, False)

