class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = []
        l1 = len(word1)
        l2 = len(word2)
        n = max(l1, l2)
        for i in range(n):
            if i < l1:
                ans.append(word1[i])
            if i < l2:
                ans.append(word2[i])
        return ''.join(ans)
