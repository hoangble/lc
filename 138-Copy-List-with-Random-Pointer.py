\\\
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
\\\

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # O(1) approach
        # first pass to create new node and put it next to other
        if head is None:
            return None
        curr = head
        while curr:
            new_node = Node(curr.val)
            new_node.next = curr.next
            curr.next = new_node
            curr = curr.next.next
        
        # second pass to take care of random
        curr = head
        while curr:

            curr.next.random = curr.random.next if curr.random is not None else None 
            curr = curr.next.next

        # third pass to separate this ones
        
        curr = head
        new_head = head.next
        while curr:
            clone = curr.next
            curr.next = curr.next.next

            clone.next = clone.next.next if clone.next is not None else None
            # curr.next = curr.next.next
            curr = curr.next
    
        return new_head
            