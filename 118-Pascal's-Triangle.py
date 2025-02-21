class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        len_each_row = 0
        for row_idx in range(numRows):
            curr_row = [0] * (row_idx + 1)
            curr_row[0], curr_row[-1] = 1, 1
            for i in range(1, len(curr_row) - 1):
                curr_row[i] = ans[row_idx-1][i-1] +  ans[row_idx-1][i]
            ans.append(curr_row)
        
        return ans
        
        