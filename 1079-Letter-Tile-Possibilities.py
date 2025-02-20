class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        res = set()

        # backtracking
        def dfs(path, t):
            if path not in res:
                if path:
                    res.add(path)
                
                for i in range(len(t)):
                    dfs(path+t[i], t[:i] + t[i + 1:])
        dfs('', tiles)
        return len(res)
        