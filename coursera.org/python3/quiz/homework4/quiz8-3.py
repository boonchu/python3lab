#! /usr/bin/env python

"""
A set S is a subset of another set T (mathematically denoted as S suset of T)
if every element x in S (mathematically denoted as x subset in S) is also a member
of T.

Which of the following sets are subsets of the set {1,2}?
"""

def subset_of_set(sets):
    '''
    just generate a power set
    sets (a tuple): original set
    returns a set of tuples
    '''
    all_set = [()]
    for item in sets:
        for subset in all_set:
            all_set = all_set + [tuple(subset) + (item, )]
           
    return all_set

print subset_of_set(set((1,2)))

print '\nPrep for Question 8 follows...'
print 'when n is 0:', len(subset_of_set(())), subset_of_set(())
print 'when n is 1:', len(subset_of_set((1, ))), subset_of_set((1, ))
print 'when n is 2:', len(subset_of_set((1, 2))), subset_of_set((1, 2))
print 'when n is 3:', len(subset_of_set((1, 2, 3))), subset_of_set((1, 2, 3))
print 'when n is 4:', len(subset_of_set((1, 2, 3, 4))), subset_of_set((1, 2, 3, 4))
print 'when n is 5:', len(subset_of_set((1, 2, 3, 4, 5))), '(subset_of_set output omitted, too long)'
print 'when n is 6:', len(subset_of_set((1, 2, 3, 4, 5, 6))), '(subset_of_set output omitted, too long)'
print 'when n is 7:', len(subset_of_set((1, 2, 3, 4, 5, 6, 7))), '(subset_of_set output omitted, too long)'
print 'when n is 8:', len(subset_of_set((1, 2, 3, 4, 5, 6, 7, 8))), '(subset_of_set output omitted, too long)', '\n'

