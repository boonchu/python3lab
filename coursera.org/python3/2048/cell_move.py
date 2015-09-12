#! /usr/bin/env python
# 
# Did anyone use traverse_grid as a method in the TwentyFortyEight Class and what do you return from that method?
# https://class.coursera.org/principlescomputing1-004/forum/thread?thread_id=247

import random

grid_height = 4
grid_width = 4

UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

initial_tiles = {
            UP: [[0, 0], [0, 1], [0, 2], [0, 3]],
            DOWN: [[3, 0], [3, 1], [3, 2], [3, 3]],
            LEFT: [[0, 0], [1, 0], [2, 0], [3, 0]],
            RIGHT: [[0, 3], [1, 3], [2, 3], [3,3]]
                 }

grid = [[random.choice([0, 2, 4]) for col in range(grid_width)]
                                  for row in range(grid_height)]
direction = RIGHT
for i in range(3):
    #direction = RIGHT
    for i in range(grid_height):
        print
        for j in range(grid_width):
            print grid[i][j],
    print

    #3-times diection RIGHT
    for item in initial_tiles[RIGHT]:
        if direction == LEFT or direction == RIGHT:
            length = grid_width
        else:
            length = grid_height
        line = []
        # line.append(grid[item[0]][item[1]])
        for step in range(1, length, 1):
            item[0] = item[0] + step * OFFSETS[direction][0]
            item[1] = item[1] + step * OFFSETS[direction][1]
            line.append(grid[row][col])
        print line

for i in range(grid_height):
    print
    for j in range(grid_width):  
        print grid[i][j],
print
