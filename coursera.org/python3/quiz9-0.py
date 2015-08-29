#! /usr/bin/env python
# 

NUMBER=25

def appendsums(lst):
    """
    Repeatedly append the sum of the current last three elements of lst to lst.
    """
    for i in range(0, NUMBER):
        if lst.__len__() > 2:
            sum_last_3 = sum(lst[-3:])
            #print sum_last_3
            lst.append(sum_last_3)
        else:        
            lst.append(lst[-1])
        #print lst
        
sum_three = [0, 1, 2]
appendsums(sum_three)
print sum_three[20]
