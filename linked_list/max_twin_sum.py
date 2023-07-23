# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
    # def pairSum(self, head: Optional[ListNode]) -> int:
    #     fast = head.next
    #     slow = head
    #     cnt = 0
         
    #     while fast and fast.next:
    #         fast = fast.next.next
    #         slow = slow.next
    #     print(cnt)
    #     if cnt == 0: return slow.val + fast.val

    #     # reverse
    #     slow.next = self.reverseList(slow.next)
    #     slow = slow.next
        
    #     # second pass
    #     max_sum = 0
    #     curr = head

    #     while slow:
    #         curr_sum = curr.val + slow.val
    #         if curr_sum > max_sum: max_sum = curr_sum
    #         slow = slow.next
    #         curr = curr.next
    #     return max_sum
    
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     prev = None
    #     curr = head
    #     while curr:
    #         tmp = curr.next
    #         curr.next = prev
    #         prev = curr        
    #         curr = tmp
#         return prev

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast = head.next
        slow = head
        cnt = 0
         
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            cnt += 1
        # print(cnt)
        if cnt == 0: return slow.val + fast.val

        # reverse
        slow.next = self.reverseList(slow.next)
        slow = slow.next
        
        # second pass
        max_sum = 0
        curr = head

        while slow:
            curr_sum = curr.val + slow.val
            if curr_sum > max_sum: max_sum = curr_sum
            slow = slow.next
            curr = curr.next
        return max_sum
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr        
            curr = tmp
        return prev

#%%
import heapq
nums = [-10,1,3,1,4]
heapq.heapify(nums)
heapq.heappush(nums, 3)
print(nums)
for _ in range(3):
    print(heapq.heappop(nums))

#%%
a = 167
b = 91
c = 0
while a - 2 > b:
    a -= 2
    c += 1
print(c)

#%%
import math
from sympy import *
a = 0
b = 2
while b < 30:
    if isprime(b): a += 81
    b += 1
print(a)

#%%
sum_ = 0
for i in range(1, 101):
    if i % 2 == 1:
        sum_ += i
    else:
        sum_ -= 2
print(sum_)

#%%

# A naive recursive implementation of 0-1 Knapsack Problem
  
# Returns the maximum value that can be put in a knapsack of
# capacity W
def knapSack(W, wt, val, n):
  
    # Base Case
    if n == 0 or W == 0 :
        return 0
  
    # If weight of the nth item is more than Knapsack of capacity
    # W, then this item cannot be included in the optimal solution
    if (wt[n-1] > W):
        return knapSack(W, wt, val, n-1)
  
    # return the maximum of two cases:
    # (1) nth item included
    # (2) not included
    else:
        return max(val[n-1] + knapSack(W-wt[n-1], wt, val, n-1),
                   knapSack(W, wt, val, n-1))
  
# end of function knapSack
  
# To test above function
wt = [3, 4, 5, 4, 7, 8, 5]
val = [10, 12, 18, 19, 20, 19, 12]
W = 18
n = len(val)
print(knapSack(W, wt, val, n))

#%%
def f(x):
    result = 1
    for i in range(1, x+1):
        result += 1
    return result
print(f(f(f(3))))