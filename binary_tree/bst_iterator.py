# 173. Binary Search Tree Iterator
# https://leetcode.com/problems/binary-search-tree-iterator/submissions/
from typing import List, Optional
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        # do inorder traversal here and put it in an array
        self.all_nodes = self.inorder_traverse(root)
        self.i = -1

    def next(self) -> int:
        self.i += 1
        return self.all_nodes[self.i]

    def hasNext(self) -> bool:
        return self.i + 1 < len(self.all_nodes)

    def inorder_traverse(self, node: Optional[TreeNode]) -> list:
        return self.inorder_traverse(node.left) + [
            node.val
        ] + self.inorder_traverse(node.right) if node else []


class IterativeBSTIterator():
    def __init__(self, root: Optional[TreeNode]):
        self.curr = root
        self.stack = []
        self.pushLeft()
        # while self.curr:
        #     self.stack.append(self.curr)
        #     self.curr = self.curr.left

    def next(self) -> int:
        self.curr = self.stack.pop()
        val = self.curr.val
        self.curr = self.curr.right
        self.pushLeft()
        # while self.curr:
        #     self.stack.append(self.curr)
        #     self.curr = self.curr.left

        return val

    def hasNext(self) -> bool:
        return self.stack

    def pushLeft(self) -> None:
        while self.curr:
            self.stack.append(self.curr)
            self.curr = self.curr.left


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()


