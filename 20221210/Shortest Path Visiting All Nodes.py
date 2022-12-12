# https://leetcode.com/problems/shortest-path-visiting-all-nodes/
# 847. Shortest Path Visiting All Nodes
from collections import deque
from typing import List


class Solution:
    from collections import deque

    def shortestPathLength(self, graph: List[List[int]]) -> int:
        all_mask = [2**i for i in range(len(graph))]
        all_path_len = []
        for start, starting_mask in enumerate(all_mask):
            all_path_len.append(self.bfs(start, starting_mask, graph))
        return min(all_path_len)

    def bfs(self, start, mask, graph) -> int:
        queue = deque()
        path_len = 0
        queue.append((start, mask, path_len))
        finish = (1 << len(graph)) - 1
        while mask != finish:
            curr_node, mask, path_len = queue.popleft()
            mask |= 1 << curr_node
            for neighbor in graph[curr_node]:
                queue.append((neighbor, mask, path_len + 1))
        return path_len


if __name__ == "__main__":
    sol = Solution()
    graph = [[1, 2, 3], [0], [0], [0]]
    print(sol.shortestPathLength(graph))
