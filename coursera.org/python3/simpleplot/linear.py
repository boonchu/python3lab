#! /usr/bin/env python

"""
Example of creating a plot using simpleplot
    
Input is a list of point lists (one per function)
Each point list is a list of points of the form 
[(x0, y0), (x1, y1, ..., (xn, yn)]
"""

import simpleplot


# create three sample functions

def f1(x):
    return 2 * x - 3

def f2(x):
    return x + 10

def f3(x):
    return x ** 2 + 2 * x + 1

def f4(x):
    return (x - 1) / (x + 1)


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
    f1_plot = [(x_val, f1(x_val)) for x_val in x_coords]
    f2_plot = [(x_val, f2(x_val)) for x_val in x_coords]
    f3_plot = [(x_val, f3(x_val)) for x_val in x_coords]
    f4_plot = [(x_val, f4(x_val)) for x_val in x_coords]
    
    # plot the list of points
    simpleplot.plot_lines("Plots of three functions", 600, 400, "x", "f(x)",
                         [f1_plot, f2_plot, f3_plot, f4_plot], 
                         True, ["f1", "f2", "f3", "f4"])


    
create_plots(0, 2, .1)
