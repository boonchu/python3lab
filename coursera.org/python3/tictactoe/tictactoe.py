#! /usr/bin/env python

"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
# do not change their names.
NTRIALS = 10        # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player

# Add your functions here.
def mc_trial(board, player):
    """
     The function should play a game starting with the given player
     by making random moves, alternating between players. The function
     should return when the game is over. The modified board will
     contain the state of the game, so the function does not return
     anything. In other words, the function should modify the board input.
    """
    play = player
    while board.check_win() is None:
        move = random.choice(board.get_empty_squares())
        board.move(move[0], move[1], play)
        play = provided.switch_player(play)
    return board

def mc_update_scores(scores, board, player):
    """
    This function takes a grid of scores (a list of lists) with the same
    dimensions as the Tic-Tac-Toe board, a board from a completed game,
    and which player the machine player is. The function should score the
    completed board and update the scores grid. As the function updates
    the scores grid directly, it does not return anything,
    """
    score = (0,0)
    if board.check_win() == provided.PLAYERX:
        score = (SCORE_CURRENT, -SCORE_OTHER)
    elif board.check_win() == provided.PLAYERO:
        score = (-SCORE_CURRENT, SCORE_OTHER)

    _dic_score = {provided.PLAYERX : score[0],
                  provided.PLAYERO : score[1],
                  provided.EMPTY   : 0.0}

    _clone = [[ _dic_score[board.square(_row,_col)] for _col in range(board.get_dim())] 
     for _row in range(board.get_dim())]
    for _row in range(len(_clone)):
        for _col in range(len(_clone)):
            scores[_row][_col] += _clone[_row][_col]
    return scores

def get_best_move(board, scores):
    """
    This function takes a current board and a grid of scores. The function
    should find all of the empty squares with the maximum score and randomly
    return one of them as a (row, column) tuple.
    
    It is an error to call this function with a board that has no empty squares
    (there is no possible next move), so your function may do whatever it wants
    in that case. The case where the board is full will not be tested.
    """
    _sets = set([])
    _sets.add(board.get_empty_squares()[0])
    best = scores[0][0]
    for _index in board.get_empty_squares():
        if best < scores[_index[0]][_index[1]]:
            _sets.pop()
            _sets.add(_index)
            best = scores[_index[0]][_index[1]]
    return _sets.pop()

def mc_move(board, player, trials):
    """
    This function takes a current board, which player the machine player is, and
    the number of trials to run.

    The function should use the Monte Carlo simulation described above to return
    a move for the machine player in the form of a (row, column) tuple.

    Be sure to use the other functions you have written!
    """
    _index = 0
    _dim = board.get_dim()
    _scores = [[0]*_dim for _index in range(_dim)]
    while _index < trials:
        _index +=1
        _boards = mc_trial(board.clone(), player)
        mc_update_scores(_scores,_boards, player)
    return get_best_move(board,_scores)

# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

if __name__ == '__main__':
    provided.play_game(mc_move, NTRIALS, False)
    poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
