# https://leetcode.com/problems/course-schedule/description/
# 207. Course Schedule

class Solution:
    from collections import defaultdict
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # construct graph
        graph = defaultdict(list)
        for prereq in prerequisites:
            graph[prereq[1]].append(prereq[0])
        print(graph)
        
        visited = [False] * numCourses
        inStack = [False] * numCourses
        stack = []

        for node in list(graph):
            # print(node)
            if not visited[node]:
                stack.append(node)
                if not self.dfs(graph, node, inStack, visited, stack): return False
        # print(visited)
        print("".join(stack[::-1]))
        return True

    # dfs on each node,
    def dfs(self, graph, node, inStack, visited, stack):

        visited[node] = True
        inStack[node] = True

        for child in graph[node]:
            if not visited[child]:
                if not self.dfs(graph, child, inStack, visited, stack): return False
            else:
                if inStack[child]: return False

        inStack[node] = False
        stack.append(node)
        # stack.pop(node)

        return True
             

           
