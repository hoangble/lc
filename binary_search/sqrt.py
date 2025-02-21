# class Solution:
#     def mySqrt(self, x: int) -> int:
#         left = 0
#         right = x

#         while left < right - 1:
#             mid = (left + right) // 2
#             if mid * mid > x:
#                 right = mid - 1
#             else:
#                 left = mid

#         return right if right * right <= x else left


class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x // 2
        while l <= r:
            m = (l + r) // 2
            e = m * m
            if e == x:
                return m

            if e < x:
                l = m + 1
            else:
                r = m - 1
        return l
