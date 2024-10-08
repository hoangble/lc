# 102. Binary Tree Level Order Traversal
# https://leetcode.com/problems/binary-tree-level-order-traversal/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List, Optional


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # stack = [root]
        if root is None:
            return []
        queue = [root]
        current_level = []
        next_level = []
        ans = []

        while queue:
            for node in queue:
                if node.left is not None:
                    next_level.append(node.left)

                if node.right is not None:
                    next_level.append(node.right)

                current_level.append(node.val)

            ans.append(current_level)
            queue = next_level
            next_level = []
            current_level = []

        return ans
