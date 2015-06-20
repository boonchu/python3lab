import random

# Rock-paper-scissors-lizard-Spock assignment 1
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

def name_to_number(name):
    map = { 'rock':0, 'Spock':1, 'paper':2, 'lizard':3, 'scissors':4 }
    if map.has_key(name):
        return map[name]
    else:
        return None


def number_to_name(number):
    int_number = str(number)
    map = { '0':'rock', '1':'Spock', '2':'paper', '3':'lizard', '4':'scissors' }
    if map.has_key(int_number):
        return map[int_number]
    else:
        return None

def rpsls(player_choice): 
    # print a blank line to separate consecutive games
    print '\n'

    # print out the message for the player's choice
    print 'Player chooses ' + player_choice

    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 4)

    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    
    # print out the message for computer's choice
    print 'Computer chooses ' + comp_choice

    # compute difference of comp_number and player_number modulo five
    diff_number = (player_number - comp_number) 
    diff = diff_number % 5

    # use if/elif/else to determine winner, print winner message
    # debug - print "%d %d" % (diff_number, diff)
    # use https://class.coursera.org/interactivepython1-003/forum/thread?thread_id=440

    if (diff == 1 or diff == 2):
        print 'Player wins!'
    elif (diff_number == 0 and diff == 0):
        print 'Player and computer tie!'
    elif (diff == 3 or diff == 4):
        print 'Computer wins!'
    else:
        print 'Unknown condition!'
        
# Test Cases
    
###################################################
# Test calls to name_to_number()
#print name_to_number("rock")
#print name_to_number("Spock")
#print name_to_number("paper")
#print name_to_number("lizard")
#print name_to_number("scissors")

###################################################
# Test calls to number_to_name()
#print number_to_name(0)
#print number_to_name(1)
#print number_to_name(2)
#print number_to_name(3)
#print number_to_name(4)
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE

rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric



