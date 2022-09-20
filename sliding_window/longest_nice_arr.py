
from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # always increment the right count
        # only increment left when there more odd number than k
        # when odd == k, increment the left to see if the # of odd is still the same
        ans = 0
        odd_cnt = 0
        left, right = 0, 0
        while right < len(nums):
            if nums[right] %2 == 1:
                odd_cnt += 1
            
            while odd_cnt > k:# and left < right:
                if nums[left] % 2 == 1:
                    odd_cnt -= 1
                left += 1
                
            if odd_cnt == k:
                ans += 1
                temp_left = left
                while nums[temp_left] % 2 == 0: # keep checking to see if we
                    temp_left += 1
                    ans += 1

            right += 1
        
        return ans
    
class PrefixSumSolution():
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # always increment the right count
        # only increment left when there more odd number than k
        # when odd == k, increment the left to see if the # of odd is still the same
        for i in range(len(nums)):
            nums[i] = int(not(nums[i]%2==0))
        # convert the porblem to the problem of counting # of window with sum = k
        # can do it with prefix sum
        sum_dict = {0: 1}
        sum_ = 0
        cnt = 0
        for i, n_ in enumerate(nums):
            sum_ += n_
            
            if sum_-k in sum_dict:
                cnt += sum_dict[sum_ - k]
                
            if sum_ not in sum_dict:
                sum_dict[sum_]  = 0
            
            sum_dict[sum_] += 1
        return cnt