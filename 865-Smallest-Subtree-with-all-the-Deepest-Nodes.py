# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.deep(root)[1]

    def deep(self, root):
        if root is None:
            return 0, None
        
        left = self.deep(root.left)
        right = self.deep(root.right)
        
        if left[0] > right[0]:
            return left[0] + 1, left[1]
        elif left[0] < right[0]:
            return right[0] + 1, right[1]
        else:
            return left[0] + 1, root
        