# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.ans = float('inf')
        self.prev_val = None
        self.dfs(root)
        return self.ans

    def dfs(self, root):
        # inorder traversal
        if not root:
            return
        
        self.dfs(root.left)
        
        if self.prev_val is not None:
            self.ans = min(self.ans, root.val - self.prev_val.val)

        self.prev_val = root
        self.dfs(root.right)
        
        