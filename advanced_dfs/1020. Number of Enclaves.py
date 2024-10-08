from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        self.dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()
        all_islands = []
        m, n = len(grid), len(grid[0])

        total = 0

        for i in range(m):
            for j in range(n):
                if (i, j) not in visited and grid[i][j] == 1:
                    this_graph = []
                    self.dfs(i, j, grid, m, n, visited, this_graph)
                    all_islands.append(this_graph)
                    total += len(this_graph)

        for island in all_islands:
            for i in island:
                if i[0] == 0 or i[1] == 0 or i[0] == m - 1 or i[1] == n - 1:
                    total -= len(island)
                    break
        return total

    def dfs(self, x, y, graph, m, n, visited, this_graph) -> None:
        if graph[x][y] == 0:
            return

        visited.add((x, y))
        this_graph.append((x, y))

        for d in self.dirs:
            new_x = x + d[0]
            new_y = y + d[1]

            if (
                self.valid(new_x, new_y, m, n)
                and (new_x, new_y) not in visited
                and graph[new_x][new_y] == 1
            ):
                self.dfs(new_x, new_y, graph, m, n, visited, this_graph)
        return

    def valid(self, x, y, m, n) -> bool:
        return 0 <= x < m and 0 <= y < n
