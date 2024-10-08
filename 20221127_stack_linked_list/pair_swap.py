# 24. Swap Nodes in Pairs
# https://leetcode.com/problems/swap-nodes-in-pairs/
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        if not head.next:
            return head

        second = head.next
        self.swap(head, second)
        head.next = self.swapPairs(head.next)
        return second

    def swap(self, slow, fast):
        slow.next = fast.next
        fast.next = slow
