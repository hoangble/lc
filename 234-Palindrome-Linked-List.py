# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # find the second half using fast-slow pointer
        if head.next == None: return True

        slow = head
        fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        second_half_ptr = self.reverse(slow.next)
        first_half_ptr = head

        while second_half_ptr and first_half_ptr:
            if second_half_ptr.val != first_half_ptr.val:
                return False
            first_half_ptr = first_half_ptr.next
            second_half_ptr = second_half_ptr.next 

        return True
        
    def reverse(self, head) -> Optional[ListNode]:
        if not head: 
            return None
        
        curr = head
        prev = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev
        