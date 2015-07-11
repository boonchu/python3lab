###### Guess Number
 * https://www.youtube.com/watch?v=40PAuHtq8o0
 * https://www.youtube.com/watch?v=AAsHKikHRdQ&feature=youtu.be

```
import simplegui

def new_game():
    global low, high, guess_count
    print
    print 'We are starting a new game.'
    print 'Think of a non-negative number less than', upper_limit
    low = 0
    high = upper_limit
    guess_count = 0
    make_guess()

def make_guess():
    global guess, guess_count
    guess = (low + high) / 2
    guess_count += 1
    print
    print 'Your number is in the range [%d, %d)' % (low, high)
    print 'My guess is:', guess

def check_limits():
    if low + 1 == high:
        game_over(low)
    else:
        make_guess()
        
def game_over(answer):
    print
    print 'Your number is %d.' % answer
    print 'I got it in %d guesses.' % guess_count
    print 'Hurray! Thanks for the game.'
    
def display_response(response):
    print 'You said:', response
    
def handle_upper_limit(input_string):
    global upper_limit
    upper_limit = int(input_string)
    new_game()

def handle_higher_button():
    global low
    low = guess + 1
    display_response('higher')
    check_limits()

def handle_lower_button():
    global high
    high = guess
    display_response('lower')
    check_limits()
    
def handle_correct_button():
    display_response('correct')
    game_over(guess)
    
frame = simplegui.create_frame('Number guesser', 0, 250, 250)
frame.add_label('Upper limit:')
frame.add_input('', handle_upper_limit, 75)
frame.add_label('')
frame.add_label('Your response to the computer\'s guess:')
frame.add_button('higher', handle_higher_button)
frame.add_button('correct', handle_correct_button)
frame.add_button('lower', handle_lower_button)
frame.start()
```
