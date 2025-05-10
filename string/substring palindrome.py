class Solution:
    def countSubstrings(self, s: str) -> int:
        # always make sure that n is odd
        t = ["#"]
        for c in s:
            t.append(c)
            t.append("#")
        n = len(t)
        dp = [0] * n
        m = r = ans = 0
        for i in range(n):
            mirror = 2 * m - i
            if i < r:
                dp[i] = min(r - i, dp[mirror])
            
            # expand the palindrome centered at i
            a = i + (1 + dp[i])
            b = i - (1 + dp[i])

            while a < n and b >= 0 and t[a] == t[b]:
                dp[i] += 1
                a += 1
                b -= 1

            # if palindrome centered at i expands past right, adjust center and right boundary
            if i + dp[i] > r:
                m = i
                r = i + dp[i]
            ans += (dp[i] + 1) // 2
        return ans


sol = Solution()
s = "abaxaba"
sol.countSubstrings(s)
