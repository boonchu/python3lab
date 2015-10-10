#! /usr/bin/env python 
"""
Cookie Clicker Simulator
"""

import simpleplot
import math

# Used to increase the timeout, if necessary
#import codeskulptor
#codeskulptor.set_timeout(40)

import poc_clicker_provided as provided

# Constants
SIM_TIME = 10000000000.0

class ClickerState:
    """
    Simple class to keep track of the game state.
    """
    
    def __init__(self):
        """
        Initialise class
        """

        # The total number of cookies produced throughout the entire game
        self._total_cookies = 0.0
        # The current number of cookies you have
        self._current_cookies = 0.0
        # The current time (in seconds) of the game
        self._current_time = 0.0
        # The current CPS
        self._current_cps = 1.0      
        # history (time, item bought (or None), item cost, 
        #                        total cookies produced by that time)
        self._history = [(0.0, None, 0.0, 0.0)]
        
    def __str__(self):
        """
        Return human readable state
        """
        return "Time: " + str(self._current_time) \
                + "\nCurrent Cookies: " + str(self._current_cookies) \
                + "\nCPS: " + str(self._current_cps) \
                + "\nTotal Cookies: " + str(self._total_cookies) 
                
    def print_history(self):
        """
        Human readable format for history
        """
        return "\nHistory (length: " + str(len(self._history)) + "):\n" \
                + str([_item for _item in self._history]).replace("),", ")\n")
 
    def get_cookies(self):
        """
        Return current number of cookies 
        """
        return self._current_cookies
    
    def get_cps(self):
        """
        Get current CPS
        """
        return self._current_cps
    
    def get_time(self):
        """
        Get current time
        """
        return self._current_time
    
    def get_history(self):
        """
        Return history list
        """
        return list(self._history)

    def time_until(self, cookies):
        """
        Return time until you have the given number of cookies
        """
        return max(math.ceil((cookies-self._current_cookies)/self._current_cps),0.0)
    
    def wait(self, time):
        """
        Wait for given amount of time and update state
        """
        if time > 0.0:
            self._current_time += time
            self._current_cookies += time * self._current_cps
            self._total_cookies += time * self._current_cps
    
    def buy_item(self, item_name, cost, additional_cps):
        """
        Buy an item and update state
        """
        if cost <= self._current_cookies:
            self._current_cookies -= cost
            self._current_cps += additional_cps
            self._history.append((self._current_time,
                                 item_name,
                                 float(cost),
                                 self._total_cookies))

    
def simulate_clicker(build_info, duration, strategy):
    """
    Function to run a Cookie Clicker game for the given
    duration with the given strategy.  Returns a ClickerState
    object corresponding to the final state of the game.
    """
    
    my_build_info = build_info.clone()
    my_clicker = ClickerState()
    
    while True:
        # Check the current time and break out of the loop 
        # if the duration has been passed.
        if my_clicker.get_time() > duration:
            break
         
        # Call the strategy function with the appropriate 
        # arguments to determine which item to purchase next. 
        # If the strategy function returns None, you should 
        # break out of the loop, as that means no more 
        # items will be purchased.
        time_left = duration - my_clicker.get_time()
        next_purchase = strategy(my_clicker.get_cookies(), 
                                 my_clicker.get_cps(), 
                                 my_clicker.get_history(), 
                                 time_left, 
                                 my_build_info)
        if next_purchase == None:
            break
        
        # Determine how much time must elapse until it is 
        # possible to purchase the item. If you would have 
        # to wait past the duration of the simulation to 
        # purchase the item, you should end the simulation.
        cookies_needed = my_build_info.get_cost(next_purchase)
        time_needed = my_clicker.time_until(cookies_needed)
        if time_left < time_needed:
            break
        
        # Wait until that time.
        my_clicker.wait(time_needed)
        
        # Buy the item.
        my_clicker.buy_item(next_purchase, 
                            cookies_needed, 
                            my_build_info.get_cps(next_purchase))
        
        # Update the build information. 
        my_build_info.update_item(next_purchase)
        
    # Continue accumulating cookies until duration
    time_left = duration - my_clicker.get_time()
    my_clicker.wait(time_left)
        
    return my_clicker


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

    list_of_items = build_info.build_items()
    item_cost = float("inf")
    for item in list_of_items:
        if build_info.get_cost(item) < item_cost:
            item_cost = build_info.get_cost(item)
            item_to_buy = item

    cookies_needed = item_cost - cookies
    time_required = cookies_needed / cps
    if time_required > time_left:
        return None
    
    return item_to_buy

def strategy_expensive(cookies, cps, history, time_left, build_info):
    """
    Always buy the most expensive item you can afford in the time left.
    """

    total_cookies = cookies + cps * time_left
    
    list_of_items = build_info.build_items()
    item_cost = float("-inf")
    item_to_buy = None
    
    for item in list_of_items:
        if build_info.get_cost(item) > item_cost and \
           build_info.get_cost(item) <= total_cookies:
            item_cost = build_info.get_cost(item)
            item_to_buy = item
    
    return item_to_buy

def strategy_best(cookies, cps, history, time_left, build_info):
    """
    The best strategy that you are able to implement.
    """
    
    next_item = [((build_info.get_cost(item) \
                   * (cps + build_info.get_cps(item)) \
                   / build_info.get_cps(item),
                 item)) 
                 for item in build_info.build_items()]
    return min(next_item)[1]
        
def run_strategy(strategy_name, time, strategy):
    """
    Run a simulation for the given time with one strategy.
    """
    state = simulate_clicker(provided.BuildInfo(), time, strategy)
    print "\n",strategy_name, ":", state

    # Plot total cookies over time

    # Uncomment out the lines below to see a plot of total cookies vs. time
    # Be sure to allow popups, if you do want to see it

#    history = state.get_history()
#    history = [(item[0], item[3]) for item in history]
#    simpleplot.plot_lines(strategy_name, 1000, 400, 'Time', 'Total Cookies', [history], True)

def run():
    """
    Run the simulator.
    """    
    run_strategy("Cursor", SIM_TIME, strategy_cursor_broken)

    # Add calls to run_strategy to run additional strategies
    run_strategy("Cheap", SIM_TIME, strategy_cheap)
    run_strategy("Expensive", SIM_TIME, strategy_expensive)
    run_strategy("Best", SIM_TIME, strategy_best)
    
run()
