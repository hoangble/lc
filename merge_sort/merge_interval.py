# https://leetcode.com/problems/merge-intervals/ 
# 56. Merge Intervals 
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
    ## sort the arrays by their start
        ans = []
        for i in sorted(intervals, key= lambda i: i[0]): # recommend rewrite as merge sort for extra practice
            if ans and ans[-1][-1] >= i[0]:
                ans[-1][-1] = max(ans[-1][-1], i[-1])
            else:
                ans.append(i)
        return ans
                
