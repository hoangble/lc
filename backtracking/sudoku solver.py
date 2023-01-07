from typing import List
from collections import defaultdict


class Solution:
    from collections import defaultdict
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        col_hash_map = defaultdict(set)
        row_hash_map = defaultdict(set)
        box_hash_map = defaultdict(set)

        for row in range(9):
            for col in range(9):
                if board[row][col] != ".":
                    num_ = board[row][col]
                    row_hash_map[row].add(int(num_))# = row_hash_map[row] | (1 << int(num_))
                    col_hash_map[col].add(int(num_))
                    box_index = (row // 3) * 3 + col // 3
                    box_hash_map[box_index].add(int(num_))
        # print(row_hash_map,1 col_hash_map, box_hash_map)
        self.backtrack(0, 0, board, row_hash_map, col_hash_map, box_hash_map)

    def backtrack(self, i, j, board, row_hash_map, col_hash_map, box_hash_map): 
        if j == 9:
            i += 1
            j = 0

        if i == 9: return True

        if board[i][j] != ".":
            # print(i, j, row_hash_map)

            if self.backtrack(i, j + 1, board, row_hash_map, col_hash_map, box_hash_map): return True
            return False

        box_index = (i // 3) * 3 + j // 3
        for x in range(1, 10):
            if not x in row_hash_map[i] and not x in col_hash_map[j] and not x in box_hash_map[box_index]:
                row_hash_map[i].add(x)
                col_hash_map[j].add(x)
                box_hash_map[box_index].add(x)
                board[i][j] = str(x)
                if self.backtrack(i, j + 1, board, row_hash_map, col_hash_map, box_hash_map): return True
                board[i][j] = "."
                row_hash_map[i].remove(x)
                col_hash_map[j].remove(x)
                box_hash_map[box_index].remove(x)


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

sol = Solution()
sol.solveSudoku(board)
