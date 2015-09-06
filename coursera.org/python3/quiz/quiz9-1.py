#! /usr/bin/env python

"""
Create a rectagular grid and iterate through
a subset of its cells in a specified direction
If running this code snippet prints 13 in the console,
what are the non-negative values of row and col?
"""

GRID_WIDTH  = 6
GRID_HEIGHT = 4

# Create a rectangular grid using nested list comprehension 
# Inner comprehension creates a single row
EXAMPLE_GRID = [ [row + col for col in range(GRID_WIDTH)] for row in range(GRID_HEIGHT)]

def run_example():
    """
    Run several example calls of traverse_grid()
    """
    print "Print out values in grid"
    for row in range(GRID_HEIGHT):
        print EXAMPLE_GRID[row]
    print
    
run_example()
