from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        new_arr = [i * i for i in nums]
        return sorted(new_arr)