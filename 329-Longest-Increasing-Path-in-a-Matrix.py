class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        indegree = [[0] * n for _ in range(m)]
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for i in range(m):
            for j in range(n):
                for dx, dy in dirs:
                    nx = i + dx
                    ny = j + dy
                    if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] < matrix[i][j]:
                        indegree[i][j] += 1

        dq = deque()
        for x in range(m):
            for y in range(n):
                if indegree[x][y] == 0:
                    dq.append((x, y))
        
        ans = 0
        while dq:
            for _ in range(len(dq)):
                x, y = dq.popleft() 
                for dx, dy in dirs:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] > matrix[x][y]:
                        indegree[nx][ny] -= 1
                        if indegree[nx][ny] == 0:
                            dq.append((nx, ny))
            
            ans += 1
        return ans