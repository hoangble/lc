from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        l = r = 0
        cnt = 0
        total = 0

        while r < len(nums):
            total += nums[r]
            if total == goal:
                cnt += 1

            while total > goal and l < r:
                total -= nums[l]
                l += 1
                if total == goal:
                    cnt += 1

            r += 1
        return cnt


Solution().numSubarraysWithSum([1, 0, 1, 0, 1], 2)
