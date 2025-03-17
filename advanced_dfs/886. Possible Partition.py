from typing import List


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = dict()

        for i in range(1, n + 1):
            graph[i] = []

        for i, j in dislikes:
            graph[i].append(j)
            graph[j].append(i)

        print(graph)

        colors = [0] * n
        # bfs with each level is a different color
        for i in range(1, n + 1):
            if colors[i - 1] == 0:
                if not self.bfs(i, graph, colors):
                    return False

        return True

    def bfs(self, node, graph, colors):
        curr = [node]
        last_color = 1

        while curr:
            next_ = []
            node = curr.pop()
            colors[node - 1] = last_color
            for nei in graph[node]:
                if colors[nei - 1] == last_color:
                    print(colors, nei)
                    return False

                if colors[nei - 1] == 0:
                    next_.append(nei)

            curr = next_
            last_color = last_color * -1
        print(colors)
        return True


Solution().possibleBipartition(4, [[1, 2], [1, 3], [2, 4]])
