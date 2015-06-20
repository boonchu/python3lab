# template for "Stopwatch: The Game"
import simplegui

# define global variables
running_time = 0
width = 500
height = 200
interval = 1 
hit_stop_counts = 0
whole_second_counts = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
# form A:BC.D where A, C and D are digits in the 
# range 0-9 and B is in the range 0-5
#
# Test Case:
#    format(0) = 0:00.0
#    format(11) = 0:01.1
#    format(321) = 0:32.1
#    format(613) = 1:01.3
def format(t):
    tenths = t % 10
    t //= 10
    sec = t % 60
    t //= 60
    min = t
    return '%d:%02d.%d' % (min, sec, tenths)

# define event handler for timer with 0.1 sec interval
# This integer will keep track of the time in tenths 
# of seconds.
def tick():
    global running_time
    global interval
    
    if timer.is_running():
        running_time += interval
    # print format(running_time)
    return True
    
# draws the current time (simply as an integer, 
# you should not worry about formatting it
# yet) in the middle of the canvas.
# 
# Insert a call to the format function into your 
# draw handler to complete the stopwatch
#
# add to two numerical counters that keep track of the 
# number of times that you have stopped the watch and 
# how many times you manage to stop the watch on a 
# whole second (1.0, 2.0, 3.0, etc.). 
#
# These counters should be drawn in the upper right-hand 
# part of the stopwatch canvas in the form "x/y" where 
# x is the number of successful stops and y is number 
# of total stops.
#
def update_time(canvas):
    global running_time
    global hit_stop_counts
    global whole_second_counts
    canvas.draw_text(format(running_time), \
                     [100, 120], 120, "Red")
    canvas.draw_text((str(whole_second_counts) + "/" \
                     + str(hit_stop_counts)), \
                     [455, 27], 20, "Yellow")
    
# define event handlers for buttons; "Start", "Stop", "Reset"
# Add "Start" and "Stop" buttons whose event handlers start and 
# stop the timer. Next, add a "Reset" button that stops the timer 
# and reset the current time to zero. The stopwatch should be 
# stopped when the frame opens.
def start_time():
    global timer
    global running_time
    if not timer.is_running():
        timer.start()
    else:
        pass

def stop_time():
    global timer
    global running_time    
    global hit_stop_counts
    global whole_second_counts
    if timer.is_running():
        timer.stop()
        if running_time % 10 == 0:
            whole_second_counts += 1
        hit_stop_counts += 1

def reset_time():
    global timer
    global running_time 
    global hit_stop_counts
    global whole_second_counts
    running_time = 0
    hit_stop_counts = 0
    whole_second_counts = 0
    timer.stop()

    # create frame
frame = simplegui.create_frame("Stop Timer", width, height)


# Construct a timer with an associated interval of 0.1 seconds 
# whose event handler increments a global integer.
# create_timer takes the interval specified in milliseconds
timer = simplegui.create_timer(100, tick)

frame.set_draw_handler(update_time)

# register event handlers
frame.add_button('Start', start_time, 50)
frame.add_button('Stop', stop_time, 50)
frame.add_button('Reset', reset_time, 50)


# start frame
frame.start()

# Please remember to review the grading rubric


