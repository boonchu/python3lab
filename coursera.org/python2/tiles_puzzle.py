# 15-puzzle by NK
#
# class Tile
# class Puzzle15
# class GameUI
#

import simplegui
import random

VERBOSE = False

WIDTH = 400
HEIGHT = WIDTH + 50
TILE_WIDTH = TILE_HEIGHT = WIDTH / 4

TILE_FONT_SIZE = 40
TILE_FONT_FACE = 'monospace'

IMAGE_URLS = [
    "https://db.tt/ZtAwSuQw", # Dali. Desintegration of Persistence
    "https://db.tt/4FspwyRX", # Dali. Last supper
    "https://db.tt/E5HTVlDh", # Dali. Slave market with disappearing bust of Voltaire
    "https://db.tt/NUSIvFYO", # Dali. Corpus Hypercube
    "https://db.tt/MDvrSPR1", # Picasso, Guernica. Haha :)
    #"https://db.tt/Dz9enkD7"  # Fun.
]

class Tile:
    height    = TILE_HEIGHT
    width     = TILE_WIDTH
    font_size = TILE_FONT_SIZE
    font_face = TILE_FONT_FACE
    
    def __init__(self, value):
        self.value = value
        
        if self.is_empty():
            self.color         = "Black"
            self.canonical_idx = 15
        else:
            self.color         = "Yellow"
            self.canonical_idx = self.value-1

        # base card in the top left corner of the gameboard
        self.first_card = [[1,            1],             # top left
                           [Tile.width-1, 1],             # top right
                           [Tile.width-1, Tile.height-2], # bottom right 
                           [1,            Tile.height-2]] # bottom left

        self.image = None
        self.image_center = self.center_of_tile(self.canonical_idx)

        self.reset() # sets other variables

    def __str__(self):
        img = "(" + str(self.image_center[0]) + "," + str(self.image_center[1]) + ")"
        return "value=" + str(self.value) + " image=" + img

    def reset(self):
        """Restore the state of the Tile to initial"""
        self.show_label = True
        self.finished   = False
        # for end game animation
        self.finishing  = False
        self.finishing_age = 1 + self.canonical_idx * 10
        
    def center_of_tile(self, idx):
        # TODO: get rid of constant 4
        coords = [ Tile.height/2 + Tile.height * (idx%4),
                   Tile.width/2  + Tile.width  * (idx/4) ]
        return coords

    def is_empty(self):
        return self.value == 0

    def label(self):
        return str(self.value)

    def toggle_label(self):
        self.show_label = not self.show_label

    # TODO: refactor <pos>: row,col or idx in list?
    def draw(self, canvas, pos, inplace=False):
        self.row, self.col = pos[0], pos[1]

        # end-game animation
        if self.finishing and not self.finished:
            self.finishing_age -= 1
            self.finished = self.finishing_age == 0
 
        # draw the image if available
        # TODO: refactor. The question is who should compute row,col? is it useless?
        if self.image:
            idx = 4*self.row + self.col
            canvas.draw_image(self.image, 
                              self.image_center,        (Tile.width, Tile.height), 
                              self.center_of_tile(idx), (Tile.width, Tile.height))

        if not self.finished or not self.image:
            color = self.color
            if inplace and not self.is_empty():
                color = "Green"

            # draw the tile border
            canvas.draw_polygon(self.corners(), 1, color)
    
            # draw the tile value
            if self.show_label:
                canvas.draw_text(self.label(), self.label_position(), 
                                Tile.font_size, color, Tile.font_face)

    def corners(self):
        # map the base card to the requested row and column
        corners = [ [p[0]+Tile.width*self.col, p[1]+Tile.height*self.row] 
                   for p in self.first_card ]
        return corners

    def label_position(self):
        width = GAME_UI.frame.get_canvas_textwidth(self.label(), 
                                           Tile.font_size, Tile.font_face)
        coords = [(Tile.width-width-2)/2            +Tile.width *self.col , 
                  (Tile.height+self.font_size-10)/2 +Tile.height*self.row]
        return coords

######################################################################

class Puzzle15():
    def __init__(self, solved=False):
        self.is_solved_demo = solved
        self.tiles = [Tile(num) for num in range(0,16)]
        self.c_wins = self.c_helped_wins = self.c_looses = 0
        self.image = None
        self.reset()

    def reset(self):
        if self.is_solved_demo:
            # rearrange to be: 1..15,0
            self.tiles.sort(key=lambda x: x.value)
            self.tiles.append(self.tiles.pop(0))
            self.message = "Solved Demo"

        else:
            for tile in self.tiles: 
                tile.reset()
            random.shuffle(self.tiles)
            self.message = "Welcome!"

        self.c_moves = 0
        self.finished = False
        self.user_success = 1 # allowed values: -1,0,1

    def set_image(self, image):
        if image:
            self.image = image
            for tile in self.tiles:
                tile.image = self.image

    def has_image(self):
        return True if self.image else False
    
    def toggle_labels(self):
        """Enable/disable showing numerical value of the Tile"""
        for tile in self.tiles:
            tile.toggle_label()
  
    def row(self, idx):
        """Computes the row in which given list index occurs in a 4x4 matrix"""
        return idx / 4

    def col(self, idx):
        """Computes the column in which given list index occurs in a 4x4 matrix"""
        return idx % 4

    def move_tile(self, dr):
        """Move the tile closest to the empty tile in the given direction"""
        
        # block any interaction past the end of the game
        # or if the game is a special (solved demo) type.
        if self.is_solved_demo or self.finished:
            return False
        
        self.console("\nMoving tile " + dr)

        empty_idx = self.index_of(0)
        self.console("Empty is:" + self.t2s(empty_idx))
    
        # find the position of the tile that can be moved to the empty cell
        peer_idx = empty_idx
        if   dr == "left"  and self.col(empty_idx) != 3: peer_idx += 1
        elif dr == "right" and self.col(empty_idx) != 0: peer_idx -= 1
        elif dr == "up"    and self.row(empty_idx) != 3: peer_idx += 4
        elif dr == "down"  and self.row(empty_idx) != 0: peer_idx -= 4

        self.console("Swapping: " + self.t2s(empty_idx) + " <-> " + self.t2s(peer_idx))

        if empty_idx == peer_idx:
            self.message = "Illegal move"
            self.console(self.message)
            
        else:
            # swap the empty and peer tiles
            self.swap_tiles(empty_idx, peer_idx)

            self.c_moves += 1
            self.message = ""
            if empty_idx+1 == self.tiles[empty_idx].value:
                self.message = "Great move!"
                
        self.finish_if_solved()

    def finish_if_solved(self):
        if self.is_solved():
            self.finished = True
            for tile in self.tiles: 
                tile.finishing = True
 
            # compute the score
            if self.user_success == 1:
                self.c_wins += 1
                self.message = "You won! Great job!"
            elif self.user_success == 0:
                self.c_helped_wins += 1
                self.message = "You won!"
            elif self.user_success == -1:
                self.player_has_lost()
  
    def player_has_lost(self):
        self.c_looses += 1
        self.message = "Don't give up!"
        
    def is_solved(self, upto=15):
        """
        Check if all tiles before the given position are arranged correctly.
        If position is not given, the whole puzzle is checked.
        """
        solved = True
        if upto == 15:
            solved = self.tiles[15].value == 0
            upto = 14
        for idx in range(upto):
            if self.tiles[idx].value != idx+1:
                solved = False
        return solved
    
    def almost_solve(self):
        """Solve the game up to the point when only a few simple moves remain"""
        if not self.finished:
            self.tiles.sort(key=lambda x: x.value)
            self.tiles.insert(12, self.tiles.pop(0))
            self.user_success = -1
 
    def swap_15_14(self): 
        """Swap 15 and 14 if the rest is solved"""
        if not self.finished:
            idx15 = self.index_of(15)
            idx14 = self.index_of(14)
            if idx15 < idx14 and self.is_solved(13):
                self.swap_tiles(idx14, idx15)
                self.user_success = 0
                self.finish_if_solved()

    def swap_tiles(self, idx1, idx2):
        self.tiles[idx1], self.tiles[idx2] = self.tiles[idx2], self.tiles[idx1]
        self.console("Swapped:  " + self.t2s(idx1) + " --- " + self.t2s(idx2))

    def index_of(self, value):
        return [t.value for t in self.tiles].index(value)
        
    def draw(self, canvas):
        self.canvas = canvas
        
        for idx,tile in enumerate(self.tiles):
            tile.draw(canvas, [self.row(idx), self.col(idx)], idx+1 == tile.value)
        
        self.draw_reports()

    def draw_reports(self):
        # draw reporting area
        lt = [2,       3+Tile.height*4]
        rt = [WIDTH-2, lt[1]]
        rb = [rt[0],   HEIGHT-2]
        lb = [lt[0],   HEIGHT-2]
        corners = [lt, rt, rb, lb]
        self.canvas.draw_polygon(corners, 1, "Grey")
    
        # common vertical alignment for all messages in the reporting area
        msg_y = HEIGHT-17
        
        # Score (Wins/Looses): Number/Number
        msg_x = lb[0]+10
        scores = [str(self.c_wins), str(self.c_helped_wins), str(self.c_looses)]
        text = "Score: " + "/".join(scores)
        color = "Cyan"
        if   self.c_wins > self.c_looses: color = "Green"
        elif self.c_wins < self.c_looses: color = "Red"
        self.canvas.draw_text(text, [msg_x, msg_y], 20, color)

        # Encouraging message
        msg_x += 110
        self.canvas.draw_text(self.message, [msg_x, msg_y], 20, "White")

        # Moves: Number
        msg_x = WIDTH - 100
        text = "Moves: " + str(self.c_moves)
        self.canvas.draw_text(text, [msg_x, msg_y], 20, "White")

    def t2s(self, idx):
        """ String representation of a tile: index/value"""
        return "[" + str(idx) + "]: " + str(self.tiles[idx])
     
    def console(self, msg):
        """Prints given message to the console only in VERBOSE mode"""
        if VERBOSE:
            print msg

######################################################################

class GameUI:
    
    def __init__(self):
        self.game = None
        self.solved_game = None

        self.new_game()
        self.create_ui()

    def create_ui(self):
        """Create a frame and assign callbacks to event handlers"""
        self.frame = simplegui.create_frame("15-puzzle", WIDTH, HEIGHT)

        self.frame.set_draw_handler(self.draw)
        self.frame.set_keydown_handler(self.on_key_press)
        self.frame.set_keyup_handler(self.on_key_release)

        self.frame.add_button("(n) New game", self.btn_new_game)
        # TODO: how to show either 'Show numbers' or 'Hide numbers'
        #       need to know the state of Tile#show_label or
        #       update a similar attribute in GameUI. How to sync
        #       the initial state?
        if self.game.has_image():
            self.frame.add_button("(l) Show/hide numbers", self.btn_toggle_labels)

        # TODO: button for preview and keypress dont play well together:
        # because the button changes the state permanenty until the next btn press
        #self.frame.add_button("(p) Show/hide preview", self.btn_toggle_preview)
        self.frame.add_button("(w) Swap 15 and 14", self.btn_swap_15_14)
        self.frame.add_button("I give up", self.btn_almost_solve)
        
        self.frame.add_label("")
        self.frame.add_label("*** Controls ***")
        self.frame.add_label("Use arrow keys")
        self.frame.add_label("Hold p pressed to preview expected outcome")

        self.frame.start()

    def new_game(self):
        """Starts a new game"""
        image = simplegui.load_image(random.choice(IMAGE_URLS))
        if self.game:
            self.game.player_has_lost()
            self.game.reset()
        else:
            self.game = Puzzle15()
            self.solved_game = Puzzle15(True)
        if image:
            self.game.set_image(image)
            self.solved_game.set_image(image)
            
    def draw(self, canvas):
        if self.game:
            self.game.draw(canvas)

    #
    # Keyboard events
    #
    def on_key_press(self, key):
        for direction in ["left", "right", "up", "down"]:
            if key == simplegui.KEY_MAP[direction]:
                self.game.move_tile(direction)

        if key == simplegui.KEY_MAP["d"]:
            self.btn_almost_solve()
        if key == simplegui.KEY_MAP["l"]:
            self.btn_toggle_labels()
        if key == simplegui.KEY_MAP["n"]:
            self.btn_new_game()
        if key == simplegui.KEY_MAP["p"] and self.game.has_image():
            self.btn_toggle_preview()
        if key == simplegui.KEY_MAP["w"]:
            self.btn_swap_15_14()

    def on_key_release(self, key):
        if key == simplegui.KEY_MAP["p"] and self.game.has_image():
            self.btn_toggle_preview()

    #
    # Button events
    #
    def btn_new_game(self):
        self.new_game()

    def btn_toggle_labels(self):
        self.game.toggle_labels()

    def btn_toggle_preview(self):
        self.game, self.solved_game = self.solved_game, self.game
 
    def btn_swap_15_14(self):
        self.game.swap_15_14()
 
    def btn_almost_solve(self):
        self.game.almost_solve()

######################################################################
# Let there be game!

GAME_UI = GameUI()

