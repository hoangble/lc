# 142. Linked List Cycle II
# https://leetcode.com/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return self.get_begin_cycle(head, slow)

        return None

    def get_begin_cycle(self, head, intersection):
        ptr1 = head
        ptr2 = intersection
        # print(ptr1.val, ptr2.val)
        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        return ptr1
