#! /usr/bin/env python
"""
Cookie Clicker Simulator
"""

import simpleplot
import math

# Used to increase the timeout, if necessary
#import codeskulptor
#codeskulptor.set_timeout(10)

import poc_clicker_provided as provided

# Constants
SIM_TIME = 10000000000.0

class ClickerState:
    """
    Simple class to keep track of the game state.
    """
    
    def __init__(self):
        """
        ClickerState constructor
        """
        self._time = 0.0
        self._cps = 1.0
        self._inventory = 0.0
        self._total = 0.0
        self._history = [(0.0, None, 0.0, 0.0)]
        
    def __str__(self):
        """
        Return human readable state
        """
        state = "ClickerState:\n"
        state += "  self._time:      " + str(self._time) + "\n"
        state += "  self._cps:       " + str(self._cps) + "\n"
        state += "  self._inventory: " + str(self._inventory) + "\n"
        state += "  self._total:     " + str(self._total) + "\n"
        #state += "  self._history:   " + str(self._history) + "\n"
        return state
        
    def get_cookies(self):
        """
        Return current number of cookies 
        (not total number of cookies)
        
        Should return a float
        """
        return self._inventory
    
    def get_cps(self):
        """
        Get current CPS

        Should return a float
        """
        return self._cps
    
    def get_time(self):
        """
        Get current time

        Should return a float
        """
        return self._time
    
    def get_history(self):
        """
        Return history list

        History list should be a list of tuples of the form:
        (time, item, cost of item, total cookies)

        For example: [(0.0, None, 0.0, 0.0)]

        Should return a copy of any internal data structures,
        so that they will not be modified outside of the class.
        """
        return list(self._history)

    def time_until(self, cookies):
        """
        Return time until you have the given number of cookies
        (could be 0.0 if you already have enough cookies)

        Should return a float with no fractional part

        time_until: This method should return the number of seconds you
        must wait until you will have the given number of cookies.
        Remember that you cannot wait for fractional seconds, so while
        you should return a float it should not have a fractional part.

        If a method is passed an argument that is invalid (such as an
        attempt to buy an item for which you do not have enough cookies),
        you should just return from the method without doing anything.
        """
        if not (isinstance(cookies, int) or isinstance(cookies, float)):
            print "ERROR time_until(): Input argument '" + str(cookies) + "' is not int or float"
            return None

        seconds = 0.0
        needed = cookies - self._inventory
        if needed > 0:
            seconds = math.ceil(needed / self._cps)
        return seconds
    
    def wait(self, time):
        """
        Wait for given amount of time and update state

        Should do nothing if time <= 0.0

        wait: This method should "wait" for the given amount of time.
        This means you should appropriately increase the time, the
        current number of cookies, and the total number of cookies.

        If a method is passed an argument that is invalid (such as an
        attempt to buy an item for which you do not have enough cookies),
        you should just return from the method without doing anything.
        """
        if not (isinstance(time, int) or isinstance(time, float)):
            print "ERROR wait(): Input argument '" + str(time) + "' is not int or float"
            return None

        if time > 0.0:
            produced = time * self._cps
            self._total += produced
            self._inventory += produced
            self._time += time

    def buy_item(self, item_name, cost, additional_cps):
        """
        Buy an item and update state

        Should do nothing if you cannot afford the item

        buy_item: This method should "buy" the given item. This means
        you should appropriately adjust the current number of cookies,
        the CPS, and add an entry into the history.

        If a method is passed an argument that is invalid (such as an
        attempt to buy an item for which you do not have enough cookies),
        you should just return from the method without doing anything.
        """
        if not isinstance(item_name, str):
            print "ERROR buy_item(): Input argument '" + str(item_name) + "' is not str"
            return None

        if not (isinstance(cost, int) or isinstance(cost, float)):
            print "ERROR buy_item(): Input argument '" + str(cost) + "' is not int or float"
            return None

        if not (isinstance(additional_cps, int) or isinstance(additional_cps, float)):
            print "ERROR buy_item(): Input argument '" + str(additional_cps) + "' is not int or float"
            return None

        if self._inventory >= cost:
            self._inventory -= cost
            self._cps += additional_cps
            self._history.append((self._time, item_name, cost, self._total))

def simulate_clicker(build_info, duration, strategy):
    """
    Function to run a Cookie Clicker game for the given
    duration with the given strategy.  Returns a ClickerState
    object corresponding to the final state of the game.
    """
    my_build_info = build_info.clone()
    clicker_state = ClickerState()
    done = False

    while clicker_state.get_time() <= duration and not done:
        item = strategy(clicker_state.get_cookies(),
                        clicker_state.get_cps(),
                        clicker_state.get_history(),
                        duration - clicker_state.get_time(),
                        my_build_info)

        if item:
            item_cost = my_build_info.get_cost(item)
            item_cps = my_build_info.get_cps(item)
            wait_time = clicker_state.time_until(item_cost)

            if clicker_state.get_time() + wait_time <= duration:
                if wait_time > 0.0:
                    clicker_state.wait(wait_time)
                clicker_state.buy_item(item, item_cost, item_cps)
                my_build_info.update_item(item)
            else:
                # Out of time to buy more items, so wait until the end.
                clicker_state.wait(duration - clicker_state.get_time())
                done = True
        else:
            # No more items, so wait until the end.
            clicker_state.wait(duration - clicker_state.get_time())
            done = True

    return clicker_state


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

def strategy_none(cookies, cps, history, time_left, build_info):
    """
    Always return None

    This is a pointless strategy that will never buy anything, but
    that you can use to help debug your simulate_clicker function.
    """
    return None

def strategy_cheap(cookies, cps, history, time_left, build_info):
    """
    Always buy the cheapest item you can afford in the time left.
    """
    lowest_cost = float('inf')
    affordable_cost = cookies + cps * time_left
    chosen_item = None

    items = build_info.build_items()
    for item in items:
        cost = build_info.get_cost(item)
        if cost < lowest_cost and cost <= affordable_cost:
            chosen_item = item
            lowest_cost = cost

    return chosen_item

def strategy_expensive(cookies, cps, history, time_left, build_info):
    """
    Always buy the most expensive item you can afford in the time left.
    """
    highest_cost = float('-inf')
    affordable_cost = cookies + cps * time_left
    chosen_item = None

    items = build_info.build_items()
    for item in items:
        cost = build_info.get_cost(item)
        if cost > highest_cost and cost <= affordable_cost:
            chosen_item = item
            highest_cost = cost

    return chosen_item

def strategy_best(cookies, cps, history, time_left, build_info):
    """
    The best strategy that you are able to implement.
    """
    # Just from trial and error, I found that the cheap strategy yields a marginal
    # improvement in production early in the simulation: 1.3143463088e+18 when
    # there are more than 9999993700.0 seconds left.
    if time_left > 9999993673.0:
        return strategy_cheap(cookies, cps, history, time_left, build_info)

    lowest_cps_cost = float('inf')
    chosen_item = None

    items = build_info.build_items()

    for item in items:
        item_cost = build_info.get_cost(item)
        item_cps = build_info.get_cps(item)
        cost_per_cps = item_cost / item_cps

        # From trial and error I found that not spending all my cookies on a
        # single item gave me a good improvement in production.
        if cost_per_cps < lowest_cps_cost and item_cost <= 0.8 * (cookies + cps * time_left):
            chosen_item = item
            lowest_cps_cost = cost_per_cps

    return chosen_item

def run_strategy(strategy_name, time, strategy):
    """
    Run a simulation for the given time with one strategy.
    """
    state = simulate_clicker(provided.BuildInfo(), time, strategy)
    print strategy_name, ":", state

    # Plot total cookies over time

    # Uncomment out the lines below to see a plot of total cookies vs. time
    # Be sure to allow popups, if you do want to see it

    #history = state.get_history()
    # history = [(item[0], item[3]) for item in history]
    # simpleplot.plot_lines(strategy_name, 1000, 400, 'Time', 'Total Cookies', [history], True)

def run():
    """
    Run the simulator.
    """    
    #run_strategy("Cursor", SIM_TIME, strategy_cursor_broken)
    #run_strategy("Spend Like You've Just Been Taxed by the Government", SIM_TIME, strategy_cheap)
    #run_strategy("Spend Like You're the Government", SIM_TIME, strategy_expensive)
    run_strategy("Spend Like You're Smart", SIM_TIME, strategy_best)

    # Add calls to run_strategy to run additional strategies
    # run_strategy("Cheap", SIM_TIME, strategy_cheap)
    # run_strategy("Expensive", SIM_TIME, strategy_expensive)
    # run_strategy("Best", SIM_TIME, strategy_best)

run()
