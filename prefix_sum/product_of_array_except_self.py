# 238. Product of Array Except Self
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prod = []
        for i in range(len(nums)):
            if i == 0:
                prefix_prod.append(nums[i])
            else:
                prefix_prod.append(nums[i] * prefix_prod[i - 1])

        suffix_prod = []
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                suffix_prod.insert(0, nums[i])
            else:
                suffix_prod.insert(0, nums[i] * suffix_prod[0])

        result = []
        for i in range(len(nums)):
            if i == 0:
                result.append(suffix_prod[i + 1])

            elif i == len(nums) - 1:
                result.append(prefix_prod[i - 1])

            else:
                result.append(prefix_prod[i - 1] * suffix_prod[i + 1])

        return result
