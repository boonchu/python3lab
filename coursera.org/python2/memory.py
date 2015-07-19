# implementation of card game - Memory
# Coursera 
# An Introduction to Interactive Programming in Python (Part 2)
# Boonchu Ngampairoijpibul - 07/18/2015 2:38 PM PDT
# change log: 
# * moves all tracking metric/counts to mouse operation
# * clean states after reset

import simplegui
import random

# Panel size
HEIGHT = 100
WIDTH  = 800

# Each card size
CARD_HEIGHT = 100
CARD_WIDTH  = 50

# Each text size
TEXT_SIZE = 70

# card's correctly turning 
turned = 0

# 7.
# You now need to add game logic to the mouse click handler for selecting 
# two cards and determining if they match. We suggest following the game logic 
# in the example code discussed in the Memory video. 
# State 0 corresponds to the start of the game. 
# In state 0, if you click on a card, that card is exposed, and you switch to state 1. 
# State 1 corresponds to a single exposed unpaired card. In state 1, if you click 
# on an unexposed card, that card is exposed and you switch to state 2. 
# State 2 corresponds to the end of a turn. In state 2, if you click on an unexposed 
# card, that card is exposed and you switch to state 1.
CARD_STATE = { 'unflipped':0, 'flipped':1, 'exposed':2 }

# 1.
# Model the deck of cards used in Memory as a list consisting of 16 numbers 
# with each number lying in the range [0,8) and appearing twice. We suggest 
# that you create this list by concatenating two list with range [0,8) together.
cards = range(0, 8) + range(0, 8)

# 3.
# Shuffle the deck using random.shuffle(). Remember to debug your canvas 
# drawing code before shuffling to make debugging easier.
random.shuffle(cards)

# 4.
# To implement this behavior, we suggest that you create a second list called exposed. 
# In the exposed list, the ith entry should be True if the ith card is face up and its 
# value is visible or False if the ith card is face down and it's value is hidden.
# 
# 6.
# Modify the event handler for mouse clicks to flip cards based on the location of the 
# mouse click. If the player clicked on the ith card, you can change the value of 
# exposed[i] from False to True. If the card is already exposed, you should ignore 
# the mouseclick. At this point, the basic infrastructure for Memory is done.
exposed = list()

# list of utilities functions
# * find the card size
# * find text position on card
# * find mouse position on card
def card_size(i, width, height):
    return (
                [i * width, 0], 
                [(i+1) * height, 0], 
                [(i+1) * width, height], 
                [i * width, height]
           )

def text_pos_on_card(i, width, height):
    return [ 
                ((i * width) + (height / 2) - 45), height - 30
    ]

def is_mouse_in_card(pos, card):
    #print "%d < %d < %d" % (card['CARD_SIZE'][0][0], pos[0], card['CARD_SIZE'][2][0])
    return (card['CARD_SIZE'][0][0] <= pos[0]) and (card['CARD_SIZE'][2][0] >= pos[0])

def clear_flipped(doc):
    for i in range(len(doc)):
        if not doc[i]['FLIPPED'] is CARD_STATE['exposed']:            
            doc[i]['FLIPPED'] = CARD_STATE['unflipped']
            #print "clear flipped state (if not exposed): (%d, %d)" % (doc[i]['CARD_VALUE'], doc[i]['FLIPPED'])

def set_exposed(doc, exposed):    
    if len(exposed) == 2 and exposed[0] == exposed[1]:
        #print "set_exposed (if in exposed and 2 exposed): ", exposed
        for i in range(len(doc)):
           if doc[i]['CARD_VALUE'] in exposed:
              doc[i]['FLIPPED'] = CARD_STATE['exposed']
            
# Deck Of Cards
doc = list()
def deck_of(cards):
    deck = []
    i=0
    for i in range(len(cards)):
        card = {	
                'CARD_SIZE': card_size(i, CARD_WIDTH, CARD_HEIGHT), 
                'DUMMY':1, 
                'CARD_BORDER':'White', 
                'CARD_COLOR':'Green', 
                'CARD_VALUE':cards[i], 
                'TEXT_POSITION': text_pos_on_card(i, CARD_WIDTH, CARD_HEIGHT), 
                'TEXT_COLOR': "Green",
                'TEXT_FONT': "monospace",
                'FLIPPED': CARD_STATE['unflipped'],
        }
        deck.append(card)
    return deck

# 10.
# Finally, implement the new_game() function (if you have not already) so that 
# the "Reset" button reshuffles the cards, resets the turn counter and restarts 
# the game. All cards should start the game hidden.
# 
# 11.
# 1 pt - The game includes a "Reset" button that resets the turn counter and 
# restarts the game.
# 
# 12.
# 1 pt - The deck is also randomly shuffled each time the "Reset" button is 
# pressed, so that the cards are in a different order each game.
def new_game():
    global doc, cards, frame, turned, exposed
    
    turned = 0
    exposed = list()
    cards = range(0, 8) + range(0, 8)
    random.shuffle(cards)
    doc = list()
    doc = deck_of(cards)
    frame.set_draw_handler(draw)
            
# define event handlers
# 5.
# Now, add functionality to determine which card you have clicked on with your mouse. 
# Add an event handler for mouse clicks that takes the position of the mouse click 
# and prints the index of the card that you have clicked on to the console. 
# 
# To make determining which card you have clicked on easy, we suggest sizing the 
# canvas so that the sequence of cards entirely fills the canvas.

# 6.
# Modify the event handler for mouse clicks to flip cards based on the location of 
# the mouse click. If the player clicked on the ith card, you can change the value 
# of exposed[i] from False to True. If the card is already exposed, you should ignore 
# the mouseclick. At this point, the basic infrastructure for Memory is done.

# checklist:
# 1 pt - The game correctly updates and displays the number of turns in the 
# current game in a label displayed in the control area. The counter may be 
# incremented after either the first or second card is flipped during a turn.
def mouseclick(pos):
    # add game state here
    global doc, exposed, turned, is_exposed
        
    for i in range(len(doc)):
        if is_mouse_in_card(pos, doc[i]):
                print "mouse click position : %d < %d < %d" % (doc[i]['CARD_SIZE'][0][0], pos[0], doc[i]['CARD_SIZE'][2][0])
                print "before mouse click : (%d, %d)" % (doc[i]['CARD_VALUE'], doc[i]['FLIPPED'])

                if doc[i]['FLIPPED'] is CARD_STATE['unflipped']:
                    print "after mouse click and flipped card : (%s, %d, %d)" % (exposed, doc[i]['CARD_VALUE'], doc[i]['FLIPPED'])
                    doc[i]['FLIPPED'] = CARD_STATE['flipped']

                    if not doc[i]['CARD_VALUE'] is exposed:
                        if len(exposed) <2:
                            print "detect here 1 (turn count++)", exposed
                            turned += 1
                        else:
                            print "detect here 1 (do nothing)", exposed
                            
                    if len(exposed) < 2:
                        print "detect here (before <2)", exposed
                        exposed.append(doc[i]['CARD_VALUE'])
                        print "detect here (after <2)", exposed
                    elif len(exposed) == 2:                        
                        if not exposed[0] is exposed[1]:
                            print "detect here (before !=2)", exposed
                            exposed = list()
                            clear_flipped(doc)
                            exposed.append(doc[i]['CARD_VALUE'])
                            doc[i]['FLIPPED'] = CARD_STATE['flipped']
                            print "detect here (after !=2)", exposed
                        else:
                            print "detect here (before ==2)", exposed
                            set_exposed(doc, exposed)
                            exposed = list()
                            exposed.append(doc[i]['CARD_VALUE'])
                            print "detect here (after ==2)", exposed
                    else:
                        print "detect here (before >2)", exposed
                        exposed = list()
                        clear_flipped(doc)
                        exposed.append(doc[i]['CARD_VALUE'])
                        print "detect here (after >2)", exposed
                    
                    break 
                elif doc[i]['FLIPPED'] is CARD_STATE['flipped']:
                    print "after mouse click and FLIPPED : (%s, %d, %d)" % (exposed, doc[i]['CARD_VALUE'], doc[i]['FLIPPED'])
                elif doc[i]['FLIPPED'] is CARD_STATE['exposed']:
                    print "after mouse click and EXPOSED : (%s, %d, %d)" % (exposed, doc[i]['CARD_VALUE'], doc[i]['FLIPPED'])
                        
# cards are logically 50x100 pixels in size    
# 2.
# Write a draw handler that iterates through the Memory deck using a for loop 
# and uses draw_text to draw the number associated with each card on the canvas. 
# The result should be a horizontal sequence of evenly-spaced numbers drawn on 
# the canvas.

# 4.
# modify the draw handler to either draw a blank green rectangle or the card's 
# value.  To implement this behavior, we suggest that you create a second list 
# called exposed. In the exposed list, the ith entry should be True if the ith 
# card is face up and its value is visible or False if the ith card is face 
# down and it's value is hidden. We suggest that you initialize exposed to 
# some known values while testing your drawing code with this modification.
# https://class.coursera.org/interactivepython2-003/forum/thread?thread_id=4

# 8.
# Note that in state 2, you also have to determine if the previous two cards are 
# paired or unpaired. If they are unpaired, you have to flip them back over 
# so that they are hidden before moving to state 1. We suggest that you use 
# two global variables to store the index of each of the two cards that were
# clicked in the previous turn.

# 9.
# Add a counter that keeps track of the number of turns and uses set_text to 
# update this counter as a label in the control panel. (BTW, Joe's record is 
# 12 turns.)  This counter should be incremented after either the first or 
# second card is flipped during a turn.

def draw(canvas):
    global doc, turned

    # draws a Deck Of Cards
    for i in range(len(doc)):
        canvas.draw_polygon(
                doc[i]['CARD_SIZE'], doc[i]['DUMMY'], 
                doc[i]['CARD_BORDER'], doc[i]['CARD_COLOR']
        )
                         
        if not doc[i]['FLIPPED'] is CARD_STATE['unflipped']:
                #print exposed
                #print "(%d, %d)" % (doc[i]['CARD_VALUE'], doc[i]['FLIPPED'])
                doc[i]['TEXT_COLOR']  = 'Green'
                doc[i]['CARD_BORDER'] = 'Black'
                doc[i]['CARD_COLOR']  = 'White'
        else:
                doc[i]['TEXT_COLOR']  = 'Green'
                doc[i]['CARD_BORDER'] = 'White'
                doc[i]['CARD_COLOR']  = 'Green'
                        
        canvas.draw_text(
                str(doc[i]['CARD_VALUE']), 
                doc[i]['TEXT_POSITION'], 
                TEXT_SIZE, 
                doc[i]['TEXT_COLOR'], 
                doc[i]['TEXT_FONT']
        )
    
    label.set_text("Turns = %s" % str(turned))

             
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", WIDTH, HEIGHT)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# get things rolling
new_game()

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

frame.start()


# Always remember to review the grading rubric
