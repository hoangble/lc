# 1590. Make Sum Divisible by P
from typing import List


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        prefix_sum_dict = {0: -1}
        prefix_sum = 0
        extra = sum(nums) % p
        min_len = len(nums)
        for i in range(len(nums)):
            prefix_sum += nums[i]

            div = prefix_sum % p
            prefix_sum_dict[div] = i

            if (div - extra) % p in prefix_sum_dict:
                curr_len = i - prefix_sum_dict[(div - extra) % p]
                if curr_len < min_len:
                    min_len = curr_len

        if min_len >= len(nums): min_len = -1
        return min_len
