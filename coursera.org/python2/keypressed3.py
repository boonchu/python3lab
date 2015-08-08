#! /usr/bin/env python

import simplegui

WIDTH = 50
HEIGHT = 50

def my_function1(arg1, arg2, arg3):
    print "Output from my_function1: ", arg1, arg2, arg3
    
def my_function2(arg1, arg2, arg3):
    print "Output from my_function2: ", arg1, arg2, arg3

def my_function3(arg1, arg2, arg3):
    print "Output from my_function3: ", arg1, arg2, arg3

down_inputs = {"up":   (my_function1, 'You', 'pressed', 'up'),
               "left": (my_function2, 'You', 'pressed', 'left'),
               "right":(my_function3, 'You', 'pressed', 'right')}
def keydown(key):
    for i,val in down_inputs.items():
        if key == simplegui.KEY_MAP[i]:
            val[0](val[1], val[2], val[3])

up_inputs = {"up":   (my_function1, 'button', 'up', 'up'),
             "left": (my_function2, 'button', 'up', 'left'),
             "right":(my_function3, 'button', 'up', 'right')}
def keyup(key):
    for i,val in up_inputs.items():
        if key == simplegui.KEY_MAP[i]:
            val[0](val[1], val[2], val[3])
            
frame = simplegui.create_frame("Input Example", WIDTH, HEIGHT)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

frame.start()
