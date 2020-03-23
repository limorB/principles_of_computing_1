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
        # self.grid = [[0 for row in range(grid_width)]
        #              for col in range(grid_height)]
        self.reset()
        self.initial_idx_dict = {1: self.get_initial_tiles_up(),
                                 2: self.get_initial_tiles_down(),
                                 3: self.get_initial_tiles_left(),
                                 4: self.get_initial_tiles_right()

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
        self.grid = [[0 for row in range(self.grid_width)]
                     for col in range(self.grid_height)]
        new_tile_a = self.new_tile()
        new_tile_b = self.new_tile()
        while new_tile_a.keys() == new_tile_b.keys():
            new_tile_a = self.new_tile()

        # return self.grid

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """

        return str(self.grid)
        # return '\n'.join([str(row) for row in self.grid])

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
        if direction == 1 or direction == 2:
            number_of_steps = self.grid_height
        elif direction == 3 or direction == 4:
            number_of_steps = self.grid_width
        else:
            return False

        all_idx_lists = []
        initial_tiles_list = self.initial_idx_dict[direction]
        for tile in initial_tiles_list:
            start_tile = tile
            index_list = []
            for step in range(number_of_steps):
                row = start_tile[0] + step * OFFSETS[direction][0]
                col = start_tile[1] + step * OFFSETS[direction][1]
                index = (row, col)
                index_list.append(index)
            all_idx_lists.append(index_list)

        number_of_grid_changes = 0
        for i in all_idx_lists:
            # i is a list of indices. the values in each list will be merged using the merged function
            indices_list = i
            line = self.get_values_from_indices(i)
            merged_list = merge(line)
            if line != merged_list:
                number_of_grid_changes += 1

            start_point = 0
            for index in indices_list:
                row = index[0]
                col = index[1]
                self.grid[row][col] = merged_list[start_point]
                start_point += 1
        if number_of_grid_changes > 0:
            self.new_tile()

        # return self.grid

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

game = TwentyFortyEight(4, 4)
game.set_tile(0, 0, 2)
game.set_tile(0, 1, 0)
game.set_tile(0, 2, 0)
game.set_tile(0, 3, 0)
game.set_tile(1, 0, 0)
game.set_tile(1, 1, 2)
game.set_tile(1, 2, 0)
game.set_tile(1, 3, 0)
game.set_tile(2, 0, 0)
game.set_tile(2, 1, 0)
game.set_tile(2, 2, 2)
game.set_tile(2, 3, 0)
game.set_tile(3, 0, 0)
game.set_tile(3, 1, 0)
game.set_tile(3, 2, 0)
game.set_tile(3, 3, 2)
# print(game.__str__())
for i in game.grid:
    print(i)
(game.move(UP))
# print(game.__str__())

print("      ")
for i in game.grid:
    print(i)


