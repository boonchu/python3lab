#! /usr/bin/env python

"""
Given the set of outcomes corresponding to a coin flip,
    {Heads,Tails},
how many sequences of outcomes of length five (repetition allowed)
are possible? 
"""

from sequence import *

def sequence_trials():
    '''
    Consider a sequence of trials in which a fair
    four-sided die (with faces numbered 1-4) is
    rolled twice.
   
    What is the expected value of the product of the two die rolls?
    '''

    outcomes = ('Head', 'Tail')
    state = gen_all_sequences(outcomes, 5)
    product = 0

    print "[DEBUG] state => %s size => %s" % (state, len(state))
    
sequence_trials()
