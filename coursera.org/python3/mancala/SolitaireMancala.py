#!/usr/bin/env python
#
# https://class.coursera.org/principlescomputing1-004/wiki/view?page=mancala
# In general, the ith entry of the list should represent the number of seeds
# in the ith house where the houses are indexed in ascending order from right
# to left.
#
# In the top configuration shown above, this list would be [0, 1, 1, 3, 0, 0, 0].
#
# Code Owltest:
# http://codeskulptor.appspot.com/owltest/?urlTests=poc.poc_mancala_machine.py&urlPylintConfig=poc.pylint_config.py
#

class SolitaireMancala:
    '''
    Simple class that implements Solitaire Mancala
    '''

    # Create a SolitaireMancala object whose configuration consists of a board with
    # an empty store and no houses
    def __init__(self):
        self.board = [0]

    # Set the board to be a copy of the supplied configuration (to avoiding referencing
    # issues). The configuration will be a list of integers
    def set_board(self, configuration):
        self.board = configuration[::]

    # Return a string corresponding to the current configuration of the Mancala board.
    # This string is formatted as a list with the store appearing in the rightmost
    # (last) entry.
    def __str__(self):
        board = self.board[::]
        board.reverse()
        return str(board)

    # Return the number of seeds in the house with index house_num. Note that house 0
    # corresponds to the store.
    def get_num_seeds(self, house_num):
        return self.board[house_num]

    # Return True if moving the seeds from house house_num is legal. Otherwise,
    # return False. If house_num is zero, is_legal_move should return False.
    def is_legal_move(self, house_num):
        if house_num == 0:
            return False
        elif self.board[house_num] == house_num:
            return True
        return False

    # Apply a legal move for house house_num to the board.
    def apply_move(self, house_num):
        if self.is_legal_move(house_num):
            self.board[house_num] = 0
            for i in range(house_num):
                self.board[i] += 1

    # Return the index for the legal move whose house is closest to the store.
    # If no legal move is available, return 0.
    def choose_move(self):
        for i in self.board[1:]:
            if self.board.index(i, 1) == i:
                return i
        return 0

    # Return True if all houses contain no seeds. Return False otherwise.
    def is_game_won(self):
        if self.board[1:].count(0) == len(self.board[1:]):
            return True
        return False

    # return a sequence (list) of legal moves based on the following heuristic: after each move,
    # move the seeds in the house closest to the store when given a choice of legal moves.
    # Note that this method should not update the current configuration of the game.
    def plan_moves(self):
        ret = []
        while not self.is_game_won():
            k = self.choose_move()
            if k != 0:
                ret.append(k)
            if k == 0: break
            self.apply_move(k)
        return ret

# Create tests to check the correctness of your code

def test_mancala():
    """
    Test code for Solitaire Mancala
    """

    my_game = SolitaireMancala()
    print "Testing init - Computed:", my_game, "Expected: [0]"

    config1 = [0, 0, 1, 1, 3, 5, 0]
    my_game.set_board(config1)

    print "Testing set_board - Computed:", str(my_game), "Expected:", str([0, 5, 3, 1, 1, 0, 0])
    print "Testing get_num_seeds - Computed:", my_game.get_num_seeds(1), "Expected:", config1[1]
    print "Testing get_num_seeds - Computed:", my_game.get_num_seeds(3), "Expected:", config1[3]
    print "Testing get_num_seeds - Computed:", my_game.get_num_seeds(5), "Expected:", config1[5]
