#! /usr/bin/env python
"""
A simple testing suite for 2048 game
Note that tests are not exhaustive and should be supplemented
"""

import poc_simpletest

def run_test(game_class):
    """
    Some informal testing code
    """

    # create a TestSuite object
    suite = poc_simpletest.TestSuite()
    # test the init
    game = game_class(4, 4)
    suite.run_test(game.grid_height, 4, "Test #0: self.grid_height")
    suite.run_test(game.grid_width, 4, "Test #1: self.grid_width")
    suite.run_test(str(game.grid), str([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]), "Test #2: self.grid")
    suite.run_test(str(game.reset()), str([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]), "Test #2: self.reset()")

    #test str function in twentyfortyeight
    height1 = 3
    width1 = 4
    game1 = game_class(3, 4)
    suite.run_test(str(game1), '[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]', 'Test #3: str function')

    #test setting tiles and get tile in the class
    h2 = 4
    w2 = 5
    game2 = game_class(4, 5)
    game2.set_tile(1,1,99)
    game2.set_tile(1,3,40)
    game2.set_tile(3,4, 21)
    suite.run_test(game2.get_tile(0,0), 0, 'Test #4: expect 0')
    suite.run_test(game2.get_tile(1,1), 99, 'Test #5:expect 99')
    suite.run_test(game2.get_tile(1,3), 40, 'Test #6:expect 40')
    suite.run_test(game2.get_tile(3,4), 21, 'Test #7:expect 21')

    suite.report_results()
