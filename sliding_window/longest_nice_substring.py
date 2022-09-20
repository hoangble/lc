# https://leetcode.com/problems/longest-nice-substring/ 
# 1763. Longest Nice Substring

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) < 1: return ""
        else:
            all_chars = set(s)
            for i, c in enumerate(s):
                if c.swapcase() not in all_chars:
                    s1 = self.longestNiceSubstring(s[:i])
                    s2 = self.longestNiceSubstring(s[i+1:])

                    return max(s1, s2, key = len) 
            return s
            