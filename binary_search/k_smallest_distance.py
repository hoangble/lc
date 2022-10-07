# https://leetcode.com/problems/find-k-th-smallest-pair-distance/
# 719. Find K-th Smallest Pair Distance
# https://leetcode.com/problems/find-k-th-smallest-pair-distance/discuss/769705/Python-Clear-explanation-Powerful-Ultimate-Binary-Search-Template.-Solved-many-problems.
from typing import List


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        """
        1. define search space
        2. define condition to remove half of search space
        """
        nums.sort()  # O(n log n)

        def isPossible(answer):
            """
            return True if there are at least k distances <= answer
            """
            count, left_ptr, right_ptr = 0, 0, 0
            while left_ptr < len(nums):
                while (right_ptr < len(nums)) and (
                    (nums[right_ptr] - nums[left_ptr]) <= answer):
                    right_ptr += 1
                count += right_ptr - left_ptr - 1
                left_ptr += 1
            return count >= k

        left = 0
        right = nums[-1] - nums[0]

        while left < right:
            mid = (left + right) // 2
            if not isPossible(mid):
                left = mid + 1
            else:
                right = mid
        return left if isPossible(left) else right


#%%

s = "aaabb"
from collections import Counter
Counter(s)