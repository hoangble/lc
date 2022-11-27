# 23. Merge k Sorted Lists 

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def merge_two_lists(left_head, right_head):
            # left_head = lists[0]
            # right_head = lists[-1]
            
            if left_head is None: return right_head
            elif right_head is None: return left_head
            
            if left_head.val < right_head.val:
                left_head.next = merge_two_lists(left_head.next, right_head)
                return left_head
            
            else:
                right_head.next = merge_two_lists(left_head, right_head.next)
                return right_head
        # base case: len(lists) == 2
        if len(lists) == 0: return None
        elif len(lists) == 1: return lists[0]
        else:     
            arr = []
            for i in range(len(lists)//2):
                arr.append(merge_two_lists(lists[i*2], lists[i*2+1]))
            if len(lists) % 2 == 1:
                arr.append(lists[-1])
            return self.mergeKLists(arr)

#%%
x = -1
sign = [False]
print(sign)

#%%
N = 2
print(1<<N)