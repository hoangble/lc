from typing import List


class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        # if sum(candies) < k:
        #     return 0

        min_candy = min(candies)
        l = 1
        r = min_candy

        while l <= r:
            m = (l + r) // 2
            print(l, r, m)

            if self.valid(candies, m, k):
                l = m + 1
            else:
                r = m - 1

        return l if self.valid(candies, l, k) else r

    def valid(self, candies, split, k):
        for i in range(len(candies)):
            if k > 0:
                k -= candies[i] // split
            else:
                return True
        print(split, k)
        return k <= 0


Solution().maximumCandies([1, 2, 3, 4, 10], 5)
