"""
Cookie Clicker Simulator
"""

# import simpleplot

# Used to increase the timeout, if necessary
# import codeskulptor
# codeskulptor.set_timeout(20)

import math

import poc_clicker_provided as provided

# Constants
SIM_TIME = 10000000000.0

class ClickerState:
    """
    Simple class to keep track of the game state.
    """
    
    def __init__(self):
        self._total_cookies = 0.0
        self._current_cookies = 0.0
        self._current_time = 0.0
        self._current_cps = 1.0
        self._history = [(0.0, None, 0.0, 0.0)]
        
        
    def __str__(self):
        """
        Return human readable state
        """
        string = ("\n" + "Time: " + str(self.get_time()) + 
                  "\n" + "Current Cookies: " + str(self.get_cookies()) +
                  "\n" + "CPS: " + str(self.get_cps()) +
                  "\n" + "Total Cookies: " + str(self._total_cookies))
        return string
        
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
        return self._history

    def time_until(self, cookies):
        """
        Return time until you have the given number of cookies
        (could be 0.0 if you already have enough cookies)

        Should return a float with no fractional part
        """
        
        if self.get_cookies() >= cookies:
            return 0.0
        else:
            cookies_needed = cookies - self.get_cookies()
            wait_time = math.ceil( cookies_needed / self.get_cps() )
            return wait_time
    
    def wait(self, time):
        """
        Wait for given amount of time and update state

        Should do nothing if time <= 0.0
        """
        
        if time <= 0.0:
            return
        else:
            self._current_time += float(time)
            cookies_gained = time * self.get_cps()
            self._current_cookies += cookies_gained
            self._total_cookies += cookies_gained
    
    def buy_item(self, item_name, cost, additional_cps):
        """
        Buy an item and update state

        Should do nothing if you cannot afford the item
        """
        
        if self.get_cookies() >= cost:
            self._current_cookies -= cost
            self._current_cps += additional_cps
            log = tuple([self.get_time(),
                         item_name,
                         cost,
                         self._total_cookies])
            # print log
            self._history.append(log)
        else:
            return
   
    
def simulate_clicker(build_info, duration, strategy):
    """
    Function to run a Cookie Clicker game for the given
    duration with the given strategy.  Returns a ClickerState
    object corresponding to the final state of the game.
    """

    # Replace with your code
    
    # clone build info
    build_info_clone = build_info.clone()
    
    # create new clicker object
    clicker = ClickerState()
    
    while 0.0 <= duration:
        # figure out next item based on strategy
        # paramters are:
        # - current number of cookies
        # - current cookies per second (cps)
        # - current history
        # - time remaining from simulation (time_left)
        # - build info
        next_item = strategy(clicker.get_cookies(),
                             clicker.get_cps(),
                             clicker.get_history(),
                             duration,
                             build_info_clone)
        # if next item returns None, break out of loop
        if next_item is None:
            break
        # if next item exists, compute cost in cookies
        next_item_cost = build_info_clone.get_cost(next_item)
        # compute the additional cps of next item
        next_item_cps = build_info_clone.get_cps(next_item)
        # compute time needed to attain next item
        needed_time = clicker.time_until(next_item_cost)
        # if time needed is greater than time remaining,
        # exit loop
        if (needed_time > duration):
            break
        # else, wait until needed time and buy item
        else:
            duration -= needed_time
            clicker.wait(needed_time)
            clicker.buy_item(next_item,
                             next_item_cost,
                             next_item_cps)
            # update build info
            build_info_clone.update_item(next_item)
    
    # wait until duration is over
    clicker.wait(duration)
    
    # return final clicker state
    # time should be equal to duration
    return clicker

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
    Returns String type.
    """
    
    # create list of item costs
    costs = [build_info.get_cost(item) for item in build_info.build_items()]
    # compute minimum cost (cheapest)
    cheapest = min(costs)
    
    # compute cookies generated when time is up
    cookies_generated = cookies + (time_left * cps)

    # return None if no options available
    if cheapest > cookies_generated:
        return None
    else:
        # iterate through every item name in build info
        for item in build_info.build_items():
            # if item cost is equal to cheapest cost, return item name
            if build_info.get_cost(item) == cheapest:
                return item

def strategy_expensive(cookies, cps, history, time_left, build_info):
    """
    Always buy the most expensive item you can afford in the time left.
    """
    
    inventory = build_info.build_items()
    name = None
    most_expensive = float('-inf')
    resource = cookies + (time_left * cps)

    for item in inventory:
        current_cost = build_info.get_cost(item)
        # still enough time to buy at least one more (most expensive) item
        if current_cost <= resource and most_expensive < current_cost:
            # found currently most expensive item, store it temporarly
            most_expensive = current_cost
            name = item
    return name


def strategy_best(cookies, cps, history, time_left, build_info):
    """
    The best strategy that you are able to implement.
    """
    
    cps_per_cookies = [((build_info.get_cps(item) / build_info.get_cost(item)), item)
                       for item in build_info.build_items()]

    # compute minimum cost (cheapest)
    most_efficient = max(cps_per_cookies)
    most_efficient_item = most_efficient[1]
    most_efficient_item_cost = build_info.get_cost(most_efficient_item)
    
    # compute cookies generated when time is up
    cookies_generated = cookies + (time_left * cps)

    # return None if no options available
    if most_efficient_item_cost > cookies_generated:
        return None
    else:
        return most_efficient_item
        
def run_strategy(strategy_name, time, strategy):
    """
    Run a simulation for the given time with one strategy.
    """
    state = simulate_clicker(provided.BuildInfo(), time, strategy)
    print strategy_name, ":", state

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
    run_strategy("Cursor", SIM_TIME, strategy_cursor_broken)

    # Add calls to run_strategy to run additional strategies
    print
    run_strategy("Cheap", SIM_TIME, strategy_cheap)
    
    print
    run_strategy("Expensive", SIM_TIME, strategy_expensive)
    
    print
    run_strategy("Best", SIM_TIME, strategy_best)
    
run()
