"""
Clone of 2048 game.

@author Miguel Alejandro Moreno Barrientos, 2015

http://www.codeskulptor.org/#user40_ntyd9O4ZQtVJss3_3.py
"""

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


######################################################
## TwentyFortyEight class
######################################################
class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self.__grid_height = grid_height
        self.__grid_width = grid_width
        #self.reset()   # reset is called in the original GUI

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self.__score = self.__moves = 0
        self.__game_over = None
        self.__matrix = [ [0] * self.get_grid_width()
                          for _ in range( self.get_grid_height() ) ]
        self.new_tile()
        self.new_tile()
        self.__max_tile = self.get_current_max_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        return "\n".join( str( self.get_row( row ) )
                          for row in range( self.get_grid_height() ) )

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self.__grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self.__grid_width
    
    def get_score( self ):
        """
        Get score.
        """
        return self.__score
    
    def get_max_tile( self ):
        """
        Get max tile.
        """
        return self.__max_tile
    
    def get_current_max_tile( self ):
        """
        Get current max tile.
        """
        return max( self.get_tile( row, col )
                    for row in range( self.get_grid_height() )
                    for col in range( self.get_grid_width() ) )
    
    def get_moves( self ):
        """
        Get number of moves
        """
        return self.__moves
    
    def get_row( self, row ):
        """
        Get a grid row
        Note: manage this list doesn't modify grid
        """
        return [ self.get_tile( row, col ) 
                 for col in range( self.get_grid_width() ) ]
    
    def get_column( self, col ):
        """
        Get a grid row
        Note: manage this list doesn't modify grid
        """
        return [ self.get_tile( row, col ) 
                 for row in range( self.get_grid_height() ) ]        

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.        
        """
        change = False
        score = 0
        width = self.get_grid_width()
        height = self.get_grid_height()        
        start = { UP: [ ( 0, index ) for index in range( width ) ],
                  DOWN: [ ( height - 1, index ) for index in range( width ) ],
                  LEFT: [ ( index, 0 ) for index in range( height ) ],
                  RIGHT: [ ( index, width - 1 ) for index in range( height ) ]
                }        
        length = height if direction in ( UP, DOWN ) else width
        
        for index in range( len( start[direction] ) ):
            start_points = start[direction][index]
            old_list = [ self.get_tile(
                             start_points[0] + step * OFFSETS[direction][0],
                             start_points[1] + step * OFFSETS[direction][1] )
                         for step in range( length ) ]
            merged = type(self).__merge( old_list )
            new_list = merged["result"]
            score += merged["score"]
            if new_list != old_list:
                change = True
                for step in range( len( new_list ) ):
                    self.set_tile(
                        start_points[0] + step * OFFSETS[direction][0],
                        start_points[1] + step * OFFSETS[direction][1],
                        new_list[ step ] )
        
        # grid has changed, check game over, update moves, score, max tile and add a new tile
        if change:
            self.__moves += 1
            self.__score += score
            self.new_tile()
            max_tile = self.get_current_max_tile()            
            if max_tile > self.__max_tile:
                self.__max_tile = max_tile      
            self.check_game_over()

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        from random import randrange, random

        # new position and value
        pos = randrange( self.__empty_tiles() )
        value = 2 if random() < 0.9 else 4
        
        # find 'pos' zero
        zero_index = 0  # current zero
        for row in range( self.get_grid_height() ):  
            for col in range( self.get_grid_width() ):
                if self.get_tile( row, col ) == 0:
                    if pos == zero_index:
                        self.set_tile( row, col, value )
                        return
                    zero_index += 1

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self.__matrix[ row ][ col ] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self.__matrix[ row ][ col ]
    
    def is_game_over( self ):
        return self.__game_over
    
    def check_game_over( self ):
        '''
        Check for game over
        '''
        # game over checked previously
        if self.__game_over:  
            return True

        # non full grid
        if self.__empty_tiles() != 0:
            return False

        # check columns for duplicates
        for row in range( self.get_grid_height() ):
            for col in range( 1, self.get_grid_width() ):
                if self.get_tile( row, col - 1 ) == self.get_tile( row, col ):
                    return False
        # check rows for duplicates
        for row in range( 1, self.get_grid_height() ):
            for col in range( self.get_grid_width() ):
                if self.get_tile( row - 1, col ) == self.get_tile( row, col ):
                    return False

        self.__game_over = True
        return True                                                
    
    def __empty_tiles( self ):
        '''
        Get number of zeros in grid
        '''
        zeros = 0
        for row in range( self.get_grid_height() ):
            for col in range( self.get_grid_width() ):
                if self.get_tile( row, col ) == 0:
                    zeros += 1
                    
        return zeros
    
    def __merge( line ):
        """
        Function that merges a single row or column in 2048.
        """
        result = [ 0 for _ in line ]
        index = -1  # result index
        score = 0
        merge_tiles = False  # check if tiles can be merged in next iteration 

        for item in line:
            # skip zeros
            if item != 0:
                # add a new tile because current and previous tiles can't be merged
                if not merge_tiles:
                    index += 1
                    result[index] = item
                    merge_tiles = True
                # add a new tile because current and previous tiles are not equals
                elif item != result[index]:
                    index += 1
                    result[index] = item
                # merge current tile and previous
                else:
                    result[index] <<= 1
                    score += result[index]
                    merge_tiles = False

        return { "score": score, "result": result }

    
######################################################
## Config game engine
######################################################
GRID_SIZE = 4, 4
GAME_ENGINE = TwentyFortyEight( *GRID_SIZE )    


######################################################
## Modify painter
######################################################
# get original painter function
POC_2048_DRAW = poc_2048_gui.GUI.draw

# new painter function
def draw( obj, canvas ):
    '''
    Modified draw
    '''
    POC_2048_DRAW( obj, canvas )
    
    text = "Score: %i" % GAME_ENGINE.get_score()
    canvas.draw_text( text, ( 11, 32 ), 24, "black" )
    canvas.draw_text( text, ( 10, 31 ), 24, "#55f" )
    text = "Moves: %i" % GAME_ENGINE.get_moves()
    canvas.draw_text( text, ( 151, 32 ), 24, "black" )
    canvas.draw_text( text, ( 150, 31 ), 24, "lime" )
    text = "Max tile: %i" % GAME_ENGINE.get_max_tile()
    canvas.draw_text( text, ( 301, 32 ), 24, "black" )
    canvas.draw_text( text, ( 300, 31 ), 24, "white" )
    if GAME_ENGINE.is_game_over():
        text = "<<<Game Over>>>"
        canvas.draw_text( text, ( 52, 202 ), 48, "black" )
        canvas.draw_text( text, ( 50, 200 ), 48, "#ee5" )        
    
# overwrite painter function
poc_2048_gui.GUI.draw = draw


######################################################
## start game gui
######################################################
poc_2048_gui.run_gui( GAME_ENGINE )




#Math notes:
# n = WIDTH * HEIGHT
# - max possible tile = 2^(n+1)


# GUI
#http://www.codeskulptor.org/#poc_2048_gui.py
