#! /usr/bin/env python

import simplegui

class Ship:
    def __init__(self):
        pass
    
    def set_angle_vel(self, vel):
        print "set_angle_vel", vel
        
    def set_thrust(self, val):
        print "set_thrust", val
        
    def shoot(self):
        print "shoot"
    
my_ship = Ship()
ang_vel = 1

# key down
inputs_down = {"left": [my_ship.set_angle_vel, -ang_vel],
                "right": [my_ship.set_angle_vel, ang_vel],
                "up": [my_ship.set_thrust, True],
                "space": [my_ship.shoot]}

def keydown(key):
    for i in inputs_down:
        if key == simplegui.KEY_MAP[i]:
                inputs_down[i][0](*inputs_down[i][1:])
            
# key up
inputs_up = {"left": [my_ship.set_angle_vel, 0],
                "right": [my_ship.set_angle_vel, 0],
                "up": [my_ship.set_thrust, False]}

def keyup(key):
    for i in inputs_up:
        if key == simplegui.KEY_MAP[i]:
            inputs_up[i][0](inputs_up[i][1])
            
            # Handler to draw on canvas
def draw(canvas):
    pass

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 300, 200)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()
