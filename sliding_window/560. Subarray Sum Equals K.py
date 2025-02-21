from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        d[0] = 1
        cnt = 0
        prefix_sum = 0
        for i, n in enumerate(nums):
            prefix_sum += n
            cnt += d[prefix_sum - k]
            d[prefix_sum - k] += 1
        return cnt


Solution().subarraySum([1, 1, 1], 2)
