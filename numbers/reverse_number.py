# 7. Reverse Integer
# https://leetcode.com/problems/reverse-integer/
class Solution:
    def reverse(self, x: int) -> int:
        sign = [1, -1][x < 0]
        rev, x = 0, abs(x)
        while x:
            x, mod = divmod(x, 10)
            rev = rev*10+mod
        if sign*rev < pow(-2, 31) or sign*rev > pow(2, 31)-1:
            return 0
        return sign*rev