class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        memo = {}
        return self.dfs(abs(x), abs(y), memo)
        
    def dfs(self, x, y, memo):
        if (x, y) in memo:
            return memo[(x, y)]
        
        if x == y == 0:
            return 0
        
        if x + y == 2:
            return 2
        
        memo[(x, y)] = 1 + min(self.dfs(abs(x - 1), abs(y - 2), memo), self.dfs(abs(x - 2), abs(y - 1), memo)) 
        return memo[(x, y)]