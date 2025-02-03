class Solution(object):
    def isToeplitzMatrix(self, matrix):
        for r, col in enumerate(matrix):
            for c, val in enumerate(col):
                if r != 0 and c !=0 and matrix[r-1][c-1] != val:
                    return False
        return True