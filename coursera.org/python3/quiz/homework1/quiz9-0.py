#! /usr/bin/env python
#
# http://stackoverflow.com/questions/2572564/python-lambda-returning-none-instead-of-empty-string?rq=1
# 
# Write a function in Python that takes a list as input and repeatedly appends the sum of the last 
# three elements of the list to the end of the list. Your function should loop for 25 times. 

NUMBER = 25

sum3 = lambda x: x.append(sum(x[-3:])) if x.__len__() > 2 else x.append(x[-1])

#def appendsums(lst):
#    """
#    Repeatedly append the sum of the current last three elements of lst to lst.
#    """
#    for i in xrange(NUMBER):
#        if lst.__len__() > 2:
#            lst.append(sum(lst[-3:]))
#        else:        
#            lst.append(lst[-1])

def appendsums(object):
    for i in xrange(NUMBER):
        sum3(object)

        
# expect value 230 from sum_three[10]
# expect value 101902 from sum_three[20]
sum_three = [0, 1, 2]
appendsums(sum_three)
print sum_three[10], sum_three[20]
