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
