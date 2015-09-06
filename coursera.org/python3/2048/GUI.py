#! /usr/bin/env python

"""
2048 GUI
"""

import os
import math
try:
  import simplegui
  import codeskulptor
except ImportError:
  import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

# Tile Images
IMAGENAME = "assets_2048.png"
TILE_SIZE = 100
HALF_TILE_SIZE = TILE_SIZE / 2
BORDER_SIZE = 45

# Directions
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

import urlparse, urllib

"""
File 2 URL
http://stackoverflow.com/questions/11687478/convert-a-filename-to-a-file-url
"""
def _path2url(path):
    home = os.path.abspath(path)
    return urlparse.urljoin('file:', urllib.pathname2url(home))

class GUI(object):
    """
    Class to run game GUI.
    """

    def __init__(self, game):
        self._directions = {"up": UP, "down": DOWN,
            "left": LEFT, "right": RIGHT}

        url = _path2url(IMAGENAME)
        print url
        self._tiles = simplegui.load_image(url)

        self._game = game
        # print "self._game.get_grid_height(): " + str(self._game.get_grid_height())
        # print "self._game.get_grid_width(): " + str(self._game.get_grid_width())

        self._rows = game.get_grid_height()
        self._cols = game.get_grid_width()
        self._frame = simplegui.create_frame('2048',
           self._cols * TILE_SIZE + 2 * BORDER_SIZE,
           self._rows * TILE_SIZE + 2 * BORDER_SIZE)

        self._frame.add_button('New Game', self.start)
        self._frame.set_keydown_handler(self.keydown)
        self._frame.set_draw_handler(self.draw)
        self._frame.set_canvas_background("#BCADA1")
        self._frame.start()

    def keydown(self, key):
        """
        Keydown handler
        """
        for dirstr, dirval in self._directions.items():
            if key == simplegui.KEY_MAP[dirstr]:
                self._game.move(dirval)
                break

    def draw(self, canvas):
        """
        Draw handler
        """
        for row in range(self._rows):
            for col in range(self._cols):
                tile = self._game.get_tile(row, col)
                if tile == 0:
                    val = 0
                else:
                    val = int(math.log(tile, 2))
                canvas.draw_image(self._tiles,
                    [HALF_TILE_SIZE + val * TILE_SIZE, HALF_TILE_SIZE],
                    [TILE_SIZE, TILE_SIZE],
                    [col * TILE_SIZE + HALF_TILE_SIZE + BORDER_SIZE,
                     row * TILE_SIZE + HALF_TILE_SIZE + BORDER_SIZE],
                    [TILE_SIZE, TILE_SIZE])

    def start(self):
        """
        Start the game.
        """
        self._game.reset()

def run_gui(game):
    """
    Instantiate and run the GUI.
    """
    print game
    gui = GUI(game)
    gui.start()
