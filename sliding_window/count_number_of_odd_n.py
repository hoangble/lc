# https://leetcode.com/problems/count-number-of-nice-subarrays/
# 1248. Count Number of Nice Subarrays
from typing import List

class PrefixSumSolution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        """
        always increment the right pointer
        only increment the left pointer when there are more odd numbers than k
        """

        # convert even number to 0, odd by 1 -> find number of ones that sum to k
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1
                
        prefix_sum = 0
        hash_map = {0: 1}
        cnt = 0
        
        for i in range(len(nums)):
            prefix_sum += nums[i]
            
            if prefix_sum - k in hash_map:
                cnt += hash_map[prefix_sum - k]
            
            if prefix_sum not in hash_map:
                hash_map[prefix_sum] = 1
            else:
                hash_map[prefix_sum] += 1
        return cnt

class SlidingWindowSolution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        """
        always increment the right pointer
        only increment the left pointer when there are more odd numbers than k
        """
        ans = 0
        odd_cnt = 0
        left = 0
        right = 0
        
        while right < len(nums):
            # add the right cnt
            if nums[right] % 2 == 1:
                odd_cnt += 1
           
            while odd_cnt > k:
                if nums[left] % 2 == 1:
                    odd_cnt -= 1
                left += 1
                
            # remove the left cnt            
            if odd_cnt == k:
                ans += 1
                # check if prefix of the current subarray only has even number
                # if so -> add to the amt
                temp_left = left
                while nums[temp_left] % 2 == 0:
                    temp_left += 1
                    ans += 1
            right += 1
        return ans        