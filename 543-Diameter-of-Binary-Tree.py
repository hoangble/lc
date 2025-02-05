# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dia = 0
        self.dfs(root)
        return self.dia 
    
    def dfs(self, node) ->int:
        if not node:
            return 0
        
        left_dia = self.dfs(node.left)
        right_dia = self.dfs(node.right)
        self.dia = max(self.dia, left_dia + right_dia)
        return max(left_dia, right_dia) + 1
