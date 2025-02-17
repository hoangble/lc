# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        ans = [[-1] * n for _ in range(m)]
        up = left = 0
        right = n - 1
        down = m - 1

        while head:
            for col in range(left, right + 1):
                if head:
                    ans[up][col] = head.val
                    head = head.next
            
            for row in range(up + 1, down + 1):
                if head:
                    ans[row][right] = head.val
                    head = head.next
                
            if up != down:
                for col in range(right -1, left -1 , -1):
                    if head:
                        ans[down][col] = head.val
                        head = head.next

            if left != right:
                for row in range(down - 1, up, -1):
                    if head:
                        ans[row][left] = head.val
                        head = head.next

            up += 1
            down -= 1
            left += 1
            right -= 1
        return ans