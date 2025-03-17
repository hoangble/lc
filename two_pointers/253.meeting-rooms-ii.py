from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals) < 2:
            return len(intervals)

        starts = sorted([x[0] for x in intervals])
        ends = sorted([x[1] for x in intervals])
        s_ptr = 0
        e_ptr = 0
        n = len(starts)

        used_rooms = 0
        while s_ptr < n:
            if starts[s_ptr] >= ends[e_ptr]:
                used_rooms -= 1
                e_ptr += 1
            used_rooms += 1
            s_ptr += 1
        return used_rooms


Solution().minMeetingRooms([[0, 30], [5, 10], [15, 20]])
