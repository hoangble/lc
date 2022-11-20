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


## Redo 11/20/2021
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.subset_helper(0, [], ans, nums) 
        return ans
    
    def subset_helper(self, start, current, ans, nums):
        ans.append(current.copy())
        for i in range(start, len(nums)):
            self.subset_helper(i + 1, current + [nums[i]], ans, nums)        