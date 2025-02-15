# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        new_head = self.swap(head, head.next)
        head.next = self.swapPairs(head.next)
        return new_head
        
    def swap(self, node1, node2):
        node1.next = node2.next
        node2.next = node1
        return node2
        