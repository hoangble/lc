class Solution:
    from collections import defaultdict
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        if not any(hasApple): return 0

        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[-1])
            graph[edge[-1]].append(edge[0])
        
        visited = set()
        visited.add(0) 
        valid_node = set()

        self.dfs(0, graph, visited, hasApple, valid_node, False)
        # print(valid_node)
        return (len(valid_node) - 1) *2

    def dfs(self, node, graph, visited, has_apple, valid_node, branch_has_apple) -> bool:
        # print(node, valid_node)
        all_children = graph[node]
      
        for child in all_children:
            if child not in visited:
                visited.add(child)
                if self.dfs(child, graph, visited, has_apple, valid_node, False) or has_apple[child]: 
                    branch_has_apple = True

        if has_apple[node] or branch_has_apple: 
            valid_node.add(node)
            return True 

        return False
