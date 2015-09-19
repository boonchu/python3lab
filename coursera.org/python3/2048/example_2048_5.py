"""
Clone of 2048 game.
"""

#import poc_2048_gui
import random

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

# To make sure that 90% of the time the new tile is 2
# using random.choice(TOTAL_AVAILABLE_MOVES)
TOTAL_AVAILABLE_MOVES = [2,2,2,2,2,2,2,2,2,4]

def merge(line):
    """
    Helper function that merges a single row or column in 2048
    Function that merges a single row or column in 2048.
    """
    result = slide(line)

    index = 0
    while index < len(result) - 1:
        if result[index] == result[index+1]:
            # It two adjacent numbers are identical,
            # merge them and increment index by 2
            # after adding a 0 in the next place
            result[index] *= 2
            result[index+1] = 0
            index += 2
        else:
            index += 1

    return slide(result)

def slide(line):
    """
    Function that slides the non-zeros in line to the left
    """

    result = [ 0 for dummy_i in range(len(line)) ]
    index = 0
    for num in line:
        if num != 0:
           # Add this num, since it's a non-zero, to result
           result[index] = num
           index += 1
    return result

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self._grid_height = grid_height
        self._grid_width = grid_width
        # initial tiles as described in the wiki
        self._initial_tiles = {
        UP : [ (0,dummy_col) for dummy_col in range(self._grid_width)],
        DOWN : [ (self._grid_height - 1, dummy_col)  for dummy_col in range(self._grid_width)],
        LEFT: [ (dummy_row,0) for dummy_row in range(self._grid_height)],
        RIGHT: [ (dummy_row, self._grid_width -1 ) for dummy_row in range(self._grid_height)]
        }
        # steps will be used for the traverse_grid function
        # It will keep a dictionary of the number of steps to traverse
        # without being OutOfBounds
        self._steps = {
        UP: self._grid_height,
        DOWN: self._grid_height,
        LEFT: self._grid_width,
        RIGHT: self._grid_width
        }
        self._game_over = False
        self.reset()

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """

        #Create a grid of zeros
        self._grid = [[0 for dummy_col in range(self._grid_width)] for dummy_row in range(self._grid_height)]
        # _available_new_tiles will be refilled every 10 moves
        self._available_new_tiles = TOTAL_AVAILABLE_MOVES[:]
        for dummy_i in range(2):
            self.new_tile()
        self._game_over = False

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        return str(self._grid).replace('],', ']\n')

    def get_grid_height(self):
        """
        Get the height of the board.
        """

        return self._grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """

        return self._grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """

        # Check if there are empty tiles available
        for row in self._grid:
            if row.count(0) != 0:
                self._game_over = False
                break
            else:
                self._game_over = True

        # If empty tiles are not available, game over
        if self._game_over == True:
            print "Sorry Game Over, Board Full"
            print self.__str__()
            return None

        # New tiles won't be needed for illegal moves
        new_tiles_needed = False

        for tile in self._initial_tiles[direction]:
            old_tiles = self.traverse_grid(tile, OFFSETS[direction], self._steps[direction])
            tiles = merge(old_tiles)
            if old_tiles != tiles:
                # The old row and the new row are different after the merge
                # New tile will be needed
                new_tiles_needed = True
            self.set_grid(tile, OFFSETS[direction], tiles)

        if new_tiles_needed == True:
            self.new_tile()

    def traverse_grid(self, start_cell, direction, num_steps):
        """
        Function that iterates through the cells in a grid
        in a linear direction

        Both start_cell is a tuple(row, col) denoting the
        starting cell

        direction is a tuple that contains difference between
        consecutive cells in the traversal

        Returns a list of elements
        """
        elements = []

        for step in range(num_steps):
            row = start_cell[0] + step * direction[0]
            col = start_cell[1] + step * direction[1]
            elements.append(self._grid[row][col])

        return elements

    def set_grid(self, start_cell, direction, elements):
        """
        Function that takes a list of new elements and replaces
        it with old elements starting from start_cell towards the
        given direction
        """

        for step in range(len(elements)):
            row = start_cell[0] + step * direction[0]
            col = start_cell[1] + step * direction[1]
            self._grid[row][col] = elements[step]

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """

        if len(self._available_new_tiles) == 0:
            # Refill the _available_new_tiles after 10 moves
            self._available_new_tiles = TOTAL_AVAILABLE_MOVES[:]

        while True:
            # Checks for 0 in a random row and column
            row = random.randrange(self._grid_height)
            col = random.randrange(self._grid_width)
            if self._grid[row][col] == 0:
                break

        new_tile = random.choice(self._available_new_tiles)
        # Remove the selected tile from _available_new_tiles
        self._available_new_tiles.remove(new_tile)
        self._grid[row][col] = new_tile

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        if row >= 0 and row < self.get_grid_height():
            if col >= 0 and col < self.get_grid_width():
                # Only set if the row and column are ok
                self._grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        if row >= 0 and row < self.get_grid_height():
            if col >= 0 and col < self.get_grid_width():
                # only return if the row and column are ok
                return self._grid[row][col]


#poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
