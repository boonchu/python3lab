# Import modules

import simplegui
import math
import time

# Define globals

t = 0
t1 = time.time()

# Definte the helper functions

def alpha(t, per):
    """
    the function returns the angle according to the speed
    of the movement. This is quantified with the help of
    per variable.
    
    The canvas is refreshed at 60 frames per second (fps)
    
    - For seconds we have 60 seconds (s) to display
    on the big dial. So the period is 60s*60fps = 3600
    
    - For thent's of seconds we have 10 0.1 seconds to
    display on the small lower dial. So the period is
    60fps*(10*0.1)s = 60
    
    - For the minutes we have 10 minutes (600s) to display
    on the big upper dial. So the period is 600s*60fps =
    36000
    """
    return (math.pi/2 - (t % per) * (math.pi / (per / 2))) % (2 * math.pi)

def x_y(center, r, offset, phi):
    """
    this function returns a set of coordinates for
    drawing the minutes, tenths, seconds and the dial
    markings. It need the center coordonates, the radius,
    an offset and an angle
    """
    
    x1 = center[0] + (r - offset) * math.cos(phi)
    y1 = center[1] - (r - offset) * math.sin(phi)
    x2 = x1 + offset * math.cos(phi)
    y2 = y1 - offset * math.sin(phi) 
    return [[x1, y1], [x2, y2]]

def draw_clock(canvas, r, center):
    """
    this function draws the big dial
    """
    
    color = "Gray"
    canvas.draw_circle(center, r, 6, color, 'White')
    
    phi = 0
    for i in range(12):
        coord = x_y(center, r, 15, phi)
        canvas.draw_line(coord[0], coord[1], 2, "Black")
        sub_phi = phi
        for j in range(4):
            sub_phi = sub_phi + math.pi / 30
            coord1 = x_y(center, r, 8, sub_phi)
            canvas.draw_line(coord1[0], coord1[1], 1, color)
            j += 1
            
        phi = phi + math.pi / 6
        i += 1

        
def draw_dial(canvas, r, center, color):
    """
    this function helps drawing the small dials
    """
    canvas.draw_circle(center, r, 2, color, 'White')
    phi = math.pi / 10
    for i in range(10):
        coord = x_y(center, r, 6, phi)
        canvas.draw_line(coord[0], coord[1] , 1, color)
        phi = phi + math.pi / 5
        i += 1
        
# Define the event handlers

def analog_clock(canvas):
    """
    it draws an analog clock with 3 dials. The big dial
    counts the seconds, the small dial from the lower part
    counts the tenth's of second and the small dial from
    the upper part counts the minutes
    """
    global t
    
    # radius of big clock
    r_s = 105
    
    # radius of small dials
    r_d = 30
    center = [150, 150]
    
    draw_clock(canvas, r_s, center)
    draw_dial(canvas, r_d, [center[0], center[1] + 50], "Green")
    draw_dial(canvas, r_d, [center[0], center[1] - 50], "Blue")
    
    phi = alpha(t, 3600)
    seconds = x_y(center, r_s, 12, phi)
    canvas.draw_line(center, seconds[0], 3, 'Red')
    
    phi = alpha(t, 60)
    tenths = x_y([center[0], center[1] + 50], r_d, 10, phi)
    canvas.draw_line([center[0], center[1] + 50], tenths[0], 2, 'Red')
    
    phi = alpha(t, 36000)
    minutes = x_y([center[0], center[1] - 50], r_d, 10, phi)
    canvas.draw_line([center[0], center[1] - 50], minutes[0], 2, 'Red')
    
    if t % 3600 == 0:
        print time.time() - t1
        
    t += 1
        
# Create the frame
f = simplegui.create_frame("Analogic Clock", 300, 300)

# Register the event handlers
f.set_draw_handler(analog_clock)

# Start the frame 
f.start()

