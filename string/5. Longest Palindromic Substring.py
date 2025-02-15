class Solution:
    def longestPalindrome(self, s: str) -> str:
        t = ["#"]
        for c in s:
            t.append(c)
            t.append("#")

        n = len(t)
        dp = [0] * n
        m = r = max_len = max_idx = 0
        for i in range(n):
            mirror = 2 * m - i
            if i < r:
                dp[i] = min(r - i, dp[mirror])

            a = i + (1 + dp[i])
            b = i - (1 + dp[i])
            while a < n and b >= 0 and t[a] == t[b]:
                dp[i] += 1
                a += 1
                b -= 1

            if i + dp[i] > r:
                m = i
                r = i + dp[i]

            if dp[i] > max_len:
                max_len = dp[i]
                max_idx = i

        start_idx = (max_idx - max_len) // 2
        return s[start_idx : start_idx + max_len]


sol = Solution()
s = "babbad"
sol.longestPalindrome(s)
