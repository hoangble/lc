# 1482. Minimum Number of Days to Make m Bouquets
# https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/

from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        # write a function to check if if we can make m bouquets in x days
        def possible(x):
            bouquet, flower = 0, 0
            for bloom in bloomDay:
                if bloom > x:
                    flower = 0
                else:
                    bouquet += (flower + 1) // k
                    flower = (flower + 1) % k
            return bouquet >= m

        # main approach is to use binary search: start from a number, check to see if we can make m bouquets in         that many day -> if yes then m//2 else m *2
        if len(bloomDay) < m * k:
            return -1
        lo, hi = min(bloomDay), sum(bloomDay)

        while lo < hi - 1:
            mid = (lo + hi) // 2
            if possible(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo if possible(lo) else hi
