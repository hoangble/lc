# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.left = None
# #         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # get parents, then dfs
        self.graph = defaultdict(list)
        self.build_graph(root)

        self.ans = []
        self.visited = set()

        self.dfs(target, 0, k)
        return self.ans

    
    def build_graph(self, node):
        if not node:
            return None

        if node.left:
            self.graph[node.left].append(node)
            self.graph[node].append(node.left)
            self.build_graph(node.left)

        if node.right:
            self.graph[node.right].append(node)
            self.graph[node].append(node.right)
            self.build_graph(node.right) 

    def dfs(self, node, dist, k):
        self.visited.add(node)

        if dist == k:
            self.ans.append(node.val)
            return
        
        for nei in self.graph[node]:
            if nei not in self.visited:
                self.dfs(nei, dist + 1, k)
        



        