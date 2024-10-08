class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        t = {}  # (pos, n_steps_have_taken): # ways
        return self.helper(t, endPos, k, startPos)
        # return t[(endPos, k)]

    def helper(self, t, p, k, startPos) -> int:
        # base cases
        if abs(p - startPos) > k:
            return 0
        if abs(p - startPos) == k:
            return 1
        #
        if (p, k) in t:
            return t[(p, k)]
        t[(p, k)] = self.helper(t, p + 1, k - 1, startPos) + self.helper(
            t, p - 1, k - 1, startPos
        )
        return t[(p, k)] % (10**9 + 7)
