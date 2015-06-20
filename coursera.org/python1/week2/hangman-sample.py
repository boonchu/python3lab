''' 
Hangman - Game
If you are not familiar with this game,
please visit http://en.wikipedia.org/wiki/Hangman_(game)
for more information.  In Summary:
- The object of the game is to guess a secret word.
- You can have upto 5 misses before you lose
'''

import simplegui
import random

# initialize global variables used in your code
secret_words = ['apple', 'balloon', 'cutlery', 'driver', 'elephant'
                , 'filter', 'gasoline', 'hammock', 'internet'
                , 'jasmine', 'knife', 'listing', 'machine'
                , 'nimble', 'ostrich', 'penguin', 'qualify'
                , 'river', 'sandwich', 'travel', 'unicorn'
                , 'violet', 'walrus', 'xylophone', 'yellow'
                , 'zebra']
num_misses = 0
the_guess = 0
valid_characters = "abcdefghijklmnopqrstuvwxyz"
user_guesses = ""
the_mask = ""

#used for hangman graphic
head = "Black"
body = "Black"
left_arm = "Black"
right_arm = "Black"
left_leg = "Black"
right_leg = "Black"
left_palm = "Black"
right_palm = "Black"
left_foot = "Black"
right_foot = "Black"

#used for displaying won/lost message
you_won = "Black"
you_lost = "Black"
you_won_counter = 0
you_lost_counter = 0

# helpr function to initialize game
def init():    
    #reset the number of guesses since this is a new game    
    global num_misses
    num_misses = 0
    #reset users guesses since this is a new game
    global user_guesses
    user_guesses = ""
    #reset messages and hangman drawing
    global head, body, left_arm, right_arm, left_leg
    global right_leg, left_palm, right_palm, left_foot
    global right_foot, you_won, you_lost
    global you_won_counter, you_lost_counter
    
    head = "Black"
    body = "Black"
    left_arm = "Black"
    right_arm = "Black"
    left_leg = "Black"
    right_leg = "Black"
    left_palm = "Black"
    right_palm = "Black"
    left_foot = "Black"
    right_foot = "Black"
    you_won = "Black"
    you_lost = "Black"
    you_won_counter = 0
    you_lost_counter = 0
    
    #console only
    #print game banner
    print "\n*** H-A-N-G-M-A-N ***"
    print "Number of Misses: ", num_misses, "(6, you lose)"
    
    #set a random word for this game
    global the_guess    
    the_guess = random.randint(0, 25)
    print_mask()
    
#helper function to print a mask for the user
#to aid in showing the progress he/she has made
def print_mask():
    #let's drop some hints for the user
    global the_mask
    the_mask = ""
    
    for x in range(0,len(secret_words[the_guess])):
        if(user_guesses.find(secret_words[the_guess][x]) >= 0):
           the_mask += " " + secret_words[the_guess][x] + " "
        else:
           the_mask += " _ "
    print "Secret Word:", the_mask
    
#helper function to check if the user won
def user_has_won():
    user_won = True
    for x in range(0,len(secret_words[the_guess])):
        #loop through the letters in the secret word...
        #if you can't find any of the letters in the secret word
        #in the user_guesses list, the user hasn't won yet
        if(user_guesses.find(secret_words[the_guess][x]) < 0):
           user_won = False
    return user_won

#helper function to draw hangman
def draw_hangman():
    if(num_misses == 1):
        global head
        head = "Red"
    elif(num_misses == 2):
        global body
        body = "Red"
    elif(num_misses == 3):
        global left_arm
        left_arm = "Red"
        global left_palm
        left_palm = "Blue"
    elif(num_misses == 4):
        global right_arm
        right_arm = "Red"
        global right_palm
        right_palm = "Blue"
    elif(num_misses == 5):
        global left_leg
        left_leg = "Red"
        global left_foot
        left_foot = "Blue"
    else:
        global right_leg
        right_leg = "Red"
        global right_foot
        right_foot = "Blue"
        
# define event handlers for control panel
def get_input(guess):
    #clear out the textbox so the user
    #doesn't have to to enter the next guess
    txtGuess.set_text("")
    
    global user_guesses
    global num_misses
    
    #make the input lower case (for ease of error-checking)
    guess = guess.lower()
    
    '''first let's make sure that the input that 
    the user made is a valid entry'''
    
    # did the user enter one character exactly
    if len(guess) != 1:
        print "Please enter a single letter"
        return None
    elif valid_characters.find(guess) < 0:
        print "Please enter a valid letter (a-z)"
        return None
    elif user_guesses.find(guess) >= 0:
        print "You already guessed " + guess + ". Please try something else."
        return None
    else:        
        #add this letter to already_guessed
        user_guesses += guess
        
    #commentary
    print "You Guessed:", guess
    print "Number of misses:", num_misses
    
    #how did they do?
    if(secret_words[the_guess].find(guess) >= 0):
        print "Great!", "\n"
        print_mask()
        print ""
    else:
        print "Sorry! Try again!", "\n"
        print_mask()
        
        #update the number of guesses the user has made
        num_misses += 1                      
        
        #draw another hangman part
        draw_hangman()
        
        #if they ran out of guesses...
        if(num_misses >= 6 and not user_has_won()):
            print "Sorry, you lost.\nThe secret word was ", secret_words[the_guess]
            global you_lost_counter
            you_lost_counter = 5
            timerLost.start();
            return None
    
    if(user_has_won()):
        print "You Won! Congratulations!!"
        global you_won_counter
        you_won_counter = 80
        timerWon.start();
              
# Handler to draw on canvas
def draw(canvas):
    canvas.draw_text("*** H-A-N-G-M-A-N ***", [50,112], 48, "Red")
    canvas.draw_text("Number of Misses: " + str(num_misses) + " (6, you lose)", [50,412], 36, "Red")
    canvas.draw_text("Secret Word: " + the_mask, [50, 372], 36, "Green")
    
    #draw the post for the hanging man
    #main pole
    canvas.draw_line((300, 150), (300, 325), 2, "Yellow")
    #base
    canvas.draw_line((275, 325), (325, 325), 2, "Yellow")
    #over-hang
    canvas.draw_line((300, 150), (350, 150), 2, "Yellow")
    #noose
    canvas.draw_line((350, 150), (350, 170), 2, "Yellow")
    
    #setup the hang-man in pieces 
    canvas.draw_circle((350, 185), 16, 2, head)
    #torso
    canvas.draw_line((350, 200), (350, 250), 2, body)
    #left arm
    canvas.draw_line((350, 200), (325, 225), 2, left_arm)
    #right arm
    canvas.draw_line((350, 200), (375, 225), 2, right_arm)
    #left leg
    canvas.draw_line((350, 250), (325, 280), 2, left_leg)
    #right leg
    canvas.draw_line((350, 250), (375, 280), 2, right_leg)
    #palm on left
    canvas.draw_circle((325, 225), 4, 2, left_palm)
    #palm on right
    canvas.draw_circle((375, 225), 4, 2, right_palm)
    #left foot
    canvas.draw_circle((325, 275), 4, 2, left_foot)
    #right foot
    canvas.draw_circle((375, 275), 4, 2, right_foot)
    
    #You Won Message
    canvas.draw_text("CONGRATS, YOU WON!", [50,60], 48, you_won)
    
    #You Lost Message
    canvas.draw_text("SORRY YOU LOST!", [50,500], 60, you_lost)
    
# timer handler - when user wins
def show_you_won():
    global you_won_counter, you_won
    #decrement counter
    you_won_counter -= 1
    #change message color
    if(you_won == "Black"):
        you_won = "White"
    else:
        you_won = "Black"
    
    if(you_won_counter <= 0):
        timerWon.stop()
        init() #start new game
        
# timer handler - when user looses
def show_you_lost():
    global you_lost_counter, you_lost
    #decrement counter
    you_lost_counter -= 1
    #change message color
    if(you_lost == "Black"):
        you_lost = "White"
    else:
        you_lost = "Black"
    
    if(you_lost_counter <= 0):
        timerLost.stop()
        init() #start new game
        
# create frame
f = simplegui.create_frame("Hangman", 600, 600)

# register event handlers for control elements
txtGuess = f.add_input("Guess a Letter:", get_input, 200)
timerWon = simplegui.create_timer(100, show_you_won)
timerLost = simplegui.create_timer(1000, show_you_lost)
button = f.add_button("New Game", init)

f.set_draw_handler(draw)

# start frame
f.start()
# start game
init()
