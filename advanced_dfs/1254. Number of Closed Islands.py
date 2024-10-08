from typing import List
# class Solution:
#     def closedIsland(self, grid: List[List[int]]) -> int:
#         # bfs/dfs/union find
#         # for bfs, we can traverse within an island
#         m, n = len(grid), len(grid[0])
#         if m <= 1 and n <= 1: return 0
#         # if m <= 2 or n <= 2: return 0

#         self.dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
#         ans = 0
#         total_island = 0
#         visited = set()
#         all_islands = []
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == 0 and (i, j) not in visited:
#                     this_island = []
#                     self.dfs(i, j, grid, visited, m, n, this_island)
#                     total_island += 1
#                     all_islands.append(this_island)
#         # print(total_island)
#         # print(all_islands)
#         for island in all_islands:
#             for (x, y) in island:
#                 if x == 0 or y == 0 or x == m - 1 or y == n - 1:
#                     total_island -= 1
#                     break
#         return total_island


#         # detect island
#         # check water-bounded # how can we bound water? actually dont need to, just take out the islands on the bound and that is alright

#     def dfs(self, x, y, graph, visited, m, n, this_island) -> None:
#         if graph[x][y] == 1:
#             return

#         visited.add((x, y))
#         this_island.append((x, y))

#         for d in self.dirs:
#             new_x = x + d[0]
#             new_y = y + d[1]

#             if self.valid(new_x, new_y, m, n):
#                 if graph[new_x][new_y] == 0 and (new_x, new_y) not in visited:
#                     self.dfs(new_x, new_y, graph, visited, m, n, this_island)
#         return

#     def valid(self, x, y, m , n):
#         return 0 <= x < m and 0 <= y < n


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            nonlocal grid
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return 0
            if grid[i][j] == 1:
                return 1
            if grid[i][j] == 2:
                return 1
            grid[i][j] = 2
            return dfs(i - 1, j) * dfs(i + 1, j) * dfs(i, j - 1) * dfs(i, j + 1)

        return sum(
            dfs(i, j)
            for i, row in enumerate(grid)
            for j, cell in enumerate(row)
            if cell == 0
        )
