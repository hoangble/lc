class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        a = [None] * len(nums)
        a[0] = nums[0]
        a[1] = max(nums[1], a[0])

        for i in range(2, len(nums)):
            a[i] = max(a[i - 2] + nums[i], a[i - 1])

        return a[-1]
