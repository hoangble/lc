# 103. Binary Tree Zigzag Level Order Traversal
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         if root is None: return []
#         queue = [root]
#         current_level = []
#         next_level = []
#         ans = []
#         direction = "right"
#         while queue:
#             for node in queue:
#                 if direction == "left":
#                     if node and node.left:
#                         next_level.append(node.left)

#                     if node and node.right:
#                         next_level.append(node.right)
#                     direction = "right"
#                 else:
#                     if node and node.right:
#                         next_level.append(node.right)

#                     if node and node.left:
#                         next_level.append(node.left)
#                     direction = "left"

#                 if node:
#                     current_level.append(node.val)

#             ans.append(current_level)
#             queue = next_level
#             next_level = []
#             current_level = []

#         return ans

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: return []
        queue = [root]
        current_level = []
        next_level = []
        ans = []
        direction = "left"
        while queue:
            for node in queue:
                # if direction == "left":
                if node and node.right:
                    next_level.append(node.right)

                if node and node.left:
                    next_level.append(node.left)
                    # direction = "right"
                # else: # direction == right
#                     if node and node.right:
#                         next_level.append(node.right)

#                     if node and node.left:
#                         next_level.append(node.left)
                    # direction = "left"
                if node:
                    current_level.append(node.val)
            if direction == "left":
                ans.append(current_level[::-1])
                direction = "right"
            else:
                ans.append(current_level)
                direction = "left"
            queue = next_level
            next_level = []
            current_level = []

        return ans


sol = Solution()
right = TreeNode(val=2)
root = TreeNode(val=1, left=None, right=right)
print(sol.zigzagLevelOrder(root))