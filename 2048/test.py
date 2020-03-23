# import random
#
# h = 4
# w = 3
#
#
# grid_width = 4
# grid_height = 3
#
# grid = [[0 for row in range(grid_width)]
#         for col in range(grid_height)]
#
#
#
# # for i in grid:
# #     print(i)
# #     # for j in i :
# #     #     print(j)
#
#
# random_row = random.randint(0, grid_height - 1)
# random_col = random.randint(0, grid_width - 1)
#
# my_list = [2] * 90 + [4] * 10
# print(random.choice(my_list))


"""
Create a rectagular grid and iterate through
a subset of its cells in a specified direction
"""

GRID_HEIGHT = 4
GRID_WIDTH = 6

# Create a rectangular grid using nested list comprehension
# Inner comprehension creates a single row
EXAMPLE_GRID = [[row + col for col in range(GRID_WIDTH)]
                for row in range(GRID_HEIGHT)]


# def traverse_grid(start_cell, direction, num_steps):
#     """
#     Function that iterates through the cells in a grid
#     in a linear direction
#
#     Both start_cell is a tuple(row, col) denoting the
#     starting cell
#
#     direction is a tuple that contains difference between
#     consecutive cells in the traversal
#     """
#
#     for step in range(num_steps):
#         row = start_cell[0] + step * direction[0]
#         col = start_cell[1] + step * direction[1]
#         print
#         "Processing cell", (row, col),
#         print
#         "with value", EXAMPLE_GRID[row][col]
#

# h = 4
# w = 3

print(EXAMPLE_GRID)