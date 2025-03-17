from typing import List


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        ans = []

        seen = {}

        n = len(grid)
        for x in range(n):
            for y in range(n):
                i = grid[x][y]
                if i not in seen:
                    seen[i] = False
                elif not seen[i]:
                    seen[i] = True
                elif seen[i]:
                    ans.append(i)

        for i in range(1, n * n + 1):
            if i not in seen:
                ans.append(i)

        return ans


Solution().findMissingAndRepeatedValues([[1, 3], [2, 2]])
