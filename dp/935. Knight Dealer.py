class Solution:
    def __init__(self):
        self.MOD = 10**9 + 7

    def knightDialer(self, n: int) -> int:
        self.moves = [
            (-2, -1),
            (-2, 1),
            (2, -1),
            (2, 1),
            (1, 2),
            (-1, 2),
            (1, -2),
            (-1, -2),
        ]
        tab = {}

        ans = 0
        for x in range(0, 4):
            for y in range(0, 3):
                if self.is_valid(x, y):
                    ans += self.dp(x, y, n, tab)

        return ans % self.MOD

    def dp(self, i: int, j: int, n: int, tab) -> int:
        if n <= 1:
            return n  # if there is 1 digit -> 1 number

        if (i, j, n) not in tab:
            tab[(i, j, n)] = 0
            for move in self.moves:
                new_x = i + move[0]
                new_y = j + move[1]

                if self.is_valid(new_x, new_y):
                    tab[(i, j, n)] += self.dp(new_x, new_y, n - 1, tab)

        return tab[(i, j, n)] % self.MOD

    def is_valid(self, x, y) -> bool:
        if x < 0 or y < 0:
            return False
        if x == 3 and y == 1:
            return True
        if x > 2 or y > 2:
            return False
        return True
