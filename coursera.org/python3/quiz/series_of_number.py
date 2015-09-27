#! /usr/bin/env python
#
# Find consecutives in list
# http://stackoverflow.com/questions/2361945/detecting-consecutive-integers-in-a-list

series = [(1, 2, 3, 4, 5), (2, 4, 5, 6, 7), (2, 3, 4, 8, 9), (1, 5, 6, 8, 9) ]

def is_in_seq(nums):
    ranges = sum((list(t) for t in zip(nums, nums[1:]) if t[0]+1 != t[1]), [])
    return ranges

for numbers in series:
    print is_in_seq(numbers)
