te for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

# any secret number in the range [low, high) can always be found in
# at most n guesses where n is the smallest integer such that
# 2 ** n >= high - low + 1
# use log to solve this: https://www.youtube.com/watch?v=TTCY1SvKNgw
# log(2 ** n) >= log(high - low + 1)
# n*log(2) >= log(high - low + 1)
# n >= log(high - low + 1) / log(2)
# n >= ceiling(log(high - low + 1) / log(2))
#
# Test Case
# how_much_guess_is(100, 0) = 7
# how_much_guess_is(1000, 0) = 10
#
def how_much_guess_is(high, low):
    return int(math.ceil(math.log(high-low)/math.log(2)))

# initalize global variables used in your code 
# use default since it calls at start of programming code
choice_max_in_range = 100
remaining_guesses = 0
secret_number = 0

# takes the input string guess, converts it to an integer, and 
# prints out a message of the form "Guess was 37"
def input_guess(guess):
    # import global variable
    global remaining_guesses
    
    if remaining_guesses == 0:
        print "You're lose!"
        print 
        new_game()
    
    # main game logic goes here	
    input = int(guess)
    print 
    print "Guess was ", input
    
    # compares the entered number to secret_number 
    # and prints out an appropriate message 
    # such as "Higher", "Lower", or "Correct".
    if secret_number > input:
        print "Higher"
        remaining_guesses -= 1
        print "Number of remaining guesses is %d" % (remaining_guesses)
        print
    elif secret_number < input:
        print "Lower"
        remaining_guesses -= 1
        print "Number of remaining guesses is %d" % (remaining_guesses)
        print
    elif secret_number == input:
        print "Correct"
        print
        new_game()
    else:
        pass
    
# helper function to start and restart the game
# initializes a global variable secret_number to be 
# a random number in the range [0, 100)
def new_game():
    # reset value of remaining_guesses to default 
    global remaining_guesses 
    remaining_guesses = how_much_guess_is(choice_max_in_range, 0) 
    
    # expressed mathematically as [low, high). So, [0, 3) means all of 
    # the numbers starting at 0 up to, but not including 3. 
    # In other words 0, 1, and 2. 
    global secret_number 
    secret_number = random.randrange(0, choice_max_in_range)
    
    # display message on right panel
    print "Start new game"
    print "Range choice is between 0 to %d" % (choice_max_in_range)
    print "Number of remaining guesses  %d" % (remaining_guesses)

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global choice_max_in_range
    choice_max_in_range = 100
    print 
    print "you push reset button to [0, 100), new game starts..."
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global choice_max_in_range
    choice_max_in_range = 1000
    print
    print "you push reset button to [0,1000), new game starts..."
    new_game()
    
# create frame
f = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements and start frame
# should add two buttons: “Range: 0 - 100” and “Range: 0 - 1000” 
# that allow the player to choose different ranges for the secret number.
f.add_button("Range is [0, 100)", range100, 200)
f.add_button("Range is [0, 1000)", range1000, 200)
f.add_input("Enter a guess", input_guess, 200)
f.start()

# call to new_game() at the bottom of the template ensures 
# that secret_number is always initialized when the program 
# starts running. 
new_game()

# always remember to check your completed program against the 
# grading rubric
# 

# Test your code by playing multiple games of “Guess the number” 
# with a fixed range.

###################################################
# Start our test #1 - assume global variable secret_number
# is the the "secret number" - change name if necessary


#secret_number = 74	
#input_guess("50")
#input_guess("75")
#input_guess("62")
#input_guess("68")
#input_guess("71")
#input_guess("73")
#input_guess("74")

###################################################
# Output from test #1
#New game. Range is from 0 to 100
#Number of remaining guesses is 7
#
#Guess was 50
#Number of remaining guesses is 6
#Higher!
#
#Guess was 75
#Number of remaining guesses is 5
#Lower!
#
#Guess was 62
#Number of remaining guesses is 4
#Higher!
#
#Guess was 68
#Number of remaining guesses is 3
#Higher!
#
#Guess was 71
#Number of remaining guesses is 2
#Higher!
#
#Guess was 73
#Number of remaining guesses is 1
#Higher!
#
#Guess was 74
#Number of remaining guesses is 0
#Correct!
#
#New game. Range is from 0 to 100
#Number of remaining guesses is 7

###################################################
# Start our test #2 - assume global variable secret_number
# is the the "secret number" - change name if necessary

#range1000()
#secret_number = 375	
#input_guess("500")
#input_guess("250")
#input_guess("375")

###################################################
# Output from test #2
#New game. Range is from 0 to 100
#Number of remaining guesses is 7
#
#New game. Range is from 0 to 1000
#Number of remaining guesses is 10
#
#Guess was 500
#Number of remaining guesses is 9
#Lower!
#
#Guess was 250
#Number of remaining guesses is 8
#Higher!
#
#Guess was 375
#Number of remaining guesses is 7
#Correct!
#
#New game. Range is from 0 to 1000
#Number of remaining guesses is 10



###################################################
# Start our test #3 - assume global variable secret_number
# is the the "secret number" - change name if necessary

#secret_number = 28	
#input_guess("50")
#input_guess("50")
#input_guess("50")
#input_guess("50")
#input_guess("50")
#input_guess("50")
#input_guess("50")

###################################################
# Output from test #3
#New game. Range is from 0 to 100
#Number of remaining guesses is 7
#
#Guess was 50
#Number of remaining guesses is 6
#Lower!
#
#Guess was 50
#Number of remaining guesses is 5
#Lower!
#
#Guess was 50
#Number of remaining guesses is 4
#Lower!
#
#Guess was 50
#Number of remaining guesses is 3
#Lower!
#
#Guess was 50
#Number of remaining guesses is 2
#Lower!
#
#Guess was 50
#Number of remaining guesses is 1
#Lower!
#
#Guess was 50
#Number of remaining guesses is 0
#You ran out of guesses.  The number was 28
#
#New game. Range is from 0 to 100
#Number of remaining guesses is 7

