#! /usr/bin/env python
"""
2048 merge timings: a program

It's time to share your work on the first mini-project: 2048 (Merge)
https://class.coursera.org/principlescomputing1-004/forum/thread?thread_id=252
"""

import time
import random

#from codeskulptor import set_timeout
#set_timeout(15)

# Increase SAMPLE_SIZE if the timings are too small
SAMPLE_SIZE = 100000
LIMIT = 2**12

def merge_1(line):
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

def merge_2(line):
    result = [ 0 for _ in line ]
    index = -1
    merge_tiles = False
    for item in line:
        if item != 0:
            if not merge_tiles:
                index += 1
                result[index] = item
                merge_tiles = True
            elif item != result[index]:
                index += 1
                result[index] = item
            else:
                result[index] <<= 1
                merge_tiles = False
    return result


def merge_3(line):
    if len(line) <= 1:
        return line
    elif line[0] == 0:
        return merge_3(line[1:]) + [0]
    elif line[1] == 0:
        return merge_3(line[:1] + line[2:])  + [0]
    elif line[0] == line[1]:
        return [line[0] + line[1]] + merge_3(line[2:]) + [0]
    return line[:1] + merge_3(line[1:])
            
def merge_4(line):
    # Start with an output list that is zeroed out.
    merged_line = [0] * len(line)

    # Used to point to the "current" output item.
    index = 0

    # Rules for merging each input item in the list:
    #
    # 1. Zeroes in the input list are ignored. The remaining rules below
    #    are only for nonzero input items.
    #
    # 2. If the input item matches the current output item, add the input
    #    item to the output item, then point to the next output item.
    #
    # 3. If the input item does not match the current output item, copy
    #    it to the next available (zero) output item.    
    for item in line:
        if item:
            # Rule 1 is met.
            if merged_line[index] == item:
                # Rule 2 applies.
                merged_line[index] += item
                index += 1
            else:
                # Rule 3 applies. Make sure that the item is copied to
                # the next available output item.
                if merged_line[index]:
                    index += 1
                merged_line[index] = item

    return merged_line

def merge_5(line):
    """
    Helper function that merges a single row or column in 2048
    """
# creates a new list with all values shifted to the beginning adding a '0' at the end of the list instead.

    line2 = list(line)
    for item in line:
        if item == 0:
            line2.remove(item)
            line2.append(item)
    
# iterates over the index of the new list to find the matching values.

    for item in range(len(line2) - 1):
        if line2[item] == line2[item + 1]:
            line2[item] *= 2
            line2[item + 1] = 0

#   creates a new list with merged values at the beginning of the list.

    line3 = line2
    for item in line2:
        if item == 0:
            line3.remove(item)
            line2.append(item)
           
    return line3

def merge_6(line):
    my_line = line[:]
    counter = 0
    # sliding the numbers to the left
    temp_line = [number for number in my_line if number != 0 ]
    temp_line = temp_line + (len(my_line)-len(temp_line)) * [0]
    my_line = temp_line
        
    #adding the same two consecutive numbers
    while counter < len(my_line) - 1 : 
        if my_line[counter] == my_line[counter + 1] :
            my_line[counter] *= 2
            my_line[counter + 1] = 0
        counter += 1
        
    # and reorder    
    temp_line = [number for number in my_line if number != 0 ]
    temp_line = temp_line + (len(my_line)-len(temp_line)) * [0]   

    return  temp_line

def merge_7(line):
    # locals
    _merged_list = []
    _trailing_zeroes = []
    _helper_list = []
    _index = 0
    
    # catch empty and singleton lists to avoid 'index out of range' error - 1st patch
    if len(line) < 2:
        return line
    
    # iterate over row|column and split into nums > 0 and nums == 0
    for _num in line:
        if _num == 0:
            _trailing_zeroes.append(_num)
        else:
            _helper_list.append(_num)
    
    # here comes the magic
    while _index < len(_helper_list) - 1:
        if _helper_list[_index] == _helper_list[_index+1]:
            _merged_list.append(_helper_list[_index] + _helper_list[_index+1])
            _trailing_zeroes.append(0)
            _index += 2
        else:
            _merged_list.append(_helper_list[_index])
            _index += 1
            
    # catch remaining singleton _helper_list - 2nd patch
    if _index == len(_helper_list) - 1:
        _merged_list.append(_helper_list[_index])
            
    return _merged_list + _trailing_zeroes    

def merge_8(line):
    """
    Helper function that merges a single row or column in 2048
    """
    new_line = [0 for dummy_x in line]
    position_tracker = 0
    for element in line:
        if element != 0:
            if new_line[position_tracker] == 0:
                new_line[position_tracker] = element
            elif new_line[position_tracker] == element:
                new_line[position_tracker] += element
                position_tracker += 1
            elif new_line[position_tracker] != element:
                position_tracker += 1
                new_line[position_tracker] = element
    return new_line

def merge_9(line):
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

ZERO = 0
def _zero_clean(line):
    '''
    fill with zero
    '''
    # return [0] * len(line)
    _zero = lambda a: a != 0
    return filter(_zero, line)

def merge_10(line):
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
    #lst = _zero_clean(lst)

    return lst + (len(line)-len(lst))*[0]

def merge_11(line):
    merged = [i for i in line if i]
    merged = reduce(lambda x, y: x[:-1] + [y * 2, 0] if x[-1] == y else x + [y], merged[1:], merged[:1])
    merged = [i for i in merged if i]
    return merged + [0] * (len(line) - len(merged))

def merge_12(line):
    merged_line = [i for i in line if i]
    if len(merged_line) <= 1:
        return merged_line + [0] * line.count(0)
    if merged_line[0] == merged_line[1]:
        merged_line[0], merged_line[1] = merged_line[0] * 2, 0
    return [merged_line[0]] +  merge_12(merged_line[1:]) + [0] * line.count(0)

def merge_13(m):
    return lambda m:(filter(int,reduce(lambda x,y:x+[y]*(y>0)if x[-1]-y else x[:-1]+[y*2,0],m,[0]))+[0]*len(m))[:len(m)]

def merge_14(line):
    """
    Function that merges a single row or column in 2048.
    """
    lst = [val for val in line if val]   # Non zero values of line
    for index in range(len(lst) - 1):
        if lst[index] == lst[index + 1]:
            lst[index] <<= 1        # Merge pairs
            lst[index + 1] = 0
    lst = [val for val in lst if val]    # Remove zeroes
    return lst + [0] * (len(line) - len(lst)) # Complete

def merge_15(line):
    """ Function that merges a single row or column in 2048. """
    outp = [0]*len(line)                 # create output list with all 0s
    idx = 0                              # var for active slot in output list
    for cur in line:                     # loop over each item in input line
        if cur:                          # if current item is not 0 (skip 0s)...
            if outp[idx]:                # if outp[idx] is not 0...  if outp[idx] ne to cur, put cur in next slot
                if outp[idx] ^ cur:      # equiv to outp[idx] != cur
                    idx = -(~idx)        # equiv to idx += 1
                    outp[idx] = cur
                else:                    # otherwise, outp[idx] is eq to cur so merge
                    outp[idx] = cur<<1   # equiv to outp[idx] = cur+cur
                    idx = -(~idx)
            else:                        # otherwise, outp[idx] is 0, so set to cur
                outp[idx] = cur
    return outp

def val_to_lst(val, base=4):
    """Converts val to a list of digits in the chosen base"""
    lst = [] if val else [0]
    while val:
        lst += [val % base]
        val /= base
    return lst

def fct(n):
    """Mystery function"""
    return 2 ** n if n else 0

def lst_produce():
    """
    Create a random list of number that could represent
    tiles from a 2048 game (not necessarily)
    """
    return map(fct, val_to_lst(random.randrange(LIMIT)))
          
def here_we_go():
    """This is were it all begins!"""
    
    # You can add or remove functions in this dictionary 
    # if necessary. Choose a description.
    functions = {
                merge_1 : "Ivan Best's merge",
                merge_2 : "Miguel's merge",
                merge_3 : "Fred's merge",
                merge_4 : "Andrew's merge",
                merge_5 : "Andrey's merge",
                merge_6 : "Rene's merge",
                merge_7 : "Stephan's merge",
                merge_8 : "Gerschel's merge",
                merge_9 : "Philippe 2's merge",
                merge_10 : "Boonchu's merge",
                merge_11 : "Ivan 1's merge",
                merge_12 : "Ivan 2's merge",
                merge_13 : "Philippe 1's merge",
                merge_14 : "Philippe 3's merge",
                merge_15 : "Mike's merge",
}

    timings = {}

    list_sample = [lst_produce() for i in range(SAMPLE_SIZE)]
    print "Means computed over %d lists" % SAMPLE_SIZE
    for func in functions.keys():
        start = time.time()
        for lst in list_sample:
            merge_lst = func(lst)
        timings[func] = (time.time() - start) / SAMPLE_SIZE

    for func, tim in sorted(timings.items(), key=lambda x: x[1], reverse = True):
        print '{time:%fs} <- {%s}' % (tim, functions[func])

here_we_go() 
