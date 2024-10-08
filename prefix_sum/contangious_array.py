from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_len = 0
        prefix_sum_dict = {0: -1}
        prefix_sum = 0
        # curr_len = 0 # out of scope

        for i in range(len(nums)):
            if nums[i] == 0:
                prefix_sum -= 1
            else:
                prefix_sum += 1

            if prefix_sum in prefix_sum_dict.keys():
                last_idx = prefix_sum_dict[prefix_sum]
                curr_len = i - last_idx
                if curr_len > max_len:
                    max_len = curr_len
            else:
                prefix_sum_dict[prefix_sum] = i
        return max_len
