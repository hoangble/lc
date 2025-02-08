class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return \\

        target_cnt = defaultdict(int)
        for c in t:
            target_cnt[c] += 1
        
        filtered_s = []
        for i, char in enumerate(s):
            if char in target_cnt:
                filtered_s.append((i, char))
        
        print(filtered_s)

        l = r = 0
        ans = (float('inf'), 0, 0)
        while r < len(filtered_s):
            char = filtered_s[r][1]
            # if s[r] in target_cnt:
            target_cnt[char] -= 1
            
            while l <= r and self.all_zeros(target_cnt):
                start = filtered_s[l][0]
                end = filtered_s[r][0]

                if end - start + 1 < ans[0]:
                    ans = (end - start + 1, start, end)
                target_cnt[filtered_s[l][1]] += 1
                l += 1        
            r += 1
        
        return \\ if ans[0] == float('inf') else s[ans[1]:ans[2]+1]

    def all_zeros(self, d):
        for k, v in d.items():
            if v > 0:
                return False
        return True
