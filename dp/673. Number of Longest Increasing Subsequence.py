class Solution:
    from collections import defaultdict

    def findNumberOfLIS(self, nums: List[int]) -> int:
        l = [1] * len(nums)
        c = [1] * len(nums)

        max_len = 0
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    if l[j] + 1 > l[i]:
                        l[i] = l[j] + 1
                        c[i] = 0

                    if l[j] + 1 == l[i]:
                        c[i] += c[j]

        max_len = max(l)

        ans = 0
        for i in range(len(nums)):
            if l[i] == max_len:
                ans += c[i]
        return ans
