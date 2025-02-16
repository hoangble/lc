class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        while l < r:
            m = (l + r) // 2
            curr_h = self.total_hours(piles, m)
            if curr_h <= h:
                r = m
            else:
                l = m + 1
        return l

    def total_hours(self, piles, k):
        ans = 0
        for p in piles:
            ans += ceil(p / k)
        return ans
        