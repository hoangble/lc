# https://leetcode.com/problems/k-radius-subarray-averages/submissions/
# 2090. K Radius Subarray Averages

from typing import List 
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        # if k > len(nums):
        #     return [-1]
        # else:
        ans = []
        sum_ = 0
        prefix_sum = [0]

        for i in range(len(nums)):
            sum_ += nums[i]
            prefix_sum.append(sum_)

        for i in range(len(nums)):
            if i < k or i+k >= len(nums) :
                ans.append(-1)
            else:
                avg = (prefix_sum[i+k+1] - prefix_sum[i-k])//(2*k+1)
                ans.append(avg)
        return ans
        

class SlidingWindowSolution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        left = 0
        right = 0
        sum_ = 0
        ans = [-1]*len(nums)
        radius = 2*k + 1
        
        while right < len(nums):
            sum_ += nums[right]
            
            if right - left + 1 >= radius:
                avg = sum_//radius
                
                ans[left+k] = avg
                
                sum_ -= nums[left]
                
                left += 1
                
            right += 1
        return ans
            