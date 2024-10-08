from typing import List


class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        if len(nums) < 2:
            return -1
        nums.sort()
        left = 0

        print(nums)
        ans = 0
        for right in range(1, len(nums)):
            sum_ = nums[left] + nums[right]
            while nums[left] + nums[right] < k and left < right:
                sum_ = nums[left] + nums[right]

                ans = max(ans, sum_)
                left += 1

        if ans == 0:
            return -1
        return ans


sol = Solution()
sol.twoSumLessThanK([34, 23, 1, 24, 75, 33, 54, 8], 60)
