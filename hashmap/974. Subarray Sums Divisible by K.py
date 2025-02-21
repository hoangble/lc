from collections import defaultdict
from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        cnt = 0
        prefix_sum = 0
        d = defaultdict(int)  # prefix sum till this point
        d[0] = 1
        for i, n in enumerate(nums):
            prefix_sum += n
            mod = prefix_sum % k
            cnt += d[mod]
            d[mod] += 1
        return cnt

Solution().subarraysDivByK([4,5,0,-2,-3,1], 5)