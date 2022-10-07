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
        nums.sort() 
        
        left = 0
        right =  nums[-1] - nums[0]
        
        while left < right - 1:
            mid = (left + right) //2
            if not self.isPossible(mid, nums):
                left = mid + 1
            else:
                right = mid
        return left if self.isPossible(left, nums) else right
            
        
    def isPossible(self, answer, nums):
        """
        return True if there are at least k distances <= answer
        """        

#%%

s = "aaabb"
from collections import Counter
Counter(s)