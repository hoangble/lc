from typing import List


class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        current_chair = 0
        x = {i: t for i, t in enumerate(times)}
        sorted_dict = {k: v for k, v in sorted(x.items(), key=lambda item: item[1][0])}

        current_leave_time = -1
        for k, v in sorted_dict.items():
            if k == targetFriend:
                return current_chair

            if v[0] > current_leave_time and current_chair > 0:
                current_chair -= 1
            else:
                current_chair += 1
                current_leave_time = max(current_leave_time, v[1])


sol = Solution()
times = [
    [33889, 98676],
    [80071, 89737],
    [44118, 52565],
    [52992, 84310],
    [78492, 88209],
    [21695, 67063],
    [84622, 95452],
    [98048, 98856],
    [98411, 99433],
    [55333, 56548],
    [65375, 88566],
    [55011, 62821],
    [48548, 48656],
    [87396, 94825],
    [55273, 81868],
    [75629, 91467],
]
targetFriend = 6
sol.smallestChair(times, targetFriend)
