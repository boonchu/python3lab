"""
Clone of 2048 game.
"""

from random import random, choice
import poc_2048_gui

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    lst = [0] * len(line) # we start with a 0-filled list.
    pos = 0     # index position in the new list
    pvl = 0     # we keep the previous value
    for val in line:
        if val: # we only care about the non zero values.
            if not pvl:        # this tile is empty
                lst[pos] = val # let's fill with val
                pvl = val
            elif pvl - val:    # different non zero values?
                pos += 1
                lst[pos] = val # tiles don't merge
                pvl = val
            else:              # same values!
                lst[pos] <<= 1 # it merges!
                pos += 1
                pvl = 0        # next value is 0
    return lst

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self._height = grid_height
        self._width = grid_width
        self.reset()
        # Extracted tiles positions for each direction
        self._tiles_pos = {
            UP: [[(j, i) for j in range(grid_height)] 
                 for i in range(grid_width)],
            DOWN: [[(grid_height - 1 - j, i) for j in range(grid_height)]
                   for i in range(grid_width)],
            LEFT: [[(i, j) for j in range(grid_width)]
                   for i in range(grid_height)],
            RIGHT: [[(i, grid_width - 1 - j) for j in range(grid_width)]
                    for i in range(grid_height)]
        }
        
    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._grid = [[0] * self._width for _ in xrange(self._height)]
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        return str(self._grid)

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        grid = [l[:] for l in self._grid] # Deep copy
        
        # Extract rows or columns and merge them
        for lst in self._tiles_pos[direction]:
            merge_list = merge([self.get_tile(*pos) for pos in lst])
            for pos, val in zip(lst, merge_list):
                self.set_tile(*pos, value = val)
        
        # Any changes?
        if grid != self._grid:
            self.new_tile()
            
        
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # Getting the list of positions of empty tiles
        indices_list = [(i, j) for i, l in enumerate(self._grid) 
                        for j in xrange(len(l)) if not l[j]]
        
        # Filling the the empty tile with a 2 or a 4
        if indices_list:
            self.set_tile(*choice(indices_list), 
                          value = 2 if random() < .9 else 4)
          
    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._grid[row][col] = value
                
    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._grid[row][col]
    
poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
