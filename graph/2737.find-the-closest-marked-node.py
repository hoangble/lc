from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:
    def minimumDistance(self, n: int, edges: List[List[int]], s: int, marked: List[int]) -> int:
        graph = defaultdict(list)
        for start, end, weight in edges:
            graph[start].append((weight, end))

        heap_q = [(0, s)]
        visited = set()
        marked = set(marked)

        while heap_q:
            curr_weight, node = heappop(heap_q)

            if node in marked:
                return curr_weight

            if node in visited:
                continue
            visited.add(node)

            for weight, nei in graph[node]:
                heappush(heap_q, (curr_weight + weight, nei))
        return -1


n = 2
edges = [
    [0, 1, 3],
    [0, 1, 3],
    [0, 1, 7],
    [1, 0, 4],
    [0, 1, 2],
    [1, 0, 1],
    [1, 0, 8],
    [1, 0, 4],
    [1, 0, 10],
    [1, 0, 10],
    [1, 0, 9],
]
s = 0
marked = [1]
Solution().minimumDistance(n, edges, s, marked)
