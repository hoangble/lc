# https://leetcode.com/problems/maximum-subarray/description/
# 53. Maximum Subarray

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [None] * len(nums)
        dp[0] = nums[0]
        max_ = nums[0]

        for i in range(1, len(nums)):
            dp[i] = nums[i] + max(0, dp[i - 1])
            max_ = max(dp[i], max_)
        return max_
