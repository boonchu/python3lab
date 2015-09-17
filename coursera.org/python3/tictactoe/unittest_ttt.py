#! /usr/bin/env python
"""
Unittest code for Tic-Tac-Toe
"""

import unittest

"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# These two lines change CodeSkulptor timeout to 1 minute (60 seconds).
# Adjust if needed.
try:
      import SimpleGUICS2Pygame.codeskulptor as codeskulptor
except ImportError:
      import codeskulptor
      codeskulptor.set_timeout(60)

from tictactoe import *

class TTTTest(unittest.TestCase):
    """
    Simple class that implements a unittest TestCase
    """

    def test_get_best_move1(self):
        """
        Testing init
        """
        self.move = get_best_move(
            provided.TTTBoard(2, False, [[provided.EMPTY, provided.EMPTY], [provided.EMPTY, provided.EMPTY]]),
            [[0, 0], [3, 0]])
        self.assertEqual(self.move, (1, 0))

    def test_get_best_move2(self):
        """
        Testing get_best_move
        """
        self.move = get_best_move(provided.TTTBoard(3, False, [[provided.EMPTY, provided.EMPTY, provided.EMPTY],
                                                               [provided.EMPTY, provided.EMPTY, provided.EMPTY],
                                                               [provided.EMPTY, provided.EMPTY, provided.EMPTY]]),
                                  [[1, 2, 3], [7, 8, 9], [4, 5, 6]])
        self.assertEqual(self.move, (1, 2))

    def test_get_best_move3(self):
        """
        Testing get_best_move
        """
        self.move = get_best_move(
            provided.TTTBoard(2, False, [[provided.EMPTY, provided.PLAYERX], [provided.EMPTY, provided.PLAYERO]]),
            [[3, 3], [0, 0]])
        self.assertEqual(self.move, (0, 0))

    def test_mc_move1(self):
        """
        Testing mc_move
        """
        self.move = mc_move(provided.TTTBoard(3, False, [[provided.PLAYERX, provided.EMPTY, provided.EMPTY],
                                                         [provided.PLAYERO, provided.PLAYERO, provided.EMPTY],
                                                         [provided.EMPTY, provided.PLAYERX, provided.EMPTY]]),
                            provided.PLAYERX, NTRIALS)
        self.assertEqual(self.move, (1, 2))

    def test_mc_move2(self):
        """
        Testing mc_move
        """
        self.move = mc_move(provided.TTTBoard(3, False, [[provided.EMPTY, provided.PLAYERX, provided.PLAYERX],
                                                         [provided.PLAYERO, provided.EMPTY, provided.PLAYERX],
                                                         [provided.PLAYERO, provided.PLAYERX, provided.EMPTY]]),
                            provided.PLAYERO, NTRIALS)
        self.assertEqual(self.move, (0, 0))

    def test_mc_move3(self):
        """
        Testing mc_move
        """
        self.move = mc_move(provided.TTTBoard(4, False,
                                              [[provided.PLAYERX, provided.PLAYERO, provided.PLAYERO, provided.EMPTY],
                                               [provided.PLAYERO, provided.EMPTY, provided.PLAYERX, provided.PLAYERX],
                                               [provided.EMPTY, provided.PLAYERX, provided.PLAYERX, provided.PLAYERO],
                                               [provided.EMPTY, provided.PLAYERX, provided.PLAYERO, provided.PLAYERO]]),
                            provided.PLAYERX, NTRIALS)
        self.assertIn(self.move, [(0, 3), (3, 0)])

    def test_mc_move4(self):
        """
        Testing mc_move
        """
        self.move = mc_move(provided.TTTBoard(3, False, [[provided.PLAYERX, provided.PLAYERX, provided.PLAYERO],
                                                         [provided.EMPTY, provided.PLAYERX, provided.PLAYERX],
                                                         [provided.PLAYERO, provided.EMPTY, provided.PLAYERO]]),
                            provided.PLAYERO, NTRIALS)
        self.assertEqual(self.move, (2, 1))

    def test_mc_trial1(self):
        """
        Testing mc_trial
        """
        self.board = provided.TTTBoard(4, False, [
            [provided.PLAYERX, provided.PLAYERO, provided.PLAYERO, provided.EMPTY],
            [provided.PLAYERO, provided.EMPTY, provided.PLAYERX, provided.PLAYERX],
            [provided.EMPTY, provided.PLAYERX, provided.PLAYERX, provided.PLAYERO],
            [provided.EMPTY, provided.PLAYERX, provided.PLAYERO, provided.PLAYERO]])
        self.move = mc_trial(self.board, 2)
        self.assertIn(self.board.square(0, 3), [provided.PLAYERX, provided.PLAYERO, provided.EMPTY])
        self.assertIn(self.board.square(1, 1), [provided.PLAYERX, provided.PLAYERO, provided.EMPTY])
        self.assertIn(self.board.square(2, 0), [provided.PLAYERX, provided.PLAYERO, provided.EMPTY])
        self.assertIn(self.board.square(3, 0), [provided.PLAYERX, provided.PLAYERO, provided.EMPTY])


if __name__ == "__main__":
    # suite = unittest.TestLoader().loadTestsFromTestCase(TTTTest)
    # unittest.TextTestRunner(verbosity=2).run(suite)
    unittest.main()
