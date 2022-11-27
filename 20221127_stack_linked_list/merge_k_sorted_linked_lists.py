# 23. Merge k Sorted Lists
# https://leetcode.com/problems/merge-k-sorted-lists/submissions/

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self,
                    lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return None
        if len(lists) == 1: return lists[0]

        arr = []
        for i in range(len(lists) // 2):
            arr.append(self.merge_two_lists(lists[i * 2], lists[i * 2 + 1]))

        if len(lists) % 2 == 1: arr.append(lists[-1])

        return self.mergeKLists(arr)

    def merge_two_lists(self, head1, head2):
        if not head1: return head2
        if not head2: return head1

        if head1.val < head2.val:
            head1.next = self.merge_two_lists(head1.next, head2)
            return head1
        else:
            head2.next = self.merge_two_lists(head1, head2.next)
            return head2