# https://leetcode.com/problems/max-consecutive-ones-ii/submissions/ 
# 487. Max Consecutive Ones II 

from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        left, right = 0, 0
        n_zeros = 0
        ans = -1
        while right < len(nums):
            n_zeros += nums[right] == 0
            
            # only move the left ptr if there are more than 1 zeros
            while n_zeros > 1:
                n_zeros -= nums[left] == 0
                left += 1
            
            # if there are less than one 1, check to get longest window
            if n_zeros <= 1:
                ans = max(ans, right - left + 1)

            # always move right
            right += 1
        return ans