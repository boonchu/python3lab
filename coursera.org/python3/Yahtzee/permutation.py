#! /usr/bin/env python

def perm (t, l, outcomes, perm_list):
    if l == 1:
        for on in outcomes:
            nt = t + (on,)
            perm_list.append(nt)
    else:
        for o in outcomes:
            nt = t + (o,)
            perm(nt, l-1, outcomes, perm_list)
        return perm_list

def permutate_a_list(outcomes, length):
    t = ()
    perm_list = []
    if len(outcomes) == 0:
        perm_list.append(t)
        return perm_list
    else:
        # print(perm_list)
        permutations = perm(t, length, outcomes, perm_list)
        return permutations

'''
- you have to fill in 4 positions - think of them for example as  4 holes, where you can put one colored ball into each hole
- for filling the position #1 you have to pick an item (i.e. an outcome) from set that has x items (from set of outcomes that has size x)
- for filling the position #2 you have to again pick an item from set that has x items
- for filling the position #3 you have to pick an item from set that has y items
- for filling the position #4 you have to pick an item from set that has y items

set of outcomes = (x)^2 * (y)^2
'''
_1_outcomes = [0,1,2,3]
_1_enumeration = set(permutate_a_list(_1_outcomes, 2))
_2_outcomes = ['a', 'b', 'c']
_2_enumeration = set(permutate_a_list(_2_outcomes, 2))

print (_1_enumeration)
print (len(_1_enumeration))
print (_2_enumeration)
print (len(_2_enumeration))

_lists_of_combination = list()
for outcome in _1_enumeration:
    _lists_of_combination += [ outcome + outc for outc in _2_enumeration ]

print _lists_of_combination
print (len(_lists_of_combination))
