from collections import defaultdict
from typing import List


class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]]) -> int:
        graph = defaultdict(list)
        for r in relations:
            graph[r[0]].append(r[1])

        for i in range(1, n + 1):
            graph[i]

        visited = {}
        parents = [False] * n
        self.max_length = -1
        for node in range(1, n + 1):
            if node not in visited:
                length = self.dfs(graph, node, visited, parents)
                if length == -1:
                    return -1
                self.max_length = max(self.max_length, length)
        return self.max_length

    def dfs(self, graph, node, visited, parents):
        if parents[node - 1]:
            return -1

        if node in visited:
            return visited[node]

        max_length = 1
        parents[node - 1] = True
        for nei in graph[node]:
            length = self.dfs(graph, nei, visited, parents)
            if length == -1:
                return -1
            max_length = max(length + 1, self.max_length)
        visited[node] = max_length

        parents[node - 1] = False
        return visited[node]


n = 3
relations = [[1, 3], [2, 3]]
print(Solution().minNumberOfSemesters(n, relations))
