# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.find(root, p, q)

    def find(self, node, p, q):
        if not node:
            return False
        
        if node == p or node == q:
            return node 

        left = self.find(node.left, p, q)
        right = self.find(node.right, p, q)

        if left and right:
            return node
        
        # if left and not right:
        #     return left
        
        # if right and not left:
        #     return right
        
        return left or right
