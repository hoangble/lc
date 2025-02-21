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
        
        if head.next is None:
            head.next = Node(insertVal, head)
            return head
        
        curr = head
        to_insert = False
        while curr:
            if curr.val <= insertVal <= curr.next.val:
                to_insert = True
            
            elif curr.val > curr.next.val:
                if insertVal <= curr.val and insertVal <= curr.next.val or insertVal >= curr.val and insertVal >= curr.next.val:
                    to_insert = True
            
            if to_insert:
                new_node = Node(insertVal, curr.next)
                curr.next = new_node 
                return head

            
            curr = curr.next
            if curr == head:
                break
        new_node = Node(insertVal, curr.next)
        curr.next = new_node 

        return head
        