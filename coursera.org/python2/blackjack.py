# Mini-project #6 - Blackjack
# https://class.coursera.org/interactivepython2-003/human_grading/view/courses/974687/assessments/33/submissions
# Boonchu Ngampairoijpibul
# Date: July 23rd 2015

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, 
                    CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], 
                    CARD_SIZE)
        
        
# define hand class
class Hand:
    global outcome, in_play
    
    # create Hand object
    def __init__(self, name):
        self.name  = name
        self.cards = []
    
    # return a string representation of a hand
    def __str__(self):
        hand = "Hand contains "
        
        for card in self.cards:
            hand += str(card) + " "
        
        return hand
    
    # add a card object to a hand
    def add_card(self, card):
        self.cards.append(card)
    
    # compute the value of the hand
    # Implement the get_value method for the Hand class. You should use 
    # the provided VALUE dictionary to look up the value of a single card 
    # in conjunction with the logic explained in the video lecture for 
    # this project to compute the value of a hand. 
    def get_value(self):
        value = 0
        aces = False
        
        for card in self.cards:
            value += VALUES[card.get_rank()]
            if card.get_rank() == 'A':
                aces = True
        if aces and (value + 10) <= 21:
                return value + 10
        return value
    
    # draw a hand on the canvas
    # Implement your own draw method for the Hand class using the draw 
    # method of the Card class. We suggest drawing a hand as a horizontal 
    # sequence of cards where the parameter pos is the position of the 
    # upper left corner of the leftmost card. 
    # 
    # Add logic using the global variable in_play that keeps track of whether 
    # the player's hand is still being played. If the round is still in play, 
    # you should draw an image of the back of a card (provided in the template) 
    # over the dealer's first (hole) card to hide it. Once the round is over, 
    # the dealer's hole card should be displayed.
    def draw(self, canvas, pos):
        for i in range(len(self.cards)):
            cards = str(self.cards[i])            
            card = Card(cards[0], cards[1])
            if self.name == 'dealer' and i == 0 and in_play:
                canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE,
                    [pos[0] + CARD_BACK_CENTER[0], pos[1] + CARD_BACK_CENTER[1]],
                    CARD_BACK_SIZE)
            else:
                card.draw(canvas, [pos[0] + i*40, pos[1]])
    
# define deck class 
class Deck:
    # create a Deck object
    def __init__(self):
        self.cards = []
        self.current_pos = 0
        
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(suit, rank))
    
    # shuffle the deck
    def shuffle(self):
        # use random.shuffle()
        self.current_pos = 0
        random.shuffle(self.cards)
    
    # deal a card object from the deck
    def deal_card(self):
        self.current_pos -= 1
        return self.cards[self.current_pos]
    
    # return a string representing the deck
    def __str__(self):
        deck = 'Deck contains '
        for card in self.cards:
            deck += str(card) + " "
        return deck

# define event handlers for buttons
# Implement the handler for a "Deal" button that shuffles the deck and deals 
# the two cards to both the dealer and the player. The event handler deal 
# for this button should shuffle the deck (stored as a global variable), 
# create new player and dealer hands (stored as global variables), and 
# add two cards to each hand. To transfer a card from the deck to a hand, 
# you should use the deal_card method of the Deck class and the add_card 
# method of Hand class in combination. The resulting hands should be printed 
# to the console with an appropriate message indicating which hand is which.
#
# Modify the logic for the "Deal" button to create and shuffle a new deck 
# (or restock and shuffle an existing deck) each time the "Deal" button 
# is clicked. This change avoids the situation where the deck becomes 
# empty during play.
#
# Finally, modify the deal function such that, if the "Deal" button is 
# clicked during the middle of a round, the program reports that the 
# player lost the round and updates the score appropriately.
deck = Deck()
player = Hand('player')
dealer = Hand('dealer')

def deal():
    global outcome, in_play, player, dealer, deck, score

    if in_play:
        in_play = False
        score -= 1
    # your code goes here
    outcome = 'Hit or stand?'
    
    player.cards = []
    dealer.cards = []
    
    deck.shuffle()

    player.add_card(deck.deal_card())
    player.add_card(deck.deal_card())
    print player.name,' -> ',player
    
    dealer.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    print dealer.name, ' ->',dealer
    
    in_play = True

# Implement the handler for a "Hit" button. If the value of 
# the hand is less than or equal to 21, clicking this button 
# adds an extra card to player's hand. 

# If the value exceeds 21 after being hit, 
# print "You have busted".
def hit():
    global outcome, in_play, player, dealer, deck, score
    # if the hand is in play, hit the player   
    if in_play:
        player.add_card(deck.deal_card())
        print player.name, ' hit ', player
        # if busted, assign a message to outcome, 
        # update in_play and score
        if player.get_value() > 21:
            outcome = "You have busted, new deal?"
            in_play = False
            score -= 1
    

# Implement the handler for a "Stand" button. If the player 
# has busted, remind the player that they have busted. 
# Otherwise, repeatedly hit the dealer until his hand has 
# value 17 or more (using a while loop). If the dealer 
# busts, let the player know. Otherwise, compare the 
# value of the player's and dealer's hands. If the value of 
# the player's hand is less than or equal to the dealer's 
# hand, the dealer wins. Otherwise the player has won. 
# Remember the dealer wins ties in our version.
# 
# Add a score counter that keeps track of wins and losses 
# for your Blackjack session. In the simplest case 
# (see our demo), the program displays wins minus losses. 
# However, you are welcome to implement a more sophisticated 
# betting/scoring system.
def stand():
    global outcome, in_play, player, dealer, deck, score
   
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if in_play:
        in_play = False
        if player.get_value() > 21:
            outcome = 'You gave busted'
            score -= 1
        else:
            # assign a message to outcome, update in_play and score
            while (dealer.get_value() < 17):
                dealer.add_card(deck.deal_card())
            if dealer.get_value() > 21 or dealer.get_value() < player.get_value():
                outcome = 'You are won'
                score += 1
            elif dealer.get_value() >= player.get_value():
                outcome = 'You are busted, new deal?'
                score -= 1
                
        print dealer.name, ' -> ', dealer
        print player.name, ' -> ', player
        print outcome
    

# draw handler    
# Replace printing in the console by drawing text messages on the canvas. 
# We suggest adding a global outcome string that is drawn in the draw 
# handler using draw_text. These messages should prompt the player to 
# take some require action and have a form similar to "Hit or stand?" 
# and "New deal?". Also, draw the title of the game, "Blackjack", 
# somewhere on the canvas.
def draw(canvas):
    global outcome, in_play, player, dealer, deck, score
    # test to make sure that card.draw works, replace with your code below
    outcome_attribute = ([150, 500], 24)
    
    #card = Card("D", "K")
    #card.draw(canvas, [300, 300])
    
    canvas.draw_text('Blackjack', [180, 40], 48, 'Black', 'monospace')
    canvas.draw_text('player', [80, 90], 24, 'Black', 'monospace')
    canvas.draw_text('dealer', [80, 340], 24, 'Black', 'monospace')
    canvas.draw_text(outcome, outcome_attribute[0], outcome_attribute[1], 'Blue', 'monospace')   
    score_text = ''
    if score < 0:
        score_text = 'Player Lose ' + str(score)
    else:
        score_text = 'Player Won ' + str(score)
    canvas.draw_text(score_text, [150, 250], 35, "Yellow", 'monospace')   
    player.draw(canvas, [100, 100])
    dealer.draw(canvas, [100, 350])

    # initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# In our version of Blackjack, a hand is automatically 
# dealt to the player and dealer when the program starts.
# In particular, the program template includes a call 
# to the deal() function during initialization.
deal()
outcome = 'Hit or stand?'
frame.start()
