from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum_dict = {0: 1}
        prefix_sum = 0
        ans = 0
        for num in nums:
            prefix_sum += num

            if prefix_sum - k in prefix_sum_dict:
                ans += prefix_sum_dict[prefix_sum - k]

            if prefix_sum not in prefix_sum_dict:
                prefix_sum_dict[prefix_sum] = 1
            else:
                prefix_sum_dict[prefix_sum] += 1

        return ans
