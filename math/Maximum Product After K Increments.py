import heapq


class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        print(nums)
        while k > 0:
            num = heapq.heappop(nums)
            num += 1
            k -= 1
            heapq.heappush(nums, num)

        return reduce(lambda p, a: p * a % (10**9 + 7), nums, 1)  # -> what's this for
