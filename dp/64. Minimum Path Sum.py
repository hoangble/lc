# https://leetcode.com/problems/minimum-path-sum/description/
# I approached this problem thinking it would be a simple djikstra problem but got TLE
# Then I checked the hint for the type of problem and it said DP
# I realized the dp embedded in the approach
class Solution:
  from heapq import heapify, heappush, heappop

  def minPathSum(self, g: List[List[int]]) -> int:
      # brute force
      # m, n = len(graph), len(graph[0])
      # self.dirs = [(0, 1), (1, 0)]
      # states = [(graph[0][0], 0, 0)]

      # while states:
      #     s, x, y = heappop(states)
      #     if x == m - 1 and y == n - 1:
      #         return s

      #     for d in self.dirs:
      #         new_x, new_y = x + d[0], y + d[1]
      #         if self.is_valid(new_x, new_y, m, n):
      #             heappush(states, (s + graph[new_x][new_y], new_x, new_y))
#       def is_valid(self, x, y, m , n):
#         return 0 <= x < m and 0 <= y < n
      # O(mn log mn)

      # at each cell do min (up and left, then return the bottom right corner)
      m, n = len(g), len(g[0])
      s = [[0 for _ in range(n)] for _ in range(m)]

      s[0][0] = g[0][0]
      for i in range(1, n): 
          s[0][i] = g[0][i] + s[0][i-1]
      for i in range(1, m): 
          s[i][0] = g[i][0] + s[i-1][0]

      # dp step
      for i in range(1, m):
          for j in range(1, n):
              s[i][j] = min(s[i-1][j], s[i][j-1]) + g[i][j] 
      return s[-1][-1]
      # O(mn)
