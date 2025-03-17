from typing import List


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        if sum(colors) == len(colors):
            return 0

        n = len(colors)
        ans = 0
        for i in range(n):
            if colors[i % n] == colors[(i + 2) % n] and colors[i % n] != colors[(i + 1) % n]:
                ans += 1
        return ans


Solution().numberOfAlternatingGroups([0, 1, 0, 0, 1])
