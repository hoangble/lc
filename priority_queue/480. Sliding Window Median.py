from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        if k == 1:
            return nums
        # for each of the heap, store (value, index)
        # dont need to
        smaller = []  # contain smaller half, max heap
        heapify(smaller)

        bigger = []  # contain bigger half, min heap
        heapify(bigger)

        for i in range(k):
            heappush(bigger, (nums[i], i))

        for i in range(k // 2):
            num = heappop(bigger)
            heappush(smaller, (num[0] * -1, num[1]))

        ans = []
        ans.append(self.find_median(smaller, bigger, k))

        for i in range(k, len(nums)):
            # if this element is bigger than the smallest item in the bigger half
            if nums[i] >= bigger[0][0]:
                heappush(bigger, (nums[i], i))
                if nums[i - k] <= smaller[0][0] * -1:
                    self.balance(bigger, smaller)  # do something???
            else:
                heappush(smaller, (nums[i] * -1, i))
                if nums[i - k] >= bigger[0][0]:
                    self.balance(smaller, bigger)  # do something???

            while bigger and bigger[0][1] < i - k + 1:
                heappop(bigger)

            while smaller and smaller[0][1] < i - k + 1:
                heappop(smaller)

            ans.append(self.find_median(smaller, bigger, k))

        return ans

    def balance(self, from_heap, to_heap):
        num = heappop(from_heap)
        heappush(to_heap, (num[0] * -1, num[1]))

    def find_median(self, max_heap, min_heap, k) -> int:
        if k % 2 == 1:
            return min_heap[0][0]
        else:
            return (max_heap[0][0] * -1 + min_heap[0][0]) / 2


Solution().medianSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)
