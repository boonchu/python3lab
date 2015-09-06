#! /usr/bin/env python
"""
list comprehension example
https://class.coursera.org/principlescomputing1-004/forum/thread?thread_id=131
"""

row0 = [(0,y) for y in range(4)]
row1 = [(1,y) for y in range(4)]
row2 = [(2,y) for y in range(4)]

# gives list of tuples that do not distinguish between rows
# [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0),...]
grid1 = []
grid1.extend(row0)
grid1.extend(row1)
grid1.extend(row2)
print grid1

# gives list of lists for rows
# [[(0, 0),...], [(1, 0),...], [(2, 0),...]]
grid2 = []
grid2.append(row0)
grid2.append(row1)
grid2.append(row2)
print grid2

# gives list of tuples for rows
# [((0, 0),...)), ((0, 1),...), ((0, 2),...)]
grid3 = zip(row0,row1,row2)
print grid3

# prints out list by columns
# [(0, 0), (1, 0), (2, 0),...]
rows = range(3)
cols = range(4)
grid4 = [(r, c) for c in cols for r in rows]
print grid4

# prints out list by rows
# [(0, 0), (1, 0), (2, 0),...]
grid5 = [(r, c) for r in rows for c in cols]
print grid5

# nested comprehension, prints out list of list where each list is one row
# [[(0, 0), (0, 1), (0, 2), (0, 3)],...] 
grid6 = [[(row,col) for col in range(4)] for row in range(3)]
print grid6
