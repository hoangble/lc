# https://leetcode.com/problems/valid-perfect-square/
# 367. Valid Perfect Square
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 1
        right = num

        while left < right - 1:
            mid = (left + right) // 2
            if mid * mid > num:
                right = mid - 1
            else:
                left = mid

        return right * right == num or left * left == num
