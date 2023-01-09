class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        ans = 0
        all_unique_islands = set()
        self.moves = [[0,1], [0,-1], [1,0], [-1,0]]
        self.moves_str = ["u", "d", "r", "l"]
        m, n = len(grid), len(grid[0]) 

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    curr_dir = ""
                    curr_dir = self.helper(row, col, m, n, grid, curr_dir)
                    print(curr_dir)
                    all_unique_islands.add(curr_dir)
                    # ans += 1

        return len(all_unique_islands)

    
    def helper(self, x, y, m, n, grid, current_island) -> str:
        # print(current_island)
        for move, move_str in zip(self.moves, self.moves_str):
            next_x = x + move[0]
            next_y = y + move[1]

            if 0 <= next_x < m and 0 <= next_y < n and grid[next_x][next_y] == 1:
                current_island += move_str
                grid[next_x][next_y] = 0
                current_island = self.helper(next_x, next_y, m, n, grid, current_island)
                current_island += "b"
        return current_island
