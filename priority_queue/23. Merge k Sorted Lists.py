# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    from heapq import heapify, heappush, heappop
    from collections import defaultdict
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        q = []
        heapify(q)

        m = defaultdict(list)
        for l in lists:
            if l:
                heappush(q, l.val)
                m[l.val].append(l)

        
        head = ListNode()
        curr = head
        while q:
            # print(curr.val)
            node_val = heappop(q)
            node = m[node_val].pop()
            curr.next = node
            
            
            if node:
                next_node = node.next
                if next_node:
                    m[next_node.val].append(next_node)
                    heappush(q, next_node.val)
            curr = curr.next
        
        return head.next
