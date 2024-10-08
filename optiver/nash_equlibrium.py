import numpy as np
import scipy, sklearn, pandas as pd, statsmodels
import math
import os
import random
import re
import sys


def get_slope(x1, y1, x2, y2):
    # slope != 0
    if x2 - x1 != 0:
        return (y2 - y1) / (x2 - x1)
    # x1 = x2
    else:
        return None


def get_line_equation(x1, y1, x2, y2):
    slope = get_slope(x1, y1, x2, y2)
    if slope is not None:
        b = y1 - slope * x1
        return slope, b
    else:
        return None, None


def tiebreak(x_knots, y_knots, x_input, x2, y2):
    # x_y_dict = {x:y for x, y in zip(x_knots, y_knots)}
    x_knots = np.array(x_knots)
    y_knots = np.array(y_knots)

    tie_ys = y_knots[x_knots == x2]
    if x_input <= x2:
        y2 = np.amin(tie_ys)
    else:
        y2 = np.amax(tie_ys)
    return x2, y2


def find_bound_pts(x_knots, y_knots, x_input):
    max_x = max(x_knots)
    # print(max_x)
    min_x = min(x_knots)

    if len(x_knots) == 2:
        x1 = max_x
        y1 = y_knots[np.argmax(x_knots)]

        x2 = min_x
        y2 = y_knots[np.argmin(x_knots)]
    else:
        if x_input > max_x:
            x1 = max_x
            y1 = y_knots[np.argmax(x_knots)]

            second_largest_idx = np.argpartition(x_knots, -2)[-2:]  # 2nd largest
            second_largest_idx = second_largest_idx[-2]
            x2 = x_knots[second_largest_idx]
            y2 = y_knots[second_largest_idx]

            x_knots = np.array(x_knots)
            if (np.array(x_knots) == x2).sum() > 1:
                x2, y2 = tiebreak(x_knots, y_knots, x_input, x2, y2)
            if (np.array(x_knots) == x1).sum() > 1:
                x1, y1 = tiebreak(x_knots, y_knots, x_input, x1, y1)

        elif x_input < min_x:
            x1 = min_x
            y1 = y_knots[np.argmin(x_knots)]

            second_smallest_idx = np.argpartition(x_knots, 2)[:2]  # 2nd largest
            second_smallest_idx = second_smallest_idx[-1]
            x2 = x_knots[second_smallest_idx]
            y2 = y_knots[second_smallest_idx]
            if (np.array(x_knots) == x2).sum() > 1:
                x2, y2 = tiebreak(x_knots, y_knots, x_input, x2, y2)
            if (np.array(x_knots) == x1).sum() > 1:
                x1, y1 = tiebreak(x_knots, y_knots, x_input, x1, y1)

        else:  # normal case find the two boundary
            x_y_dict = {x: y for x, y in zip(x_knots, y_knots)}
            x_knots = np.array(x_knots)
            x1 = x_knots[x_knots > x_input].min()
            y1 = x_y_dict[x1]
            x2 = x_knots[x_knots < x_input].max()
            y2 = x_y_dict[x2]
            if (np.array(x_knots) == x2).sum() > 1:
                x2, y2 = tiebreak(x_knots, y_knots, x_input, x2, y2)
            if (np.array(x_knots) == x1).sum() > 1:
                x1, y1 = tiebreak(x_knots, y_knots, x_input, x1, y1)
    return x1, y1, x2, y2


def linear_interpolate(n, x_knots, y_knots, x_input):
    # Write your code here
    x1, y1, x2, y2 = find_bound_pts(x_knots, y_knots, x_input)

    # write function to get the equation of line when there are two points (find slopes and y-intercept)
    slope, y_intercept = get_line_equation(x1, y1, x2, y2)
    # slope, y_intercept = np.round(slope, 3),  np.round(y_intercept, 3)
    print(slope, y_intercept)
    # plug in the x_input to get output
    if slope is not None:
        output = slope * x_input + y_intercept
        return round(output, 3)
    else:
        return None


def interpolate_test(x_knots, y_knots, x_input):
    x_y_dict = {x: y for x, y in zip(x_knots, y_knots)}
    # x_knots = np.array(x_knots)

    x_knot_sorted = sorted(x_knots)
    y_knot_sorted = [x_y_dict[x] for x in x_knot_sorted]

    return np.interp(x=x_input, xp=x_knot_sorted, fp=y_knot_sorted)


if __name__ == "__main__":
    # Test case 1
    # n = 5
    # x_knots = [1.0, 2.0, -2.0, -1.0, 0.0]
    # y_knots = [0.0, 5.0, 0.0, 10.0, 15.0]
    # x_input = -0.3

    # Test case 2
    # n = 5
    # x_knots = [-2.0, -1.0, 0.0, 1.0, 2.0]
    # y_knots = [0.0, 10.0, 15.0, 0.0, 5.0]
    # x_input = -3.0

    # Test case 3
    # n = 6
    # x_knots = [-2.0, -1.0, -1.0, 0.0, 1.0, 2.0]
    # y_knots = [0.0, 10.0, 12.0, 15.0, 0.0, 5.0]
    # x_input = -0.5

    # Test case 4
    # n = 2
    # x_knots = [1.0, -1.0]
    # y_knots = [1.0, -1.0]
    # x_input = -0.5

    # Test case 5
    # n = 3
    # x_knots = [1.0, 1.0, 1.0]
    # y_knots = [1.0, -1.0, 2.0]
    # x_input = -0.5

    # Test case 6
    # n = 2
    # x_knots = [1.0, 1.0]
    # y_knots = [1.0, -1.0]
    # x_input = -0.5

    # Test case 7
    # n = 5
    # x_knots = [-2.0, -1.0, 0.0, 1.0, 2.0]
    # y_knots = [0.0, 10.0, 15.0, 0.0, 5.0]
    # x_input = 3.0

    # Test case 8
    # n = 2
    # x_knots = [1.0, 2.0]
    # y_knots = [0.0, 5.0]
    # x_input = 3.0

    # Test case 9
    # n = 30
    # x_knots = [-99.0, -87.0, -75.0, -73.0, -53.0, -46.0, -41.0, -31.0, -26.0, -23.0, -23.0, -13.0, -10.0, -9.0, -8.0, -5.0, 0.0, 7.0, 21.0, 25.0, 26.0, 36.0, 43.0, 44.0, 46.0, 80.0, 82.0, 88.0, 91.0, 93.0]
    # y_knots = [-64.0, 92.0, -77.0, 12.0, -19.0, 79.0, 74.0, -28.0, 24.0, -99.0, -96.0, -43.0, 52.0, -34.0, 94.0, 27.0, -3.0, 97.0, 66.0, 23.0, -5.0, -23.0, 77.0, 44.0, 79.0, 75.0, -68.0, 41.0, -38.0, -40.0]
    # x_input = -25.0

    # Test case 10
    n = 30
    x_knots = [
        -98.0,
        -88.0,
        -82.0,
        -77.0,
        -76.0,
        -71.0,
        -68.0,
        -64.0,
        -64.0,
        -32.0,
        -30.0,
        -29.0,
        -21.0,
        9.0,
        14.0,
        19.0,
        27.0,
        46.0,
        50.0,
        56.0,
        59.0,
        60.0,
        67.0,
        82.0,
        84.0,
        87.0,
        89.0,
        94.0,
        94.0,
        99.0,
    ]
    y_knots = [
        -66.0,
        80.0,
        8.0,
        -13.0,
        -8.0,
        -51.0,
        94.0,
        58.0,
        62.0,
        -12.0,
        -56.0,
        40.0,
        83.0,
        -27.0,
        -19.0,
        9.0,
        -35.0,
        -69.0,
        -12.0,
        -69.0,
        -81.0,
        26.0,
        -11.0,
        -73.0,
        -31.0,
        18.0,
        45.0,
        -75.0,
        -33.0,
        88.0,
    ]
    x_input = 120.0

    print(find_bound_pts(x_knots, y_knots, x_input))
    print(linear_interpolate(n, x_knots, y_knots, x_input))
    print(interpolate_test(x_knots, y_knots, x_input))


# %%
# import numpy as np
# y = np.array([2, 3, 4])
# print((y==3).sum())
