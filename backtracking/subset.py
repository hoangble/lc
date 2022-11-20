from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.subsets_helper(nums, start=0, curr_subset=[], ans=ans)
        return ans

    def subsets_helper(self, nums, start, curr_subset, ans):
        ans.append(curr_subset)
        for i in range(start, len(nums)):
            self.subsets_helper(nums, i + 1, curr_subset + [nums[i]], ans)
