# 2457. Minimum Addition to Make Integer Beautiful 
# https://leetcode.com/problems/minimum-addition-to-make-integer-beautiful/

class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        arr = []
        original_n = n
        i = 10
        while not self.beautiful(n, target):
            n += i - n % i

            i *= 10
        return n - original_n
            
            
        
    
    def beautiful(self, num, target):
        sum_ = 0;
        while (num > 0):
            sum_ = sum_ + num % 10;
            num = num // 10;
        
        return sum_ <= target
        