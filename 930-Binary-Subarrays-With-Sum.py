class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        l = r = 0
        cnt = 0
        total = 0
        prefix_zero = 0
        for r, i in enumerate(nums):
            total += nums[r]

            while l < r and (nums[l] == 0 or total > goal):
                if nums[l] == 0:
                    prefix_zero += 1
                else:
                    prefix_zero = 0
                
                total -= nums[l]
                l += 1
            
            if total == goal:
                cnt += 1 + prefix_zero
        return cnt