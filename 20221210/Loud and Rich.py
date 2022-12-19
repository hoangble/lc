# https://leetcode.com/problems/loud-and-rich/
# 851. Loud and Rich
from typing import List
from collections import defaultdict


class Solution:
    def loudAndRich(self, richer: List[List[int]],
                    quiet: List[int]) -> List[int]:
        if not richer: return sorted(quiet)
        rich = defaultdict(list)
        for i, j in richer:
            rich[j].append(i)
        ans = [-1] * len(quiet)
        for i in range(len(quiet)):
            self.dfs(ans, i, rich, quiet)
        return ans

    def dfs(self, ans, i, rich, quiet):
        if ans[i] >= 0: return ans[i]
        ans[i] = i
        for j in rich[i]:
            if quiet[ans[i]] > quiet[self.dfs(ans, j, rich, quiet)]:
                ans[i] = ans[j]
        return ans[i]