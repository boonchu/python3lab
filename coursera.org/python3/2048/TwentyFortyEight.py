#! /usr/bin/env python

"""
TwentyFortyEight Game
Principle of Computing Part 1
Boonchu Ngampairoijpibul
"""

import random
try:
  import poc_2048_gui
except:
  import GUI as poc_2048_gui

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

ZERO = 0

def _zero_clean(line):
    '''
    fill with zero
    '''
    _zero = lambda a: a != 0
    return filter(_zero, line)

def merge(line):
    '''
    merge 2048
    '''
    saved_len = len(line)

    # fill with zero
    line = _zero_clean(line)

    # slide all tiles towards the front by removing empty spaces (ZERO values)
    for tile in xrange(len(line)):
        # hit at the end of list
        if tile + 1 > len(line) - 1:
            break
        # merge 2048 pair
        if line[tile] == line[tile + 1]:
            # double value the first in pair
            line[tile] *= 2
            line[tile + 1] = ZERO

    # slide all the tiles towards the front and fill the rest with zeros
    line = _zero_clean(line)
    while len(line) != saved_len:
        line.append(0)

    return line


class TwentyFortyEight:

    """
    __init__(self, grid_height, grid_width): This method takes the height and width of the
    grid and creates the initial 2048 board. You should store the height and width of the
    grid for use in other methods and then call the reset method to create an initial grid
    of the proper size.
    """

    def __init__(self, grid_height, grid_width):
        """
        __init__
        """

        self.grid_height = grid_height
        self.grid_width = grid_width
        self.grid = list()
        self.reset()
        self.initial_tiles_dict = {}

        # generate dictionary of initial tiles
        # d = {1: 'a', 2: 'b', 3: 'c'}
        #initial_tiles = {UP: [(0, 0), (0, 1), (0, 2), (0, 3)], 
        #                 DOWN: [(3, 0), (3, 1), (3, 2), (3, 3)]}   
        #                 LEFT: [(0, 0), (1, 0), (2, 0), (3, 0)]
        #                 RIGHT: [(0, 3), (1, 3), (2, 3), (3, 3)]   
        #
        up_row = [0 for x in range(self.grid_width)]  # grid_width
        up_col = [x for x in range(self.grid_width)]
        down_row = [self.grid_height-1 for x in range(self.grid_width)]
        down_col = [x for x in range(self.grid_width)]
        left_row = [x for x in range(self.grid_height)]
        left_col = [0 for x in range(self.grid_height)]
        right_row = [x for x in range(self.grid_height)]
        right_col = [self.grid_width-1 for x in range(self.grid_height)]

        self.initial_tiles_dict = {UP: zip(up_row,up_col), 
                        DOWN: zip(down_row,down_col),
                        LEFT: zip(left_row, left_col),
                        RIGHT: zip(right_row, right_col)}


    """
    reset(self): This method should create a grid of height x width zeros and then use the new_tile
    method to add two initial tiles. This method will be called by __init__ to create the initial
    grid. It will also be called by the GUI to start a new game, so the point of this method is
    to reset any state of the game, such as the grid, so that you are ready to play again.
    """

    def reset(self):
        """
        Reset the game so the grid is empty except for two initial tiles.
        """
        self.grid = [[0 + 0 for col in range(self.grid_width)] for row in range(self.grid_height)]

    """
    __str__(self): This method should return a human readable string representing your 2048 board.
    You may format this string however you would like. This method will be helpful to you as you
    develop and debug your code and will be used by OwlTest to display your game board when there
    are errors.
    """

    def __str__(self):
        """
        Run several example calls of traverse_grid()
        """
        return str(self.grid)

    """
    get_grid_height(self): This method should return the height of the grid. It will be used by the
    GUI to determine the size of the board.
    """

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self.grid_height

    """
    get_grid_width(self): This method should return the width of the grid. It will be used by the
    GUI to determine the size of the board.
    """

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self.grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        changed = False
        
        initial_tiles = self.initial_tiles_dict.get(direction)
        #print "initial tiles", initial_tiles
        offset = OFFSETS[direction]

        if direction == UP or direction == DOWN:
            size = self.grid_height
        elif direction == LEFT or direction == RIGHT:
            size = self.grid_width
         
        for tile_index in initial_tiles: 
            
            tile_indices = []
            # iterate through adding offset
            for dummy_i in range(size):
                tile_indices.append(tile_index)
           
                tile_index = [(sum(x)) for x in zip(tile_index,offset)]
                tile_index = tuple(tile_index)
      
            before_merge = []
            for tile_index in tile_indices:
                tile = self.get_tile(tile_index[0], tile_index[1])
                before_merge.append(tile)
            print tile_indices
            
            after_merge = merge(before_merge)

            
            for tile_index, tile_value in zip(tile_indices, after_merge):
                  if tile_value != self.get_tile(tile_index[0], tile_index[1]):
                    self.set_tile(tile_index[0], tile_index[1], tile_value)
                    changed = True
     
        if changed == True:
            self.new_tile()

    """
    new_tile(self): This method should randomly select an empty grid square (one
    that currently has a value of 0) if one exists and place a new tile in that
    square.
    The new tile should have the value 2 90% of the time and the value 4 10% of
    the time. You should implement this by selecting a tile randomly with that
    proportion, not by guaranteeing that every 10th tile is a 4.
    """

    def new_tile(self):
        """
        new_tile(self)
        """
        zero_grid_square = list()
        for row in range(self.grid_height):
            for col in range(self.grid_width):
                if self.grid[row][col] == 0:
                    zero_grid_square.append((row, col))

        rt = ramdom.choice(zero_grid_square)
        self.grid[rt[0]][rt[1]] = random.choice([2, 2, 2, 2, 2, 2, 2, 2, 2, 4])

    """
    set_tile(self, row, col, value): This method should set the tile at position (row,col) in
    the grid to value. This method will be helpful to you as you test your code with different
    configurations and will be used by OwlTest for the same purpose. Note that the rows of the
    grid are indexed from top to bottom starting at zero while the columns are indexed from 
    left to right starting at zero.
    """
    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self.grid[row][col] = value

    """
    get_tile(self, row, col): This method should return the value of the tile at position (row,col)
    in the grid. This method will be used by the GUI to draw the game board and by OwlTest to check
    your code.
    """
    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self.grid[row][col]

import test_suite
test = TwentyFortyEight
test_suite.run_test(test)

tfe = TwentyFortyEight(4, 4)
poc_2048_gui.run_gui(tfe)
