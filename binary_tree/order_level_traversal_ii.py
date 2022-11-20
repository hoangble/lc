# 107. Binary Tree Level Order Traversal II
# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

from typing import Optional, List

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        curr_level = [root]
        next_level = []
        ans = []
        while curr_level:
            curr_val = []
            for node in curr_level:
                if node.left: next_level.append(node.left)
                if node.right: next_level.append(node.right)
                curr_val.append(node.val)

            ans.append(curr_val)
            curr_level = next_level
            next_level = []

        return ans[::-1]