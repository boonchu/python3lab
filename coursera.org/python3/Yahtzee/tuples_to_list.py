#! /usr/bin/env python

item = (1,)
answer_set = set([()])
temp_set = set()
for partial_sequence in set([(1,), (4,), (5,)]):
    new_sequence = list(partial_sequence) + list(item)
    temp_set.add(tuple(new_sequence))
answer_set = temp_set

print answer_set
