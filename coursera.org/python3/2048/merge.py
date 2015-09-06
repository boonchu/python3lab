#! /usr/bin/env python

'''
helper function that merges a single row or column in 2048

implement a function merge(line) that models the process of merging all of the tile
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
    merge 2048
    '''
    saved_len = len(line)

    # fill with zero
    line = _zero_clean(line)

    # slide all tiles towards the front by removing empty spaces (ZERO values)
    for tile in xrange(len(line)):
        # hit at the end of list
        if tile + 1 > len(line) - 1:
            break
        # merge 2048 pair
        if line[tile] == line[tile + 1]:
            # double value the first in pair
            line[tile] *= 2
            line[tile + 1] = ZERO

    # slide all the tiles towards the front and fill the rest with zeros
    line = _zero_clean(line)
    while len(line) != saved_len:
        line.append(0)

    return line

def test_merge():
    '''
    few simple tests
    For example, if a row of the board started as follows:
    print merge([2, 0, 2, 2])
    And you slide the tiles left, the row would become:
        - Note that the two leftmost tiles merged to become a 4
        - the third 2 just slides over next to the 4.
        - Keep in mind, however, that any tile should only be merged once
        that these merges should happen in order from lowest index to
        highest index.
        returns [4, 2, 0, 0]

    test case:

    [2, 0, 2, 4] should return [4, 4, 0, 0]
    [0, 0, 2, 2] should return [4, 0, 0, 0]
    [2, 2, 0, 0] should return [4, 0, 0, 0]
    [2, 2, 2, 2, 2] should return [4, 4, 2, 0, 0]
    [8, 16, 16, 8] should return [8, 32, 8, 0]
    '''

    print '  [2, 0, 2, 4] should return [4, 4, 0, 0] -> ', merge([2, 0, 2, 4])
    print '  [0, 0, 2, 2] should return [4, 0, 0, 0] ->', merge([0, 0, 2, 2])
    print '  [2, 2, 0, 0] should return [4, 0, 0, 0] ->', merge([2, 2, 0, 0])
    print '  [2, 2, 2, 2, 2] should return [4, 4, 2, 0, 0] ->', merge([2, 2, 2, 2, 2])
    print '  [8, 16, 16, 8] should return [8, 32, 8, 0] ->', merge([8, 16, 16, 8])

#test_merge()
