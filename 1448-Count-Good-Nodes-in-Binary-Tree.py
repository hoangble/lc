# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.cnt = 0
        max_val = root.val
        self.dfs(root, max_val)
        return self.cnt 

    def dfs(self, node, max_val) -> None:
        if not node:
            return
        
        if node.val >= max_val:
            self.cnt += 1
        
        max_val = max(max_val, node.val)
        self.dfs(node.left, max_val)
        self.dfs(node.right, max_val)
