#! /usr/bin/env python
"""
Cookie Clicker Simulator
"""

import math
import simpleplot
import poc_clicker_provided as provided

# Used to increase the timeout, if necessary
#try:
#  import SimpleGUICS2Pygame.codeskulptor as codeskulptor
#except ImportError:
#  import codeskulptor
#codeskulptor.set_timeout(20)


# Constants
SIM_TIME = 10000000000.0

class ClickerState:
    """
    Simple class to keep track of the game state.

    The ClickerState class must keep track of four things:

    The total number of cookies produced throughout the entire game (this should be initialized to 0.0).
    The current number of cookies you have (this should be initialized to 0.0).
    The current time (in seconds) of the game (this should be initialized to 0.0).
    The current CPS (this should be initialized to 1.0).

    We will track the history as a list of tuples. Each tuple in the list will contain 4 values: a time,
    an item that was bought at that time (or None), the cost of the item, and the total number of cookies
    produced by that time. This history list should therefore be initialized as [(0.0, None, 0.0, 0.0)].

    """

    def __init__(self):
        self._total_cookies = 0.0
        self._current_cookies = 0.0
        self._current_time = 0.0
        self._current_cps = 1.0
        self._item_name = None
        self._item_cost = 0.0
        self._history_list = [(self._current_time, self._item_name, self._item_cost, self._total_cookies)]

    def __str__(self):
        """
        Return human readable state
    
        return the state (possibly without the history list) as a string in a human readable format.
        This is primarily to help you develop and debug your program
        """
        output = "Time: " + str(self.get_time()) +\
        " Current Cookies: " + str(self.get_cookies()) +\
        " CPS: " + str(self.get_cps()) +\
        " Total Cookies: " + str(self._total_cookies) +\
        " History (length: " + str(len(self.get_history())) + "): " + str(self.get_history())
        return output

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
        history_list = self._history_list
        return history_list

    def time_until(self, cookies):
        """
        Return time until you have the given number of cookies
        (could be 0.0 if you already have enough cookies)

        return the number of seconds you must wait until you will have the given number of cookies.
        Remember that you cannot wait for fractional seconds, so while you should return a float it
        should not have a fractional part. 
        """
        if cookies > 0 and cookies >= self._current_cookies:
            return math.ceil((cookies-self._current_cookies)/self._current_cps)
        else:
            return 0.0

    def wait(self, time):
        """
        Wait for given amount of time and update state

        Should do nothing if time <= 0.0

        should "wait" for the given amount of time. This means you should appropriately increase the time,
        the current number of cookies, and the total number of cookies. 
        """
        if time > 0:
            self._current_time += time
            self._current_cookies += self._current_cps * time
            self._total_cookies += self._current_cps * time

    def buy_item(self, item_name, cost, additional_cps):
        """
        Buy an item and update state

        Should do nothing if you cannot afford the item

        should "buy" the given item. This means you should appropriately adjust the current number of cookies,
        the CPS, and add an entry into the history. 
        """
        if self._current_cookies >= cost:
            self._item_name = item_name
            self._item_cost = cost
            self._current_cookies -= cost
            self._current_cps += additional_cps
            _tuple = (self._current_time, self._item_name, self._item_cost, self._total_cookies)
            self._history_list.append(_tuple)


def simulate_clicker(build_info, duration, strategy):
    """
    Function to run a Cookie Clicker game for the given
    duration with the given strategy.  Returns a ClickerState
    object corresponding to the final state of the game.

    simulate_clicker function should take a BuildInfo class, the number of seconds to run the simulation for,
    and a strategy function. Note that simulate_clicker is a higher-order function: it takes a strategy function
    as an argument! 

    For each iteration of the loop, your simulate_clicker function should do the following things:

      - Check the current time and break out of the loop if the duration has been passed.
      - Call the strategy function with the appropriate arguments to determine which item to
      purchase next. If the strategy function returns None, you should break out of the loop,
      as that means no more items will be purchased.
      - Determine how much time must elapse until it is possible to purchase the item. If you
      would have to wait past the duration of the simulation to purchase the item, you should
      end the simulation.
      - Wait until that time.
      - Buy the item.
      - Update the build information.

    """
    _next_purchase = build_info.clone()
    _click = ClickerState()

    while _click.get_time() <= duration:
        _time_left = duration - _click.get_time()
        _item_name = strategy(_click.get_cookies(), _click.get_cps(), _click.get_history(), _time_left, _next_purchase)
        if _item_name == None:
            break
        if _click.time_until(_next_purchase.get_cost(_item_name)) > _time_left:
            break
        else:
            _click.wait(_click.time_until(_next_purchase.get_cost(_item_name)))
            _click.buy_item(_item_name, _next_purchase.get_cost(_item_name), _next_purchase.get_cps(_item_name))
            _next_purchase.update_item(_item_name)

    _click.wait(_time_left)
    return _click

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
    item_list  = build_info.build_items()
    list_costs = map(build_info.get_cost, item_list)
    cheap_index = list_costs.index(min(list_costs))
    cheap_item  = item_list[cheap_index]
    if (cookies + cps * time_left) < list_costs[cheap_index]:
        return None
    else:
        return cheap_item

def strategy_expensive(cookies, cps, history, time_left, build_info):
    """
    Always buy the most expensive item you can afford in the time left.
    """
    list_items  = build_info.build_items()
    list_costs = map(build_info.get_cost, list_items)

    temp_items = list()
    temp_costs = list()
    for idx in xrange(len(list_costs)):
        if list_costs[idx] <= cookies + (cps * time_left):
            temp_items.append(list_items[idx])
            temp_costs.append(list_costs[idx])
    if temp_costs == []:
        return None
    else:
        return temp_items[temp_costs.index(max(temp_costs))]
    

def strategy_best(cookies, cps, history, time_left, build_info):
    """
    The best strategy that you are able to implement.
    """
    list_items  = build_info.build_items()
    list_costs = map(build_info.get_cost, list_items)
    list_cps   = map(build_info.get_cps, list_items)
    list_best  = list()
    for idx in xrange(len(list_items)):
        list_best.append(list_cps[idx]/list_costs[idx])
    return list_items[list_best.index(max(list_best))]

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
    #history = [(item[0], item[3]) for item in history]
    #simpleplot.plot_lines(strategy_name, 1000, 400, 'Time', 'Total Cookies', [history], True, ["Total Cookies"])

def run():
    """
    Run the simulator.
    """
    run_strategy("Cursor", SIM_TIME, strategy_cursor_broken)

    # Add calls to run_strategy to run additional strategies
    run_strategy("Cheap", SIM_TIME, strategy_cheap)
    run_strategy("Expensive", SIM_TIME, strategy_expensive)
    run_strategy("Best", SIM_TIME, strategy_best)

if __name__ == '__main__':
    """
    POC run test suite
    """
    run()
