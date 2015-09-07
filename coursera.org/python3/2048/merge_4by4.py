#! /usr/bin/env python

'''
helper function that merges a single row or column in 2048

implement a function merge_v1(line) that models the process of merging all of the tile
values in a single row or column. This function takes the list line as a parameter
and returns a new list with the tile values from line slid towards the front of the
list and merged. Note that you should return a new list and you should not modify
the input list. This is one of the more challenging parts of implementing the game.

https://class.coursera.org/principlescomputing1-004/wiki/view?page=2048_%28Merge%29

Here is one basic strategy to implement the merge function:
  Iterate over the input and create an output list that has all of the non-zero tiles
  slid over to the beginning of the list with the appropriate number of zeroes at the
  end of the list.

  Iterate over the list created in the previous step and create another new list in
  which pairs of tiles in the first list are replaced with a tile of twice the value
  and a zero tile.

  Repeat step one using the list created in step two to slide the tiles to the
  beginning of the list again.
'''

ZERO = 0
def _zero_clean(line):
    '''
    fill with zero
    '''
    _zero = lambda a: a != 0
    return filter(_zero, line)

def merge(line):
    '''
    merge 2048 v2

    Here is how I first did it in 7 lines for those who are interested (as Eric in a message above).
    First line: Create a list with only the non zero values of the original list.
    Lines 2 to 5: A for loop where I merge tiles.
    Lines 6: Same thing as first line (except I don't take the values from the original list again).
    Lines 7: I return the list, with eventual additional zeros at the end if the list isn't long enough.

    Example:
    line = [2, 2, 0, 8]

        lst = [2, 2, 8] (filter)
        lst = [4, 0, 8] (for loop)
        lst = [4, 8] (filter)
        return [4, 8] + 2 * [0] = [4, 8, 0, 0] (zero padding)

    '''
    

    lst = _zero_clean(line)
    for value in xrange(len(lst)):
        if value + 1 > len(lst) - 1:
            break
        if lst[value] == lst[value+1]:
           lst[value] *= 2
           lst[value+1] = 0
    lst = _zero_clean(lst)

    return lst + (len(line)-len(lst))*[0]
   

def get_grid(list):
    return str([row for row in aList]).replace("],", "]\n")


def rotate_clockwise(matrix, degree=90):
    if degree not in [0, 90, 180, 270, 360]:
      # raise error or just return nothing or original
      return matrix if not degree else rotate_clockwise(zip(*matrix[::-1]), degree-90)

"""
Example from 2048 page: https://class.coursera.org/principlescomputing1-004/wiki/view?page=2048
4 by 4 UP direction
"""
print "**** UP ****"
aList=[[4, 2, 2, 2], [0, 0, 2, 8], [4, 2, 2, 8], [0, 2, 0, 4]]
print get_grid(aList)

# 90 degrees clockwise
aList = zip(*aList)[::-1]
aList = [list(row) for row in aList]
#print get_grid(aList)
aList = [ merge(row) for row in aList ]
#print get_grid(aList)

# 270 degrees clockwise
aList = zip(*aList)[::-1]
aList = zip(*aList)[::-1]
aList = zip(*aList)[::-1]
aList = [list(row) for row in aList]

print get_grid(aList)

"""
4 by 4 DOWN direction
"""
print "**** DOWN ****"
aList=[[4, 2, 2, 2], [0, 0, 2, 8], [4, 2, 2, 8], [0, 2, 0, 4]]
print get_grid(aList)

## 270 degrees clockwise
aList = zip(*aList)[::-1]
aList = zip(*aList)[::-1]
aList = zip(*aList)[::-1]
aList = [list(row) for row in aList]
aList = [ merge(row) for row in aList ]

## 90 degrees clockwise
aList = zip(*aList)[::-1]
aList = [list(row) for row in aList]

print get_grid(aList)

"""
4 by 4 LEFT direction
"""
print "**** LEFT ****"
aList=[[4, 2, 2, 2], [0, 0, 2, 8], [4, 2, 2, 8], [0, 2, 0, 4]]
print get_grid(aList)

aList = [ merge(row) for row in aList ]
print get_grid(aList)

"""
4 by 4 RIGHT direction
"""
print "**** RIGHT ****"
aList=[[4, 2, 2, 2], [0, 0, 2, 8], [4, 2, 2, 8], [0, 2, 0, 4]]
print get_grid(aList)

## 180 degrees clockwise
aList = zip(*aList)[::-1]
aList = zip(*aList)[::-1]
aList = [list(row) for row in aList]
aList = [ merge(row) for row in aList ]

## 180 degrees clockwise
aList = zip(*aList)[::-1]
aList = zip(*aList)[::-1]
aList = [list(row) for row in aList]
print get_grid(aList)
