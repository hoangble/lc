class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        res = []
        self.dfs(s, word_set, [], res, 0)
        return res
    
    def dfs(self, s, word_set, curr, res, start_idx):
        if start_idx == len(s):
            res.append(' '.join(curr))
        
        for end_idx in range(start_idx + 1, len(s) + 1):
            word = s[start_idx:end_idx]
            if word in word_set:
                curr.append(word)
                self.dfs(s, word_set, curr, res, end_idx)
                curr.pop()