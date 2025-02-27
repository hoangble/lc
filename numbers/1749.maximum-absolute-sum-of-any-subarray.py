from typing import List


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        curr_sum = 0
        ans = 0

        for i in range(len(nums)):
            if abs(curr_sum + nums[i]) >= abs(nums[i]):
                curr_sum = curr_sum + nums[i]
            else:
                curr_sum = nums[i]

            ans = max(abs(curr_sum), ans)
        return ans


arr = [-7, -1, 0, -2, 1, 3, 8, -2, -6, -1, -10, -6, -6, 8, -4, -9, -4, 1, 4, -9]

Solution().maxAbsoluteSum(arr)
