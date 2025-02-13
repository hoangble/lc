class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]

        curr_ = nums[0]
        ans = nums[0]
        for n in nums[1:]:
            curr_ = max(n, curr_+n)
            ans = max(ans, curr_)
        return ans
        