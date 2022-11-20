# 236. Lowest Common Ancestor of a Binary Tree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/ 
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution():
    def __init__(self):
        self.lca = None
        
    def lowestCommonAncestor(self, root, p, q):
        # self.contain_p_or_q(root, p , q)
        # if root == p or root == q: return root
        self.contain_p_or_q(root, p, q)
        return self.lca        
    
    def contain_p_or_q(self, node, p, q):
        if not node: return False
        is_left = self.contain_p_or_q(node.left, p, q) 
        is_right = self.contain_p_or_q(node.right, p, q)
        
        if node == p or node == q: 
            if is_left or is_right:
                self.lca = node
            return True
        
        if is_left and is_right:
            self.lca = node
            # return True
        
        return is_left or is_right