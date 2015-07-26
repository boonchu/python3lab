#! /usr/bin/env python

inputs = { 
	"up": 	[1,-2],
	"down": [1, 2],
	"w":	[0,-2],
	"s":	[0, 2]
}

def keypressed(key)
	for i in inputs:
		if key == simplegui.KEY_MAP[i]:
			paddle_vel[inputs[i][0]] += inputs[i][1]
