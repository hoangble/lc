from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque([])
        ans = []

        for i in range(k):
            while q and nums[i] > nums[q[-1]]:
                q.pop()
            q.append(i)

        ans.append(nums[q[0]])

        for i in range(k, len(nums)):
            while q and nums[i] > nums[q[-1]]:
                q.pop()
            if q and q[0] == i - k:
                q.popleft()
            q.append(i)
            ans.append(nums[q[0]])
        return ans


Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)
