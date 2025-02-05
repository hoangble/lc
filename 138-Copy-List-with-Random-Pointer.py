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
        if head is None:
            return None

        new_head = Node(head.val)
        clones = {head: new_head}
        curr = head
        while curr:
            if curr not in clones:
                new_node = Node(curr.val)
                clones[curr] = new_node
            
            new_node = clones[curr]

            if curr.next is not None:
                if curr.next not in clones:
                    new_next_node = Node(curr.next.val)
                    clones[curr.next] = new_next_node
                new_node.next = clones[curr.next]
            

            if curr.random is not None:
                if curr.random not in clones:
                    new_random_node = Node(curr.random.val)
                    clones[curr.random] = new_random_node
                new_node.random = clones[curr.random]
            
            curr = curr.next
        
        return new_head
            