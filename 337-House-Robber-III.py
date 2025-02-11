# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        self.rob = {}
        self.not_rob = {}
        return self.helper(root, False)
        
    def helper(self, node, parent_rob) -> int:
        if not node:
            return 0
        
        if parent_rob:
            if node in self.not_rob:
                return self.not_rob[node]
            
            val = self.helper(node.left, False) + self.helper(node.right, False)
            self.not_rob[node] = val
            return self.not_rob[node]

        else:
            if node in self.rob:
                return self.rob[node]
            rob = node.val + self.helper(node.left, True) + self.helper(node.right, True)
            not_rob =  self.helper(node.left, False) + self.helper(node.right, False)
            self.rob[node] = max(rob, not_rob)
            return self.rob[node]
