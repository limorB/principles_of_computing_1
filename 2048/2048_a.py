# import poc_2048_gui
import random

"""
Clone of 2048 game.
"""

# import poc_2048_gui

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}


def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    non_merged_list = [0 for i in range(len(line))]
    merged_list = [0 for i in range(len(line))]
    result_list = [0 for i in range(len(line))]
    j_index = 0
    index = 0

    if 0 not in line:
        non_merged_list = line
    else:
        for i in range(len(line)):
            if line[i] != 0:
                for j in non_merged_list:
                    if non_merged_list[j_index] == 0:
                        non_merged_list[j_index] = line[i]
                        j_index += 1
                        break
    # print(non_merged_list)

    for num in non_merged_list:
        if index == (len(non_merged_list) - 1):
            merged_list[index] = non_merged_list[index]
        elif index > (len(non_merged_list) - 1):
            break
        elif non_merged_list[index] == non_merged_list[index + 1] and non_merged_list[index] != 0:
            merged_list[index] = (2 * non_merged_list[index])
            index += 2
            if index == len(non_merged_list):
                break
        else:
            merged_list[index] = non_merged_list[index]
            index += 1

    # print(merged_list)

    for i in range(len(merged_list)):
        if merged_list[i] != 0:
            for j in range(len(merged_list)):
                if result_list[j] == 0:
                    result_list[j] = merged_list[i]
                    break

    return result_list


class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):

        self.grid_height = grid_height
        self.grid_width = grid_width
        self.grid = [[0 for row in range(grid_width)]
                     for col in range(grid_height)]
        self.initial_idx_dict = {"up": self.get_initial_tiles_up(),
                                 "down": self.get_initial_tiles_down(),
                                 "left": self.get_initial_tiles_left(),
                                 "right": self.get_initial_tiles_right()

                                 }

    def get_initial_tiles_up(self):
        initial_tiles_up = []
        for col in range(self.grid_width):
            # index = self.grid[0][col]
            index = (0, col)
            initial_tiles_up.append(index)
        return initial_tiles_up

    def get_initial_tiles_down(self):
        initial_tiles_down = []
        for col in range(self.grid_width):
            # index = self.grid[self.grid_height-1][col]
            index = (self.grid_height - 1, col)
            initial_tiles_down.append(index)
        return initial_tiles_down

    def get_initial_tiles_left(self):
        initial_tiles_left = []
        for row in range(self.grid_height):
            # index = self.grid[row][0]
            index = (row, 0)
            initial_tiles_left.append(index)
        return initial_tiles_left

    def get_initial_tiles_right(self):
        initial_tiles_right = []
        for row in range(self.grid_height):
            # index = self.grid[row][self.grid_width-1]
            index = (row, self.grid_width - 1)
            initial_tiles_right.append(index)
        return initial_tiles_right

    def new_tile(self):

        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        return a dict which key is the index of the new tile and the value is the grid
        """
        my_list = [2] * 90 + [4] * 10
        new_tile = random.choice(my_list)
        random_row = random.randint(0, self.grid_height - 1)
        random_col = random.randint(0, self.grid_width - 1)
        # check that the tile index is empty
        while self.grid[random_row][random_col] != 0:
            random_row = random.randint(0, self.grid_height - 1)
            random_col = random.randint(0, self.grid_width - 1)

        self.grid[random_row][random_col] = new_tile
        tile_dict = {(random_row, random_col): self.grid}
        return tile_dict

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        new_tile_a = game.new_tile()
        new_tile_b = game.new_tile()
        while new_tile_a.keys() == new_tile_b.keys():
            new_tile_a = game.new_tile()

        return self.grid

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        for i in game.grid:
            print(i)
        pass

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self.grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self.grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # replace with your code
        pass

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self.grid[row][col] = value
        pass

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        value = self.grid[row][col]
        return value

    @staticmethod
    def traverse_by_direction(initial_tiles_list, direction, number_of_steps):
        """
        Return all indices list by the direction
        """
        all_idx_lists = []
        for tile in initial_tiles_list:
            # print(tile)
            start_tile = tile
            index_list = []
            for step in range(number_of_steps):
                row = start_tile[0] + step * direction[0]
                col = start_tile[1] + step * direction[1]
                index = (row, col)
                index_list.append(index)
            # print(index_list)
            all_idx_lists.append(index_list)

        return all_idx_lists

    def get_values_from_indices(self, idx_list):
        tiles_values_list = []
        for index in idx_list:
            row = index[0]
            col = index[1]
            tiles_values_list.append(self.grid[row][col])
        return tiles_values_list

    def is_grid_full(self):
        number_of_non_empty_tiles = 0
        for row in self.grid:
            for col in row:
                if col != 0:
                    number_of_non_empty_tiles += 1

        if number_of_non_empty_tiles == self.grid_width * self.grid_height:
            return True
        else:
            return False


# game = TwentyFortyEight(3, 4)
# poc_2048_gui.run_gui(TwentyFortyEight(4, 4))

game = TwentyFortyEight(4, 4)


print("welcome to 2048 game, below is the game board" + '\n' + "good luck!")
game.reset()
for i in game.grid:
    print(i)
while not game.is_grid_full():
    user_input = input("please pick one of the following directions: up/down/left/right: ")
    while user_input.lower() not in ["up", "down", "left", "right"]:
        user_input = input("invalid input. please type in one of the following directions: up/down/left/right: ")

    if user_input.lower() == "up":
        grid_idx = game.traverse_by_direction(game.initial_idx_dict['up'], OFFSETS[1], game.grid_height)
        # print(grid_idx)
    elif user_input.lower() == "down":
        grid_idx = game.traverse_by_direction(game.initial_idx_dict['down'], OFFSETS[2], game.grid_height)
    elif user_input.lower() == "left":
        grid_idx = game.traverse_by_direction(game.initial_idx_dict['left'], OFFSETS[3], game.grid_width)
    elif user_input.lower() == "right":
        grid_idx = game.traverse_by_direction(game.initial_idx_dict['right'], OFFSETS[4], game.grid_width)


    for i in grid_idx:
        print(i)

#     for i in grid_idx:
#         # i is a list of indices. the values in each list will be merged using the merged function
#         # print(i)
#         indices_list = i
#         # print(game.get_values_from_indices(i))
#         line = game.get_values_from_indices(i)
#         merged_list = merge(line)
#         # print(merged_list)
#         start_point = 0
#         for index in indices_list:
#             row = index[0]
#             col = index[1]
#             game.grid[row][col] = merged_list[start_point]
#             start_point += 1
#     # print(game.grid)
#     for x in game.grid:
#         print(x)
#     game.new_tile()
#     print("just added another random tile")
#
#     for x in game.grid:
#         print(x)
#
# print("game is over")
