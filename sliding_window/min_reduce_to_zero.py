# https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/
# 1658. Minimum Operations to Reduce X to Zero

from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        if sum(nums) == x:
            return len(nums)
        elif nums[-1] == x or nums[0] == x:
            return 1
        elif sum(nums) < x:
            return -1
        else:
            ## sliding window to solve the sum(nums)-x -> take outside of this window
            target = sum(nums) - x
            left, right = 0, 0
            sum_ = 0
            max_len = 0
            found = False
            while right < len(nums):
                sum_ += nums[right]

                while sum_ > target and left <= right:
                    sum_ -= nums[left]
                    left += 1

                if sum_ == target:
                    max_len = max(max_len, right - left + 1)
                    found = True

                right += 1
            return len(nums) - max_len if found else -1
