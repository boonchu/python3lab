#! /usr/bin/env python
"""
    https://class.coursera.org/principlescomputing1-004/forum/thread?thread_id=235
    https://class.coursera.org/principlescomputing1-004/forum/thread?thread_id=239

    def move(self, direction):
        # Calcuate the number of steps (number of tiles) in the row or
        # column, based on the direction the tiles are being slid. Use
        # the direction height or width (depending on direction) to
        # determine this.

        # Main loop: iterate through each row or column being slid.
        for initial_tile in self._initial_tiles[direction]:
            # Step through each tile in the current row or column and
            # build a list of all values in that row or column. I used
            # a "for" loop based on the number of steps. In the loop
            # I combine the initial tile, the step number, and the
            # OFFSETS dictionary to walk through each tile in the row
            # or column. The resulting list is the input to your
            # merge() function.

            # Next, merge the list you created above into a new list:
            new_line = merge(line)

            # Now store the merged line into the board. I used another
            # "for" loop, similar to the previous one, to step through
            # each tile in the current row or column, and I change the
            # tile value according to the merged list (new_line).

        # If the board has changed, call new_tile().
        # In my code, I compared "line" with "new_line", and set a boolean
        # variable to "True" if the lines were different (means the board
        # changed). An alternative approach is to save a copy of the board
        # at the top of this function, then compare it to the resulting
        # board to see if the changed.
"""

import random

grid_height = 4
grid_width = 4

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

initial_tiles = {}
grid = []

"""
https://class.coursera.org/principlescomputing1-004/forum/thread?thread_id=393

What is happening is that you are defining a dictionary key and value pair like this:

dict[UP] = something

UP is a global variable that is set to 1, so this is the equivalent of saying:

dict[1] = something

and that's fine. Look at the OFFSETS dictionary (top of your 2048 module) and you 
will see it uses the same keys. This makes it easy in your move() method because all 
you need to do access the dictionary values with the supplied direction parameter that 
is passed into move(). 

Since direction must be UP (1), DOWN (2), LEFT (3) or RIGHT (4), you can just use 
direction as a key to your dictionary and the appropriate initial tile tuples list will 
be accessed.

Sure, if you used strings ( 'UP' ) for the keys, you could make it work:

if direction == UP:
 #do something with self._initial_tiles['UP']
 if direction == DOWN:
   #do something with self._initial_tiles['DOWN']

   But that is a lot more work and unnecessarily complex when you can do this instead:

   #do something with self._initial_tiles[direction]
"""

def set_tiles(width, height):
    """ 
    1. initializes all tiles (columns x rows)
    2. random generates grid
    """
    tiles = {
     UP:    [],
     DOWN:  [],
     LEFT:  [],
     RIGHT: [],
    }
    for col in range(height):
        tiles[UP].append([0, col])
        tiles[DOWN].append([height-1, col])

    for row in range(width):
        tiles[LEFT].append([row, 0])
        tiles[RIGHT].append([row, width-1])
    return tiles

def set_grid(_width, _height):
    return [[random.choice([0, 2, 4]) for col in range(_width)] for row in range(_height)]

def dump_grid(_grid):
    return str([x for x in _grid]).replace("],", "]\n")

def dump_grid2(_grid, _width, _height):
    """
    Return a string representation of the grid for debugging.
    """
    # tile_width is number of digits in largest number in the grid.
    tile_width = len(str(max(map(max, _grid))))
    horizontal_border = '+' + ('-' * (tile_width + 2) + '+') * _width
    row_separator = '|' + ('-' * (tile_width + 2) + '|') * _width
    result = horizontal_border + '\n'

    for row in range(_height):
      row_string = '|'
      for col in range(_width):
        value = _grid[row][col]
        row_string += ' ' + str(value).center(tile_width) + ' |'
      result += row_string + '\n'
      if row < _height - 1:
        result += row_separator + '\n'
      else:
        result += horizontal_border + '\n'

    return result

def merge(line):
    _merge = lambda m:(filter(int,reduce(lambda x,y:x+[y]*(y>0)if x[-1]-y else x[:-1]+[y*2,0],m,[0]))+[0]*len(m))[:len(m)]
    return _merge(line)

def move(direction):
    # saved grid for compare
    saved_grid = str(grid)
    # calculate # of cols according to the direction
    cols = len(initial_tiles[direction])
    # calculate # of rows according to the direction
    if direction == LEFT or direction == RIGHT:
      rows = grid_width
    else:
      rows = grid_height

    # create empty lists
    for item in range(cols):
      list = []
      saved_rows = []
      saved_cols = []
      for step in range(rows):
          row = initial_tiles[direction][item][0] + step * OFFSETS[direction][0]
          saved_rows += [row]
          col = initial_tiles[direction][item][1] + step * OFFSETS[direction][1]
          saved_cols += [col]
          list.append(grid[row][col])
      merged_line = merge(list)
      # use saved row/col to put merged tiles back on the grid
      for step in range(rows):
          grid[saved_rows[step]][saved_cols[step]] = merged_line[step]

    if str(grid) == saved_grid:
      print "*** No moved after merged!!! ***"

print "** initialize tiles **"
initial_tiles = set_tiles(grid_width, grid_height)

print "** starting new grid **"
grid = set_grid(grid_width, grid_height)
print dump_grid2(grid, grid_width, grid_height)
print

move(UP)
print "** UP **"
print dump_grid2(grid, grid_width, grid_height)
print

move(DOWN)
print "** DOWN **"
print dump_grid2(grid, grid_width, grid_height)
print

move(LEFT)
print "** LEFT **"
print dump_grid2(grid, grid_width, grid_height)
print

move(RIGHT)
print "** RIGHT **"
print dump_grid2(grid, grid_width, grid_height)
print
