#! /usr/bin/env python
"""
A simple testing suite for 2048 game
Note that tests are not exhaustive and should be supplemented

Discussion: Error owl test unit test failure in move __str__ return different
https://class.coursera.org/principlescomputing1-004/forum/thread?thread_id=125
"""
import poc_simpletest

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4


def run_test(game_class):
    """
    run test
    """
    suite = poc_simpletest.TestSuite()

    # test the init
    obj = game_class(2, 2)
    obj.reset()
    suite.run_test(obj._grid_height, 2, "Test #0: obj.grid_height")
    suite.run_test(obj._grid_width, 2, "Test #1: obj.grid_width")
    suite.run_test(obj, "[[0, 0]\n [0, 0]]", "Test #1: obj.reset()")

    obj = game_class(4, 4)
    obj.set_tile(0, 0, 2)
    obj.set_tile(0, 1, 0)
    obj.set_tile(0, 2, 0)
    obj.set_tile(0, 3, 0)
    obj.set_tile(1, 0, 0)
    obj.set_tile(1, 1, 2)
    obj.set_tile(1, 2, 0)
    obj.set_tile(1, 3, 0)
    obj.set_tile(2, 0, 0)
    obj.set_tile(2, 1, 0)
    obj.set_tile(2, 2, 2)
    obj.set_tile(2, 3, 0)
    obj.set_tile(3, 3, 0)
    obj.set_tile(3, 1, 0)
    obj.set_tile(3, 2, 0)
    obj.set_tile(3, 3, 2)
    obj.move(UP)
    suite.run_test(str(obj), '[[2, 2, 2, 2], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]', 'Test #2: obj.set_tile() ')

    suite.report_results()
