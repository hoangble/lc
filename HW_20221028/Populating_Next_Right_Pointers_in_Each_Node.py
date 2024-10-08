# 116. Populating Next Right Pointers in Each Node
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

from typing import Optional

"""
# Definition for a Node.
"""


class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        # do order level traversal then do the right pointer connection
        if not root:
            return root
        current_level = [root]
        next_level = []
        while current_level:
            curr_len = len(current_level)
            for idx, node in enumerate(current_level):
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

                if idx < curr_len - 1:
                    node.next = current_level[idx + 1]
                else:
                    node.next = None

            current_level = next_level
            next_level = []
        return root
