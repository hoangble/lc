from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # if there are negative element, check https://leetcode.com/problems/subarray-sum-equals-k/description/
        # since no negative numbers -> sliding window
        l, r = 0, 0
        total = 0
        cnt = 0
        while r < len(nums):
            total += nums[r]
            if total == k and l - r + 1 >= 2:
                return True

            while total > k and l < r:
                total -= nums[l]
                l += 1

                if total == k and l - r + 1 >= 2:
                    return True

            r += 1
        return False


Solution().checkSubarraySum([23, 2, 4, 6, 7], 6)
