#! /usr/bin/env python
"""
TwentyFortyEight Game
Principle of Computing Part 1
Boonchu Ngampairoijpibul
Date: 09/10/2015
"""

import random
import sys
import poc_2048_gui

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

    - if the line contains one element or less, return the line (nothing to merge here!)
    - if the first element is zero, merge the line from the second element, and add a zero at the end
    - if the second element is zero, merge the line without this zero, and add a zero at the end
    - if the first element is equal to the second element, add these two elements, and add them to the merge of the rest.
    - if none of the above, return the first element of the line + the merge of the rest

    How many lines did your implementation of 2048 (merge) take?
    https://class.coursera.org/principlescomputing1-004/forum/thread?thread_id=87

    Here is how I first did it in 7 lines for those who are interested (as Eric in a message above).
    First line: Create a list with only the non zero values of the original list.
    Lines 2 to 5: A for loop where I merge tiles.
    Lines 6: Same thing as first line (except I don't take the values from the original list again).
    Lines 7: I return the list, with eventual additional zeros at the end if the list isn't long enough.

    Example:
    line = [2, 2, 0, 8]

      lst = [2, 2, 8] (filter)
      lst = [4, 0, 8] (for loop)
      lst = [4, 8] (filter)
      return [4, 8] + 2 * [0] = [4, 8, 0, 0] (zero padding)
    '''
    lst = _zero_clean(line)
    for value in xrange(len(lst)):
        if value + 1 > len(lst) - 1:
            break
        if lst[value] == lst[value+1]:
           lst[value] *= 2
           lst[value+1] = 0
    lst = _zero_clean(lst)

    return lst + (len(line)-len(lst))*[0]

def cmp_list(temp1, temp2):
    """
    compare temp1 and temp2 array
    """
    if [v1 for (v1, v2) in zip(temp1, temp2) if v1 != v2 ]:
      return False
    else:
      return True

class CustomGUI(poc_2048_gui.GUI):
    """
    Class extension from GUI poc 2048
    https://class.coursera.org/principlescomputing1-004/forum/thread?thread_id=104
    """
    def __init__(self, game):
        pass

class TwentyFortyEight:
    """
    TwentyFortyEight(object): class
    """

    def __init__(self, grid_height, grid_width):
        """
        __init__(self, grid_height, grid_width): This method takes the height and width of the
        grid and creates the initial 2048 board. You should store the height and width of the
        grid for use in other methods and then call the reset method to create an initial grid
        of the proper size.
        """
        self._grid_height = grid_height
        self._grid_width = grid_width
        self._grid = list()
        # game GUI call reset() at def start()
        # https://class.coursera.org/principlescomputing1-004/forum/thread?thread_id=210
        self.reset()


    def reset(self):
        """
        reset(self): This method should create a grid of height x width zeros and then use the new_tile
        method to add two initial tiles. This method will be called by __init__ to create the initial
        grid. It will also be called by the GUI to start a new game, so the point of this method is
        to reset any state of the game, such as the grid, so that you are ready to play again.

        Reset the game so the grid is empty except for two initial tiles.
        https://class.coursera.org/principlescomputing1-004/forum/thread?thread_id=168

        Grid Representation
        https://class.coursera.org/principlescomputing1-004/wiki/grids

        Given a square, we can store the index associated with a square as the tuple (row,col) in Python.
        Then, we can represent some relevant property of that square as the entry cells[row][col] in
        the 2D list cells. Note the expression cells[row] returns a 1D list corresponding to a row of the grid.
        We can initialize this 2D list via the code fragment:

        cells = [ [... for col in range(grid_width)] for row in range(grid_height)]

        """
        self._grid = [[0 + 0 for _ in range(self._grid_width)] for _ in range(self._grid_height)]
        self.new_tile()
        self.new_tile()


    def __str__(self):
        """
        __str__(self): This method should return a human readable string representing your 2048 board.
        You may format this string however you would like. This method will be helpful to you as you
        develop and debug your code and will be used by OwlTest to display your game board when there
        are errors.
        Run several example calls of traverse_grid()
        """
        return str([x for x in self._grid]).replace("],", "]\n")

    def get_grid_height(self):
        """
        get_grid_height(self): This method should return the height of the grid. It will be used by the
        GUI to determine the size of the board.
        """
        return self._grid_height

    def get_grid_width(self):
        """
        get_grid_width(self): This method should return the width of the grid. It will be used by the
        GUI to determine the size of the board.
        """
        return self._grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        first create an initial list for the directions, as I have to reshape the list to
        match the merge fucntion then given the direction UP etc, reconstruct the list of grids
        """
        saved_grid = self._grid
        if direction == UP:

            # 90 degrees clockwise
            self._grid = zip(*self._grid)[::-1]
            self._grid = [list(row) for row in self._grid]
            self._grid = [ merge(row) for row in self._grid ]

            # 270 degrees clockwise
            self._grid = zip(*self._grid)[::-1]
            self._grid = zip(*self._grid)[::-1]
            self._grid = zip(*self._grid)[::-1]
            self._grid = [list(row) for row in self._grid]
            # print self._grid
        elif direction == DOWN:

            ## 270 degrees clockwise
            self._grid = zip(*self._grid)[::-1]
            self._grid = zip(*self._grid)[::-1]
            self._grid = zip(*self._grid)[::-1]
            self._grid = [list(row) for row in self._grid]
            self._grid = [ merge(row) for row in self._grid ]

            ## 90 degrees clockwise
            self._grid = zip(*self._grid)[::-1]
            self._grid = [list(row) for row in self._grid]
            # print self._grid
        elif direction == RIGHT:

            ## 180 degrees clockwise
            self._grid = zip(*self._grid)[::-1]
            self._grid = zip(*self._grid)[::-1]
            self._grid = [list(row) for row in self._grid]
            self._grid = [ merge(row) for row in self._grid ]

            ## 180 degrees clockwise
            self._grid = zip(*self._grid)[::-1]
            self._grid = zip(*self._grid)[::-1]
            self._grid = [list(row) for row in self._grid]
            # print self._grid
        else:
            self._grid = [ merge(row) for row in self._grid ]
            # print self._grid
            
        # https://class.coursera.org/principlescomputing1-004/forum/thread?thread_id=208
        # Basically you add a tile each time you press one of the arrow keys. In terms of
        # programming: You add a tile each time you make a call to 'move'. Just be sure
        # to add the tile after calls to 'merge', NOT before!
        # 
        # This goes on until all the grid squares have numbers in them, and none of them
        # can be merged, game over.
        # 
        # Ronaldo C. G. de Souza replied:
        # i think the error is because an UP on this configuration shouldn't change anything
        # (which is what OWL is expecting) but you are adding a tile, which should only be
        # done if there's change on the board.
        # 
        # Cannot generate a new tile as long as there is not tile that is moving.
        if not cmp_list(saved_grid, self._grid):
            self.new_tile()

    def new_tile(self):
        """
        new_tile(self): This method should randomly select an empty grid square (one
        that currently has a value of 0) if one exists and place a new tile in that
        square.

        The new tile should have the value 2 90% of the time and the value 4 10% of
        the time. You should implement this by selecting a tile randomly with that
        proportion, not by guaranteeing that every 10th tile is a 4.

        https://class.coursera.org/principlescomputing1-004/forum/thread?thread_id=133

        https://class.coursera.org/principlescomputing1-004/forum/thread?thread_id=174
        """
        random_row = random.randint(0, self._grid_width - 1)
        random_col = random.randint(0, self._grid_height - 1)
        random_value = random.choice([2] * 9 + [4] * 1)

        # need to check if there is at least one empty position to place it
        if 0 in [num for elem in self._grid for num in elem]:
            # new tile can be placed in empty space only
            if self.get_tile(random_col, random_row) == 0:
                self.set_tile(random_col, random_row, random_value)
            else:
                self.new_tile()
        else:
            pass

    def set_tile(self, row, col, value):
        """
        set_tile(self, row, col, value): This method should set the tile at position (row,col) in
        the grid to value. This method will be helpful to you as you test your code with different
        configurations and will be used by OwlTest for the same purpose. Note that the rows of the
        grid are indexed from top to bottom starting at zero while the columns are indexed from
        left to right starting at zero.

        Set the tile at position row, col to have the given value.
        """
        self._grid[row][col] = value

    def get_tile(self, row, col):
        """
        get_tile(self, row, col): This method should return the value of the tile at position (row,col)
        in the grid. This method will be used by the GUI to draw the game board and by OwlTest to check
        your code.

        Return the value of the tile at position row, col.
        """
        return self._grid[row][col]

def run_first_test(rows, cols, moves):
    """
    Start a game using a "rows" x "cols" board. Then make "moves"
    random moves, displaying the board after each move.
    """
    directions = { UP:"up", DOWN:"down", LEFT:"left", RIGHT:"right" }

    game = TwentyFortyEight(rows, cols)

    # Display initial board
    print "Start of game:"
    print str(game)

    # Make some random moves, showing the board after each move.
    for move_number in range(moves):
        move = random.choice([UP, DOWN, LEFT, RIGHT])
        print
        print "Move:", move_number + 1, "- Sliding tiles", directions[move]
        game.move(move)
        print str(game)

def run_second_test():
    """
    Simulate the test from CodeSkulptor
    """
    print "Start of second test: "
    # sample test 2
    print "1st test with obj.reset() from 2x2 (expected 2 new tiles):"
    obj = TwentyFortyEight(2, 2)
    obj.reset()
    alist = [[0,0], [0, 0]]
    if not cmp_list(obj._grid, alist):
        print "Passed "
    else:
        print obj
        print "Expected two new tiltes"
        sys.exit(1)

    print "2nd test with obj.set_tile() from 4x4 (tiles moved):"
    obj = TwentyFortyEight(4, 4)
    obj.set_tile(0, 0, 2)
    obj.set_tile(0, 1, 0)
    obj.set_tile(0, 2, 0)
    obj.set_tile(0, 3, 0)
    obj.set_tile(1, 0, 0)
    obj.set_tile(1, 1, 2)
    obj.set_tile(1, 2, 0)
    obj.set_tile(1, 3, 0)
    obj.set_tile(2, 0, 0)
    obj.set_tile(2, 1, 0)
    obj.set_tile(2, 2, 2)
    obj.set_tile(2, 3, 0)
    obj.set_tile(3, 0, 0)
    obj.set_tile(3, 1, 0)
    obj.set_tile(3, 2, 0)
    obj.set_tile(3, 3, 2)
    obj.move(UP)
    alist = [[2, 2, 2, 2], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    if not cmp_list(obj._grid, alist):
        print "Passed "
    else:
        print obj
        print "Expected: \n" + str([row for row in alist]).replace("],", "]\n")
        sys.exit(1)

    print "3rd test with obj.set_tile() from 4x4 (no tiles move):"
    obj = TwentyFortyEight(4, 4)
    obj.set_tile(0, 0, 2)
    obj.set_tile(0, 1, 4)
    obj.set_tile(0, 2, 8)
    obj.set_tile(0, 3, 16)
    obj.set_tile(1, 0, 16)
    obj.set_tile(1, 1, 8)
    obj.set_tile(1, 2, 4)
    obj.set_tile(1, 3, 2)
    obj.set_tile(2, 0, 0)
    obj.set_tile(2, 1, 0)
    obj.set_tile(2, 2, 8)
    obj.set_tile(2, 3, 16)
    obj.set_tile(3, 0, 0)
    obj.set_tile(3, 1, 0)
    obj.set_tile(3, 2, 4)
    obj.set_tile(3, 3, 2)
    obj.move(UP)
    alist = [[2, 4, 8, 16], [16, 8, 4, 2], [0, 0, 8, 16], [0, 0, 4, 2]]
    if cmp_list(obj._grid, alist):
        print "Passed "
    else:
        print obj
        print "Expected: \n" + str([row for row in alist]).replace("],", "]\n")
        sys.exit(1)

run_first_test(5, 4, 20)
run_second_test()

TFE = TwentyFortyEight(4, 4)
poc_2048_gui.run_gui(TFE)
