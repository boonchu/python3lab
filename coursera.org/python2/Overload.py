#! /usr/bin/env python
#
# Python does not support overloading, i.e., having multiple definitions of the same method. 
#
# Instead, Python supports very flexible function and method definitions. While we haven't 
# illustrated it for you previously, we could have accomplished the same idea as above 
# with a single method definition. 
#

class Overload:
    def __init__(self, one, two=0):
        """Example of method that takes one required argument and one optional argument."""
        if one and two ==0:
		print "one is ", one
	if one and two>0:
		print "one is ", one, " two is ", two

# Overload main calls
Overload(1)        # Implicitly, we leave the second argument as its default value, 0.
Overload(1,2)
