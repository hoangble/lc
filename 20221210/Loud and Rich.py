# https://leetcode.com/problems/loud-and-rich/
# 851. Loud and Rich
from typing import List
from collections import defaultdict


class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        if not richer:
            return sorted(quiet)
        rich = defaultdict(list)
        for i, j in richer:
            rich[j].append(i)
        ans = [-1] * len(quiet)
        for i in range(len(quiet)):
            self.dfs(ans, i, rich, quiet)
        return ans

    def dfs(self, ans, i, rich, quiet):
        if ans[i] >= 0:
            return ans[i]
        ans[i] = i
        for j in rich[i]:
            if quiet[ans[i]] > quiet[self.dfs(ans, j, rich, quiet)]:
                ans[i] = ans[j]
        return ans[i]


if __name__ == "__main__":
    sol = Solution()
    richer = [[1, 0], [2, 1], [3, 1], [3, 7], [4, 3], [5, 3], [6, 3]]
    quiet = [3, 2, 5, 4, 6, 1, 7, 0]

    sol.loudAndRich(richer=richer, quiet=quiet)

# %%

k = 2
matrix = [[0] * k] * k
matrix[0][1] = 1
print(matrix)

# %%
matrix[1][1]
