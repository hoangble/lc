# 930. Binary Subarrays With Sum
from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_sum = 0
        cnt = 0

        sum_dict = {0: 1}  # {prefix-k: # times appear}

        for i in nums:
            prefix_sum += i

            if prefix_sum - goal in sum_dict:
                cnt += sum_dict[prefix_sum - goal]

            if prefix_sum not in sum_dict.keys():
                sum_dict[prefix_sum] = 1
            else:
                sum_dict[prefix_sum] += 1
        return cnt
