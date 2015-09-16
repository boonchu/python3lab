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

def merge_v1(line):
    '''
    merge 2048
    '''
    saved_len = len(line)

    # fill with zero
    line = _zero_clean(line)

    # slide all tiles towards the front by removing empty spaces (ZERO values)
    for tile in xrange(len(line)):
        # if element exists at the end of list? lets move on.
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

def merge_v2(line):
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

def merge_v3(line):
    """
    Function that merges a single row or column in 2048.
    """
    lst = [0] * len(line) # we start with a 0-filled list.
    pos = 0     # index position in the new list
    pvl = 0     # we keep the previous value
    for val in line:
        if val: # we only care about the non zero values.
            if not pvl:        # this tile is empty
                lst[pos] = val # let's fill with val
                pvl = val
            elif pvl - val:    # different non zero values?
                pos += 1
                lst[pos] = val # tiles don't merge
                pvl = val
            else:              # same values!
                lst[pos] = val << 1  # it merges!
                pos += 1
                pvl = 0        # next value is 0
    return lst

def merge_v4(line):
    merged = [0] * len(line)
    idx = 0
    for num in line:
        if num:
            if num == merged[idx]:
                merged[idx] *= 2
                idx += 1
            else:
                if merged[idx]:
                    idx += 1
                merged[idx] = num
    return merged

def merge_v5(line):
    _merge = lambda m:(filter(int,reduce(lambda x,y:x+[y]*(y>0)if x[-1]-y else x[:-1]+[y*2,0],m,[0]))+[0]*len(m))[:len(m)]
    return _merge(line)

def merge_v6(line):
    """
    Function that merges a single row or column in 2048.
    """
    new = [num for num in line if num]
    idx = 0
    while idx < len(new) - 1:
        if new[idx] == new[idx + 1]:
            new[idx] += new.pop(idx + 1)
        idx += 1
    return new + [0] * (len(line) - len(new))

def test_merge_v1():
    '''
    few simple tests
    For example, if a row of the board started as follows:
    print merge_v1([2, 0, 2, 2])
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

    print '  [2, 0, 2, 4] should return [4, 4, 0, 0] -> ', merge_v1([2, 0, 2, 4])
    print '  [0, 0, 2, 2] should return [4, 0, 0, 0] ->', merge_v1([0, 0, 2, 2])
    print '  [2, 2, 0, 0] should return [4, 0, 0, 0] ->', merge_v1([2, 2, 0, 0])
    print '  [2, 2, 2, 2, 2] should return [4, 4, 2, 0, 0] ->', merge_v1([2, 2, 2, 2, 2])
    print '  [8, 16, 16, 8] should return [8, 32, 8, 0] ->', merge_v1([8, 16, 16, 8])

def test_merge_v2():
    print '  [2, 0, 2, 4] should return [4, 4, 0, 0] -> ', merge_v2([2, 0, 2, 4])
    print '  [0, 0, 2, 2] should return [4, 0, 0, 0] ->', merge_v2([0, 0, 2, 2])
    print '  [2, 2, 0, 0] should return [4, 0, 0, 0] ->', merge_v2([2, 2, 0, 0])
    print '  [2, 2, 2, 2, 2] should return [4, 4, 2, 0, 0] ->', merge_v2([2, 2, 2, 2, 2])
    print '  [8, 16, 16, 8] should return [8, 32, 8, 0] ->', merge_v2([8, 16, 16, 8])

def test_merge_v3():
    print '  [2, 0, 2, 4] should return [4, 4, 0, 0] -> ', merge_v3([2, 0, 2, 4])
    print '  [0, 0, 2, 2] should return [4, 0, 0, 0] ->', merge_v3([0, 0, 2, 2])
    print '  [2, 2, 0, 0] should return [4, 0, 0, 0] ->', merge_v3([2, 2, 0, 0])
    print '  [2, 2, 2, 2, 2] should return [4, 4, 2, 0, 0] ->', merge_v3([2, 2, 2, 2, 2])
    print '  [8, 16, 16, 8] should return [8, 32, 8, 0] ->', merge_v3([8, 16, 16, 8])

def test_merge_v4():
    print '  [2, 0, 2, 4] should return [4, 4, 0, 0] -> ', merge_v4([2, 0, 2, 4])
    print '  [0, 0, 2, 2] should return [4, 0, 0, 0] ->', merge_v4([0, 0, 2, 2])
    print '  [2, 2, 0, 0] should return [4, 0, 0, 0] ->', merge_v4([2, 2, 0, 0])
    print '  [2, 2, 2, 2, 2] should return [4, 4, 2, 0, 0] ->', merge_v4([2, 2, 2, 2, 2])
    print '  [8, 16, 16, 8] should return [8, 32, 8, 0] ->', merge_v4([8, 16, 16, 8])

def test_merge_v5():
    print '  [2, 0, 2, 4] should return [4, 4, 0, 0] -> ', merge_v5([2, 0, 2, 4])
    print '  [0, 0, 2, 2] should return [4, 0, 0, 0] ->', merge_v5([0, 0, 2, 2])
    print '  [2, 2, 0, 0] should return [4, 0, 0, 0] ->', merge_v5([2, 2, 0, 0])
    print '  [2, 2, 2, 2, 2] should return [4, 4, 2, 0, 0] ->', merge_v5([2, 2, 2, 2, 2])
    print '  [8, 16, 16, 8] should return [8, 32, 8, 0] ->', merge_v5([8, 16, 16, 8])

def test_merge_v6():
    print '  [2, 0, 2, 4] should return [4, 4, 0, 0] -> ', merge_v6([2, 0, 2, 4])
    print '  [0, 0, 2, 2] should return [4, 0, 0, 0] ->', merge_v6([0, 0, 2, 2])
    print '  [2, 2, 0, 0] should return [4, 0, 0, 0] ->', merge_v6([2, 2, 0, 0])
    print '  [2, 2, 2, 2, 2] should return [4, 4, 2, 0, 0] ->', merge_v6([2, 2, 2, 2, 2])
    print '  [8, 16, 16, 8] should return [8, 32, 8, 0] ->', merge_v6([8, 16, 16, 8])

#test_merge_v1()
#test_merge_v2()
#test_merge_v3()
#test_merge_v4()
#test_merge_v5()
test_merge_v6()
