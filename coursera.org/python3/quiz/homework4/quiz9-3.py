#! /usr/bin/env python

import math

"""
Given a standard 52 card deck of playing cards, what is the probability
of being dealt a five card hand where all five cards are of the same suit?

Hint: Use the formula for combinations to compute the number of possible
five card hands when the choice of cards is restricted to a single suit
versus when the choice of cards is unrestricted.

Compute your answer in Python using math.factorial and enter the answer
below as a floating point number with at least four significant digits
of precision. 
"""

combination_subset =  math.factorial(13)/(math.factorial(13-5)*math.factorial(5))
print 4.0 * float(combination_subset)
combination_superset = math.factorial(52)/(math.factorial(52-5)*math.factorial(5))
print float(combination_superset)

print "probability of drawing 5 cards and have same suit outcome %s" % str(4.0*float(combination_subset)/float(combination_superset))
