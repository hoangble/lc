from typing import List


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        ans = 0
        cnt = 1
        last_color = colors[0]

        for i in range(1, n + k - 1):
            idx = i % n
            if colors[idx] == last_color:
                cnt = 1
                last_color = colors[idx]
                continue
            cnt += 1
            if cnt >= k:
                ans += 1
            last_color = colors[idx]
        return ans


Solution().numberOfAlternatingGroups([0, 1, 0, 0, 1, 0, 1], 6)
