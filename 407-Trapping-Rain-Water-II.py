class Solution:
    from heapq import heapify, heappush, heappop
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        m, n = len(heightMap), len(heightMap[0])

        visited = set()
        pq = []
        heapify(pq) 
        for i in range(m):
            heappush(pq, (heightMap[i][0], i, 0))
            visited.add((i, 0))

            heappush(pq, (heightMap[i][n-1], i, n-1))
            visited.add((i, n-1))

        for i in range(n):
            heappush(pq, (heightMap[0][i], 0, i))
            visited.add((0, i))
            heappush(pq, (heightMap[m-1][i], m-1, i))
            visited.add((m-1, i))
        
        min_bound_hei = -1
        ans = 0

        while pq:
            curr_height, x, y = heappop(pq)
            min_bound_hei = curr_height
            for d in dirs:
                new_x = x + d[0]
                new_y = y + d[1]
                if 0 <= new_x < m and 0 <= new_y < n and (new_x, new_y) not in visited:
                    if heightMap[new_x][new_y] < min_bound_hei:
                        ans += min_bound_hei - heightMap[new_x][new_y]
                    heappush(pq, (max(min_bound_hei, heightMap[new_x][new_y]), new_x, new_y))
                    visited.add((new_x, new_y))
        return ans
                