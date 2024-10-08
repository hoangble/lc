# 773. Sliding Window
# https://leetcode.com/problems/sliding-puzzle/description/
from typing import List
from collections import deque


class Solution:
    def __init__(self):
        self.swap_map = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4],
        }

    def slidingPuzzle(self, board: List[List[int]]) -> int:
        board_state = self.convert_board_state(board)
        visited = {board_state}

        q = deque()
        q.append([board_state, 0])

        while q:
            curr_board, n_step = q.popleft()
            if curr_board == "123450":
                return n_step
            for neighbor in self.get_neighbors(curr_board):
                if neighbor not in visited:  # O(1): set is o(1)???
                    visited.add(neighbor)
                    q.append([neighbor, n_step + 1])

        return -1

    def convert_board_state(self, board: List[List[int]]) -> str:
        state_ = ""
        for row in board:
            for col in row:
                state_ += str(col)
        return state_

    def get_neighbors(self, board_state: str) -> List[str]:
        idx_zero = board_state.find("0")
        neighbors = []
        for swap_idx in self.swap_map[idx_zero]:
            neighbor_state = [*board_state]

            tmp = neighbor_state[swap_idx]
            neighbor_state[swap_idx] = neighbor_state[idx_zero]
            neighbor_state[idx_zero] = tmp

            neighbors.append("".join(neighbor_state))

        return neighbors


### steps to do:
# 1. convert table to state (str/int) -> def()
# 2. bfs traverse:
# 2.1 check if visited. If not, add to queue
# 2.3 pop from queue -> recurse on popped node and +1 n_steps -> def bfs(visited, curr_board) -> bool
# 3 stopping condition: check if meet desire state or queue is empty -> check if two states are equal
