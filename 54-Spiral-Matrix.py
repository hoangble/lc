class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])

        up = left = 0
        down = m - 1
        right = n - 1
        ans = []
        while len(ans) < m *n:
            for col in range(left, right + 1):
                ans.append(matrix[up][col])
            
            for row in range(up + 1, down + 1):
                ans.append(matrix[row][right])
            
            if up != down:
                for col in range(right - 1, left - 1, -1):
                    ans.append(matrix[down][col])
                
            if left != right:
                for row in range(down - 1, up, -1):
                    ans.append(matrix[row][left])
            
            left += 1
            right -= 1
            up += 1
            down -= 1
        return ans
            


        