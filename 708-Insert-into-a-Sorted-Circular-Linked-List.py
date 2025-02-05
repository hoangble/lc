"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if head is None:
            new_node = Node(insertVal)
            new_node.next = new_node
            return new_node
        
        curr = head
        to_insert = False

        while curr:
            if curr.val <= insertVal <= curr.next.val:
                to_insert = True
            elif curr.val > curr.next.val:
                if insertVal <= curr.next.val or insertVal >= curr.val:
                    to_insert = True
            
            if to_insert:
                new_node = Node(insertVal, curr.next)
                curr.next = new_node
                return head
            
            if curr.next == head:
                break
            
            curr = curr.next
        
        new_node = Node(insertVal)
        new_node.next = curr.next
        curr.next = new_node
        # curr.next = Node(insertVal, curr.next.next)
        return head
        