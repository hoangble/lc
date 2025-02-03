from heapq import heapify, heappop, heappush
from math import ceil
from typing import List


class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        _nums = [-1 * i for i in nums]
        heapify(_nums)

        # greedily get the score
        score = 0
        while k > 0:
            current_max = heappop(_nums) * -1
            score += current_max
            heappush(_nums, ceil(current_max / 3) * -1)
            k -= 1
        return score
