# https://leetcode.com/problems/find-leaves-of-binary-tree/
# 366. Find Leaves of Binary Tree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List, Optional


class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        #         # basically dfs???
        ans = []

        def traverse(node):
            if node is None:
                return None

            if not (node.left or node.right):
                ans[-1].append(node.val)
                return None

            node.left = traverse(node.left)
            node.right = traverse(node.right)

            return node

        while root:
            ans.append([])
            root = traverse(root)
        return ans


#         res = []
#         def recurse(node):
#             if not node:
#                 return None
#             if not(node.left or node.right):
#                 res[-1].append(node.val)
#                 return None
#             node.left = recurse(node.left)
#             node.right = recurse(node.right)
#             return node
#         while root:
#             res.append([])
#             root = recurse(root)
#         return res
