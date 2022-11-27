# 25. Reverse Nodes in k-Group
# https://leetcode.com/problems/reverse-nodes-in-k-group/
from typing import List, Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# redo
class Solution:
    def reverseKGroup(self, head: Optional[ListNode],
                      k: int) -> Optional[ListNode]:
        i = 0
        curr = head
        while i < k and curr:
            curr = curr.next
            i += 1
        if i < k: return head

        new_head = self.reverse_linked_list(head, k)
        head.next = self.reverseKGroup(curr, k)
        return new_head

    def reverse_linked_list(self, head, k):
        prev = None
        curr = head

        while k > 0:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
            k -= 1
        return prev