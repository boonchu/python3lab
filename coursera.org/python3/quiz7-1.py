#! /usr/bin/env python

'''
In Python, floating point numbers are represented in a binary version of scientific 
notation where the base 10 is replaced by 2 and the mantissa is a binary number that 
lies in the range 1<|a|<2 and has 53 significant bits. Floating point numbers are 
usually printed out with up to 12 significant digits (although with trailing zeros suppressed).

In some homework problems, you will be asked to write code that computes an answer as a 
floating point number and then enter your answer as decimal number with a specified number 
of significant digits. In practice, Python computes more significant digits than are 
required so you should round your answer to the closest decimal number with the specified 
number of significant digits.

For this question, look up (or compute) the decimal representation of the number PI and 
enter the value of PI with five significant digits of precision in the box below. Remember 
to round as describe above.

round a floating number with significant figure
http://stackoverflow.com/questions/3410976/how-to-round-a-number-to-significant-figures-in-python
'''

import math
def round_sig(x, sig=5):
    x = abs(x)
    return round(x, sig-int(math.floor(math.log10(x)))-1)

print 'original pi value ' + str(math.pi)
print 'round with 5 significant figures ' + str(round_sig(math.pi))

print 'original value ' + str(-0.0244289239)
print 'round with 5 significant figures ' + str(round_sig(-0.0244289239))
