#! /usr/bin/env python

from yahtzee import *
import poc_simpletest


def test_score(func):

    suite = poc_simpletest.TestSuite()

    suite.run_test(func((1,1,1,1,1)), 5, "Test 0: Scoring (1,1,1,1,1).")
    suite.run_test(func((2,2)), 4, "Test 1: Scoring (2,2).")
    suite.run_test(func((2,3)), 3, "Test 2: Scoring (2,3).")
    suite.run_test(func((2,2,3,3)), 6, "Test 3: Scoring (2,2,3,3).")
    suite.run_test(func((3,3,3,6)), 9, "Test 4: Scoring (3,3,3,6).")
    suite.run_test(func((1,2,3,4,5)), 5, "Test 5: Scoring (1,2,3,4,5).")
    suite.run_test(func((1,3,4,5,10)), 10, "Test 6: Scoring (1,3,4,5,10).")

    suite.report_results()


def test_expected_value(func):

    suite = poc_simpletest.TestSuite()

    #simple tests
    suite.run_test(func((1,), 2, 1), 2, "Test 1: two-sided die, one held die (1), one free die.")
    suite.run_test(func((2,), 2, 1), 3, "Test 2: two-sided die, one held die (1), one free die.")
    suite.run_test(func((1,1), 2, 1), 2.5, "Test 3: two-sided die, two held die (1,1), one free die.")
    suite.run_test(func((1,2), 2, 1), 3, "Test 4: two-sided die, two held die (1,2), one free die.")
    suite.run_test(func((2,2), 2, 1), 5, "Test 5: two-sided die, two held die (2,2), one free die.")
    suite.run_test(func((1,), 2, 2), 2.75, "Test 6: two-sided die, one held die (1), two free die.")
    suite.run_test(func((2,), 2, 2), 4, "Test 7: two-sided die, one held die (2), two free die.")

    #complicated tests
    suite.run_test(func((1,2,3), 3, 2), 50/9.0, "Test 8: three-sided die, three held die (1,2,3), two free die.")

    suite.report_results()


def test_strategy(func):

    suite = poc_simpletest.TestSuite()

    suite.run_test(func((1,2), 2), (3.0, (2,)), "Test 1: two-sided die, hand is (1,2).")
    suite.run_test(func((1,2), 3), (28/9.0, ()), "Test 2: three-sided die, hand is (1,2).")

    suite.report_results()


if __name__ == '__main__':
    '''
    POC run test suite
    '''
    test_score(score)
    test_expected_value(expected_value)
    test_strategy(strategy)
