# 2455. Average Value of Even Numbers That Are Divisible by Three
# https://leetcode.com/problems/average-value-of-even-numbers-that-are-divisible-by-three/

from typing import List


class Solution:
    def averageValue(self, nums: List[int]) -> int:
        sum_ = 0
        cnt_ = 0
        for i in nums:
            if i % 2 == 0 and i % 3 == 0:
                sum_ += i
                cnt_ += 1
        if cnt_ == 0:
            return 0
        return sum_ // cnt_
