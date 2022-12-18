# https://leetcode.com/problems/shortest-path-to-get-all-keys/
# 864. Shortest Path to Get All Keys
from typing import List
from collections import deque
from copy import deepcopy


class Solution:
    from collections import deque
    from copy import deepcopy

    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [[0, 1], [-1, 0], [1, 0], [0, -1]]

        keys = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5}
        locks = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5}

        total_keys = 0
        for i in range(m):
            for j in range(n):
                total_keys += grid[i][j] in keys
                if grid[i][j] == "@": starting_point = [i, j]

        queue = deque()
        queue.append((starting_point[0], starting_point[1], 0, 0))
        # (x_coordinates, y_coordinates, have_keys (bitmask), n_steps)
        visited = set()
        visited.add((starting_point[0], starting_point[1], 0))
        while queue:
            x_pos, y_pos, have_keys, n_step = queue.popleft()

            if have_keys == (1 << total_keys) - 1: return n_step - 1

            curr = grid[x_pos][y_pos]

            if curr in locks and not ((have_keys >> locks[curr]) & 1): continue

            if curr in keys: have_keys |= (1 << keys[curr])

            for direction in directions:
                new_x = x_pos + direction[0]
                new_y = y_pos + direction[1]
                if self.moveable(
                        new_x, new_y, m, n,
                        grid) and (new_x, new_y, have_keys) not in visited:
                    queue.append((new_x, new_y, have_keys, n_step + 1))
                    visited.add((new_x, new_y, have_keys))
        return -1

    def moveable(self, new_x, new_y, m, n, grid):
        return 0 <= new_x < m and 0 <= new_y < n and grid[new_x][new_y] != "#"