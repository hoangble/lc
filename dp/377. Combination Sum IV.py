class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        memo = [-1] * (target + 1)
        self.dp(memo, nums, target)
        return memo[-1]

    def dp(self, memo, nums, remain) -> int:
        if remain == 0: return 1

        if memo[remain] != -1 : return memo[remain]

        result = 0
        for num in nums:
            if remain-num >= 0:
                result += self.dp(memo, nums, remain - num)

        memo[remain] = result
        return memo[remain]
