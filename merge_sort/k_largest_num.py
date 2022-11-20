# https://leetcode.com/problems/kth-largest-element-in-an-array/submissions/
# 215. Kth Largest Element in an Array
import heapq
from typing import List


class Solution: # using priority heap, kinda cheating
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # keep a list of k largest number
        k_largest = []
        heapq.heapify(k_largest)
        for num_ in nums:
            heapq.heappush(k_largest, num_)
            if len(k_largest) > k:
                heapq.heappop(k_largest)
        return k_largest[0]
    # O(nlog k), O(k)

class Solution: # quick select
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # keep a list of k largest number
        k_largest = []
        heapq.heapify(k_largest)
        for num_ in nums:
            heapq.heappush(k_largest, num_)
            if len(k_largest) > k:
                heapq.heappop(k_largest)
        return k_largest[0]
