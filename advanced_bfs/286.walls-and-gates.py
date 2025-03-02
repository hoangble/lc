from collections import deque
from typing import List


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        EMPTY = 2147483647
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        q = deque([])
        m, n = len(rooms), len(rooms[0])

        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    q.append((i, j))

        while q:
            x, y = q.popleft()
            for d in dirs:
                new_x = x + d[0]
                new_y = y + d[1]
                if (
                    new_x < 0
                    or new_x >= m
                    or new_y < 0
                    or new_y >= n
                    or rooms[new_x][new_y] != EMPTY
                ):
                    continue

                rooms[new_x][new_y] = rooms[x][y] + 1
                q.append((new_x, new_y))

        return rooms
