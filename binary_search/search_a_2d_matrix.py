# 74. Search a 2D Matrix 
# https://leetcode.com/problems/search-a-2d-matrix/ 

from typing import List 

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n_rows = len(matrix)
        n_cols = len(matrix[0])
        
        left = 0
        right = (n_rows*n_cols)-1
        
        while left < right - 1:
            mid = (left + right) // 2
            row_idx = mid // n_cols
            col_idx = mid % n_cols
            
            if target < matrix[row_idx][col_idx]:
                right = mid - 1
            else:
                left = mid
        return target == matrix[left//n_cols][left%n_cols] or target==matrix[right//n_cols][right%n_cols]