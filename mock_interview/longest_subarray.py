# Give a street where each block is a plot of land with the same size, but different prices. You have a fixed amount of money and need to buy the longest continuous plot of land possible.

# prices = [1, 5, 3, 4], k = 10. ans = 3
# len(prices) > 0 
# k > 0
# ans = 0

from typing import List 
def longest_subarray(prices: List, k: int) -> int:
    if len(prices) == 1:
        if prices[0] <= k: return 1
        else : return 0
    
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
# prices = [[1, 5, 3, 1], [2, 4, 6, 1], [2, 5, 9, 1]], k = 12, ans = 3
# [[1, 5, 3, 1], 
# [2, 4, 6, 1], 
# [2, 5, 9, 1]]

from typing import List 
def longest_subarray_2d(prices: List[List], k: int) -> int:
    m, n = len(prices), len(prices[0])
    prefix_sum = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(m):
        for j in range(n):
            prefix_sum[i][j] = prefix_sum[i][j] + prices[i][j]
    
    left_corner_x = 0
    left_corner_y = 0

    while left_corner_x < n and left_corner_y < m:



    ans = 0
    return ans

   0  1. 2  3
0 [1, 2, 3, 4]
1 [1, 2, 3, 4]
2 [1, 2, 3, 8]

sum from [0, 0] to [2, 3]

sum[2, 3] = array[2, 3] + sum[1, 3] + sum[2, 2] - sum[1, 2]

sum[i, j] = array[i, j] + sum[i-1, j] + sum[i, j-1] - sum[i-1, j-1]

sum(a, b, x, y) = sum[x, y] - sum[x, b-1] - sum[a-1, y] + sum[a-1, b-1]
