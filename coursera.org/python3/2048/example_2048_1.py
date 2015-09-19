"""
Clone of 2048 game.
"""

import poc_2048_gui
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

def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    result = [0] * len(line)
    index = 0

    for num in [num for num in line if num]:
        if result[index] == num:
            result[index] += num
            index += 1
        else:
            index += (result[index] != 0)
            result[index] = num
    return result

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self._height = grid_height
        self._width = grid_width
        self._initial_tiles = self.get_initial_tiles()
        self.reset()

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._grid = [ [0 for _ in range(self._width)]
                          for _ in range(self._height)]
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        # tile_width is number of digits in largest number in the grid.
        tile_width = len(str(max(map(max, self._grid))))
        horizontal_border = '+' + ('-' * (tile_width + 2) + '+') * self._width
        row_separator = '|' + ('-' * (tile_width + 2) + '|') * self._width
        result = horizontal_border + '\n'

        for row in range(self._height):
            row_string = '|'

            for col in range(self._width):
                value = self.get_tile(row, col)
                row_string += ' ' + str(value).center(tile_width) + ' |'

            result += row_string + '\n'

            if row < self._height - 1:
                result += row_separator + '\n'
            else:
                result += horizontal_border + '\n'

        return result

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

        # This is used at the bottom of the function to determine if
        # it is possible to add a new tile.
        board_has_changed = False

        # Calcuate the number of steps (number of tiles) in the row or
        # column, based on the direction the tiles are being slid.
        step_direction = OFFSETS[direction]

        num_steps = self._height * abs(step_direction[0]) + \
                    self._width * abs(step_direction[1])

        # This loop iterates through each row or column being slid.
        for initial_tile in self._initial_tiles[direction]:
            line = []

            # Step through each tile in the current row or column and
            # build a list of all values in that row or column.
            for step in range(num_steps):
                row = initial_tile[0] + step * step_direction[0]
                col = initial_tile[1] + step * step_direction[1]
                line.append(self.get_tile(row, col))

            new_line = merge(line)

            if new_line != line:
                board_has_changed = True

            # Now store the merged line into the board
            for step in range(num_steps):
                row = initial_tile[0] + step * step_direction[0]
                col = initial_tile[1] + step * step_direction[1]
                self.set_tile(row, col, new_line[step])

        if board_has_changed:
            self.new_tile()

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        empty_tiles = self.get_empty_tiles()

        if len(empty_tiles) > 0:
            if random.random() < 0.9:
                num = 2
            else:
                num = 4

            tile = random.choice(empty_tiles)
            self.set_tile(tile[0], tile[1], num)

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

    def get_empty_tiles(self):
        """
        Return a list of (row, col) tuples for each empty tile.
        An empty list is returned if there are no empty tiles.
        """
        result = []

        for row in range(self._height):
            for col in range(self._width):
                if self._grid[row][col] == 0:
                    result.append((row, col))

        return result

    def get_initial_tiles(self):
        """
        Helper function to return a dictionary that represents the initial
        tiles for the directions UP, DOWN, LEFT and RIGHT
        """
        initial_tiles = {}

        initial_tiles[UP] =[(0, col) for col in range(self._width)]
        initial_tiles[DOWN] = [(self._height - 1, col) for col in range(self._width)]
        initial_tiles[LEFT] = [(row, 0) for row in range(self._height)]
        initial_tiles[RIGHT] = [(row, self._width - 1) for row in range(self._height)]

        return initial_tiles

poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
