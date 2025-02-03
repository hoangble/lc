from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i = 1
        arr = set(arr)
        while k > 0:
            if i not in arr:
                k -= 1
            i += 1
        return i


sol = Solution()
sol.findKthPositive([2, 3, 4, 7, 11], 5)
