# BlackJack using the IIPP2 rules 
# GFX (c) http://pichost.me/1357822/
# SFX (s) http://opengameart.org/content/54-casino-sound-effects-cards-dice-chips

import simplegui
import random
import math

# dimensions, positions and related constants of the main game elements on the canvas
CANVAS_SIZE = (700, 600)
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
DECK_POS = (595, 290)
DEALER_POS = (170, 160)
PLAYER_POS = (170, 410)
SCORE_DEALER_POS = (65, 250)
SCORE_PLAYER_POS = (69, 490)
MSG_POS = (566, 360)
CARDS_PER_ROW = 4
CARDS_SPACING_H = 100
CARDS_SPACING_V = 40
MOVE_RATE = 30.0
CARD_WIGGLE = 30
DECK_WIGGLE = 10
HAND_AREA_COLOR = "#006400"
HAND_VALUE_COLOR = "#cccccc"
HAND_VALUE_SHADOW = "#444444"
HAND_VALUE_SHADOW_OFFSET = 1
HAND_VALUE_FONT = "sans-serif"
TEXT_SIZE = 36
TEXT_COLOR = "#eeeeee"
TEXT_SHADOW = "#444444"
TEXT_SHADOW_OFFSET = 3
TEXT_FONT = "serif"
TEXT_BOX_COLOR = "rgba(0, 90, 0, 0.5)"

# constants for easier code reading
CONCEALED = True
PLAYER_HAND = True
DEALER_HAND = False
STATIC = '@'
NEW = 0
ONGOING = 1
PAUSED = 2
DEALER_WON = 3
PLAYER_WON = 4

# game state can be the one of the following constants above:
# NEW, ONGOING, PAUSED, DEALER_WON, PLAYER_WON
game_state = NEW

# ordinary message is displayed when the game is over
message = "Press Deal to start new game!"

# temporary message is displayed while the cards are being dealt initially;
# mainly needed for displaying the message about the Player "giving up"
# when they pressed Deal without finishing the round
message_tmp = ""

# [ Dealer's score, Player's score ]
score = [0, 0]

# drawing queue is a list of cards to be drawn in succession
# see draw() below for drawing queue implementation
drawing_queue = []

# audio index selects which sound to be played next out of a collection
audio_index = 0

# suits and ranks of all the cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

# load images
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")
table_bg = simplegui.load_image("https://www.dropbox.com/s/f8289nuuc7u5suc/bj_back6.jpg?dl=1")

# load sounds
audio_deal = [simplegui.load_sound('http://www.dropbox.com/s/ug8kxrt1g9uluiy/card1.wav?dl=1'),
    simplegui.load_sound('http://www.dropbox.com/s/hw1e1bt968jse31/card2.wav?dl=1'),
    simplegui.load_sound('http://www.dropbox.com/s/m06ewvz4r4uw3mr/card3.wav?dl=1'),
    simplegui.load_sound('http://www.dropbox.com/s/myknatchk54f584/card4.wav?dl=1'),
    simplegui.load_sound('http://www.dropbox.com/s/z2d1tt3yijrmjgq/card5.wav?dl=1'),
    simplegui.load_sound('http://www.dropbox.com/s/wk89e315yvnpgyv/card6.wav?dl=1')]


# standard Card class with a few added properties and methods:
# shadow, pos, vel, faceup, concealed, moving
class Card:
    def __init__(self, suit, rank, shadow = True):

        # assign given suit and rank to each instantiated card 
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

        # shadow determines whether card shadow should be drawn
        # (cards in the deck do not have shadows)
        self.shadow = shadow
        
        # current card position on screen
        self.pos = None
        
        # vel will be card's velocity while it moves
        self.vel = (0, 0)
        
        # faceup determines what if the card is currently facing up
        # all cards start face down (from the deck) and may or may not
        # be flipped over, depending on their concealed property
        self.faceup = False
        
        # concealed determines if the card should be kept hidden even
        # after it finished moving (moving cards is face down and then flipped)
        self.concealed = False
        
        # moving is a counter that goes from some value down to 0
        # while card is in motion, it also serves as a flag when card is static
        self.moving = 0

        # every card will have a small random angle to be drawn at
        # even smaller angle range for cards with no shadow (i.e. deck cards)
        if shadow:
            self.angle = random.randrange(CARD_WIGGLE) / 100.0 - CARD_WIGGLE / 200.0
        else:
            self.angle = random.randrange(DECK_WIGGLE) / 100.0 - DECK_WIGGLE / 200.0
            
    # return card rank
    def get_rank(self):
        return self.rank
    
    # return card's ID (suit + rank) as a string
    def __str__(self):
        return self.suit + self.rank

    # set card's position on screen
    def set_pos(self, pos):
        self.pos = pos

    # mark the card to be concealed once it needs to be drawn in the hand
    def conceal(self):
        self.concealed = True
        
    # returns the concealed status of a card
    def is_concealed(self):
        return self.concealed

    # open previously concealed card
    def open(self):
        self.concealed = False
        self.faceup = True
    
    # set card's velocity to start card movement from the deck
    # move_rate will determine how many canvas refreshes
    # would be required that the card reaches its final destination
    # so if move_rate = 30, at 60 FPS canvas refresh rate, the card
    # will reach its final position in 0.5 seconds
    def set_vel(self, vel, move_rate):
        self.vel = vel
        self.moving = move_rate

    # returns boolean that tells whether the card is currently moving
    def is_static(self):
        return not bool(self.moving)

    # draw a card using all of its properties, like pos, vel, faceup, shadow
    def draw(self, canvas):
        
        # if the card has no pos, it is "in the deck" so nothing to draw
        if self.pos == None:
            return
        
        # if the card is still moving, change its position by velocity
        if self.moving:
            self.pos[0] += self.vel[0]
            self.pos[1] += self.vel[1]
            self.moving -= 1

            # check if the card has reached the end of all moving steps; if so,
            # reset its velocity and flip (only if not supposed to be concealed)
            if self.moving == 0:
                self.vel = (0,0)
                self.faceup = not self.concealed

        # if the card is in its final position and must have shadow,
        # draw card's back shifted 1px to the right and down to create fake shadow
        if not self.moving and self.shadow:
            canvas.draw_image(card_back, CARD_CENTER, CARD_SIZE,
                [self.pos[0] + CARD_CENTER[0] + 1,
                 self.pos[1] + CARD_CENTER[1] + 1], CARD_SIZE, self.angle)

        # if the card is supposed to be facing up, find the right tile in the
        # tiled image using rank and suit and display it in card's current position
        if self.faceup:
            card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                        CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
            
            canvas.draw_image(card_images, card_loc, CARD_SIZE,
                [self.pos[0] + CARD_CENTER[0],
                 self.pos[1] + CARD_CENTER[1]], CARD_SIZE, self.angle)
            
        # if the card is facing down, just draw the back of the card in its current pos
        else:
            canvas.draw_image(card_back, CARD_CENTER, CARD_SIZE,
                [self.pos[0] + CARD_CENTER[0],
                 self.pos[1] + CARD_CENTER[1]], CARD_SIZE, self.angle)


# the Hand class has been appended with a few methods, like get_visible_value()
# and is_static(), as well as the pos and move_rate property in the __init__ method
class Hand:
    
    # pos determines the top left corner of the area that will be used to display
    # all Hand's objects (like cards in hand and hand's value) 
    # move_rate determines how fast the card should travel from the deck to the hand
    def __init__(self, pos, move_rate):
        self.cards = []
        self.pos = pos
        self.move_rate = move_rate

    # add a card object to a hand, concealed determines whether this card will be kept
    # concealed until the end of the current round (usually only for Dealer's Hand)
    def add_card(self, card, concealed = False):

        # if the card should be concealed, set its state (default is not concealed)
        if concealed:
            card.conceal()

        # see what order this newly card is going to be in hand (0, 1st, 2nd, an so on)
        index = len(self.cards)
        
        # determine this cards's final position on the canvas once it reaches the Hand;
        # this position will depend on things like where the hand's area is on canvas,
        # how many cards per one row should be displayed and on card's horizontal and
        # vertical spacing (all set as constants at the beginning of the program)
        pos_x = self.pos[0] + (index % CARDS_PER_ROW ) * CARDS_SPACING_H \
                    + index / CARDS_PER_ROW * CARDS_SPACING_H / 4
        pos_y = self.pos[1] + index / CARDS_PER_ROW * CARDS_SPACING_V
        
        # determine this card's velocity so that it could reach its final position in hand
        # at a move_rate, given in the Hand's __init__ method, relative to Deck's position
        vel_x = (pos_x - DECK_POS[0]) / self.move_rate
        vel_y = (pos_y - DECK_POS[1]) / self.move_rate

        # set card's initial position and velocity, i.e. prepare it for movement from
        # the deck to the respective Hand
        card.set_pos([DECK_POS[0], DECK_POS[1]])
        card.set_vel((vel_x, vel_y), self.move_rate)
        
        # append card object to the Hand object so that the Hand can control what cards
        # should be drawn a the next canvas refresh and that the Hand value can be obtained
        self.cards.append(card)

    # calculate true Hand value (opposed to "currently visible" value below)
    def get_value(self):

        # first sum up all the cards in hand, counting Aces as "1"
        value = sum([VALUES[card.get_rank()] for card in self.cards])
        
        # if there is at least one Ace in Hand, check if counting it as 11
        # does not exceed 21 points. If so, add 10 to the value of the hand
        if "A" in [card.get_rank() for card in self.cards] and value + 10 <= 21:
            value += 10

        # return Hand's value
        return value

    # similar to the method above but the Hand value is only calculated for
    # currently visible cards which will be displayed on canvas; this is needed
    # because we do not want to show real hand's value BEFORE card has done moving
    def get_visible_value(self):
        
        # reset total Hand's value and a flag that would tell us if there is an Ace
        value = 0
        hasAce = False
        
        # go through each card and add its value to the total amount only if the card
        # is not concealed, also see if there was a non-concealed Ace
        for card in self.cards:
            if card.is_static() and not card.is_concealed():
                value += VALUES[card.get_rank()]
                if card.get_rank() == "A":
                    hasAce = True

        # if there was at least one Ace, which wasn't concealed, apply the same logic
        # like above when calculating true Hand's value
        if hasAce and value + 10 <= 21:
            value += 10
            
        # return Hand's visible value
        return value
    
    # determine whether a particular card in this Hand is currently moving on screen
    # this will be required to handle the drawing queue properly (see draw() below)
    def is_static(self, card_id):
        for card in self.cards:
            if str(card) == card_id:
                return card.is_static()
    
    # open the hole card of the Dealer (usually at the very end of the round)
    # the hole card is always the very first card in the Dealer's Hand, i.e. index 0
    def open_hole_card(self):
        self.cards[0].open()
    
    # draw the Hand until the card specified as until_card
    # the cards in Hand (i.e. objects in the self.cards list) are not necessarily
    # displayed immediately on canvas, because the cards are drawn from deck
    # one by one and need time to get drawn as "moving" from Deck into a Hand.
    # the until_card parameter is needed by the draw_queue to prevent all cards
    # drawn at the same time, instead they will be drawn in succession as required
    # until_card can be either a str() value of a card in the deck or a special value
    # STATIC (set as a constant at the beginning of the program). STATIC means that
    # only the cards of this Hand which are currently not moving should be drawn
    def draw(self, canvas, until_card = None):
        
        # first draw shadowed rectangle that will represent Hand's area on canvas
        # the area will be slightly larger than the actual place where the cards will fall
        # which is going to be determined by things like Hand's position on the canvas,
        # the number of cards per row and the horizontal and vertical spacing between them
        extra_rows = math.ceil(5.0 / CARDS_PER_ROW) - 1

        height = CARD_SIZE[1] + CARDS_SPACING_V * extra_rows + 20
        
        width = CARD_SIZE[0] + CARDS_SPACING_H * (CARDS_PER_ROW - 1) \
                    + extra_rows * CARD_SIZE[0] / 3

        canvas.draw_line((self.pos[0] - 10, self.pos[1] + height / 2 - 10),
                            (self.pos[0] + width, self.pos[1] + height / 2 - 10),
                                height, HAND_AREA_COLOR)

        # go through each card in deck and draw all cards that are allowed to be drawn
        for i, card in enumerate(self.cards):
            # if only static cards should be drawn and the current card is moving
            # (or is queued for moving) then stop drawing cards
            if until_card == STATIC and not card.is_static():
                break

            # otherwise draw current card (wherever it is on canvas)
            card.draw(canvas)
            
            # if until_card was given and we've just drawn it, stop drawing
            if until_card and str(card) == until_card:
                break

        # determine and draw the Hand's value of all *visible* cards;
        # "visible" value is needed, because we want to avoid the situation where
        # the card is still moving from the deck to the hand (face down) but
        # the Hand value that includes that card is already being displayed before
        # we have seen the card which is still face down and moving;
        visible_value = self.get_visible_value()
        concealed = ""

        # see if there are any concealed cards in the hand and append string "..."
        if any([card.is_concealed() for card in self.cards]):
            concealed = "..."

        # if there is some value greater than zero, display it relative to the
        # hand's canvas position
        if visible_value:
            draw_text_shadow(canvas, "Hand value: %d %s" %(visible_value, concealed),
                (15, self.pos[1] + 120), 18, HAND_VALUE_COLOR, HAND_VALUE_SHADOW_OFFSET,
                    HAND_VALUE_SHADOW, HAND_VALUE_FONT)


# the Deck class gets new property: pos, which will be used to draw a deck of
# cards on the table; the cards for the deck will be some fake cards only used
# for display, we are not going to draw all 52 cards on canvas and really draw
# from them, so our deck will be a dummy, just to make things pretty
class Deck:
    
    # create brand new deck of cards when required
    def __init__(self, pos):
        
        # instantiate cards of all suits and all ranks
        self.cards = [Card(S, R) for S in SUITS for R in RANKS]
        
        # also create a dummy deck_on_canvas collection of cards (only 6 of them)
        self.deck_on_canvas = [Card('C', 'A', False) for card in range(0,6)]
        
        # set position for the cards in the dummy deck to be drawn when needed
        for i, card in enumerate(self.deck_on_canvas):
            card.set_pos((pos[0] - i * 2 + 10, pos[1] - i * 2 + 10))

    # shuffle cards in the real deck
    def shuffle(self):
        random.shuffle(self.cards)

    # get (i.e. delete) a single card out of the shuffled deck and return it
    # to be appended to the Hand object, hopefully
    def deal_card(self):
        return self.cards.pop()
    
    # draw the dummy deck: go through each card in the dummy deck and display it
    def draw(self, canvas):
       [card.draw(canvas) for card in self.deck_on_canvas]


# this is a helper function that will do the following:
# it will extract a card from the Deck
# it will put card's ID into the drawing queue
# it will append this card to the given hand
# optionally it will set the "concealed" property to the card drawn (hole card)
def deal_single_card(hand, concealed = False):
    global drawing_queue
    card = deck.deal_card()
    drawing_queue.append((hand, str(card)))
    if hand == PLAYER_HAND:
        player_hand.add_card(card)
    else:
        dealer_hand.add_card(card, concealed)


# a helper function to play the sound of card being dealt (or flipped)
# also rotates the audio index to pick some different sound next time
def play_deal_sound():
    global audio_index
    audio_deal[audio_index].play()
    audio_index = (audio_index + 1) % 6


# the "Deal" button handler that initiates new round
def deal():
    global game_state, deck, player_hand, dealer_hand, score
    global message, message_tmp, drawing_queue
    
    # if there are currently cards being drawin as moving, do nothing
    if any(drawing_queue):
        return
    
    # reset the outcome message and the drawing queue
    message = ""
    drawing_queue = []
    
    # if the game was already ongoing and the Player pressed "Deal", it means
    # they "gave up" and lost to the dealer; give a point to the Dealer and
    # display the temporary message about this (will be visible as long as
    # new cards are being dealt for the next round)
    if game_state == ONGOING:
        game_state = NEW
        score[0] += 1
        message_tmp = "You gave up (and lost)!"

    # initialize brand new deck with all the cards in it and shuffle it
    deck = Deck(DECK_POS)
    deck.shuffle()
    
    # initialize both the Dealer and the Player hand with the positions and
    # move_rate set as the constants at the beginning of the program
    player_hand = Hand(PLAYER_POS, MOVE_RATE)
    dealer_hand = Hand(DEALER_POS, MOVE_RATE)
    
    # deal four cards according to the rules of the game, one of them concealed
    deal_single_card(PLAYER_HAND)
    deal_single_card(DEALER_HAND, CONCEALED)
    deal_single_card(PLAYER_HAND)
    deal_single_card(DEALER_HAND)
    
    # change game state and set the message for the Player to be prompted
    game_state = ONGOING
    message = "Hit or stand?"


# the "New Game" button handler: resets scores and deals again
def start_new():
    global game_state
    score[0] = score[1] = 0
    game_state = NEW
    deal()


# the "Hit" button handler: supposed to add another card to Player's Hand
def hit():
    global game_state, message
    
    # if the game is not in the ongoing state or some cards are still moving
    # on canvas (the drawing_queue is not empty), then do nothing
    if game_state != ONGOING or any(drawing_queue):
        return
    
    # if the current Player's Hand value is below 21, draw another card
    if player_hand.get_value() < 21:
        deal_single_card(PLAYER_HAND)
        
        # if after drawing that card the hand value is over 21, Player has lost
        if player_hand.get_value() > 21:
            # the game state changes but the score will be updated when
            # all other drawing has been finished (see draw() handler below)
            game_state = DEALER_WON
            message = "You are busted! Deal again?"


# the "Stand" button handler: supposed to finish Player's actions and give
# the Dealer a chance to win the game by applying Dealer's drawing logic
def stand():
    global game_state, message
    
    # if the button was pressed at the wrong time (the cards are moving or
    # the game has already ended), then do nothing
    if game_state != ONGOING or any(drawing_queue):
        return

    # change game to PAUSED state, so that no interaction would be allowed
    game_state = PAUSED
    
    # open the hole card first (and play card dealing sound)
    dealer_hand.open_hole_card()
    play_deal_sound()
    
    # if the Dealer's hand value is less than 17, keep dealing card to their Hand
    while dealer_hand.get_value() < 17:
        deal_single_card(DEALER_HAND)
        
    # now if the Dealers Hand value is over 21, they have lost the game
    if dealer_hand.get_value() > 21:
        game_state = PLAYER_WON
        message = "Dealer is busted! Deal again?"

    # otherwise, it may be a draw or the Player may win
    else:
        # if it's a draw or the Player's Hand value is less
        # than Dealer's, Player loses
        if player_hand.get_value() <= dealer_hand.get_value():
            message = "You lose! Deal again?"
            game_state = DEALER_WON
            
        # otherwiser, the Player is the winner	
        else:
            message = "You win! Deal again?"
            game_state = PLAYER_WON

            
# a helper function to draw text with a shadow
# the shadow is the same text drawn with dark color at a given offset
def draw_text_shadow(canvas, text, pos, size = TEXT_SIZE, col = TEXT_COLOR, 
                        shad_off = TEXT_SHADOW_OFFSET, shad_col = TEXT_SHADOW,
                            font = TEXT_FONT):
    canvas.draw_text(text, (pos[0] + shad_off, pos[1] + shad_off), size, shad_col, font)
    canvas.draw_text(text, pos, size, col, font)


# a helper function that draws the rectangle that should surround the
# announcement message for the Player; the message is also drawn here
def draw_text_box(canvas, message):
    width = frame.get_canvas_textwidth(message, TEXT_SIZE, TEXT_FONT)
    pos_start = [MSG_POS[0] - width - 20, MSG_POS[1] - TEXT_SIZE / 3 + 3]
    pos_end = [MSG_POS[0], MSG_POS[1] - TEXT_SIZE / 3 + 3]
    canvas.draw_line(pos_start, pos_end, TEXT_SIZE + 16, TEXT_BOX_COLOR)
    draw_text_shadow(canvas, message, (MSG_POS[0] - width - 10, MSG_POS[1]))


# the one that rules them all: the draw handler
def draw(canvas):
    global drawing_queue, audio_index, message_tmp, game_state
    
    # draw the background image
    canvas.draw_image(table_bg, (CANVAS_SIZE[0]/2, CANVAS_SIZE[1]/2), CANVAS_SIZE,
                       (CANVAS_SIZE[0]/2, CANVAS_SIZE[1]/2), CANVAS_SIZE)
    
    # draw scores in their designated locations
    draw_text_shadow(canvas, str(score[0]), SCORE_DEALER_POS)
    draw_text_shadow(canvas, str(score[1]), SCORE_PLAYER_POS)
    
    # draw the dummy deck
    deck.draw(canvas)
    
    # check the drawing queue (the list of card ID's) if it has anything in it
    if any(drawing_queue):
        
        # drawing queue is the FIFO list: first in, first out
        card = drawing_queue[0]
        
        # if the card in the queue is from the Player's Hand
        if card[0] == PLAYER_HAND:
            # draw Player's hand until the card that is now first in the queue is drawn
            player_hand.draw(canvas, card[1])
            
            # draw only static cards from the Dealer's hand (i.e. already finished moving)
            dealer_hand.draw(canvas, STATIC)
            
            # if after drawing the above, Player's card has become static, i.e.
            # the card which is first in the drawing_queue has reached its final position
            if player_hand.is_static(card[1]):
                
                # remove the card from the drawing queue
                drawing_queue.pop(0)
               
                # play card dealing sound                    
                play_deal_sound()

        # if the card in the drawing queue is from the Dealer's Hand
        else:
            # apply the reverse logic to the one shown above for the Player's Hand
            dealer_hand.draw(canvas, card[1])
            player_hand.draw(canvas, STATIC)
            if dealer_hand.is_static(card[1]):
                drawing_queue.pop(0)
                play_deal_sound()

                # also check if there are ANY cards left in the drawing queue
                if not any(drawing_queue):
                    # if the card dealing is over, clear the temporary message
                    message_tmp = ""

    # if the drawing queue is empty the game is over, or has not yet started
    # this is a good time to display things like messages or update scores
    else:
        # just draw whatever is on the Hands
        dealer_hand.draw(canvas)
        player_hand.draw(canvas)

        # also draw the message (if there is any)
        if message:
            draw_text_box(canvas, message)
            
        # if the game state is one of the "winning", i.e. game is over,
        # the scores need to be updated now (and not earlier, otherwise
        # the score will be updated before cards finished moving)
        if game_state == PLAYER_WON or game_state == DEALER_WON:
            score[game_state - 3] += 1
            game_state = NEW

    # the temporary message should be displayed if present no matter
    # if there is a drawing queue or not
    if message_tmp:
        draw_text_box(canvas, message_tmp)


# init frames and buttons
frame = simplegui.create_frame("Blackjack", CANVAS_SIZE[0], CANVAS_SIZE[1])
frame.set_canvas_background("Green")
frame.add_button("Deal", deal, 200)
frame.add_label("")
frame.add_label("")
frame.add_label("")
frame.add_button("Hit",  hit, 200)
frame.add_label("")
frame.add_button("Stand", stand, 200)
frame.add_label("")
frame.add_label("")
frame.add_label("")
frame.add_label("")
frame.add_label("")
frame.add_label("")
frame.add_button("New Game", start_new, 200)
frame.set_draw_handler(draw)

# init deck and hands (because we don't immediately deal but have to draw)
deck = Deck(DECK_POS)
player_hand = Hand(PLAYER_POS, MOVE_RATE)
dealer_hand = Hand(DEALER_POS, MOVE_RATE)

# start things rolling
frame.start()
