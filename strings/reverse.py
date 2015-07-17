#! /usr/bin/env python

myString = 'Coursera provides the best MOOC of the world'
reversed = ""
for word in myString.split()[::-1] : reversed = reversed + word + " "
print reversed.strip()
