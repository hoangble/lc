# https://leetcode.com/problems/maximum-product-subarray/description/
# 152. Maximum Product Subarray
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_ = nums[0]
        min_ = nums[0]
        curr_max = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < 0:
                max_, min_ = self.swap(max_, min_)

            max_ = max(nums[i], max_ * nums[i])
            min_ = min(nums[i], min_ * nums[i])

            curr_max = max(curr_max, max_)

        return curr_max

    def swap(self, a, b):
        tmp = a
        a = b
        b = tmp
        return a, b
