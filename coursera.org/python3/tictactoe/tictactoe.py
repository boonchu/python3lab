#! /usr/bin/env python

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

    _clone = [[ _dic_score[board.square(_row,_col)] for _col in range(board.get_dim())] for _row in range(board.get_dim())]
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

    https://class.coursera.org/principlescomputing1-004/forum/thread?thread_id=418 

        1) empty_squares = board.get_empty_squares()
        2) find maximum value in these empty_squares
        3) find all the squares with this maximum value
        4) do the intersection of list of tuples you got from step 1 and step 3
        5) return the tuple that you get by applying random.choice on the output of step 4

    https://class.coursera.org/principlescomputing1-004/forum/thread?thread_id=346

    #square with max score:
    row, col = reduce(lambda x, y: x if scores[x[0]][x[1]] >= scores[y[0]][y[1]] else y,  board.get_empty_squares())
    #list of squares with max score
    filter(lambda cell: scores[cell[0]][cell[1]] == scores[row][col], board.get_empty_squares())

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

    Calling mc_update_scores() from mc_move()
    https://class.coursera.org/principlescomputing1-004/forum/thread?thread_id=402
    """
    _index = 0
    _dim = board.get_dim()
    _scores = [[0]*_dim for _index in range(_dim)]
    while _index < trials:
        _index +=1
        _boards = mc_trial(board.clone(), player)
        mc_update_scores(_scores,_boards, player)
    return get_best_move(board,_scores)


# Your Tic-Tac-Toe implementation goes here
# testing game
# https://class.coursera.org/principlescomputing1-004/forum/thread?thread_id=414

def run_computer_versus_computer(ngames = 10,
                                 first_player = provided.PLAYERX,
                                 draw_board = False,
                                 board_size = 3):
    """
    Computer plays ngames against itself, then win, lost, draw
    statistics are displayed. Default for ngames is 10.

    first_player is either provided.PLAYERX or provided.PLAYERO.
    Default is provided.PLAYERX

    draw_board can be set to True if you want to see the
    play-by-play moves. The default is False.

    board_size is the number of squares per row and column.
    Default is 3 (standard Tic-Tac-Toe board size).
    """
    wins_x = 0
    wins_o = 0
    draws  = 0

    for dummy_game_number in xrange(ngames):
        if draw_board:
            print "GAME #", dummy_game_number + 1
        board = provided.TTTBoard(board_size)
        player = first_player

        while not board.check_win():
            move = mc_move(board, player, NTRIALS)
            board.move(move[0], move[1], player)
            player = provided.switch_player(player)
            if draw_board:
                print
                print str(board)

        game_result = board.check_win()

        if game_result == provided.PLAYERX:
            if draw_board:
                print "X wins"
            wins_x += 1
        elif game_result == provided.PLAYERO:
            if draw_board:
                print "O wins"
            wins_o += 1
        else:
            if draw_board:
                print "It's a draw"
            draws += 1

        if draw_board:
            print

    print "X won", wins_x, "out of", ngames, "(", 100.0 * wins_x / ngames, "%)"
    print "O won", wins_o, "out of", ngames, "(", 100.0 * wins_o / ngames, "%)"
    print "draws", draws,  "out of", ngames, "(", 100.0 * draws  / ngames, "%)"

# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

if __name__ == '__main__':
    # Play single game simulation,
    # Play computer vs. computer with default settings:
    #    10 games
    #    'X' goes first
    #    Quiet mode (board details not displayed)
    #    Standard 3x3 board
    run_computer_versus_computer()

    # This one runs plays 5 games. 'X' goes first, game details are shown.
    #run_computer_versus_computer(150, provided.PLAYERX, False, 3)

    # This one runs plays 5 games. 'O' goes first, game details are shown.
    #run_computer_versus_computer(1000, provided.PLAYERO, False, 3)

    # two lines here for real game
    #provided.play_game(mc_move, NTRIALS, False)
    poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)

