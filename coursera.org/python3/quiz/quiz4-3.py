#! /usr/bin/env python

from sequence import *

def seq_size(outcomes):
    return math.log(outcomes)/math.log(2)

def is_in_seq(nums):
    ranges = sum((list(t) for t in zip(nums, nums[1:]) if t[0]+1 != t[1]), [])
    return len(ranges) == 0

def sequence_trials():
    '''
    Given a trial in which a decimal digit is selected from the list
    ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"] with equal
    probability 0.1, consider a five-digit string created by a
    sequence of such trials (leading zeros and repeated digits are allowed).
    
    What is the probability that this five-digit string consists of five
    consecutive digits in either ascending or descending order (e.g; "34567" or "43210") ?

    Enter your answer as a floating point number with at least
    four significant digits of precision.
    '''
    outcomes = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    state = gen_all_sequences(outcomes, 5)
    product = 0

    print "[DEBUG] state => %s size => %s" % (state, len(state))
    
    count=0.0
    for item in state:
        if is_in_seq(item):
            print "item is %s or %s" % (str(item), str(tuple(reversed(item))))
            count += 2.0

    print "length of state => %s" % len(state)
    print "count is %s" % str(count)

    return float(count/len(state))

print 'Question 4 answer:', sequence_trials()
