class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        prev = -float('inf')
        i = 0
        ans = 0
        while i < len(intervals):
            if intervals[i][0] >= prev:
                prev = intervals[i][1]
            else:
                ans += 1
            i += 1
        return ans
        