from typing import List


class Solution:
    def minSwaps(self, data: List[int]) -> int:
        ones = sum(data)

        l = 0
        r = 0
        cnt = 0
        max_ones = 0
        while r < len(data):
            cnt += data[r] == 1

            while r - l > ones:
                cnt -= data[l] == 1
                l += 1

            r += 1

            max_ones = max(max_ones, cnt)

        return ones - max_ones


Solution().minSwaps([1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1])
