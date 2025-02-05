"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        self.dia = 0
        self.dfs(root, 0)
        return self.dia
    
    def dfs(self, node, curr_depth):
        if not node:
            return 0
        
        if len(node.children) == 0:
            return curr_depth
        
        all_dias = []
        max_depth_1, max_depth_2 = curr_depth, 0
        for child in node.children:
            child_depth = self.dfs(child, curr_depth + 1)
            if child_depth > max_depth_1:
                max_depth_1, max_depth_2 = child_depth, max_depth_1
            elif child_depth > max_depth_2:
                max_depth_2 = child_depth

        dis = max_depth_1 + max_depth_2 - 2 * curr_depth
        self.dia = max(self.dia, dis)
        return max_depth_1