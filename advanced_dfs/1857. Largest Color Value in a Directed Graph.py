from collections import defaultdict, deque
from typing import List


class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        # TLE as it repeats checking the same path for multiple nodes in the path
        #     ans = -1
        #     n = len(colors)
        #     m = len(edges)
        #     g = defaultdict(list)
        #     c = defaultdict(int)

        #     for edge in edges:
        #         g[edge[0]].append(edge[1])
        #         # g[edge[1]].append(edge[0])

        #     for i in range(n): g[i]
        #     # print(g)
        #     stack = [False] * n

        #     for i in range(n):
        #         max_ = self.dfs(i, g, c, stack, 0, colors)
        #         if max_ == -1: return -1
        #         ans = max(ans, max_)
        #         # print(ans)

        #     return ans

        # def dfs(self, node, g, c, stack, ans, colors) -> int:
        #     if stack[node]: return -1

        #     stack[node] = True
        #     # print(node, stack, c)

        #     c[colors[node]] += 1
        #     ans = max(ans, max(c.values()))
        #     for nei in g[node]:
        #         max_ = self.dfs(nei, g, c, stack, ans, colors)
        #         if max_ == -1: return -1
        #         ans = max(ans, max_)

        #     stack[node] = False
        #     c[colors[node]] -= 1

        #     return ans

        # cache the immediate result

        # Another approach: Kahn's algo
        # TODO: Intuition ???

        n = len(colors)
        g = defaultdict(list)

        indegree = [0] * n

        for edge in edges:
            g[edge[0]].append(edge[1])
            indegree[edge[1]] += 1

        for i in range(n):
            g[i]

        cnt = [
            defaultdict(int) for _ in range(n)
        ]  # cnt color, n_node x n_unique_colors (26 to keep max)

        q = deque([])
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)

        ans, seen = 0, 0

        while q:
            node = q.popleft()
            cnt[node][colors[node]] += 1
            ans = max(ans, cnt[node][colors[node]])
            seen += 1

            for nei in g[node]:
                for c in cnt[node]:
                    cnt[nei][c] = max(cnt[node][c], cnt[nei][c])

                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        if seen < n:
            return -1
        return ans
