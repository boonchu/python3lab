#! /usr/bin/env python

from poc_simpletest import TestSuite
from cookie_clicker import *

def run_test():
    """
    https://class.coursera.org/principlescomputing1-004/forum/thread?thread_id=681
    """
    suite = TestSuite()
    state_1 = ClickerState()
    suite.run_test(state_1.wait(45.0), None , 'Wrong wait #1')
    suite.run_test(state_1.buy_item('item', 1.0, 3.5), None , "Error with buy item")
    suite.run_test(state_1.__str__(), ("Time: 45.0 Current Cookies: 44.0 CPS: 4.5 Total Cookies: 45.0 History (length: 2): [(0.0, None, 0.0, 0.0), (45.0, 'item', 1.0, 45.0)]"),\
    "Different message from test1")

    state_2 = ClickerState()
    suite.run_test(state_2.wait(45.0), None , 'Wrong wait #2')
    suite.run_test(state_2.__str__(), ("Time: 45.0 Current Cookies: 45.0 CPS: 1.0 Total Cookies: 45.0 History (length: 1): [(0.0, None, 0.0, 0.0)]"),\
    "Different message from test2")

    state_3 = simulate_clicker(provided.BuildInfo({'Cursor': [15.0, 0.10000000000000001]}, 1.15), 5000.0, strategy_none)
    suite.run_test(state_3.__str__(), ("Time: 5000.0 Current Cookies: 5000.0 CPS: 1.0 Total Cookies: 5000.0 History (length: 1): [(0.0, None, 0.0, 0.0)]"), "Different message from test3")
    suite.report_results()

if __name__ == '__main__':
    '''
    POC run test suite
    '''
    run_test()
