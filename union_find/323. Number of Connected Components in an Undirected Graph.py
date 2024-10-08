# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/description/
class Solution:
    # from collections import defaultdict
    # def countComponents(self, n: int, edges: List[List[int]]) -> int:
    #     graph = defaultdict(list)
    #     for edge in edges:
    #         graph[edge[0]].append(edge[-1])
    #         graph[edge[-1]].append(edge[0])

    #     for i in range(n):
    #         graph[i]

    #     visited = set()
    #     cnt = 0
    #     for node in list(graph.keys()):
    #         if not node in visited:
    #             visited.add(node)
    #             cnt += 1
    #             self.traverse(node, graph, visited)
    #     return cnt

    # def traverse(self, node, graph, visited):
    #     for child in graph[node]:
    #         if not child in visited:
    #             visited.add(child)
    #             self.traverse(child, graph, visited)

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        self.parent = [i for i in range(n)]
        self.rank = [1 for i in range(n)]

        ans = n
        for edge in edges:
            print(edge)
            if self.union(edge[0], edge[1]):
                ans -= 1
        return ans

    def find(self, node) -> int:
        if node == self.parent[node]:
            return self.parent[node]
        # while node != self.parent[node]:
        self.parent[node] = self.find(self.parent[node])
        # node = self.parent[node]
        return self.parent[node]

    def union(self, x, y) -> bool:
        parent_x = self.find(x)
        parent_y = self.find(y)

        if parent_x != parent_y:
            if self.rank[parent_x] <= self.rank[parent_y]:
                self.parent[parent_x] = parent_y
                self.rank[parent_y] += self.rank[parent_x]
            else:
                self.parent[parent_y] = parent_x
                self.rank[parent_x] += self.rank[parent_y]
            return True
        return False
