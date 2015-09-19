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
    # locals
    _merged_list = []
    _trailing_zeroes = []
    _helper_list = []
    _index = 0
    
    # catch empty and singleton lists to avoid 'index out of range' error
    if len(line) < 2:
        return line
    
    # iterate over row|column and split into nums > 0 and nums == 0
    for _num in line:
        if _num == 0:
            _trailing_zeroes.append(_num)
        else:
            _helper_list.append(_num)
    
    # here comes the magic
    while _index < len(_helper_list) - 1:
        if _helper_list[_index] == _helper_list[_index+1]:
            _merged_list.append(_helper_list[_index] + _helper_list[_index+1])
            _trailing_zeroes.append(0)
            _index += 2
        else:
            _merged_list.append(_helper_list[_index])
            _index += 1
            
    # catch remaining singleton _helper_list
    if _index == len(_helper_list) - 1:
        _merged_list.append(_helper_list[_index])
            
    return _merged_list + _trailing_zeroes

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        # replace with your code
        #helper lists for coordinate dict generation
        _uplist =[]
        _downlist = []
        _leftlist = []
        _rightlist = []
        # set grid size
        self._row_max = grid_height
        self._col_max = grid_width
        # generate helper dict with coordinates of starting row|column for traversing
        for _col in range(self._col_max):
            _uplist += [(0, _col)]
            _downlist += [(self._row_max - 1, _col)]
        for _row in range(self._row_max):
            _leftlist += [(_row, 0)]
            _rightlist += [(_row, self._col_max - 1)]
        self._initial_indices = {UP : _uplist,
                                 DOWN : _downlist,
                                LEFT : _leftlist,
                                RIGHT : _rightlist}
        print self._initial_indices
        # build initial game grid
        self.reset()

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        # replace with your code
        self._gamegrid = [[0 for _index in range(self._col_max)] for _index in range(self._row_max)]
        self.new_tile()
        self.new_tile()
        print self._gamegrid

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        # replace with your code
        _return_string = ""
        for _row in range(self._row_max):
            _return_string += "| "
            for _col in range(self._col_max):
                _return_string += str(self._gamegrid[_row][_col]) + " | "
            _return_string += "\n"
        return _return_string

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        # replace with your code
        return self._row_max

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        # replace with your code
        return self._col_max

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # replace with your code
        _gamegrid_before = [_item[:] for _item in self._gamegrid]
        _merger_list =[]
        _merged_list = []
        _add_tiles = False
        
        if direction == "UP" or direction =="DOWN":
            _num_steps = self._row_max
        else:
            _num_steps = self._col_max
            
        _start_cells = self._initial_indices.get(direction)

        _heading = OFFSETS.get(direction)

        for _start_cell in _start_cells:
            for _step in range(_num_steps):
                _row = _start_cell[0] + _step * _heading[0]
                _col = _start_cell[1] + _step * _heading[1]
                print "Processing cell", (_row, _col), 
                print "with value", self._gamegrid[_row][_col]
                _merger_list += [self._gamegrid[_row][_col]]                
            print _merger_list
            _merged_list += merge(_merger_list)
            _merger_list = []
        print _merged_list

        _index = 0
        for _start_cell in _start_cells:
            for _step in range(_num_steps):
                _row = _start_cell[0] + _step * _heading[0]
                _col = _start_cell[1] + _step * _heading[1]
                print "Processing cell", (_row, _col), 
                print "with value", self._gamegrid[_row][_col]
                self._gamegrid[_row][_col] = _merged_list[_index]
                _index += 1
                
        print "Before :", _gamegrid_before
        print "After  :", self._gamegrid
        for _row in range(self._row_max):
            for _col in range(self._col_max):
                if self._gamegrid[_row][_col] != _gamegrid_before[_row][_col]:
                    _add_tiles = True
                    print _add_tiles
                    
        if _add_tiles:
            self.new_tile()
            

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # replace with your code
        _nums = [2,2,2,2,2,2,2,2,2,4]
        _empty_cells = []
        
        for _row in range(self._row_max):
            for _col in range(self._col_max):
                if self._gamegrid[_row][_col] == 0:
                    _empty_cells += [(_row, _col)]
                    
        _index = random.choice(_empty_cells)
        self._gamegrid[_index[0]][_index[1]] = random.choice(_nums)

  
    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        # replace with your code
        if row < 0 or col < 0 or row >= self._row_max or col >= self._col_max:
            return
        self._gamegrid[row][col] = value
        

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        # replace with your code
        if row < 0 or col < 0 or row >= self._row_max or col >= self._col_max:
            return 0
        return self._gamegrid[row][col]


#poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
TwentyFortyEight(5,6)
