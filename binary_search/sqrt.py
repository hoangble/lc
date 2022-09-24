class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        
        while left < right - 1:
            mid = (left + right) // 2
            if mid * mid > x:
                right = mid - 1
            else:
                left = mid
            
        return right if right*right <= x else left