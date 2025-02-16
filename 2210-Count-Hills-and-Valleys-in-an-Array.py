class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        left = nums[0]
        cnt = 0
        for i in range(1, len(nums) - 1):
            if nums[i] > nums[i+1] and nums[i] > left or nums[i] < nums[i+1] and nums[i] < left:
                cnt += 1
                left = nums[i]
        return cnt
