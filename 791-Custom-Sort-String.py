class Solution:
    def customSortString(self, order: str, s: str) -> str:
        d = {}
        for c in order:
            d[c] = 0
        
        left_over = []
        for c in s:
            if c in d:
                d[c] += 1
            else:
                left_over.append(c)
        
        ans = []
        for c in order:
            for i in range(d[c]):
                ans.append(c)
        
        ans += left_over
        return ''.join(ans)
        