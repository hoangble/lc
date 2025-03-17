class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        #     # print(len(s))
        #     tab = [[-1] * len(s) for _ in range(len(s))]

        #     return self.dp(0, len(s) -1, s, tab) <= k

        # def dp(self, i, j, s, tab):
        #     if i == j: # 1 letter remaining
        #         return 0

        #     if i == j - 1: # 2 letters remaining
        #         return int(s[i] != s[j])

        #     if tab[i][j] != -1:
        #         return tab[i][j]

        #     if s[i] == s[j]:
        #         tab[i][j] = self.dp(i + 1, j - 1, s, tab)
        #     else:
        #         tab[i][j] = min(self.dp(i, j - 1, s, tab), self.dp(i + 1, j, s, tab)) + 1

        #     return tab[i][j]

        # space optimized
        # if len(s) < 2:  # trivial cases
        #     return True

        # memo = [0] * len(s)
        # temp = prev = 0

        # for i in range(len(s) - 2, -1, -1):
        #     prev = 0
        #     for j in range(i + 1, len(s)):
        #         temp = memo[j]
        #         if s[i] == s[j]:
        #             memo[j] = prev
        #         else:
        #             memo[j] = 1 + min(memo[j], memo[j - 1])
        #         prev = temp
        # return memo[-1] <= k

        if len(s) < 2: # trivial cases
            return True 

        n = len(s)
        memo = [[0] * n for _ in range(n)]
        # temp = prev = 0
    
        for i in range(len(s) - 2, -1, -1):
            # prev = 0
            for j in range(i + 1, len(s)):
                # temp = memo[j]
                if s[i] == s[j]:
                    memo[i][j] = memo[i + 1][j - 1]
                else:
                    memo[i][j] = 1 + min(memo[i+1][j], memo[i][j-1])
        return memo[-1] <= k


Solution().isValidPalindrome("abbababa", k=2)
