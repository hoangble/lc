from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # # bfs
        # graph = defaultdict(list)
        # indeg = [0] * numCourses
        # for i, j in prerequisites:
        #     graph[j].append(i)
        #     indeg[i] += 1

        # print(graph)
        # dq = deque([])

        # for i in range(numCourses):
        #     graph[i]
        #     if indeg[i] == 0:
        #         dq.append(i)

        # visited = set()
        # while dq:
        #     # print(dq)
        #     node = dq.popleft()

        #     if node not in visited:
        #         visited.add(node)

        #     for nei in graph[node]:
        #         indeg[nei] -= 1
        #         if indeg[nei] == 0:
        #             dq.append(nei)
        # # print(visited)

        # return len(visited) == numCourses

        # dfs
        graph = defaultdict(list)
        for i, j in prerequisites:
            graph[j].append(i)

        in_stack = [False] * numCourses
        seen = set()
        for i in range(numCourses):
            if i not in seen:
                if not self.dfs(i, in_stack, seen, graph):
                    return False
        return True

    def dfs(self, node, in_stack, seen, graph):
        print(node)
        if in_stack[node]:
            return False

        in_stack[node] = True
        seen.add(node)

        for nei in graph[node]:
            if node not in seen:
                if not self.dfs(nei, in_stack, seen, graph):
                    return False
            else:
                if in_stack[nei]:
                    return False

        in_stack[node] = False
        return True


Solution().canFinish(2, [[1, 0], [0, 1]])
