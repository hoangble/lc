# https://leetcode.com/problems/sliding-window-maximum/submissions/
# 239. Sliding Window Maximum

from typing import List
from collections import deque


class Solution:
    from collections import deque

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        right = 0
        max_queue = deque()

        ans = []
        while right < len(nums):
            # remove all elements that are smaller than the current max
            # so that the max is gonna be at the left end of the deque
            while len(max_queue) > 0 and nums[right] > max_queue[-1]:
                max_queue.pop()

            # if window len is smaller than k, keep adding to the max queue
            if right - left + 1 < k:
                max_queue.append(nums[right])
                right += 1

            else:
                #  add the current number to the deque
                max_queue.append(nums[right])
                # pop the left (max kept to the left)
                ans.append(max_queue[0])
                # if the current max is the left one, remove it
                if nums[left] == max_queue[0]:
                    max_queue.popleft()

                # move window
                left += 1
                right += 1
        return ans
