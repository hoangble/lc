class Solution:
    from collections import defaultdict
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[-1])
            graph[edge[-1]].append(edge[0])
        
        for i in range(n):
            graph[i]
        
        visited = set()
        cnt = 0
        for node in list(graph.keys()):
            if not node in visited:
                visited.add(node)
                cnt += 1
                self.traverse(node, graph, visited)
        return cnt

    
    def traverse(self, node, graph, visited):
        for child in graph[node]:
            if not child in visited:
                visited.add(child)
                self.traverse(child, graph, visited)
