from collections import deque
from typing import List


class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        # bfs
        m, n = len(grid), len(grid[0])
        total_buildings = 0
        buildings = []
        lands = []

        ans = []
        for i in range(m):
            ans.append([])
            for j in range(n):
                ans[i].append([0, 0])
                if grid[i][j] == 1:
                    total_buildings += 1
                    buildings.append((i, j))
                elif grid[i][j] == 0:
                    lands.append((i, j))

        curr_land = 0
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def bfs(i, j):
            q = deque([(i, j, 0)])
            visited = set()
            while q:
                x, y, dist = q.popleft()

                
                if grid[x][y] != 1:
                    ans[x][y][0] += 1
                    ans[x][y][1] += dist
                    # grid[x][y] -= 1

                for d in dirs:
                    new_x = x + d[0]
                    new_y = y + d[1]
                    if (
                        in_bound(new_x, new_y)
                        and (new_x, new_y) not in visited
                        and grid[new_x][new_y] == 0
                    ):
                        q.append((new_x, new_y, dist + 1))
                        visited.add((new_x, new_y))


        def in_bound(x, y):
            return 0 <= x < m and 0 <= y < n

        for i, j in buildings:
            bfs(i, j)
            # curr_land -= 1

        print(ans)
        min_val = float("inf")
        updated = False
        for i in range(m):
            for j in range(n):
                if ans[i][j] == total_buildings:
                    min_val = min(min_val, ans[i][j])
                    updated = True

        return min_val if updated else -1


sol = Solution()
grid = [[1, 0, 2, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]
sol.shortestDistance(grid)
