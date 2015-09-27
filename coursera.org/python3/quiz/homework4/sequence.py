#! /usr/bin/env python

import math
import itertools

# helper functions

def gen_all_sequences(outcomes, length):
    '''
    function that enumerates the set of all sequences of outcomes of given length;
    original code from the lecture, do not modify
    '''
    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set

if __name__ == "__main__":
    state = gen_all_sequences((1, 2, 3, 4), 2)
    print state, len(state)
