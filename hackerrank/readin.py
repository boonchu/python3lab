#! /usr/bin/env python

import sys

class readin(object):
	def __init__(self):
		self.line = []

	def start(self):
		_input = sys.stdin.readlines()
		for i in _input:    
    			self.line.append(i.rstrip())

	def pan(self):
		try:
			self.line:
		execpt ValueError:	
			print "Oops! It might be empty. Try again..."
				
if __name__ == '__main__':
	x = readin()
	x.start()
	print x.line
