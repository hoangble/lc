class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        memo = {}
        return self.dfs(abs(x), abs(y), memo)

        # O(1)
        # x, y = abs(x), abs(y)
        # if (x < y): x, y = y, x
        # if (x == 1 and y == 0): return 3        
        # if (x == 2 and y == 2): return 4        
        # delta = x - y
        # if (y > delta):
        #     return delta - 2 * ((delta - y) // 3)
        # else:
        #     return delta - 2 * ((delta - y) // 4)
        
    def dfs(self, x, y, memo):
        if (x, y) in memo:
            return memo[(x, y)]
        
        if x == y == 0:
            return 0
        
        if x + y == 2:
            return 2
        
        memo[(x, y)] = 1 + min(self.dfs(abs(x - 1), abs(y - 2), memo), self.dfs(abs(x - 2), abs(y - 1), memo)) 
        return memo[(x, y)]