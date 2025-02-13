class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        memo = [[-1] * len(s) for _ in range(len(s))] 
        return self.recurse(0, len(s) - 1, s, memo) <= k
    
    def recurse(self, i, j, s, memo):
        if i == j:
            return 0
        
        if i == j - 1:
            return int(s[i] != s[j])
        
        if memo[i][j] != -1:
            return memo[i][j]
        
        if s[i] == s[j]:
            return self.recurse(i + 1, j -1, s, memo)
        
        memo[i][j] = 1 + min(self.recurse(i + 1, j, s, memo), self.recurse(i, j - 1, s, memo))
        return memo[i][j]