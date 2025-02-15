from typing import List


class Solution:
    def intervalIntersection(
        self, firstList: List[List[int]], secondList: List[List[int]]
    ) -> List[List[int]]:
        ans = []
        m, n = len(firstList), len(secondList)
        i, j = 0, 0
        while i < m and j < n:
            low = max(firstList[i][0], secondList[j][0])
            hi = min(firstList[i][1], secondList[j][1])
            if low <= hi:
                ans.append([low, hi])
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
        return ans


sol = Solution()
firstList = [[0, 2], [5, 10], [13, 23], [24, 25]]
secondList = [[1, 5], [8, 12], [15, 24], [25, 26]]
sol.intervalIntersection(firstList, secondList)
