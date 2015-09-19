#! /usr/bin/env python

fourth_list = [ list(dummy_list) for dummy_list in [[0] * 4] * 4]
print "Fourth try, original list:"
print fourth_list
fourth_list[0][0] = 99
print fourth_list
