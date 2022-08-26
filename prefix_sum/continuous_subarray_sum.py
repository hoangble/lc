# 523. Continuous Subarray Sum
from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix_sum = 0
        div_dict = {0: -1}
        # div_set.add(0)
        for i in range(len(nums)):
            prefix_sum += nums[i]
            d = prefix_sum % k
            # if d % k == 0: return True
            if d in div_dict:
                if i - div_dict[d] >= 2:
                    return True
            else:
                div_dict[d] = i
        return False
