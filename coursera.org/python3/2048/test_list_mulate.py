#! /usr/bin/env python
#
# https://class.coursera.org/principlescomputing1-004/forum/thread?thread_id=54
#

test_list = [3, 0, 2, 4, 5, 0, 0]

def double_value(x):
  x[:] = [i * 2 for i in x]

def remove_zero(x):
  # return [x.pop(0) for _ in range(len(x))]
  return [i for i in x if i]

double_value(test_list)
print test_list

list2 = set()
list2 = remove_zero(test_list)
print list2
