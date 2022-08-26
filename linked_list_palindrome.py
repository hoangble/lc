from typing import Optional, List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        curr = head
        if curr is not None:
            val_ = curr.val
            
            if len(stack) == 0:
                stack.append(val_)
            else:
                print(val_)
                if val_ == stack[-1]:
                    stack.pop(-1)
                else:
                    stack.append(val_)
            curr = curr.next
            
                
        if len(stack) == 0:
            return True
        else:
            return False

if __name__ == "__main__":
    sol = Solution()
    # input_ = [1,2,2,1]
    sol.isPalindrome(input_)