# 94. Binary Tree Inorder Traversal
# https://leetcode.com/problems/binary-tree-inorder-traversal/

from typing import Optional, List
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        if not (root.left or root.right):
            return [root.val]
        ans = []
        self.traverse(root.left, ans)
        ans.append(root.val)
        self.traverse(root.right, ans)
        return ans
        # return  self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []

    def traverse(self, node, ans):
        if not node:
            return None
        # if not (node.left or node.right): return node.val

        self.traverse(node.left, ans)
        ans.append(node.val)
        self.traverse(node.right, ans)
        return ans


class IterativeSolution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack_ = []
        ans = []
        curr_node = root
        while curr_node or stack_:
            if curr_node:
                stack_.append(curr_node)
                curr_node = curr_node.left
            else:
                curr_node = stack_.pop()
                ans.append(curr_node.val)
                curr_node = curr_node.right
        return ans

    # better one liner


r = TreeNode(3)
r2 = TreeNode(5)
l2 = TreeNode(4)
l1 = TreeNode(2, left=l2, right=r2)

root = TreeNode(1, right=r, left=l1)

sol = IterativeSolution()
sol.inorderTraversal(root)
