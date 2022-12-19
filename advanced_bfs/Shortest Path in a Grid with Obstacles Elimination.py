# 1293. Shortest Path in a Grid with Obstacles Elimination
# https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/description/

from typing import List
from collections import deque


class Solution:
    from collections import deque

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        queue = deque()
        queue.append((0, 0, k, 0))  #(x, y, k, n_step)
        visited = set()
        visited.add((0, 0, k))

        while queue:
            x, y, curr_k, n_step = queue.popleft()

            if x == m - 1 and y == n - 1: return n_step

            for direction in directions:
                new_x = x + direction[0]
                new_y = y + direction[1]
                if self.check_valid(new_x, new_y, m, n):
                    new_k = curr_k - grid[new_x][new_y]
                    if new_k >= 0 and (new_x, new_y, new_k) not in visited:
                        queue.append((new_x, new_y, new_k, n_step + 1))
                        visited.add((new_x, new_y, new_k))
        return -1

    def check_valid(self, x, y, m, n):
        return 0 <= x < m and 0 <= y < n