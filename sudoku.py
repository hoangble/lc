from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col_dict = {}
        row_dict = {}
        square_dict = {}
        for i in range(9):
            col_dict[i] = []
            row_dict[i] = []
            square_dict[i] = []

        for row in range(len(board)):
            for col in range(len(board[0])):
                print(row, col)
                # if board[row][col] != ".":
                #     num_ = board[row][col]
                #     if num_ not in col_dict[col]:
                #         col_dict[col].append(num_)
                #     else:
                #         return False

                #     if num_ not in row_dict[row]:
                #         row_dict[row].append(num_)
                #     else:
                #         return False

                square_key = 3 * (row // 3) + col // 3
                print(square_key)
                    # if num_ not in square_dict[square_key]:
                    #     square_dict[square_key].append(num_)
                    # else:
                    #     return False
        return True


if __name__ == "__main__":
    sol = Solution()
    input_ = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
              ["6", ".", ".", "1", "9", "5", ".", ".", "."],
              [".", "9", "8", ".", ".", ".", ".", "6", "."],
              ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
              ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
              ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
              [".", "6", ".", ".", ".", ".", "2", "8", "."],
              [".", ".", ".", "4", "1", "9", ".", ".", "5"],
              [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    print(len(input_))
    print(len(input_[0]))

    sol.isValidSudoku(input_)
#%%
3*(1//3)+1//3
#%%
