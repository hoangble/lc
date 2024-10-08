class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        def merge(left_head, right_head):
            if left_head is None:
                return right_head
            elif right_head is None:
                return left_head

            if left_head.val < right_head.val:
                left_head.next = merge(left_head.next, right_head)
                return left_head

            else:
                right_head.next = merge(left_head, right_head.next)
                return right_head

        def find_mid(head):
            slow, fast = head, head
            while slow.next and fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        mid = find_mid(head)  # , (mid-1).next = None
        right_head = mid.next  # sortList(mid.next)
        mid.next = None
        left_head = self.sortList(head)
        right_head = self.sortList(right_head)

        return merge(left_head, right_head)
