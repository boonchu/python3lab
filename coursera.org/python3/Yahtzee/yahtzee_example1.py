"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""

# Used to increase the timeout, if necessary
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

    return max([idx*hand.count(idx) for idx in range(1,1+max(hand))])


def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    # generate all of the possible sequences
    all_sequences = gen_all_sequences(range(1,num_die_sides+1), num_free_dice)
    # sum the scores for the sequences
    total_score = sum([score(held_dice + sequence) for sequence in all_sequences])
    # return the mean of the scores
    return float(total_score) / len(all_sequences)


def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    
    # make a list of tuples with the values and their count
    if hand <> ():
        counts = [(idx+1,hand.count(idx+1)) for idx in range(max(hand))]
    
    answer_set = set([()])
    for dummy_idx in range(len(hand)):

        # make a copy of the answer_set that can be added to
        #  the original is used in the for loop and is immutable
        temp_set = set(answer_set)

        # loop over the tuples already in the answer set
        for partial_sequence in answer_set:

            # loop over each dice value in the original hand
            for dice_value in hand:

                # make a list from the tuple so that it can be added to
                new_sequence = list(partial_sequence)

                # Only use this dice_value if it is in the new sequence
                # fewer times than in the hand
                if new_sequence.count(dice_value) < counts[dice_value-1][1]:

                    # append to the new sequence and sort the list
                    new_sequence.append(dice_value)
                    new_sequence.sort()
                    # Add as a tuple to the set -- not very efficient 
                    # but using a set avoids duplicates
                    temp_set.add(tuple(new_sequence))

        # end partial_sequence for loop
        
        # save the temporary set to the master set
        answer_set = temp_set
    # end dummy_idx for loop

    return answer_set

def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    
    # for each possible hold, get it's expected value
    possible_hold = \
        [(expected_value(hold, num_die_sides, \
                         len(hand)-len(hold)),hold) \
         for hold in gen_all_holds(hand)]

    return max(possible_hold)


#def run_example():
#    """
#    Compute the dice to hold and expected score for an example hand
#    """
#    num_die_sides = 6
#    hand = (1, 1, 1, 5, 6)
#    print "score:",score(hand)
#    hand_score, hold = strategy(hand, num_die_sides)
#    print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score, "\n"
#    
#    
#run_example()
#
#
#import poc_holds_testsuite
#poc_holds_testsuite.run_suite(gen_all_holds)
#                                       
#import poc_simpletest
#
#def test_score(func):
#    
#    suite = poc_simpletest.TestSuite()
#    
#    suite.run_test(func((1,1,1,1,1)), 5, "Test 0: Scoring (1,1,1,1,1).")
#    suite.run_test(func((2,2)), 4, "Test 1: Scoring (2,2).")
#    suite.run_test(func((2,3)), 3, "Test 2: Scoring (2,3).")
#    suite.run_test(func((2,2,3,3)), 6, "Test 3: Scoring (2,2,3,3).")
#    suite.run_test(func((3,3,3,6)), 9, "Test 4: Scoring (3,3,3,6).")
#    suite.run_test(func((1,2,3,4,5)), 5, "Test 5: Scoring (1,2,3,4,5).")
#
#    suite.run_test(func((1,)), 1, "OwlTest: Scoring (1,).")
#        
#    suite.report_results()
##
#test_score(score)    
#    
#def test_expected_value(func):
#
#    suite = poc_simpletest.TestSuite()
#    
#    #simple tests
#    suite.run_test(func((1,), 2, 1), 2, "Test 1: two-sided die, one held die (1), one free die.")
#    suite.run_test(func((2,), 2, 1), 3, "Test 2: two-sided die, one held die (1), one free die.")
#    suite.run_test(func((1,1), 2, 1), 2.5, "Test 3: two-sided die, two held die (1,1), one free die.")
#    suite.run_test(func((1,2), 2, 1), 3, "Test 4: two-sided die, two held die (1,2), one free die.")
#    suite.run_test(func((2,2), 2, 1), 5, "Test 5: two-sided die, two held die (2,2), one free die.")
#    suite.run_test(func((1,), 2, 2), 2.75, "Test 6: two-sided die, one held die (1), two free die.")
#    suite.run_test(func((2,), 2, 2), 4, "Test 7: two-sided die, one held die (2), two free die.")
#    
#    #from OwlTest
#    suite.run_test(func((2, 2), 6, 2), 35/6.0, "OwlTest: 6-sided, two held die (2,2), two free die.")
#    suite.run_test(func((3, 3), 8, 5), 93053/8192.0, "OwlTest: 8-sided, two held die (3,3), five free die.")
#
#    #complicated tests
#    suite.run_test(func((1,2,3), 3, 2), 50/9.0, "Test 8: three-sided die, three held die (1,2,3), two free die.")
#    suite.run_test(func((2, 2), 6, 1), 29/6.0,"Hao-Wen Sim: 6-sided, two held die (2,2), one free die.")
#    suite.run_test(func((2, 4), 6, 3),1663/216.0,"Hao-Wen Sim: 6-sided, two held die (2,4), three free die.")
#    suite.run_test(func((5, 5), 6, 4),8833/648.0,"Hao-Wen Sim: 6-sided, two held die (5,5), four free die.")
#    #
#    suite.report_results()
#
#test_expected_value(expected_value)
#    
#def test_gen_all_holds(func):
#    suite = poc_simpletest.TestSuite()
#
#    suite.run_test(func((1,2,3,3,4)), set([(), (2, 3, 3, 4), (1, 2, 3), (1, 2, 4), (1,), (2,), (3,), (4,), (1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 3), (3, 4), (1, 3, 3), (1, 3, 4), (2, 3, 3), (2, 3, 4), (3, 3, 4), (1, 2, 3, 3), (1, 2, 3, 4), (1, 3, 3, 4), (1, 2, 3, 3, 4)]), "Test 3. gen_all_holding((1,2,3,3,4))")
#    suite.report_results()  
#
#test_gen_all_holds(gen_all_holds)
#
#def test_strategy(func):
#    
#    suite = poc_simpletest.TestSuite()
#    
#    suite.run_test(func((1,2), 2), (3.0, (2,)), "Test 1: two-sided die, hand is (1,2).")
#    suite.run_test(func((1,2), 3), (28/9.0, ()), "Test 2: three-sided die, hand is (1,2).")
#    suite.run_test(func((1,), 6), (3.5, ()), "OwlTest: 6-sided, hand is (1,).")
#    suite.report_results()  
#
#test_strategy(strategy)
