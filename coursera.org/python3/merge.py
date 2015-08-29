#! /usr/bin/env python

'''
helper function that merges a single row or column in 2048
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
def merge(line):
    original_lenght = len(line)
    empty_space = 0

    # slide all tiles towards the front by removing empty spaces (zero values)
    while empty_space in line:
        line.remove(empty_space)

    for tile in xrange(len(line)):
        # arrived at the end of list
        if tile + 1 > len(line) - 1:
            break
        # merge pair of eligible neighbors
        if line[tile] == line[tile + 1]:
            line[tile] *= 2
            del line[tile + 1]
            line.insert(tile + 1, empty_space)

    # slide all the tiles towards the front and fill the rest with zeros
    while empty_space in line:
        line.remove(empty_space)
    while len(line) != original_lenght:
        line.append(empty_space)

    return line

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

print merge([2, 0, 2, 4])
print merge([0, 0, 2, 2])
print merge([2, 2, 0, 0])
print merge([2, 2, 2, 2, 2])
print merge([8, 16, 16, 8])
