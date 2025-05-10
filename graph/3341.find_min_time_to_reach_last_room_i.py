from heapq import heappop, heappush
from typing import List


def minTimeToReach(moveTime: List[List[int]]) -> int:
    # bfs - djistra
    m = len(moveTime)
    n = len(moveTime[0])
    dirs = [(0, 1), (1, 0), (0, -1), (0, 1)]

    pq = []
    heappush(pq, (0, (0, 0)))  # (total cost, (x, y))
    visited = set()
    visited.add((0, 0))
    while pq:
        cost, (x, y) = heappop(pq)

        if x == m - 1 and y == n - 1:
            return cost

        for d in dirs:
            new_x = x + d[0]
            new_y = y + d[1]

            if 0 <= new_x < m and 0 <= new_y < n and (new_x, new_y) not in visited:
                visited.add((new_x, new_y))
                new_time = max(cost, moveTime[new_x][new_y]) + 1
                heappush(pq, (new_time, (new_x, new_y)))
    return -1


moveTime = [[94, 79, 62, 27, 69, 84], [6, 32, 11, 82, 42, 30]]
minTimeToReach(moveTime)
