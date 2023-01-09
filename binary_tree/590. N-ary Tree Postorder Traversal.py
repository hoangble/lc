"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def __init__(self): self.ans = []
    def postorder(self, root: 'Node') -> List[int]:
        if not root: return self.ans

        for child in root.children:
            self.postorder(child)
        self.ans.append(root.val)
        return self.ans
