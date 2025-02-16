class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        t1_price, t2_price = float('inf'), float('inf'),
        t1_profit, t2_profit = 0, 0
        for i, p in enumerate(prices):
            t1_price = min(p, t1_price)
            t1_profit = max(t1_profit, p - t1_price)
            t2_price = min(t2_price, p - t1_profit)
            t2_profit = max(t2_profit, p - t2_price)


        return t2_profit 
        