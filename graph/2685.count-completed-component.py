from collections import defaultdict
from typing import List


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # dfs, find circle
        graph = defaultdict(list)
        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)
        
        ans = 0
        seen = set()
        for i in range(n):
            if i not in graph:
                ans += 1
                seen.add(i)
        
        in_stack = [False] * n
        
        for i in range(n):
            if i not in seen:
                seen.add(i)
                if self.dfs(i, in_stack, seen, graph, i):
                    ans += 1
            
        return ans

    def dfs(self, node, stack, seen, graph, parent):
        # if stack[node]:
        #     return True

        stack[node] = True
        
        for nei in graph[node]:
            if nei not in seen:
                seen.add(nei)
                if self.dfs(nei, stack, seen, graph, node):
                    return True
            elif parent != nei:
                    return True 

        stack[node] = False


Solution().countCompleteComponents(n=6, edges=[[0, 1], [0, 2], [1, 2], [3, 4], [3, 5]])
