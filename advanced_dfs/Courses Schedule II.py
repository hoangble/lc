from typing import List


class Solution:
    from collections import defaultdict

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites:
            return range(numCourses)
        graph = defaultdict(list)

        for prereq in prerequisites:
            graph[prereq[-1]].append(prereq[0])

        for i in range(numCourses):
            if i not in graph:
                graph[i]

        visited = [False] * numCourses
        in_stack = [False] * numCourses
        stack = []
        for node in list(graph):
            if not visited[node]:
                if not self.dfs(node, graph, visited, in_stack, stack):
                    return []
                stack.append(node)

        return reversed(stack)

    def dfs(self, node, graph, visited, in_stack, stack) -> bool:
        visited[node] = True
        in_stack[node] = True

        for child in graph[node]:
            if not visited[child]:
                if not self.dfs(child, graph, visited, in_stack, stack):
                    return False
                stack.append(child)
            else:
                if in_stack[child]:
                    return False

        in_stack[node] = False
        return True
