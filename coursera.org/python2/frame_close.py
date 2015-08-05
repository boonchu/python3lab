# CodeSkulptor runs Python programs in your browser.
# Click the upper left button to run this simple demo.

# CodeSkulptor runs in Chrome 18+, Firefox 11+, and Safari 6+.
# Some features may work in other browsers, but do not expect
# full functionality.  It does NOT run in Internet Explorer.

# https://class.coursera.org/interactivepython2-003/forum/thread?thread_id=834

import simplegui

#create a Frame unload_handler routine
def unload_timer_check():
    try:
        t = frame.get_canvas_textwidth("t",12)
    except:
        t = 0
    if t==0:
        unload();
        unload_timer.stop()

message = "Welcome!"

# Handler for mouse click
def click():
    global message
    message = "Good job!"

# Handler to draw on canvas
def draw(canvas):
    canvas.draw_text(message, [50,112], 48, "Red")
    
def unload():
    print "The frame has been closed."

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 300, 200)
frame.add_button("Click me", click)
frame.set_draw_handler(draw)

unload_timer = simplegui.create_timer(1000,unload_timer_check)
unload_timer.start()

# Start the frame animation
frame.start()

