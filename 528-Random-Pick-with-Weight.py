class Solution:

    def __init__(self, w: List[int]):
        prefix_sum = 0
        self.prefix_sum = []
        for i in range(len(w)):
            prefix_sum += w[i]
            self.prefix_sum.append(prefix_sum)
        self.total_sum = prefix_sum

    def pickIndex(self) -> int:
        idx = random.random() * self.total_sum
        # binary search
        l, r = 0, len(self.prefix_sum)
        while l < r:
            m = (l + r) // 2
            if idx > self.prefix_sum[m]:
                l = m + 1
            else:
                r = m
        return l


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()