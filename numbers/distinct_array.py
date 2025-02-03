from collections import defaultdict
from math import ceil
from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        c = defaultdict(int)
        for i in range(len(nums) - 1, -1, -1):
            if c[nums[i]] > 0:
                return ceil((i + 1) / 3)
            c[nums[i]] += 1
        return 0


sol = Solution()
sol.minimumOperations([4, 5, 6, 4, 4])
