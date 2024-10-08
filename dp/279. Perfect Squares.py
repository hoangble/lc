from math import sqrt


class Solution:
    def numSquares(self, n: int) -> int:
        if self.is_perf_sq(n):
            return 1

        tab = {}  # if
        self.dp(n, tab)
        print(tab)
        return tab[n]

    def dp(self, n: int, tab: dict) -> int:
        if n == 0 or n == 1:
            return 1

        if n not in tab:
            all_ans = []
            for i in range(n, 0, -1):
                if self.is_perf_sq(i):
                    all_ans.append(self.dp(n - i, tab) + 1)
            tab[n] = min(all_ans)

        return tab[n]

    def is_perf_sq(self, i: int) -> bool:
        return sqrt(i).is_integer()


sol = Solution()
sol.numSquares(8)
