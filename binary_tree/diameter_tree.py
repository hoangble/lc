# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # diameter = height(node.left) + height(node.right) + 2 #left sub tree + right subtree

        # base cases
        if not root:
            return -1

        return max(
            self.get_height(root.left) + self.get_height(root.right) + 2,
            self.diameterOfBinaryTree(root.left),
            self.diameterOfBinaryTree(root.right),
        )

    def get_height(self, node) -> int:
        # base case:
        if not node:
            return -1

        return max(self.get_height(node.left), self.get_height(node.right)) + 1
