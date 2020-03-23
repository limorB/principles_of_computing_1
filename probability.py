"""
Program that computes mystery number
"""

import math
import random


def inside_unit_circle(point):
    """
    Compute distance of point from origin
    """
    distance = math.sqrt(point[0] ** 2 + point[1] ** 2)
    return distance < 1


def estimate_mystery(num_trials):
    """
    Main function
    """
    num_inside = 0

    for dumm_idx in range(num_trials):
        new_point = [2 * random.random() - 1, 2 * random.random() - 1]
        if inside_unit_circle(new_point):
            num_inside += 1
    print(num_inside)
    print(num_trials)
    return float(num_inside) / num_trials


print(estimate_mystery(100000000))


# def format(tenths):
#     if tenths > 600 :
#         A = tenths%600

# A:BC.D
# A=minutes
# BC=seconds
# D =tenths of a second


# print(random.randrange(1,7))
