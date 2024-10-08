from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j, cnt = 1, 1
        n = len(nums)

        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                cnt += 1
            else:
                cnt = 1

            if cnt <= 2:
                nums[j] = nums[i]
                j += 1
        return j


sol = Solution()
nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
sol.removeDuplicates(nums=nums)
