#! /usr/bin/env python

#following defines one way to concatenate multiple lists. For example, 
#list_extend_many([[1,2], [3], [4, 5, 6], [7]]) returns [1, 2, 3, 4, 5, 6, 7] 
#and doesn't mutate anything. 

# OK
#def list_extend_many(lists):
    #"""Returns a list that is the concatenation of all the lists in the given list-of-lists."""
    #result = []
    #for l in lists:
        #result.extend(l)
    #return result

# Not OK
#def list_extend_many(lists):
#    result = []
#    for i in range(len(lists) - 1, -1, -1):
#        result.extend(lists[i])
#    return result

# OK
#def list_extend_many(lists):
#    result = []
#    i = 0
#    while i < len(lists): 
#        result += lists[i]
#        i += 1
#    return result

# OK
#def list_extend_many(lists):
#    result = []
#    for i in range(len(lists)):
#        result.extend(lists[i])
#    return result

# Not OK
def list_extend_many(lists):
    result = []
    i = 0
    while i <= len(lists): 
        result.extend(lists[i])
        i += 1
    return result

print list_extend_many([[1,2], [3], [4, 5, 6], [7]])


