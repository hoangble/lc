\\\
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
\\\

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        cloned = {node: Node(node.val)}

        dq = deque()
        dq.append(node)
        while dq:
            curr_node = dq.popleft()
            for nei in curr_node.neighbors:
                if nei not in cloned:
                    cloned[nei] = Node(nei.val)
                    dq.append(nei)
                cloned[curr_node].neighbors.append(cloned[nei])
        return cloned[node]
        