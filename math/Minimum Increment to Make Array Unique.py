# https://leetcode.com/problems/minimum-increment-to-make-array-unique/description/
# 945. Minimum Increment to Make Array Unique

from typing import List


class Solution:
    from collections import Counter

    def minIncrementForUnique(self, nums: List[int]) -> int:
        res = need = 0
        for i in sorted(nums):
            res += max(need - i, 0)
            need = max(need + 1, i + 1)
        return res