from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left_ptr = 0 
        # right_ptr = -1
        min_size = len(nums)+1
        running_sum = 0
        for right_ptr in range(len(nums)):
            # curr_sum = nums[left_ptr:right_ptr+1] # actually for lôp 
            running_sum += nums[right_ptr]
            while running_sum >= target:
                # if right_ptr - left_ptr + 1 > min_size:
                #     min_size = right_ptr - left_ptr + 1
                min_size = min(right_ptr - left_ptr + 1, min_size)
                running_sum -= nums[left_ptr]
                left_ptr += 1
        
        if min_size == len(nums)+1:
            min_size = 0
        return min_size