"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def levelOrder(self, root: "Node") -> List[List[int]]:
        if not root:
            return []

        ans = []
        queue = [root]
        while queue:
            next_level = []
            curr_level_ans = []
            for node in queue:
                curr_level_ans.append(node.val)
                for child in node.children:
                    if child:
                        next_level.append(child)
            queue = next_level
            ans.append(curr_level_ans)
        return ans
