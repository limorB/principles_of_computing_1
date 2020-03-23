"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
# import poc_ttt_gui
# import poc_ttt_provided as provided


# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
# NTRIALS = 1         # Number of trials to run
# SCORE_CURRENT = 1.0 # Score for squares played by the current player
# SCORE_OTHER = 1.0   # Score for squares played by the other player
#
# h = 4
# w = 3
#
#
# # print(scores_grid)
# list = [2,2,2]
# print(max(list))
list_of_max_indices = []
scores = [[-1.0, 0, 0], [-1.0, -1.0, 0], [0, -1.0, 0]]
for x in scores:
    print(x)
max_value = 0
for row_index, row in enumerate(scores):
    for item_index, item in enumerate(row):
        if item == max_value:
            print(item)
            list_of_max_indices.append((row_index, item_index))
print("below is the list of max indices")
print(list_of_max_indices)
if len(list_of_max_indices) == 1:
    print(list_of_max_indices[0])
else:
    random_max_index = random.choice(list_of_max_indices)
    print(random_max_index)


