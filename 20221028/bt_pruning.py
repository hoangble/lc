# 814. Binary Tree Pruning
# https://leetcode.com/problems/binary-tree-pruning/ 
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not self.contain_ones(root): return None
        return root
        
    def contain_ones(self, node):
        if not node: return False
        
        contain_ones_left = self.contain_ones(node.left)
        contain_ones_right = self.contain_ones(node.right)
        
        if not contain_ones_left: node.left = None
        if not contain_ones_right: node.right = None
        
        return node.val == 1 or contain_ones_left or contain_ones_right
        