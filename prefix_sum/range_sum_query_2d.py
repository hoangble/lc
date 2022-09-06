from typing import List
# 304. Range Sum Query 2D - Immutable
# https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix    
        self.prefix_sum = {} # or save it in a matrix, either way
        m = len(self.matrix)
        n = len(self.matrix[0])
        # create a prefix sum hashmap
        for i in range(m):
            prefix_sum_row = 0

            if i not in self.prefix_sum:
                self.prefix_sum[i] = {}
            for j in range(n):
                # prefix_sum += self.matrix[i][j]   
                # self.prefix_sum[i][j] = prefix_sum
                prefix_sum_row += self.matrix[i][j]
                if i == 0 and j == 0:
                    # prefix_sum  = 
                    self.prefix_sum[i][j] = self.matrix[0][0]    
                else: #if i != 0 or j != 0:
                    if i == 0:
                        self.prefix_sum[i][j] = self.prefix_sum[0][j-1] + self.matrix[i][j]   
                    elif j == 0:
                        self.prefix_sum[i][j] = self.prefix_sum[i-1][0] + self.matrix[i][j]   
                    else:
                        self.prefix_sum[i][j] = self.prefix_sum[i-1][j] + prefix_sum_row                                                                                       
        print("done")                       
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # big_sum - the row - the col + the overlapping
        if row1 == 0 or col1 == 0 or row2 == 0 or col2 == 0:
            big_sum = self.prefix_sum[row2][col2]
            row_sum = 0
            col_sum = 0
            overlapping = 0
            
            if col1 != 0:
                col1_minus = int(col1 > 0)
                col_sum = self.prefix_sum[row2][col1-col1_minus]
                # overlapping = 


            elif row1 != 0:
                row1_minus = int(row1 > 0)

                row_sum = self.prefix_sum[row1-row1_minus][col2]

            # return big_sum 
        elif col1 == col2 and row1 == row2:
            return self.matrix[row1][col1]
        else:
            row1_minus = int(row1 > 0)
            row2_minus = int(row2 > 0)
            col1_minus = int(col1 > 0)
            col2_minus = int(col2 > 0)

            big_sum = self.prefix_sum[row2][col2]
            row_sum = self.prefix_sum[row1-row1_minus][col2]
            col_sum = self.prefix_sum[row2][col1-col1_minus]
            overlapping = self.prefix_sum[row1-row1_minus][col1-col1_minus]
        return big_sum - row_sum - col_sum + overlapping


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

# if __name__ == "__main__":
#     mat = [[8,-4,5],[-1,4,4],[-2,3,1],[-4,4,3]]
#     # mat = [[[[8,-4,5],[-1,4,4],[-2,3,1],[-4,4,3]]],[0,1,0,2],[1,1,1,2],[0,1,0,2]]
#     sol = NumMatrix(mat)
#     # [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]
#     sol.sumRegion(0,1,0,2)
#     sol.sumRegion(1,1,1,2)
#     sol.sumRegion(1, 2, 2, 4)
