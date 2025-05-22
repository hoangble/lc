from typing import List

# class Solution:
#     def minCostClimbingStairs(self, cost: List[int]) -> int:
#         t = [None] * (len(cost) + 1)
#         self.helper(len(cost), t, cost)
#         return t[-1]

#     def helper(self, pos, t, cost) -> int:
#         if pos == 0 or pos == 1:
#             return 0

#         if t[pos] is not None:
#             return t[pos]

#         t[pos] = min(
#             self.helper(pos - 1, t, cost) + cost[pos - 1],
#             self.helper(pos - 2, t, cost) + cost[pos - 2],
#         )
#         return t[pos]


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # cost = min(this + last[i-2], last[i-1])
        tab = {}
        reach_end_from_pen_ultimate = self.dp(len(cost) - 2, cost, tab)
        reach_end = self.dp(len(cost) - 1, cost, tab) + cost[-1]
        print(tab)
        return min(reach_end, reach_end_from_pen_ultimate)

    def dp(self, i, cost, tab):
        # if i < 0:
        #     return 0

        if i == 0:
            return cost[0]

        if i == 1:
            return cost[1]

        if i in tab:
            return tab[i]

        tab[i] = min(cost[i] + self.dp(i - 2, cost, tab), self.dp(i - 1, cost, tab))
        return tab[i]


cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
sol = Solution().minCostClimbingStairs(cost)
