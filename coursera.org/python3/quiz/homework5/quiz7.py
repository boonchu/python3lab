#! /usr/bin/env python

"""
Simulator for greedy boss scenario

What happens if your boss is really greedy and will increase your salary by $100 dollar per day
every time you give him $1000 dollars? How fast would your salary increase? Finally, let say that
your boss is both greedy and smart. He wants a bigger bribe every time he increases your salary.

What would happen???

"""

import simpleplot
import math
try:
  import SimpleGUICS2Pygame.codeskulptor as codeskulptor
except ImportError:
  import codeskulptor
codeskulptor.set_timeout(20)

STANDARD = True
LOGLOG = False

# constants for simulation
'''
In your simulator, you should assume that your initial salary is $100 per day and
that each bribe paid to your boss increases your salary by $100 per day.

You can also assume that the cost of the initial bribe is $1000. Your main task is to
complete the body of the function greedy_boss(days_in_simulation, bribe_cost_increment, plot_type)
which takes as input the number of days in the simulation (an integer) and the amount by
which the boss increases the cost of a bribe after each bribe (an integer).
'''

INITIAL_SALARY = 100
SALARY_INCREMENT = 100
INITIAL_BRIBE_COST = 1000

def greedy_boss(days_in_simulation, bribe_cost_increment, plot_type = STANDARD):
    """
    Simulation of greedy boss

    The function greedy_boss() should return the list days_vs_earnings. To signal the start of
    the simulation, the return list days_vs_earnings is initialized with the tuple (0, 0).
    
    Earnings from your daily salary should then accumulate starting at day one and so forth.
    """
    current_day = 0
    total_salary = 0
    savings = 0
    bribe_cost = INITIAL_BRIBE_COST
    salary = INITIAL_SALARY

    # initialize necessary local variables

    # initialize list consisting of days vs. total salary earned for analysis
    days_vs_earnings = [(0, 0)]

    # Each iteration of this while loop simulates one bribe
    while current_day < days_in_simulation:

        # check whether we have enough savings to bribe without waiting
        time_to_bribe = max([0, int(math.ceil((bribe_cost - savings) / float(salary)))]) 

        # advance current_day to day of next bribe (DO NOT INCREMENT BY ONE DAY)
        current_day += time_to_bribe

        # update state of simulation to reflect bribe
        savings += salary * time_to_bribe - bribe_cost
        total_salary += salary * time_to_bribe
        bribe_cost += bribe_cost_increment
        salary += SALARY_INCREMENT

        # update list with days vs total salary earned for most recent bribe
        # use plot_type to control whether regular or log/log plot

        # q4: convert the output of greedy_boss() into Log/Log form by taking the
        # logarithm of both current_day and the total salary earned using 
        # math.log() before they appended to the list days_vs_earnings

        # discussion:
        # https://class.coursera.org/principlescomputing1-004/forum/thread?thread_id=651

        if plot_type == STANDARD:
           days_vs_earnings.append((current_day, total_salary))
        elif plot_type == LOGLOG:
           days_vs_earnings.append((math.log(current_day), math.log(total_salary)))

    return days_vs_earnings


def run_simulations():
    """
    Run simulations for several possible bribe increments

    Examine the case when the cost of a bribe does not increase, 

        i.e; bribe_cost_increment == 0

    Our first task is to check whether the total salary earned is a polynomial function
    of the number of days in this case. To this end, create a Log/Log plot of the output
    of greedy_boss

    """
    plot_type = LOGLOG
    days = 100
    inc_0 = greedy_boss(days, 0, plot_type)
    simpleplot.plot_lines("Greedy boss", 600, 600, "days", "total earnings",
                          [inc_0], False,
                         [ "Bribe increment = 0" ])

if __name__ == '__main__':
    '''
    POC run test suite
    '''
    run_simulations()
