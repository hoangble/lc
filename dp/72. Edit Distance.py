class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)
        if n1 == 0 or n2 == 0:
            return n1 + n2
        t = [[None for _ in range(n2)] for i in range(n1)]

        self.helper(t, n1 - 1, n2 - 1, word1, word2)
        return t[-1][-1]

    def helper(self, t, x, y, word1, word2) -> int:
        # base cases
        if x == -1 and y == -1:
            return 0
        if x == -1:
            return y + 1
        if y == -1:
            return x + 1

        if t[x][y] is not None:
            return t[x][y]

        #
        if word1[x] == word2[y]:
            t[x][y] = self.helper(t, x - 1, y - 1, word1, word2)
            return t[x][y]

        insert = self.helper(t, x, y - 1, word1, word2)
        delete = self.helper(t, x - 1, y, word1, word2)
        replace = self.helper(t, x - 1, y - 1, word1, word2)
        t[x][y] = min(insert, delete, replace) + 1
        return t[x][y]
