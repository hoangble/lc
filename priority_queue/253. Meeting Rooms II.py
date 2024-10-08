class Solution:
    import heapq

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        q = []
        heapq.heapify(q)
        intervals.sort(key=lambda x: x[0])
        heapq.heappush(q, intervals[0][-1])
        # print(q)
        ans = 1
        for i in intervals[1:]:
            # print(i, q)
            while len(q) > 0 and i[0] >= q[0]:
                heapq.heappop(q)
            heapq.heappush(q, i[-1])
            ans = max(ans, len(q))
        return ans
