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


def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score 
    """
    return 0 if len(hand)==0 else max([_num*hand.count(_num) for _num in set(hand)])


def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value

    https://class.coursera.org/principlescomputing1-004/forum/thread?thread_id=471

    expected value:
    The hand (1,2,3,4,5) comes in 5! = 120 variants, the hand (1,1,2,2,2) comes in 5! / (2! * 3!) = 10 variants.

    (n+m)!/n!m!

    Shouldn't you be generating all enumerations of free dice?  You then determine all possible outcomes.  Each
    outcome has equal probability of occurring.  It doesn't matter which are variants of which, since you listed
    every possible outcome (including variants), and so this will be incorporated into your calculations already.

    """
    _outcomes = gen_all_sequences(range(1, num_die_sides+1), num_free_dice)
    sum_of_events = float(sum([score(held_dice + _event) for _event in _outcomes]))
    total_probabilities  = float(len(_outcomes))
    #print "sum of possible outcomes %s vs. sum of probabilities %s" % (str(sum_of_events), str(total_probabilities))
    return sum_of_events/total_probabilities


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


def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold

    num_free_dice:
    Use the more general formula: num_free_dice = len(hand) - len(held_dice)
    """
    items = gen_all_holds(hand)
    max_val = 0
    holds = list()
    for item in items:
        val = expected_value(item, num_die_sides, len(hand)-len(item))
        if max_val < val:
            max_val = val
            holds = item
    return (max_val, holds)


def run_example():
    '''
    Compute the dice to hold and expected score for an example hand

    https://class.coursera.org/principlescomputing1-004/forum/thread?thread_id=468

    https://class.coursera.org/principlescomputing1-004/forum/thread?thread_id=483
    expected_value(held_dice=(1, 1), num_die_sides=6, num_free_dice=1)
    all possilbe sequences after re-roll their respective hand values, and probabilities:
    (1, 1, 1) = 3 = 3/6
    (1, 1, 2) = 2 = 2/6
    (1, 1, 3) = 3 = 3/6
    (1, 1, 4) = 4 = 4/6
    (1, 1, 5) = 5 = 5/6
    (1, 1, 6) = 6 = 6/6
    expected value (yatzee hand score) = 23/6 = 3.833

    '''
    print expected_value((1, 1), 6, 1), " value should be => 3.83333333333"
    print expected_value((2, 2), 6, 2), " value should be => 5.83333333333"
    print expected_value((2, 2), 6, 1), " value should be => 4.83333333333"
    print expected_value((2, 4), 6, 3), " value should be => 7.69907407407"
    print expected_value((5, 5), 6, 4), " value should be => 13.6311728395"

    num_die_sides = 6
    hand = (1,)
    hand_score, hold = strategy(hand, num_die_sides)
    print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score

    num_die_sides = 6
    hand = (1, 1, 1, 5, 6)
    hand_score, hold = strategy(hand, num_die_sides)
    print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score


if __name__ == '__main__':
    '''
    POC run test suite
    '''
    import poc_holds_testsuite
    run_example()
    poc_holds_testsuite.run_suite(gen_all_holds)
