"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
# import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 1000  # Number of trials to run
SCORE_CURRENT = 1.0  # Score for squares played by the current player
SCORE_OTHER = 1.0  # Score for squares played by the other player
PLAYERX = 2
PLAYERO = 3
EMPTY = 1
DRAW = 4

#board = provided.TTTBoard(3, reverse=False)




# Add your functions here.
def pick_random_move(board):
    """ randomly picks an empty square """
    empty_squares_list = board.get_empty_squares()
    random_square = random.choice(empty_squares_list)
    return random_square


def mc_trial(board, player):
    """ switch between playres who play random moves. """
    """ the function should modify the board and return once """
    """ the game ends """
    while board.check_win() is None:
        # while the game is in progress
        random_square = pick_random_move(board)
        board.move(random_square[0], random_square[1], player)
        player = provided.switch_player(player)
    return None


def create_board_as_list(board):
    """ creates board as list """
    row = 0
    col = 0
    board_as_list = []
    for row in range(board.get_dim()):
        row_list = []
        for col in range(board.get_dim()):
            index = board.square(row, col)
            row_list.append(index)
        board_as_list.append(row_list)
    return board_as_list


def mc_update_scores(scores, board, player):
    """ score the completed board and update the scores grid """
    list_board = create_board_as_list(board)
    winner = board.check_win()
    # print(list_board)
    if winner == player:
        for row_index, row in enumerate(list_board):
            for item_index, item in enumerate(row):
                if item == player:
                    scores[row_index][item_index] += SCORE_CURRENT
                if item != player and item != EMPTY:
                    scores[row_index][item_index] -= SCORE_OTHER
    elif winner not in (player, DRAW, None):
        # meaning that the other player has won the game
        for row_index, row in enumerate(list_board):
            for item_index, item in enumerate(row):
                if item == player:
                    scores[row_index][item_index] -= SCORE_CURRENT
                if item != player and item != EMPTY:
                    scores[row_index][item_index] += SCORE_OTHER
    else:
        pass

    return None


def get_best_move(board, scores):
    """ finds all of the empty squares with the maximum score and randomly return one of them as a tuple (the index) """
    empty_squares_list_indices = board.get_empty_squares()
    if len(empty_squares_list_indices) == 0:
        print("board is full")
        return None
    list_of_max_indices = []
    empty_squares_scores_dict = {}
    for item in empty_squares_list_indices:
        row = item[0]
        col = item[1]

        empty_squares_scores_dict[item] = scores[row][col]
    # empty_squares_dict hold the scores(as values) and the index(as key) of all the empty sqaures
    max_value = max(empty_squares_scores_dict.values())
    all_max_values_indices = [k for k, v in empty_squares_scores_dict.items() if v == max_value]
    # find all the the indices of empty squares with max values
    random_max_index = random.choice(all_max_values_indices)

    return random_max_index


def mc_move(board, player, trials):
    """ function should run a ranodm game simulation according to the given number of trials """
    """ should use a monte carlo simulation to return a move for the machine player in a tuple form """
    scores = [[0 for dummy in range(board.get_dim())]
              for dummy_1 in range(board.get_dim())]

    for trial in range(trials):
        trial_board = board.clone()
        mc_trial(trial_board, player)
        mc_update_scores(scores, trial_board, player)

    move_tuple = get_best_move(board, scores)
    print(board)
    return move_tuple





print(mc_move(provided.TTTBoard(4, False,
                                [[provided.PLAYERX, provided.PLAYERO, provided.PLAYERO, provided.EMPTY],
                                 [provided.PLAYERO, provided.EMPTY, provided.PLAYERX, provided.PLAYERX],
                                 [provided.EMPTY, provided.PLAYERX, provided.PLAYERX, provided.PLAYERO],
                                 [provided.EMPTY, provided.PLAYERX, provided.PLAYERO, provided.PLAYERO]]),
              provided.PLAYERX, NTRIALS))

# mc_update_scores(scores, board, PLAYERX)
# print(scores)

# print(mc_move(board,PLAYERX,1))
# mc_trail(board, PLAYERX)
# # print(create_board_as_list(board))
# print("score grid before:")
# print(scores)
# (mc_update_scores(scores, board, PLAYERX))
# print("score grid after:")
# print(scores)
# print(get_best_move(board, scores))

# Test game with the console or the GUI.  Uncomment whichever
# you prefer.  Both should be commented out when you submit
# for testing to save time.

# provided.play_game(mc_move, NTRIALS, False)
# poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
