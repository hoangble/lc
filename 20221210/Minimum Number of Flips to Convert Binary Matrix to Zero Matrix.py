# https://leetcode.com/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/

from typing import List
from collections import deque
from copy import deepcopy


class Solution:
    from collections import deque
    from copy import deepcopy
    
    def minFlips(self, mat: List[List[int]]) -> int:
        self.directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        m, n = len(mat), len(mat[0])
        goal = "".join(["0"]*m*n)
        board_str = self.convert_board_to_string(mat)
        
        queue = deque()
        queue.append((board_str, 0))
        visited = set()
        visited.add(board_str)

        while queue:
            print(queue)
            board, n_step = queue.popleft()
            if board == goal: return n_step
            mat = self.convert_str_to_board(board, m, n)

            for row in range(m):
                for col in range(n):
                    flipped_mat = deepcopy(mat)

                    flipped_mat = self.flip(flipped_mat, [row, col])
                    new_board = self.convert_board_to_string(flipped_mat)

                    if new_board not in visited:
                        visited.add(new_board) 
                        queue.append((new_board, n_step + 1))
        return -1


    def convert_board_to_string(self, mat):
        str_ = ""
        for row in mat:
            for col in row:
                str_ += str(col)
        return str_
    
    def convert_str_to_board(self, str_, m, n): # you're just being lazy at this point
        mat = []
        cnt = 0
        for row in range(m):
            each_row = []
            for col in range(n):
                each_row.append(int(str_[cnt]))
                cnt += 1
            mat.append(each_row)
        return mat

    
    def flip(self, flipped_mat, position):
        for direction in self.directions:
            new_x = position[0] + direction[0]
            new_y = position[1] + direction[1]
            if 0 <= new_x < len(flipped_mat) and 0 <= new_y < len(flipped_mat[0]):
                if flipped_mat[new_x][new_y] == 0: flipped_mat[new_x][new_y] = 1
                else: flipped_mat[new_x][new_y] = 0
            
        if flipped_mat[position[0]][position[1]] == 0:
            flipped_mat[position[0]][position[1]] = 1
        else:
            flipped_mat[position[0]][position[1]] = 0
        return flipped_mat




if __name__ == "__main__":
    sol = Solution()
    mat = [[0, 0], [0, 1]]
    sol.minFlips(mat)

#%%
(1<<3)