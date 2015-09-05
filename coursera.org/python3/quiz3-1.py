#! /usr/bin/env python
"""
Example of creating a plot using simpleplot
    
Input is a list of point lists (one per function)
Each point list is a list of points of the form 
[(x0, y0), (x1, y1, ..., (xn, yn)]
"""

import simpleplot
import math


# create three sample functions

def log1(x):
    return math.log( (5 ** 7) ** 0.5, 5) 


def create_plots(begin, end, stride):
    """ 
    Plot the function double, square, and exp
    from beginning to end using the provided stride
    
    The x-coordinates of the plotted points start
    at begin, terminate at end and are spaced by 
    distance stride
    """
    
    # generate x coordinates for plot points
    x_coords = []
    current_x = begin
    while current_x < end:
        x_coords.append(current_x)
        current_x += stride
        
    # compute list of (x, y) coordinates for each function
    log1_plot = [(x_val, log1(x_val)) for x_val in x_coords]

    
    # plot the list of points
    simpleplot.plot_lines("Plots of three functions", 600, 400, "x", "f(x)",
                         [log1_plot], 
                         True, ["log1"])


    
create_plots(0, 2, .1)
