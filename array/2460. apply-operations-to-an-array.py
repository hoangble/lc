from typing import List 


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        write_idx = 0
        for i in range(n):
            if i < n -1 and nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

            if nums[i] != 0:
                if i != write_idx:
                    nums[write_idx], nums[i]  = nums[i], nums[write_idx]
                write_idx += 1
        
        return nums
