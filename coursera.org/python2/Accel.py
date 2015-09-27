#! /usr/bin/env python

# Consider a spaceship where the ship's thrusters can accelerate the ship 
# by 10 pixels per second for each second that the thrust key is held down. 
# If the friction induces a deceleration that is 10% of the ship's velocity 
# per second, what is the maximal velocity of the ship? If you are having 
# trouble, consider writing a short program to help understand this problem. 

def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def update():
	acc  = angle_to_vector()
	vel += acc*0.1
	vel *= .90
