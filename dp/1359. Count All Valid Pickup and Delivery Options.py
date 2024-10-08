class Solution:
    MOD = 10**9 + 7

    def countOrders(self, n: int) -> int:
        # dp
        memo = {}
        self.dp(memo, n, n)
        print(memo)
        return memo[(n, n)]

    def dp(self, memo, undelivered, unpicked) -> int:
        if undelivered == 0 and unpicked == 0:
            return 1

        if unpicked < 0 or undelivered < 0 or undelivered < unpicked:
            return 0

        if (undelivered, unpicked) not in memo:
            waysToPick = (
                unpicked * self.dp(memo, unpicked - 1, undelivered)
            ) % self.MOD
            waysToDeliver = (
                (undelivered - unpicked) * self.dp(memo, unpicked, undelivered - 1)
            ) % self.MOD

            memo[(undelivered, unpicked)] = waysToPick + waysToDeliver

        return memo[(undelivered, unpicked)]


class Solution:
    def countOrders(self, n: int) -> int:
        MOD = 10**9 + 7
        ans = 1
        for i in range(1, n + 1):
            ans *= i
            ans *= 2 * i - 1
            ans = ans % MOD
        return ans


sol = Solution()
sol.countOrders(n=1)
