#! /usr/bin/env python

"""
Given a 4x4 grid, what values for start_cell and direction would cause traverse_grid to
traverse the diagonal of grid connecting the lower right tile to the upper left tile?
"""

GRID_HEIGHT = 4
GRID_WIDTH = 4

# Create a rectangular grid using nested list comprehension 
# Inner comprehension creates a single row
EXAMPLE_GRID = [[row + col for col in range(GRID_WIDTH)]
                           for row in range(GRID_HEIGHT)]

def traverse_grid(start_cell, direction, num_steps):
    """
    Function that iterates through the cells in a grid
    in a linear direction
    
    Both start_cell is a tuple(row, col) denoting the
    starting cell
    
    direction is a tuple that contains difference between
    consecutive cells in the traversal
    """
    
    for step in range(num_steps):
        row = start_cell[0] + step * direction[0]
        col = start_cell[1] + step * direction[1]
        print "Processing cell", (row, col), 
        print "with value", EXAMPLE_GRID[row][col] 

def run_example():
    """
    Run several example calls of traverse_grid()
    """
    print "Print out values in grid"
    for row in range(GRID_HEIGHT):
        print EXAMPLE_GRID[row]
    print
    
    print " traverse the diagonal of grid upper left to lower right"
    traverse_grid((0, 0), (1, 1), GRID_WIDTH)
    print

    print " traverse down of grid upper right to lower right"
    traverse_grid((3, 0), (0, 1), GRID_WIDTH)
    print

    print " traverse down of grid lower right to upper left"
    traverse_grid((3, 3), (-1, -1), GRID_WIDTH)
    print
    
run_example()
