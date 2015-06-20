# Lazy Sunday: a brief study in handling life events
# by Barron
# https://www.youtube.com/watch?v=q8O7zgh59P4
import simplegui
import time

# Helper function that waits for 4 seconds
def fiddle_around():
    start_time = time.time()
    while (time.time() - start_time) < 4:
        pass
    return

# Handler for timer
def timer():
    print "Calling Olivia...\n"

# Handler for doorbell
def doorbell():
    fiddle_around()
    print "Opening door...\n"

# Handler for when the phone rings
def phonecall():
    print "Answering phone...\n"
    
# Create a frame and assign callbacks to event handlers
timer = simplegui.create_timer(3000, timer)
frame = simplegui.create_frame("Lazy Sunday", 100, 100)
frame.add_button("Ring Doorbell", doorbell)
frame.add_button("Call phone", phonecall)

# Start the frame
timer.start()
frame.start()

