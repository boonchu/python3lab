#! /usr/bin/env python

from sequence import *

def seq_size(outcomes):
    return math.log(outcomes)/math.log(2)

def sequence_trials():
    '''
    Consider a sequence of trials in which a fair
    four-sided die (with faces numbered 1-4) is
    rolled twice.

    What is the expected value of the product of the two die rolls?
    '''
    outcomes = (1, 2, 3, 4)
    state = gen_all_sequences(outcomes, 2)
    product = 0

    print "[DEBUG] state => %s size => %s" % (state, len(state))

    for item in state:
        product += item[0] * item[1]

    print "[DEBUG] seq outcomes size is %s" % (seq_size(16.0))

    return product * 1 / (2**float(len(outcomes)))

print 'Question 3 answer:', sequence_trials()
