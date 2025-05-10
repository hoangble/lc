from heapq import heappop, heappush
from typing import List


class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(grid), len(grid[0])
        sorted_queries = sorted([(x, i) for i, x in enumerate(queries)])
        print(sorted_queries)

        pq = []
        heappush(pq, (grid[0][0], (0, 0)))

        total_cnt = 0
        ans = [0] * len(queries)
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        visited = set()
        visited.add((0, 0))
        for query, idx in sorted_queries:
            while len(pq) > 0 and pq[0][0] < query:
                val, coord = heappop(pq)
                print(val)
                x, y = coord
                total_cnt += 1

                for d in dirs:
                    new_x = x + d[0]
                    new_y = y + d[1]

                    if 0 <= new_x < m and 0 <= new_y < n and (new_x, new_y) not in visited:
                        heappush(pq, (grid[new_x][new_y], (new_x, new_y)))
                        visited.add((new_x, new_y))

            ans[idx] = total_cnt
        return ans


sol = Solution()
grid = [[1, 2, 3], [2, 5, 7], [3, 5, 1]]
queries = [5, 6, 2]
sol.maxPoints(grid, queries)
