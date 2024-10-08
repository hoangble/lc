# https://leetcode.com/problems/max-consecutive-ones-iii/submissions/

from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left_ptr = 0
        right_ptr = 0
        num_zeros = 0
        max_size = -1
        while right_ptr < len(nums):
            if nums[right_ptr] == 0:
                num_zeros += 1
            while num_zeros > k and left_ptr <= right_ptr:
                if nums[left_ptr] == 0:
                    num_zeros -= 1
                left_ptr += 1
            max_size = max(max_size, right_ptr - left_ptr + 1)
            right_ptr += 1
        return max_size
