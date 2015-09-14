#! /usr/bin/env python
""" 
Program that computes mystery number
"""

import math
import random
import simpleplot

def inside_unit_circle(point):
    """
    Compute distance of point from origin
    """
    distance = math.sqrt(point[0] ** 2 + point[1] ** 2)
    return distance < 1


def estimate_mystery(num_trials):
    """
    Main function
    """
    num_inside = 0

    for dumm_idx in range(num_trials):
        new_point = [2 * random.random() - 1, 2 * random.random() - 1]
        if inside_unit_circle(new_point):
            num_inside += 1

    return float(num_inside) / num_trials

def run():
    """
    Run Monte Carlo simulations with different numbers
    of trials to estimate the expectation that you will
    get 3-of-a-kind when rolling 5 dice.

    Actual probability of 3-of-a-kind: .1929
    """
    trial_sizes = [
        10, 100, 1000, 10000, 20000, 30000, 40000, 50000, 60000,
        70000, 80000, 90000, 100000, 200000, 300000, 400000, 500000, 
        600000, 700000, 800000, 900000, 1000000, 1100000, 1200000
    ]
    estimates = []
    for ntrials in trial_sizes:
        estimates.append((ntrials, estimate_mystery(ntrials) * 4))
    for ntrials, est in estimates:
        print ntrials, ":", est

    log_estimates = [(math.log(ntrials, 10), est) for ntrials, est in estimates]
    simpleplot.plot_lines("Estimate Mystery", 400, 300, "Log(Trials)", "Expectation", [log_estimates], False, ["log_estimates"])

run()
