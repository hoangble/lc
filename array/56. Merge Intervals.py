from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort interval
        intervals = sorted(intervals, key=lambda x: x[0])

        ans = []
        curr_int = intervals[0]
        # then just iterate thru
        for interval in intervals:
            # curr_int = ans.pop()
            if interval[0] <= curr_int[-1]:
                curr_int[-1] = max(curr_int[-1], interval[-1])
            else:
                ans.append(curr_int)
                curr_int = interval
        ans.append(curr_int)
        return ans


sol = Solution()
print(sol.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
