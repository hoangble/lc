from collections import defaultdict


class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0

        freq = defaultdict(int)
        ans = 0
        l = 0
        r = 0
        n = len(s)

        while r < n:
            freq[s[r]] += 1

            while freq[s[r]] > 1:
                freq[s[l]] -= 1
                l += 1

            if r - l + 1 >= k:
                ans += 1

            r += 1
        return ans


Solution().numKLenSubstrNoRepeats("havefunonleetcode", 5)
