# https://leetcode.com/problems/contains-duplicate-ii/
# 219. Contains Duplicate II

from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(set(nums)) == len(nums):
            return False

        left = 0
        right = 0

        while right < len(nums):
            while right - left > k:
                if nums[right] == nums[left]:
                    return True
                left += 1
            right += 1
        return False

    ### easier solution
    def EasierSol(self, nums: List[int], k: int) -> bool:
        hashmap_ = {}
        for i, num_ in enumerate(nums):
            if num_ in hashmap_:
                if i - hashmap_[num_] <= k:
                    return True
            hashmap_[num_] = i
        return False


# %%
len(set([1, 2]))

# %%
len()
