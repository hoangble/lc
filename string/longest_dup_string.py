from collections import defaultdict


class Solution:
    def longestDupSubstring(self, s: str) -> str:
        MOD = 10**9 + 7

        a = 26
        n = len(s)

        nums = [ord(s[i]) - ord("a") for i in range(n)]

        start = -1

        left, right = 0, n - 1
        while left <= right:
            m = (left + right) // 2
            start_of_duplicate = self.rabin_karp(m, a, MOD, n, nums)
            if start_of_duplicate != -1:
                left = m + 1
                start = start_of_duplicate
            else:
                right = m - 1
        return s[start : start + left - 1]

    def rabin_karp(self, length, a, mod, n, nums):
        # compute the has of the substring s[:L]
        h = 0
        for i in range(length):
            h = (h * a + nums[i]) % mod

        seen = defaultdict(list)
        seen[h].append(0)

        aL = pow(a, length, mod)
        for start in range(1, n - length + 1):
            h = (h * a - nums[start - 1] * aL + nums[start + length - 1]) % mod
            if h in seen:
                curr_substr = nums[start : start + length]
                if any(curr_substr == nums[idx : idx + length] for idx in seen[h]):
                    return start
            seen[h].append(start)
        return -1


Solution().longestDupSubstring("banana")
