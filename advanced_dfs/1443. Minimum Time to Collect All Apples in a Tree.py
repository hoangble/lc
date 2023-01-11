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
        valid_node, _ = self.dfs(0, graph, visited, hasApple, 1, False)
        return valid_node

    def dfs(self, node, graph, visited, has_apple, valid_node, branch_has_apple) -> (int, bool):
        all_children = graph[node]
        if len(all_children) == 0:
            return 0, False

        for child in all_children:
            curr_valid_node, has_apple = self.dfs(child, graph, visited, has_apple, valid_node, branch_has_apple)
            if has_apple: branch_has_apple = True
            valid_node += curr_valid_node

        if branch_has_apple:  
            valid_node += 2

        return valid_node, branch_has_apple
