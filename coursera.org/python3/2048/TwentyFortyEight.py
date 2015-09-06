#! /usr/bin/env python

"""
TwentyFortyEight Game
Principle of Computing Part 1
Boonchu Ngampairoijpibul
Date: 09/06/2015
"""

from random import randint

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

        up_lst = []
        down_lst = []
        right_lst = []
        left_lst = []

        for i in range(self.grid_width):
            down_ele = (self.grid_height-1, i)
            down_lst.append(down_ele)
        for j in range(self.grid_height):
            right_ele = (j, self.grid_width - 1)
            left_ele = (j, 0)
            right_lst.append(right_ele)
            left_lst.append(left_ele)

        self.direct = {
            UP:up_lst,
            DOWN:down_lst,
            RIGHT:right_lst,
            LEFT:left_lst
        }


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
        return self.grid

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

        first create an initial list for the directions, as I have to reshape the list to
        match the merge fucntion then given the direction UP etc, reconstruct the list of grids
        """
        offsets = OFFSETS[direction]
        starting_lst = self.direct[direction]

        if direction == 1:
            for i in range(len(starting_lst)):
                starting_grid = starting_lst[i]
                pos_h = starting_grid[0]
                pos_w = starting_grid[1]
                temp_lst = []
                grid_pos = []
                while pos_h < self.grid_height:
                    grid_pos.append((pos_h, pos_w))
                    temp_lst.append(self.grid[pos_h][pos_w])
                    pos_h = pos_h + offsets[0]
                    pos_w = pos_w + offsets[1]
                merge_lst = merge(temp_lst)
                for j in range(len(grid_pos)):
                    self.grid[grid_pos[j][0]][grid_pos[j][1]] = merge_lst[j]
        elif direction == 2:
            for i in range(len(starting_lst)):
                starting_grid = starting_lst[i]
                pos_h = starting_grid[0]
                pos_w = starting_grid[1]
                temp_lst = []
                grid_pos = []
                while pos_h >= 0:
                    grid_pos.append((pos_h, pos_w))
                    temp_lst.append(self.grid[pos_h][pos_w])
                    pos_h = pos_h + offsets[0]
                    pos_w = pos_w + offsets[1]
                merge_lst = merge(temp_lst)
                for j in range(len(grid_pos)):
                    self.grid[grid_pos[j][0]][grid_pos[j][1]] = merge_lst[j]
        elif direction == 3:
            for i in range(len(starting_lst)):
                starting_grid = starting_lst[i]
                pos_h = starting_grid[0]
                pos_w = starting_grid[1]
                temp_lst = []
                grid_pos = []
                while pos_w < self.grid_width:
                    grid_pos.append((pos_h, pos_w))
                    temp_lst.append(self.grid[pos_h][pos_w])
                    pos_h = pos_h + offsets[0]
                    pos_w = pos_w + offsets[1]
                merge_lst = merge(temp_lst)
                for j in range(len(grid_pos)):
                    self.grid[grid_pos[j][0]][grid_pos[j][1]] = merge_lst[j]
        else:
            for i in range(len(starting_lst)):
                starting_grid = starting_lst[i]
                pos_h = starting_grid[0]
                pos_w = starting_grid[1]
                temp_lst = []
                grid_pos = []
                while pos_w >= 0:
                    grid_pos.append((pos_h, pos_w))
                    temp_lst.append(self.grid[pos_h][pos_w])
                    pos_h = pos_h + offsets[0]
                    pos_w = pos_w + offsets[1]
                merge_lst = merge(temp_lst)
                for j in range(len(grid_pos)):
                    self.grid[grid_pos[j][0]][grid_pos[j][1]] = merge_lst[j]
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

        # first select the grid
        # then generate a value either 2 or 4
        pos_0 = []
        for height in range(self.grid_height):
            for width in range(self.grid_width):
                if self.grid[height][width] == 0:
                    pos_0.append((height, width))
        if len(pos_0) == 0:
            message = 'You lose!'
            return message
        else:
            high_end = len(pos_0) - 1
            low_end = 0
            #pos is the postion in pos_0
            pos = pos_0[randint(low_end, high_end)]
            #pos[0] is the height; pos[1] is the width
            #apply it to self.grids, and find the corresponding row and col
            #then generate a value either 2 or 4
            decision_thres = randint(0, 9)
            if decision_thres == 9:
                self.grid[pos[0]][pos[1]] = 4
            else:
                self.grid[pos[0]][pos[1]] = 2

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
