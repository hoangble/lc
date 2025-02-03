class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        # self.visited = set()
        self.islands = {}
        self.m, self.n = len(grid), len(grid[0]) 
        self.dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        island_id = 1
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 1:
                    island_id += 1
                    self.islands[island_id] = self.explore(grid, i, j, island_id)
        
        if island_id == 1: return 1

        if len(self.islands) == 1:
            if self.islands[island_id] == self.m*self.n:
                return self.islands[island_id]
            else:
                return self.islands[island_id] + 1
        
        # another dfs to convert 1
        ans = 1
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 0:
                    current_island_size = 1
                    neigh_island = set()
                    if i + 1 < self.m and grid[i + 1][j] > 1:
                        neigh_island.add(grid[i + 1][j])
                    if 0 <= i - 1 and grid[i - 1][j] > 1:
                        neigh_island.add(grid[i - 1][j])
                    if j + 1 < self.n and grid[i][j + 1] > 1:
                        neigh_island.add(grid[i][j+1])
                    if 0 <= j - 1 and grid[i][j - 1] > 1:
                        neigh_island.add( grid[i][j - 1])
                    
                    for island_id in neigh_island:
                        current_island_size +=  self.islands[island_id]
                    ans = max(ans, current_island_size)
        return ans


    def explore(self, grid, i, j, island_id):
        ans  = 1
        grid[i][j] = island_id
        
        for x, y in self.dirs:
            new_x, new_y = i + x, j + y
            if self.valid(new_x, new_y) and grid[new_x][new_y] == 1:
                ans += self.explore(grid, new_x, new_y, island_id)
        return ans


    def valid(self, i, j):
        return 0 <= i < self.m and 0 <= j < self.n
        