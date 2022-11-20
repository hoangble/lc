# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
# 106. Construct Binary Tree from Inorder and Postorder Traversal
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int],
                  postorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: idx for idx, val in enumerate(inorder)}

        def dfs(start, end):
            if start > end: return None
            root = postorder.pop()
            root_idx = inorder_map[root]
            node = TreeNode(val=root)
            node.right = dfs(root_idx + 1, end)
            node.left = dfs(start, root_idx - 1)
            return node

        return dfs(0, len(postorder) - 1)
