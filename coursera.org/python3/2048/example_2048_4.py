"""Clone of 2048 game."""
import poc_2048_gui
import random

UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4
TURN = 5
TEXT_SIZE = 40
GOAL = 2048
GAME_OVER_MESSAGE = 'GAME OVER'

OFFSETS = {UP: (1, 0), DOWN: (-1, 0), LEFT: (0, 1), RIGHT: (0, -1)}

def merge(line):
    """Helper function that merges a single row or column in 2048"""
    merged = [i for i in line if i]
    merged = reduce(lambda x, y: x[:-1] + [y << 1, 0] if x[-1] == y else x + [y], merged[1:], merged[:1])
    merged = [i for i in merged if i]
    return merged + [0] * (len(line) - len(merged))

class TwentyFortyEight:
    """Class to run the game logic."""
    def __init__(self, grid_height, grid_width):
        self._height = grid_height
        self._width = grid_width
        self.reset()

    def reset(self):
        """Reset the game so the grid is empty except for two initial tiles."""
        self._grid = [[0 for _ in range(self._width)] for _ in range(self._height)]
        self._keep = lambda *grid: [row for row in grid]
        # grid transformation params
        self._rotation = {UP: (zip, 1, 1), DOWN: (zip, 1, -1), LEFT: (self._keep, 1, 1),
                          RIGHT: (self._keep, -1, 1), TURN: (zip, -1, 1)}
        self._snapshot = self.get_snapshot()  # list of 0 tile coordinates
        self._fourth = 0  # number of randomly placed 4 tiles, needed for score calculation
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """Return a string representation of the grid for debugging."""
        return '\n'.join([' '.join([str(item) for item in row]) for row in self._grid])

    def get_grid_height(self):
        """Get the height of the board."""
        return self._height

    def get_grid_width(self):
        """Get the width of the board."""
        return self._width

    def move(self, direction):
        """Move all tiles in the given direction and add a new tile if any tiles moved."""
        self._snapshot = self.get_snapshot()  # before move grid state
        # get the grid transformation params from the rotation dictionary
        func, r_dir, c_dir = self._rotation[direction]
        # transform grid and merge lines
        merged_grid = map(merge, func(*[row[::r_dir] for row in self._grid[::c_dir]]))
        # transform grid back
        func, r_dir, c_dir = self._rotation[direction if direction != DOWN else TURN]
        self._grid = map(list, func(*[row[::r_dir] for row in merged_grid[::c_dir]]))
        if self._snapshot != self.get_snapshot():
            self.new_tile()

    def new_tile(self):
        """Create a new tile in a randomly selected empty square.
        The tile should be 2 90% of the time and 4 10% of the time."""
        self._snapshot = self.get_snapshot()
        if self._snapshot:
            tile = 2 if random.random() <= .9 else 4
            if tile == 4:
                self._fourth += 1
            self.set_tile(*(random.choice(self._snapshot) + [tile]))

    def set_tile(self, row, col, value):
        """Set the tile at position row, col to have the given value."""
        self._grid[row][col] = value

    def get_tile(self, row, col):
        """Return the value of the tile at position row, col."""
        return self._grid[row][col]

    def get_snapshot(self, value=0):
        """Return the list of cells in the grid with given value."""
        return [[row, col] for col in range(self._width)
                           for row in range(self._height) if self.get_tile(row, col) == value]

    def get_fourth(self):
        """Return number of initial 4-valued tiles for score calculation."""
        return self._fourth


class CustomGUI(poc_2048_gui.GUI):
    """poc_2048_gui extension to displays messages."""
    def __init__(self, game):
        """Initialize super class."""
        poc_2048_gui.GUI.__init__(self, game)
        self._score = '0'
        self._game_over = False
        self._goal = GOAL
        self._top_msg_y = 40
        self._bottom_msg_y = poc_2048_gui.BORDER_SIZE + \
                            (self._rows * poc_2048_gui.TILE_SIZE + TEXT_SIZE) - 5

    def draw(self, canvas):
        """Extend draw handler with message drawing."""
        poc_2048_gui.GUI.draw(self, canvas)
        txt = 'Score: ' + self._score
        txt_center = self.get_text_center(txt)
        canvas.draw_text(txt, (txt_center, self._bottom_msg_y), 40, 'Black')
        if self._game_over:
            txt_center = self.get_text_center(GAME_OVER_MESSAGE)
            canvas.draw_text(GAME_OVER_MESSAGE, (txt_center, self._top_msg_y), 40, 'Red')
        elif self._goal > GOAL:
            goal = 'Well done! Next goal is ' + str(self._goal)
            txt_center = self.get_text_center(goal, 20)
            canvas.draw_text(goal, (txt_center, self._top_msg_y - 5), 20, 'Blue')

    def keydown(self, key):
        """Keydown handler extension."""
        poc_2048_gui.GUI.keydown(self, key)
        self._score = self.get_score()
        self._game_over = self.is_game_over()
        if self._game.get_snapshot(self._goal):
            self._goal *= 2

    def get_score(self):
        """Returns current score based on grid layout."""
        score = 0
        for row in range(self._rows):
            for col in range(self._cols):
                tile = self._game.get_tile(row, col)
                if tile not in (0, 2):
                    score += tile * (bin(tile).count("0") - 2)
        score -= self._game.get_fourth() * 4
        return str(score)

    def is_game_over(self):
        """Returns True if the game is over, else False."""
        for row in range(self._rows):
            for col in range(self._cols):
                cell = self._game.get_tile(row, col)
                if col < self._cols - 1:
                    merge_cell = self._game.get_tile(row, col + 1)
                    if not cell or not merge_cell or merge_cell == cell:
                        return False
                if row < self._rows - 1:
                    merge_cell = self._game.get_tile(row + 1, col)
                    if not cell or not merge_cell or merge_cell == cell:
                        return False
        return True

    def get_text_center(self, text, text_size=TEXT_SIZE):
        """Returns X coordinate of text centered on canvas."""
        return poc_2048_gui.BORDER_SIZE + (self._cols * poc_2048_gui.TILE_SIZE - \
               self._frame.get_canvas_textwidth(text, text_size, 'sans-serif')) / 2

    def start(self):
        """Game reset extension."""
        poc_2048_gui.GUI.start(self)
        self._score = '0'
        self._game_over = False
        self._goal = GOAL


CustomGUI(TwentyFortyEight(4, 4)).start()
