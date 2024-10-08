class Solution:
    from typing import Any

    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        self.parent = []
        self.rank = []

        for _ in range(m):
            for _ in range(n):
                self.parent.append(-1)
                self.rank.append(0)

        self.directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        ans = []
        self.cnt = 0
        for x, y in positions:
            int_map = x * n + y
            self.add_land(int_map)

            for x_, y_ in self.directions:
                new_x = x + x_
                new_y = y + y_
                if self.valid(new_x, new_y, m, n) and self.is_land(new_x * n + new_y):
                    self.union(int_map, new_x * n + new_y)

            ans.append(self.cnt)
        return ans

    def add_land(self, x) -> None:
        if self.parent[x] >= 0:
            return
        self.parent[x] = x
        self.rank[x] += 1
        self.cnt += 1

    def is_land(self, x) -> bool:
        return self.parent[x] >= 0

    def find(self, x) -> List[int]:
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y) -> None:
        parent_x = self.find(x)
        parent_y = self.find(y)

        if parent_x != parent_y:
            if self.rank[parent_x] <= self.rank[parent_y]:
                self.parent[parent_x] = parent_y
                self.rank[parent_x] += self.rank[parent_y]
            else:
                self.parent[parent_y] = parent_x
                self.rank[parent_y] += self.rank[parent_x]
            self.cnt -= 1

    def valid(self, x, y, m, n):
        return 0 <= x < m and 0 <= y < n
