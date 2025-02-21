class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = [nums[0]]
        for i in range(1, len(nums)):
            num = nums[i]
            
            if num > sub[-1]:
                sub.append(num)
            else:
                idx = self.binary_search(sub, num)
                if idx != len(sub):
                    sub[idx] = num
        return len(sub)
            
    def binary_search(self, nums, target) -> int:
        # find left bound
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2

            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            elif nums[m] == target:
                r = m - 1
        
        # post-processing
        return l

