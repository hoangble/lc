from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        answer_list = []
        for row in range(numRows):
            this_row = []
            for col in range(row+1):
                if col == 0 or col == row:
                    this_row.append(1)
                else:
                    sum_from_above = answer_list[row-1][col-1] + answer_list[row-1][col] 
                    this_row.append(sum_from_above)
            answer_list.append(this_row)
        return answer_list
                    