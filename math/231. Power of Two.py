# https://leetcode.com/problems/power-of-two/description/


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # if n <= 0: return False
        # while abs(n) > 1:
        #     if n % 2 != 0: return False
        #     n = n // 2
        # return True
        if n == 0:
            return False
        return n & (n - 1) == 0
