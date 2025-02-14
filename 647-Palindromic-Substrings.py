class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            ans += self.check_palindrome(s, i, i)
            ans += self.check_palindrome(s, i, i + 1)
        return ans

    
    def check_palindrome(self, s, l, h) -> int:
        n = len(s)
        ans = 0
        while l >= 0 and h <= n - 1:
            if s[l] != s[h]:
                break
            ans += 1
            l -= 1
            h += 1
        return ans