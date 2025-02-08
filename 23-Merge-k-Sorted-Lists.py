# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 1:
            return lists[0]

        head = ListNode()
        curr = head

        if lists is None:
            return curr.next

        n = len(lists)
        interval = 1
        while interval < n:
            for i in range(0, n - interval, interval * 2):
                lists[i] = self.mergeTwoLists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if n > 0 else None

    def mergeTwoLists(self, list1, list2) -> ListNode:
        if not list1:
            return list2
        
        if not list2:
            return list1
        
        head = ListNode()
        curr = head
        l1 = list1
        l2 = list2

        
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        
        curr.next = l1 if l1 is not None else l2
        return head.next

