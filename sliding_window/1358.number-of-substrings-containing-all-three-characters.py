class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)

        l = 0
        r = 0
        freq = {"a": 0, "b": 0, "c": 0}

        ans = 0
        for r in range(n):
            freq[s[r]] += 1
            while self.has_all_three(freq):
                freq[s[l]] -= 1
                l += 1
            ans += l
        return ans

    def has_all_three(self, freq):
        for k, v in freq.items():
            if v <= 0:
                return False
        return True


Solution().numberOfSubstrings("abcabc")
