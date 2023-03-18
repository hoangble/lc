class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        t = [None] * (len(cost) + 1)
        self.helper(len(cost), t, cost)
        return t[-1]
    
    def helper(self, pos, t, cost) -> int:
        if pos == 0 or pos == 1:
            return 0
        
        if t[pos] is not None:
            return t[pos]

        t[pos] = min(self.helper(pos-1, t, cost) + cost[pos - 1], self.helper(pos-2, t, cost) + cost[pos-2])
        return t[pos]
    
    
