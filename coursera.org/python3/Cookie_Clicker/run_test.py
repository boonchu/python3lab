#! /usr/bin/env python

from poc_simpletest import TestSuite
from cookie_clicker import *

def run_test():
    """
    https://class.coursera.org/principlescomputing1-004/forum/thread?thread_id=681
    https://class.coursera.org/principlescomputing1-004/forum/thread?thread_id=697
    https://class.coursera.org/principlescomputing1-004/forum/thread?thread_id=700
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
    suite.run_test(state_3.__str__(), ("Time: 5000.0 Current Cookies: 5000.0 CPS: 1.0 Total Cookies: 5000.0 History (length: 1): [(0.0, None, 0.0, 0.0)]"),\
        "Different message from test3")

    # For the cheap strategy, you need to choose the item that has the lowest cost (cheapest) each time.
    # This may change throughout the simulation because an item's cost increases after you buy an item.
    #
    # OwlTest tells you that:
    #
    # A - cost 5.0, CPS increment: 1.0
    # B - cost: 50000.0, CPS increment 3.0
    # C - cost: 500.0, CPS increment 2.0
    #
    # - Since you start with 500000.0 cookies, you can definitely build all of them (A, B and C).
    # - Of the items that can be built, append the item costs to a list.  [5.0, 50000.0, 500.0]
    # - Find the cheapest item cost. 5.0
    # - Return the name of the item which costs this amount. A
    state_4 = strategy_cheap(500000.0, 1.0, [(0.0, None, 0.0, 0.0)], 5.0, provided.BuildInfo({'A': [5.0, 1.0], 'C': [50000.0, 3.0], 'B': [500.0, 2.0]}, 1.15))
    suite.run_test(state_4, ("A"), "expect A from test 4")

    # For the expensive strategy, this is just the opposite.  Choose the item that has the highest cost
    # (most expensive) each time.  However, you also need to factor in how much time is left when
    # deciding which item you can buy.
    state_5 = strategy_expensive(500000.0, 1.0, [(0.0, None, 0.0, 0.0)], 5.0, provided.BuildInfo({'A': [5.0, 1.0], 'C': [50000.0, 3.0], 'B': [500.0, 2.0]}, 1.15))
    suite.run_test(state_5, ("C"), "expect C from test 5")

    # To achieve this, ensure that the simulate_clicker function continues to loop until the strategy function is either:
    # 1) beyond the time limit (not equal to - since it can still buy items with 0.0 seconds remaining); or
    # 2) returns None (because it no longer wants to buy any items)
    # 
    state_6 = simulate_clicker(provided.BuildInfo({'Cursor': [15.0, 50.0]}, 1.15), 16.0, strategy_cursor_broken)
    suite.run_test(state_6.__str__(), ("Time: 16.0 Current Cookies: 13.9125 CPS: 151.0 Total Cookies: 66.0 History (length: 4): [(0.0, None, 0.0, 0.0), (15.0, 'Cursor', 15.0, 15.0), (16.0, 'Cursor', 17.25, 66.0), (16.0, 'Cursor', 19.8375, 66.0)]"),
        "Different message from test6")

    state_7 = simulate_clicker(provided.BuildInfo({\
        'Cursor': [15.0, 0.10000000000000001],\
        'Portal': [1666666.0, 6666.0],\
        'Shipment': [40000.0, 100.0],\
        'Grandma': [100.0, 0.5],\
        'Farm': [500.0, 4.0],\
        'Time Machine': [123456789.0, 98765.0],\
        'Alchemy Lab': [200000.0, 400.0],\
        'Factory': [3000.0, 10.0],\
        'Antimatter Condenser': [3999999999.0, 999999.0],\
        'Mine': [10000.0, 40.0]}, 1.15), 10000000000.0,\
        strategy_expensive)
    suite.run_test(str(state_7.get_cookies()), '2414.64612076', "Expect value 2414.64612076 from test 7.1")
    suite.run_test(str(state_7.get_cps()), '133980795.7', "Expect value 133980795.7 from test 7.2")
    suite.run_test(str(state_7._total_cookies), '6.83676443443e+17', "Expect value 6.83676443443e+17 from test 7.3")
    #print str(state_7.get_history())

    # Best score from strategy
    # https://class.coursera.org/principlescomputing1-004/forum/thread?thread_id=#3
    #
    state_8 = simulate_clicker(provided.BuildInfo({\
        'Cursor': [15.0, 0.10000000000000001],\
        'Portal': [1666666.0, 6666.0],\
        'Shipment': [40000.0, 100.0],\
        'Grandma': [100.0, 0.5],\
        'Farm': [500.0, 4.0],\
        'Time Machine': [123456789.0, 98765.0],\
        'Alchemy Lab': [200000.0, 400.0],\
        'Factory': [3000.0, 10.0],\
        'Antimatter Condenser': [3999999999.0, 999999.0],\
        'Mine': [10000.0, 40.0]}, 1.15), 10000000000.0,\
        strategy_best)
    print 'Best score from strategy ' + str(state_8._total_cookies)

    suite.report_results()

if __name__ == '__main__':
    '''
    POC run test suite
    '''
    run_test()
