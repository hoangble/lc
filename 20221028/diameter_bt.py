# 543. Diameter of Binary Tree
# https://leetcode.com/problems/diameter-of-binary-tree/ 
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    max_diameter = -1
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        # diameter = height(node.left) + height(node.right) + 2 #left sub tree + right subtree
        
        # base cases
        # if not root: return -1
        self.get_height(root)
        return max_diameter
        
        # return max(self.get_height(root.left) + self.get_height(root.right) + 2, max_diameter)
                   
                   # self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
    
    def get_height(self, node):
        # base case:
        if not node: return -1
        
        left_height = self.get_height(node.left)
        right_height = self.get_height(node.right)
        
        max_diameter = max(left_height + right_height + 2, max_diameter)
        return max(left_height, left_height) + 1