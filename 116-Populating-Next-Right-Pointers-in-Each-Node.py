"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        
        left_most = root

        while left_most.left:
            head = left_most

            while head:
                # connection 1

                head.left.next = head.right

                if head.next:
                    head.right.next = head.next.left
                head = head.next
            
            left_most = left_most.left
        return root

        