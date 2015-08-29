# sliding tile puzzle game
# http://www.codeskulptor.org/#user40_nIVQuLHOI7_9.py
import simplegui
import random



WIDTH  = 600
HEIGHT = 500

RATIO = 1.0 * WIDTH / HEIGHT

CELL_SIDE = 100

URL_INPUT_WIDTH = 200



def round(value, factor):
    x = value / factor * factor
    y = value % factor
    if y >= factor / 2:
        result = x + factor
    else:
        result = x

    return result



class Cell:
    def __init__(self, position, value):
        self.original_position = position
        self.current_position = position
        self.value = value

    def __str__(self):
        result  = 'Cell:\n'
        result += '  Original position: ' + str(self.original_position) + '\n'
        result += '  Current position: ' + str(self.current_position) + '\n'
        result += '  Value: ' + str(self.value) + '\n'

        return result

    def update_position(self, new_position):
        self.current_position = new_position

    def get_original_position(self):
        return self.original_position

    def get_current_position(self):
        return self.current_position

    def get_value(self):
        return self.value

    def draw(self):
        print str(self.value)
        pass



class Board:
    def __init__(self, rows = 4, cols = 4, image = None):
        self.rows = rows
        self.cols = cols
        self.num_tiles = rows * cols
        self.image = image
        self.cells = []
        self.moves = []
        self.num_moves = 0
        self.locked = False
        self.show_solved_only = False

        # Initialize all but the last (bottom right cell), which
        # should be empty.
        for i in range(rows * cols - 1):
            self.cells.append(Cell(i, i))

        # Initialize the empty cell with a value of None.
        self.empty_cell = rows * cols - 1
        self.cells.append(Cell(self.empty_cell, None))

        self.find_moves()

    def __str__(self):
        result  = 'Board:\n'
        result += '  Number of rows: ' + str(self.rows) + '\n'
        result += '  Number of columns: ' + str(self.cols) + '\n'
        result += '  Image: ' + str(self.image) + '\n'
        result += '  Empty cell: ' + str(self.empty_cell) + '\n'
        result += '  Available moves: ' + str(self.moves) + '\n'
        result += '  Cells:\n'


        for i in range (self.rows * self.cols):
            result += ' ' + str(self.cells[i])

        return result

    def shuffle(self):
        for i in range(500 * self.rows * self.cols):
            choice = random.choice(self.moves)
            self.move(random.choice(self.moves))

        # Do not count moves incurred during shuffling, so reset to 0
        self.num_moves = 0

    def move(self, cell):
        if cell in self.moves:
            # Swap the selected cell with the empty cell
            temp_cell = self.cells[self.empty_cell]
            self.cells[self.empty_cell] = self.cells[cell]
            self.cells[cell] = temp_cell
            self.empty_cell = cell
            self.num_moves += 1

            # Refresh available moves
            self.find_moves()

    def move_tile(self, row, col):
        self.move(row * self.cols + col)

    def move_tile_up(self):
        self.move(self.empty_cell + self.cols)

    def move_tile_down(self):
        self.move(self.empty_cell - self.cols)

    def move_tile_left(self):
        self.move(self.empty_cell + 1)

    def move_tile_right(self):
        self.move(self.empty_cell - 1)

    def get_empty_cell(self):
        return self.empty_cell

    def get_num_moves(self):
        return self.num_moves

    def get_num_tiles(self):
        return self.num_tiles

    def get_solved_tiles(self):
        result = 0

        for i in range(self.rows * self.cols):
            if self.cells[i].get_original_position() == i:
                result += 1

        return result

    def lock(self):
        self.locked = True

    def unlock(self):
        self.locked = False

    def is_locked(self):
        return self.locked

    def show_solved(self):
        self.show_solved_only = True

    def show_all(self):
        self.show_solved_only = False

    def find_moves(self):
        # Available moves include the cells immediately above,
        # below, to the left, and to the right of the empty
        # cell, as long as those cells do not go off the edge
        # of the board.

        moves = []

        # Cell immediately above empty cell
        candidate = self.empty_cell - self.cols
        # Make sure candidate is not before first row
        if candidate >= 0:
            moves.append(candidate)

        # Cell immediately below empty cell
        candidate = self.empty_cell + self.cols
        # Make sure candidate is not past last row
        if candidate < self.rows * self.cols:
            moves.append(candidate)

        # Cell immediately to the left of empty cell
        candidate = self.empty_cell - 1
        # Make sure candidate did not wrap to the previous row
        if candidate % self.cols != self.cols - 1:
            moves.append(candidate)

        # Cell immediately to the right of empty cell
        candidate = self.empty_cell + 1
        # Make sure candidate did not wrap to the next row
        if candidate % self.cols != 0:
            moves.append(candidate)

        self.moves = moves

    def draw(self, canvas):
        for row in range(self.rows):
            for col in range(self.cols):
                index = row * self.cols + col
                if self.empty_cell != index:
                    value = self.cells[index].get_value()
                    col_image = value %  self.cols
                    row_image = value // self.cols

                    if self.is_locked():
                        col_canvas = col_image
                        row_canvas = row_image
                    else:
                        col_canvas = col
                        row_canvas = row

                    if not self.show_solved_only or (self.show_solved_only and self.cells[index].get_original_position() == index):
                        canvas.draw_image(self.image,
                                          ((col_image + 0.5) * g_image_cell_width, (row_image + 0.5) * g_image_cell_height),
                                          (g_image_cell_width, g_image_cell_height),
                                          ((col_canvas + 0.5) * CELL_SIDE, (row_canvas + 0.5) * CELL_SIDE),
                                          (CELL_SIDE, CELL_SIDE))
                        canvas.draw_polyline([(col_canvas * CELL_SIDE, row_canvas * CELL_SIDE),
                                              (col_canvas * CELL_SIDE + CELL_SIDE - 1, row_canvas * CELL_SIDE),
                                              (col_canvas * CELL_SIDE + CELL_SIDE - 1, row_canvas * CELL_SIDE + CELL_SIDE - 1),
                                              (col_canvas * CELL_SIDE, row_canvas * CELL_SIDE + CELL_SIDE - 1)],
                                             1,
                                             'Black')



def input_handler(url):
    global g_image_loaded, g_image
    g_image_loaded = False
    g_image = simplegui.load_image(url)



def mouse_handler(pos):
    if not g_puzzle.is_locked():
        col = pos[0] // CELL_SIDE
        row = pos[1] // CELL_SIDE
        g_puzzle.move_tile(row, col)



def keydown_handler(key):
    empty_cell = g_puzzle.get_empty_cell()

    if key == simplegui.KEY_MAP['up']:
        g_puzzle.move_tile_up()
    elif key == simplegui.KEY_MAP['down']:
        g_puzzle.move_tile_down()
    elif key == simplegui.KEY_MAP['left']:
        g_puzzle.move_tile_left()
    elif key == simplegui.KEY_MAP['right']:
        g_puzzle.move_tile_right()
    pass



def shuffle_puzzle_handler():
    if g_image_loaded and not g_puzzle.is_locked():
        g_puzzle.shuffle()



def show_picture_handler():
    global g_button_show_picture

    if g_image_loaded:
        if g_puzzle.is_locked():
            g_button_show_picture.set_text('Show Picture')
            g_puzzle.unlock()
        else:
            g_puzzle.lock()
            g_button_show_picture.set_text('Resume Puzzle')



def show_solved_handler():
    global g_button_show_solved

    if g_image_loaded:
        if g_puzzle.is_locked():
            g_button_show_solved.set_text('Show Solved Tiles')
            g_puzzle.show_all()
            g_puzzle.unlock()
        else:
            g_puzzle.lock()
            g_puzzle.show_solved()
            g_button_show_solved.set_text('Resume Puzzle')



def draw_handler(canvas):
    global g_image_loaded, g_frame_height, g_frame_width, g_image_width, g_image_height, \
           g_num_rows, g_num_cols, g_image_cell_width, g_image_cell_height, g_puzzle, \
           g_label_num_moves, g_label_solved_tiles

    if g_image_loaded:
        g_puzzle.draw(canvas)
        g_label_num_moves.set_text('Number of moves: ' + str(g_puzzle.get_num_moves()))
        g_label_solved_tiles.set_text('Solved tiles: ' + str(g_puzzle.get_solved_tiles()) +
                                       '/' + str(g_puzzle.get_num_tiles()))
    elif g_image and g_image.get_height():
        g_image_width = g_image.get_width()
        g_image_height = g_image.get_height()

        image_ratio = 1.0 * g_image_width / g_image_height

        if RATIO > image_ratio:
            g_frame_height = HEIGHT
            g_frame_width = round(int(1.0 * g_image_width * g_frame_height / g_image_height), CELL_SIDE)
        else:
            g_frame_width = WIDTH
            g_frame_height = round(int(1.0 * g_image_height * g_frame_width / g_image_width), CELL_SIDE)
        g_image_loaded = True

        g_num_rows = g_frame_height // CELL_SIDE
        g_num_cols = g_frame_width // CELL_SIDE
        g_image_cell_width = float(g_image_width) / g_num_cols
        g_image_cell_height = float(g_image_height) / g_num_rows

        g_puzzle = Board(g_num_rows, g_num_cols, g_image)

        start_frame()



def start_frame():
    global g_frame, g_label_num_moves, g_label_solved_tiles, g_button_show_picture, g_button_show_solved

    g_frame = simplegui.create_frame('Sliding Tile Puzzle', g_frame_width, g_frame_height)
    g_frame.set_draw_handler(draw_handler)
    g_frame.set_mouseclick_handler(mouse_handler)
    g_frame.set_keydown_handler(keydown_handler)

    g_frame.add_input('Enter a URL for a picture or image:', input_handler, URL_INPUT_WIDTH)
    g_frame.add_label('')
    g_frame.add_button('Shuffle', shuffle_puzzle_handler)
    g_frame.add_label('')
    g_button_show_picture = g_frame.add_button('Show Picture', show_picture_handler)
    g_frame.add_label('')
    g_button_show_solved = g_frame.add_button('Show Solved Tiles', show_solved_handler)
    g_frame.add_label('')
    g_label_num_moves = g_frame.add_label('')
    g_frame.add_label('')
    g_label_solved_tiles = g_frame.add_label('')
    g_frame.add_label('')
    g_frame.add_label('Move tiles by clicking on a tile adjacent to the empty tile ' +
                      'or using the arrow keys.')
    g_frame.start()

initial_image_url = 'http://commondatastorage.googleapis.com/codeskulptor-assets/gutenberg.jpg'

random.seed()

g_image_loaded = False
g_image = None
g_frame_width = WIDTH
g_frame_height = HEIGHT
g_image_width = 0
g_image_height = 0
g_num_rows = 0
g_num_cols = 0
g_image_cell_width = 0.0
g_image_cell_height = 0.0
g_puzzle = None
g_frame = None
g_button_show_picture = None
g_button_show_solved = None
g_label_num_moves = None
g_label_solved_tiles = None

start_frame()
input_handler(initial_image_url)
