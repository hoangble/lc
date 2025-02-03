class Solution:
    def makePalindrome(self, s: str) -> bool:
        diff = 0
        n = len(s)
        i = 0
        for i in range(n // 2):
            if s[i] != s[n - i - 1] and diff < 3:
                diff += 1
            if diff >= 3:
                return False
        # 0 change === 2 changes
        return True


sol = Solution()
print(sol.makePalindrome("zbcfedcba"))
