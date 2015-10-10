#! /usr/bin/env python
"""
Cookie Clicker Simulator
"""

import simpleplot
import math

# Used to increase the timeout, if necessary
#import codeskulptor
#codeskulptor.set_timeout(20)

import poc_clicker_provided as provided

# Constants
SIM_TIME = 10000000000.0

class ClickerState:
    """
    Simple class to keep track of the game state.
    """
    
    def __init__(self):
        self._total_cookies   = 0.0
        self._current_cookies = 0.0
        self._current_time    = 0.0
        self._current_cps     = 1.0
        self._history         = [(0.0, None, 0.0, 0.0)]
        
    def __str__(self):
        """
        Return human readable state
        """
        return 'total_cookies   ' + str(self._total_cookies)   + '\n' + \
               'current_cookies ' + str(self._current_cookies) + '\n' + \
               'current_time    ' + str(self._current_time)    + '\n' + \
               'current_cps     ' + str(self._current_cps)     + '\n' + \
               'history         ' + str(self._history)
        
    def get_cookies(self):
        """
        Return current number of cookies 
        (not total number of cookies)
        
        Should return a float
        """
        return self._current_cookies
    
    def get_cps(self):
        """
        Get current CPS

        Should return a float
        """
        return self._current_cps
    
    def get_time(self):  
        """
        Get current time

        Should return a float
        """
        return self._current_time
    
    def get_history(self):
        """
        Return history list

        History list should be a list of tuples of the form:
        (time, item, cost of item, total cookies)

        For example: [(0.0, None, 0.0, 0.0)]

        Should return a copy of any internal data structures,
        so that they will not be modified outside of the class.
        """
        return self._history[:]

    def time_until(self, cookies):
        """
        Return time until you have the given number of cookies
        (could be 0.0 if you already have enough cookies)

        Should return a float with no fractional part
        """
        if self._current_cookies >= cookies:
            return 0.0
        else:
            return math.ceil((cookies - self._current_cookies) / \
                             self._current_cps)
    
    def wait(self, time):
        """
        Wait for given amount of time and update state

        Should do nothing if time <= 0.0
        """
        if time > 0.0:
            self._current_time    += time
            self._current_cookies += time * self._current_cps
            self._total_cookies   += time * self._current_cps
    
    def buy_item(self, item_name, cost, additional_cps):
        """
        Buy an item and update state

        Should do nothing if you cannot afford the item
        """
        if self._current_cookies >= cost:
            self._current_cookies -= cost
            self._current_cps += additional_cps
            self._history.append((self._current_time, item_name, \
                                 cost, self._total_cookies))

    
def simulate_clicker(build_info, duration, strategy):
    """
    Function to run a Cookie Clicker game for the given
    duration with the given strategy.  Returns a ClickerState
    object corresponding to the final state of the game.
    """
    info = build_info.clone()
    state = ClickerState()
    while state.get_time() <= duration:
        item = strategy(state.get_cookies(), state.get_cps(), 
                        state.get_history(),
                        duration - state.get_time(), info)
        if item == None:
            break
        cost = info.get_cost(item)
        time_until = state.time_until(cost)
        if state.get_time() + time_until > duration:
            break
        state.wait(time_until)
        state.buy_item(item, cost, info.get_cps(item))
        info.update_item(item)
    time_left = duration - state.get_time()
    if time_left > 0:
        state.wait(time_left)
    return state


def strategy_cursor_broken(cookies, cps, history, time_left, build_info):
    """
    Always pick Cursor!

    Note that this simplistic (and broken) strategy does not properly
    check whether it can actually buy a Cursor in the time left.  Your
    simulate_clicker function must be able to deal with such broken
    strategies.  Further, your strategy functions must correctly check
    if you can buy the item in the time left and return None if you
    can't.
    """
    return "Cursor"
# Cursor : total_cookies   153308849166.0
#          current_cookies 6965195661.5
#          current_time    10000000000.0
#          current_cps     16.1

def strategy_none(cookies, cps, history, time_left, build_info):
    """
    Always return None

    This is a pointless strategy that will never buy anything, but
    that you can use to help debug your simulate_clicker function.
    """
    return None
# None : total_cookies   10000000000.0
#        current_cookies 10000000000.0
#        current_time    10000000000.0
#        current_cps     1.0

def strategy_cheap(cookies, cps, history, time_left, build_info):
    """
    Always buy the cheapest item you can afford in the time left.
    """
    items = build_info.build_items()
    bestitem, bestcost = None, None
    for item in items:
        cost = build_info.get_cost(item)
        time_needed = max(0, cost - cookies) / cps
        if time_needed <= time_left and \
           (bestcost == None or cost < bestcost):
            bestitem, bestcost = item, cost
    return bestitem
# Cheap : total_cookies   1.15285935621e+18
#         current_cookies 1.49360255736e+14
#         current_time    10000000000.0
#         current_cps     123436706.3

def strategy_expensive(cookies, cps, history, time_left, build_info):
    """
    Always buy the most expensive item you can afford in the time left.
    """
    items = build_info.build_items()
    bestitem, bestcost = None, None
    for item in items:
        cost = build_info.get_cost(item)
        time_needed = max(0, cost - cookies) / cps
        if time_needed <= time_left and \
           (bestcost == None or cost > bestcost):
            bestitem, bestcost = item, cost
    return bestitem
# Expensive : total_cookies   6.83676443443e+17
#             current_cookies 2414.64612076
#             current_time    10000000000.0
#             current_cps     133980795.7

def strategy_best(cookies, cps, history, time_left, build_info):
    """
    The best strategy that you are able to implement.
    best = max total_cookies
    """
    if len(history) < 148:
        return strategy_cheap(cookies, cps, history, time_left, build_info)
    items = build_info.build_items()
    bestitem, bestval = None, 0
    for item in items:
        delta_cps = build_info.get_cps(item)
        cost = build_info.get_cost(item)
        time_needed = max(0, cost - cookies) / cps
        delta_time = max(0, time_left - time_needed)
        val = delta_cps**2.0375 * delta_time**0.49 / cost**2.01
        if val > bestval:
            bestitem, bestval = item, val
    return bestitem  
# Best : total_cookies   1.31434601025e+18
#        current_cookies 465233336347.0
#        current_time    10000000000.0
#        current_cps     139876725.2

def run_strategy(strategy_name, time, strategy):
    """
    Run a simulation for the given time with one strategy.
    """
    state = simulate_clicker(provided.BuildInfo(), time, strategy)
    print strategy_name, ":", state._total_cookies

    # Plot total cookies over time

    # Uncomment out the lines below to see a plot of total cookies vs. time
    # Be sure to allow popups, if you do want to see it

    # history = state.get_history()
    # history = [(item[0], item[3]) for item in history]
    # simpleplot.plot_lines(strategy_name, 1000, 400, 'Time', 'Total Cookies', [history], True)

def run():
    """
    Run the simulator.
    """    
    run_strategy("Cursor",    SIM_TIME, strategy_cursor_broken)
    run_strategy("None",      SIM_TIME, strategy_none)
    run_strategy("Cheap",     SIM_TIME, strategy_cheap)
    run_strategy("Expensive", SIM_TIME, strategy_expensive)
    run_strategy("Best",      SIM_TIME, strategy_best)
    
run()
    
# item                 initial_cost  delta_cps
# Alchemy Lab              200000.0      400.0
# Antimatter Condenser 3999999999.0   999999.0
# Cursor                       15.0        0.1
# Factory                    3000.0       10.0
# Farm                        500.0        4.0
# Grandma                     100.0        0.5
# Mine                      10000.0       40.0
# Portal                  1666666.0     6666.0
# Shipment                  40000.0      100.0
# Time Machine          123456789.0    98765.0
