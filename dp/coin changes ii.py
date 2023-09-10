from typing import List
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        # for c in coins:
            # memo[c] = 1
        coins = set(coins)
        self.dp(amount, coins, memo)
        return memo[amount]
    
    def dp(self, amt, coins, memo):
        if amt <= 0:
            return 0
        
        if amt in memo:
            return memo[amt]
        
        cnt = 0
        for c in coins:
            cnt += self.dp(amt - c, coins, memo) + 1
        memo[amt] = cnt
        return memo[amt]
    
sol = Solution()
sol.change(5, [1, 2, 4])