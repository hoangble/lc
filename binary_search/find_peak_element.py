# 162. Find Peak Element
# https://leetcode.com/problems/find-peak-element/

from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        #### get rid of element lower than
        # if len(nums) == 1: return 0
        # elif len(nums) == 2: return 0 if nums[0] > nums[1] else 1
        left = 0
        right = len(nums) - 1
        while left < right - 1:
            mid = (left + right) // 2
            # if mid > 0 and nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
            #     return mid
            if nums[mid] > nums[mid - 1]:
                left = mid + 1
            else:
                right = mid - 1
        return left if nums[left] > nums[right] else right
