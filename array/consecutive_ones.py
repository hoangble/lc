from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        start_ = None
        end_ = None
        max_len = 0
        for i in range(len(nums)):
            if nums[i] == 1 and start_ is None:
                start_ = end_ = i
                curr_len = 0
            if start_ is not None:
                if nums[i] == 0:
                    curr_len = end_ - start_ + 1
                    max_len = max(curr_len, max_len)
                    start_ = None
                else:
                    end_ = i
            ### end of array

            if i == len(nums) - 1:
                if start_ is None:
                    curr_len = 0
                else:
                    if nums[i] == 0:
                        curr_len = end_ - start_
                        max_len = max(curr_len, max_len)
                    elif nums[i] == 1:
                        curr_len = end_ - start_ + 1
                max_len = max(curr_len, max_len)

        return max_len


# O(n)


### A cleaner solution
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr_cnt = 0
        max_cnt = 0
        for idx, num in enumerate(nums):
            if num == 1:
                curr_cnt += 1
            else:
                max_cnt = max(curr_cnt, max_cnt)
                curr_cnt = 0
        return max(max_cnt, curr_cnt)
