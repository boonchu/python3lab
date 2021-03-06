#! /usr/bin/env python
#
# https://class.coursera.org/principlescomputing1-004/forum/thread?thread_id=590

from sequence import *

def seq_size(outcomes):
    return math.log(outcomes)/math.log(2)

def is_in_seq(nums):
    ranges = sum((list(t) for t in zip(nums, nums[1:]) if t[0]+1 != t[1]), [])
    return len(ranges) == 0

def sequence_trials():
    '''
    Consider a trial in which five digit strings are formed as permutations
    of the digits ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]. (In
    this case, repetition of digits is not allowed.) If the probability of
    each permutation is the same, what is the probability that this five
    digits string consists of consecutive digits in either ascending or
    descending order (e.g; "34567" or "43210") ? 

    i.e. Number of successes = number of five-digit strings with consecutive
    digits - "01234", "12345", "23456" etc.  So count them all.

    i.e. Total number of outcomes = number of five-digit strings
    Think about enumerations.

    Answer (probability) = Number of successes / Total number of outcomes
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
    '''
    So Number of successes counted manually (we'll use x)  x = 12

    {0,1,2,3,4}
    {1,2,3,4,5}
    {2,3,4,5,6}
    {3,4,5,6,7}
    {4,5,6,7,8}
    {5,6,7,8,9}
    and then their reversal;
    {9,8,7,6,5}
    {8,7,6,5,4}
    {7,6,5,4,3}
    {6,5,4,3,2}
    {5,4,3,2,1}
    {4,3,2,1,0}
    '''
    print "count is %s" % str(count)

    # http://www.mathwords.com/p/permutation_formula.htm
    # with permutation probability
    # math.factorial(n)/math.factorial(n-k)
    '''
    "So here we just calculate how many sequences of length 5 (n) are possible if the SET of outcomes has size 10 (m)"
    answer = x/(m!/(m-n)!)
    '''
    factor = float(math.factorial(10)/math.factorial(10-5))
    return float(count/factor)

print 'Question 5 answer:', sequence_trials()
