#! /usr/bin/env python
#
#
# In a previous homework, we implemented an iterative method for generating permutations of a set of outcomes. Permutations can
# also be generated recursively.
#
# Given a list outcomes of length n, we can perform the following recursive computation to generate the set of all permutations of length n:
#
# Compute the set of permutations rest_permutations for the list outcomes[1:] of length n-1
# For each permutation perm in rest_permutations, insert outcome[0] at each possible position of perm to create permutations of length n,
# Collect all of these permutations of length n into a set and return that set.
#
# If p(n) is the number of permutations returned by this method, what recurrence below captures the behavior of p(n)?

#
# http://stackoverflow.com/questions/360748/computational-complexity-of-fibonacci-sequence
# https://books.google.com/books?id=my3mAgAAQBAJ&pg=PT101&lpg=PT101&dq=The+number+of+recursive+calls+to+fib+in+the+previous+problem+grows+quite+quickly.&source=bl&ots=NTFFvYWYiM&sig=_jxsEdMlJDefMLx5CwaXlJrMzlU&hl=en&sa=X&ved=0CB4Q6AEwAGoVChMIhry89bHWyAIVA_BjCh2eeAAi#v=onepage&q=The%20number%20of%20recursive%20calls%20to%20fib%20in%20the%20previous%20problem%20grows%20quite%20quickly.&f=false
# https://gist.github.com/bradmontgomery/4717521
#
from collections import Counter
import math
count = 0


def fib(num, counter):
    counter['fib'] += 1
    if n < 3:
        return 1
    else:
        return fib(num - 1, counter) + fib(num - 2, counter)

n = 2
print ("%12s%15s" % ("Problem size", "Calls"))
for count in range(5):
    c = Counter()
    fib(n, c)
    print ("%12s%15s" % (n, c['fib']))
    n *= 2

#calculate calls
# T(n-1) = O(2^n-1)
# T(n) = T(n-1) + T(n-2) + O(1)
# T(n) = O(2^n-1) + O(2^n-2) + O(1)
# T(n) ~ O(2^n)
#
# f(n) = f(n-1) + f(n-2)
# https://en.wikipedia.org/wiki/Fibonacci_number#Closed_form_expression
# 
# O((1/sqrt(5) * 1.618^(n+1)) = O(1.618^(n+1)
#result = 1.618**(n+1)
#print "estimated calls:",result
