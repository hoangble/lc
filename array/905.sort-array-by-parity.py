from typing import List 
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # odds = []
        # evens = []

        # for i, n_ in enumerate(nums):
        #     if n_ % 2 == 0:
        #         evens.append(i)
        #     else:
        #         odds.append(i)
        
        # ans = []

        # for i in evens:
        #     ans.append(nums[i])
        
        # for i in odds:
        #     ans.append(nums[i])
        # return ans

        # one pass
        i, j = 0, len(nums) - 1
        while i < j:
            if nums[i] % 2 > nums[j] % 2:
                nums[i], nums[j] = nums[j], nums[i] 
            
            if nums[i] % 2 == 0: i += 1
            if nums[j] % 2 != 0: j -= 1
        return nums
        


        