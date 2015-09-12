#! /usr/bin/env python

temp1 = [[1,2,3],[4,5,6],[7,8,9]]
temp2 = [[0,1,2],[4,6,5],[7,8,9]]
temp3 = [[0,1,2],[4,6,5],[7,8,9]]

def cmp_list(temp1, temp2):
    if [v1 for (v1, v2) in zip(temp1, temp2) if v1 != v2 ]:
        return False
    else:
        return True

print cmp_list(temp1, temp2)
print cmp_list(temp2, temp3)
