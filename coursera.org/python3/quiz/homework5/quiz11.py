#! /usr/bin/env python

"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""

# Used to increase the timeout, if necessary
try:
  import SimpleGUICS2Pygame.codeskulptor as codeskulptor
except ImportError:
  import codeskulptor
codeskulptor.set_timeout(20)

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """

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


def store_tuples(hand, length):
    """
    store all possible events from dice

    """
    if length == 0:
        return set([()])
    first = hand[0]
    temps  = store_tuples(hand[1:], length-1)
    tuples = set([()])
    for temp in temps:
        lst = list(temp)
        lst.append(first)
        tuples.add(tuple(sorted(lst)))
    tuples.update(temps)
    return tuples


def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold

    """
    return store_tuples(hand, len(hand))


TEST_CASES = [(), (2,), (3,), (6,), (2, 3), (2, 6), (3, 6), (2, 3, 6)]
#gen_all_holds(tuple([2, 3, 6])) )

if __name__ == '__main__':
    '''
    POC run test suite
    '''
    #import poc_holds_testsuite
    #poc_holds_testsuite.run_suite(gen_all_holds)
