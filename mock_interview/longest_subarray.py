# Give a street where each block is a plot of land with the same size, but different prices. You have a fixed amount of money and need to buy the longest continuous plot of land possible.

# prices = [1, 5, 3, 4], k = 10. ans = 3
# len(prices) > 0
# k > 0
# ans = 0

from typing import List


def longest_subarray(prices: List, k: int) -> int:
    if len(prices) == 1:
        if prices[0] <= k:
            return 1
        else:
            return 0

    left_ptr = 0
    right_ptr = left_ptr
    longest = 0
    total_cost = 0

    while right_ptr <= len(prices) - 1:
        # calculate the total cost:
        total_cost += prices[right_ptr]

        while total_cost > k:
            # move the left_ptr right
            total_cost -= prices[left_ptr]
            left_ptr += 1

        longest = max(longest, right_ptr - left_ptr + 1)
        right_ptr += 1

    return longest


prices = [1]
k = 10
print(longest_subarray(prices, k))

prices = [1]
k = 0
print(longest_subarray(prices, k))

# 2D plot of lands
# prices = [[1, 5, 3, 1], [2, 4, 6, 1], [2, 5, 9, 1]], k = 12, ans = 2
# [[1, 5, 3, 1],
# [2, 4, 6, 1],
# [2, 5, 9, 1]]
# approach:
# 1. start from the top left corner, we will increase the size until the sum > k
# 2. move to the next point being the next left corner of the square, if the sum is small -> increase the size
# 3. if we can't increase the size and rotate thru all possible left corner -> return k

from typing import List


def longest_subarray_2d(prices: List[List], k: int) -> int:
    con_sum_ = consecutive_sum(prices)

    left_corner_x = 0
    left_corner_y = 0

    m, n = len(prices), len(prices[0])
    ans = 0
    while left_corner_x < n and left_corner_y < m:
        while (
            valid(left_corner_x + ans, left_corner_y + ans, m, n)
            and prefix_sum(
                con_sum_,
                left_corner_x,
                left_corner_y,
                left_corner_x + ans,
                left_corner_y + ans,
            )
            <= k
        ):
            print(
                left_corner_x,
                left_corner_y,
                ans,
                prefix_sum(
                    con_sum_,
                    left_corner_x,
                    left_corner_y,
                    left_corner_x + ans,
                    left_corner_y + ans,
                ),
            )
            ans += 1
        left_corner_y += 1
        if left_corner_y == n:
            left_corner_y = 0
            left_corner_x += 1
    return ans


def consecutive_sum(prices: List[int]) -> List[int]:
    m, n = len(prices), len(prices[0])

    prefix_sum = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(m):
        prev_row = i - 1 if i - 1 >= 0 else 0
        for j in range(n):
            prev_col = j - 1 if j - 1 >= 0 else 0
            if i == 0:
                prefix_sum[i][j] = prices[i][j] + prefix_sum[0][prev_col]
            elif j == 0:
                prefix_sum[i][j] = prices[i][j] + prefix_sum[prev_row][0]
            else:
                prefix_sum[i][j] = (
                    prices[i][j]
                    + prefix_sum[prev_row][j]
                    + prefix_sum[i][prev_col]
                    - prefix_sum[prev_row][prev_col]
                )
    return prefix_sum


def prefix_sum(prefix_sum: List[int], x0: int, y0: int, x1: int, y1: int) -> List[int]:
    prev_x0 = x0 - 1 if x0 - 1 >= 0 else 0
    prev_y0 = y0 - 1 if y0 - 1 >= 0 else 0
    if x0 == 0 or y0 == 0:
        prefix_sum[prev_x0][prev_y0] = 0
    if x0 == 0:
        prefix_sum[prev_x0][y1] = 0
    if y0 == 0:
        prefix_sum[x1][prev_y0] = 0

    return (
        prefix_sum[x1][y1]
        - prefix_sum[x1][prev_y0]
        - prefix_sum[prev_x0][y1]
        + prefix_sum[prev_x0][prev_y0]
    )


def valid(x, y, m, n):
    return 0 <= x < m and 0 <= y < n


####
# Example and explanation of prefix sum
#    0  1. 2  3
# 0 [1, 2, 3, 4]
# 1 [1, 2, 3, 4]
# 2 [1, 2, 3, 8]

# sum from [0, 0] to [2, 3]

# sum[2, 3] = array[2, 3] + sum[1, 3] + sum[2, 2] - sum[1, 2]

# sum[i, j] = array[i, j] + sum[i-1, j] + sum[i, j-1] - sum[i-1, j-1]


# sum(x0, y0, x, y) = sum[x, y] - sum[x, y0-1] - sum[x0-1, y] + sum[x0-1, y0-1]
def print_mat(mat):
    for row in mat:
        print(row)


if __name__ == "__main__":
    prices = [[1, 5, 3, 1], [2, 4, 6, 1], [2, 5, 9, 1]]
    print(longest_subarray_2d(prices, 37))
    # print_mat(prices)
    # print("prefix sum")
    # con_sum_ = consecutive_sum(prices)
    # print_mat(con_sum_)
    # print(prefix_sum(con_sum_, x0= 0, y0 = 0, x1 = 1, y1 = 1))
